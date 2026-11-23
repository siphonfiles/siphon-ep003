"""Generate a ~5 s Thomas clip with LongCat-Video-Avatar 1.6 via a ZeroGPU Space (uses the
account's daily ZeroGPU quota through HF_TOKEN; no paid credits as long as quota remains and
auto-recharge stays off).

Usage: python scripts/longcat_clip.py presenter/clips/inputs/<job>.json out/
"""
import json, os, shutil, sys, time
from gradio_client import Client, handle_file

job = json.load(open(sys.argv[1]))
out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
space = job.get("space", "victor/LongCat-Video-Avatar-1.6")

image = job["image"]
cf = job.get("continue_from")
if cf:  # seamless chain: start from the exact frame of the previous clip at the seam
    import subprocess
    image = os.path.join(out_dir, job["name"] + "_seed_frame.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", cf["clip"], "-ss", str(cf["at"]), "-frames:v", "1", image], check=True)
    print("continuing from", cf["clip"], "at", cf["at"], "s")
client = Client(space, token=os.environ["HF_TOKEN"])
t0 = time.time()
res = client.predict(
    handle_file(image), handle_file(job["audio"]), job["prompt"], job["resolution"],
    job["seed"], job["vocal_mode"], job["acceleration"], api_name="/generate")
wall = time.time() - t0
path = res["video"] if isinstance(res, dict) else res
dst = os.path.join(out_dir, job["name"] + ".mp4")
shutil.copy(path, dst)
meta = dict(job, wall_seconds=round(wall, 1), space=space, output=os.path.basename(dst))
json.dump(meta, open(os.path.join(out_dir, job["name"] + ".json"), "w"), indent=2)
print(json.dumps(meta, indent=2))
