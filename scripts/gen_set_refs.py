"""Generate Thomas Archer seated at the investigation desk (16:9 reference for LongCat).
Step 1: empty set plates with Z-Image-Turbo. Step 2: Qwen-Image-Edit-2511 places Thomas (from the portrait) into the set."""
import json, os, shutil, time
from gradio_client import Client, handle_file

TOKEN = os.environ["HF_TOKEN"]
OUT = "out"; os.makedirs(OUT, exist_ok=True)
PORTRAIT = "presenter/portrait_v1_896x1152.png"
log = []

def keep(path, name):
    dst = f"{OUT}/{name}"; shutil.copy(path, dst); return dst

def gallery_paths(g):
    res = []
    for item in g or []:
        img = item.get("image") if isinstance(item, dict) else item
        res.append(img["path"] if isinstance(img, dict) else img)
    return res

PLATE_PROMPT = (
    "Cinematic photograph of an empty investigative journalist's office at night, 16:9 wide medium shot from seated eye level. "
    "In the foreground a dark walnut desk spans the bottom of the frame, with a closed manila case folder, a few printed documents "
    "and a warm brass desk lamp on the right side casting amber light. Behind the desk, an empty leather office chair, slightly left of centre. "
    "The back wall is an evidence board with pinned printouts, transaction diagrams and documents connected by thin amber threads, "
    "and a monitor showing a dark network graph, all softly out of focus with shallow depth of field. "
    "Dark charcoal and deep navy tones, amber accent light, moody but clean, nobody in the room, photorealistic, 35mm lens, film grain."
)

z = Client("Tongyi-MAI/Z-Image-Turbo", token=TOKEN)
plates = []
for seed in (20251120, 777001):
    t = time.time()
    try:
        g, used, _ = z.predict(prompt=PLATE_PROMPT, resolution="1536x864 ( 16:9 )", seed=seed, steps=8, shift=3.0,
                               random_seed=False, gallery_images=[], api_name="/generate")
        p = keep(gallery_paths(g)[0], f"plate_{seed}.png"); plates.append(p)
        log.append({"step": "plate", "seed": seed, "seconds": round(time.time() - t, 1), "file": p})
    except Exception as e:
        log.append({"step": "plate", "seed": seed, "error": f"{type(e).__name__}: {e}"})
    print(log[-1], flush=True)

EDIT_PROMPT = (
    "Place the man from image 1 into the office from image 2. He sits in the chair behind the desk, upper body visible from the waist up, "
    "positioned slightly left of centre, facing the camera and looking straight into the lens with a calm, composed expression. "
    "Both forearms rest on the desk and his hands lie still and relaxed on the desk surface, near the case folder, fingers natural. "
    "Keep his face, hair, short stubble and his plain dark charcoal crew-neck sweater exactly as in image 1. "
    "Soft even frontal light on his face, warm amber lamp light on the desk, background softly out of focus. Photorealistic, 16:9."
)
SOLO_PROMPT = (
    "Show this exact man seated behind a dark walnut desk in an investigative journalist's office at night, upper body from the waist up, "
    "slightly left of centre, looking straight into the camera, calm expression. Both forearms rest on the desk and his hands lie still and relaxed on it, "
    "next to a closed manila case folder; a warm brass desk lamp on the right; behind him an out-of-focus evidence board with pinned documents and amber threads "
    "and a monitor with a dark network graph. Keep his face, hair, short stubble and dark charcoal crew-neck sweater exactly the same. "
    "Soft frontal light on his face, amber accents, photorealistic, 16:9."
)

q = Client("Qwen/Qwen-Image-Edit-2511", token=TOKEN)
jobs = []
for i, pl in enumerate(plates):
    for seed in ((11, 22) if i == 0 else (33,)):
        jobs.append((f"thomas_set_plate{i+1}_s{seed}.png", [PORTRAIT, pl], EDIT_PROMPT, seed))
jobs.append(("thomas_set_solo_s44.png", [PORTRAIT], SOLO_PROMPT, 44))

for name, imgs, prompt, seed in jobs:
    t = time.time()
    try:
        g, _ = q.predict(images=[{"image": handle_file(p), "caption": None} for p in imgs], prompt=prompt, seed=seed,
                         randomize_seed=False, true_guidance_scale=4.0, num_inference_steps=40, height=768, width=1344,
                         rewrite_prompt=False, api_name="/infer")
        p = keep(gallery_paths(g)[0], name)
        log.append({"step": "edit", "name": name, "seed": seed, "seconds": round(time.time() - t, 1), "file": p})
    except Exception as e:
        log.append({"step": "edit", "name": name, "seed": seed, "error": f"{type(e).__name__}: {e}"})
    print(log[-1], flush=True)

json.dump(log, open(f"{OUT}/log.json", "w"), indent=2)
