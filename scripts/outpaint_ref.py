"""Extend Thomas's 16:9 reference to the right (Thomas ends up at ~38% of the width).
Qwen-Image-Edit-2511 fills the grey strip; the original pixels are then pasted back over everything except the new strip,
so Thomas's face, hands and the existing set stay pixel-identical."""
import json, os, shutil, time
import numpy as np
from PIL import Image
from gradio_client import Client, handle_file

TOKEN = os.environ["HF_TOKEN"]
SRC = "presenter/reference/outpaint_canvas_1920x1080.png"   # original shifted left, grey strip x>=1675
KEEP_W, FEATHER = 1675, 48
OUT = "out"; os.makedirs(OUT, exist_ok=True)
PROMPT = ("Fill only the flat grey area on the right side of this image so the room continues naturally: the same dark charcoal wall, "
          "a dark wooden shelf with a few archive boxes softly out of focus, and the walnut desk surface continuing to the right edge, "
          "lit by the same warm amber desk lamp. Same lighting, colours, focus and film grain. Do not change anything else: "
          "keep the man, his face, hands, sweater, the lamp and everything on the desk exactly as they are.")

orig = Image.open(SRC).convert("RGB")
q = Client("Qwen/Qwen-Image-Edit-2511", token=TOKEN)
log = []
for seed in (101, 202):
    t = time.time()
    try:
        g, _ = q.predict(images=[{"image": handle_file(SRC), "caption": None}], prompt=PROMPT, seed=seed, randomize_seed=False,
                         true_guidance_scale=4.0, num_inference_steps=28, height=768, width=1344, rewrite_prompt=False, api_name="/infer")
        item = g[0]; p = item["image"]["path"] if isinstance(item.get("image"), dict) else item["image"]
        gen = Image.open(p).convert("RGB").resize(orig.size, Image.LANCZOS)
        a = np.zeros((orig.size[1], orig.size[0]), np.float32)
        a[:, :KEEP_W - FEATHER] = 1.0
        a[:, KEEP_W - FEATHER:KEEP_W] = np.linspace(1, 0, FEATHER)[None, :]
        a = a[..., None]
        final = (np.asarray(orig, np.float32) * a + np.asarray(gen, np.float32) * (1 - a)).clip(0, 255).astype(np.uint8)
        name = f"thomas_ref_v1_extended_s{seed}_1920x1080.png"
        Image.fromarray(final).save(f"{OUT}/{name}"); shutil.copy(p, f"{OUT}/raw_s{seed}.png")
        log.append({"seed": seed, "seconds": round(time.time() - t, 1), "file": name})
    except Exception as e:
        log.append({"seed": seed, "error": f"{type(e).__name__}: {e}"})
    print(log[-1], flush=True)
json.dump(log, open(f"{OUT}/log.json", "w"), indent=2)
