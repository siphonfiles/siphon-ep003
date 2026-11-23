"""Fix the desk props of the (mirrored) three-quarter reference with ONE Qwen-Image-Edit-2511 edit.
Image 1 = mirrored three-quarter view (keep man, pose, lamp, background); image 2 = front reference (the props to copy)."""
import json, os, shutil, time
from gradio_client import Client, handle_file

OUT = "out"; os.makedirs(OUT, exist_ok=True)
BASE = "presenter/reference/thomas_ref_threequarter_s55_mirrored.png"
FRONT = "presenter/reference/thomas_ref_v1_source_1344x768.png"
SEED = int(os.environ.get("SEED", "55"))
PROMPT = (
    "Edit image 1 only on the desk surface; keep everything else in image 1 exactly the same: the same man, face, hair, sweater, pose, "
    "hands, chair, the brass desk lamp on the right side of the frame, the background and the lighting. "
    "Make the desk objects match image 2: replace the thick ring binder with the same thin closed manila case folder lying flat "
    "on a dark leather desk pad, with his hands resting on it and his eyes reading it. "
    "Add the stack of white papers held with a black binder clip on the desk in the left foreground, nearest to the camera. "
    "Add a few loose white sheets of paper on the desk near the base of the lamp. "
    "Photorealistic, same dark charcoal and deep navy tones with warm amber lamp light, 16:9."
)
t = time.time()
q = Client("Qwen/Qwen-Image-Edit-2511", token=os.environ["HF_TOKEN"])
g, _ = q.predict(images=[{"image": handle_file(p), "caption": None} for p in (BASE, FRONT)], prompt=PROMPT, seed=SEED,
                 randomize_seed=False, true_guidance_scale=4.0, num_inference_steps=40, height=768, width=1344,
                 rewrite_prompt=False, api_name="/infer")
item = g[0]; img = item.get("image") if isinstance(item, dict) else item
shutil.copy(img["path"] if isinstance(img, dict) else img, f"{OUT}/thomas_ref_threequarter_fix_s{SEED}.png")
json.dump({"seed": SEED, "seconds": round(time.time() - t, 1), "prompt": PROMPT}, open(f"{OUT}/log.json", "w"), indent=2)
print("done", round(time.time() - t, 1), "s")
