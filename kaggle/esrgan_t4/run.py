"""Siphon Files: sharpen Thomas's LongCat clips (480p) to the size they are shown at in the episode.

Real-ESRGAN realesr-general-x4v3 (code + weights BSD-3, xinntao), blended 50/50 with the
"wdn" (denoise) variant, run x4 on a Kaggle T4 in fp16, then Lanczos down to 2.25x
(832x480 -> 1872x1080, the exact scale ep001.py uses to place the 480p clips). Audio copied.
The network is defined here (SRVGGNetCompact) so no basicsr install is needed.
"""
import glob, os, subprocess, time, urllib.request
import numpy as np, torch, torch.nn as nn, torch.nn.functional as F
from PIL import Image

T0 = time.time()
def log(*a): print(f"[{time.time()-T0:7.1f}s]", *a, flush=True)

CLIPS = sorted(glob.glob("/kaggle/input/**/thomas_resync_*.mp4", recursive=True))  # run 4: only the 8 re-synced clips (the 12 HF clips are done: run-16)
OUT = "/kaggle/working"
SCALE = 2.25
W = "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/"

class SRVGG(nn.Module):
    def __init__(s, nf=64, nc=32, up=4):
        super().__init__(); s.up = up
        b = [nn.Conv2d(3, nf, 3, 1, 1), nn.PReLU(nf)]
        for _ in range(nc): b += [nn.Conv2d(nf, nf, 3, 1, 1), nn.PReLU(nf)]
        b += [nn.Conv2d(nf, 3 * up * up, 3, 1, 1)]
        s.body = nn.ModuleList(b); s.ps = nn.PixelShuffle(up)
    def forward(s, x):
        o = x
        for m in s.body: o = m(o)
        return s.ps(o) + F.interpolate(x, scale_factor=s.up, mode="nearest")

def weights(name):
    p = f"/tmp/{name}.pth"
    if not os.path.exists(p): urllib.request.urlretrieve(W + name + ".pth", p)
    return torch.load(p, map_location="cpu")["params"]

a, b = weights("realesr-general-x4v3"), weights("realesr-general-wdn-x4v3")
DNI = 1.0  # 1.0 = plain x4v3 (keeps skin/sweater texture); 0.5 made skin waxy (run 1)
net = SRVGG(); net.load_state_dict({k: DNI * a[k] + (1 - DNI) * b[k] for k in a})
net = net.cuda().half().eval()
log("model ready", torch.cuda.get_device_name(0))

def probe(f, entry):
    return subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", f"stream={entry}",
                           "-of", "csv=p=0", f], capture_output=True, text=True).stdout.strip()

log("inputs:", len(CLIPS), CLIPS[:2])
assert CLIPS, "no input clips found under /kaggle/input"
for f in CLIPS:
    name = os.path.basename(f)[:-4]
    w, h = map(int, probe(f, "width,height").split(","))
    fps = probe(f, "r_frame_rate")
    ow, oh = int(round(w * SCALE / 2)) * 2, int(round(h * SCALE / 2)) * 2
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", f, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    dst = f"{OUT}/{name}_sr2.mp4"
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{ow}x{oh}", "-r", fps,
                            "-i", "-", "-i", f, "-map", "0:v", "-map", "1:a?", "-c:v", "libx264", "-preset", "slow", "-crf", "14",
                            "-pix_fmt", "yuv420p", "-c:a", "copy", "-shortest", dst], stdin=subprocess.PIPE)
    n = 0
    while True:
        buf = dec.stdout.read(w * h * 3)
        if len(buf) < w * h * 3: break
        x = torch.from_numpy(np.frombuffer(buf, np.uint8).reshape(h, w, 3).copy()).cuda().permute(2, 0, 1)[None].half() / 255
        with torch.no_grad(): y = net(x).clamp(0, 1)
        y = (y[0].permute(1, 2, 0).float().cpu().numpy() * 255 + 0.5).astype(np.uint8)
        enc.stdin.write(np.asarray(Image.fromarray(y).resize((ow, oh), Image.LANCZOS)).tobytes()); n += 1
    enc.stdin.close(); enc.wait(); dec.wait()
    log(f"{name}: {n} frames -> {ow}x{oh}, {os.path.getsize(dst) >> 10} KB")
log("all done")
