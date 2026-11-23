"""Kaggle probe: does a GPU session survive real CUDA work past ~30 s? 3 min of matmuls on the T4."""
import time, subprocess
t0 = time.time()
print("probe start", flush=True)
print(subprocess.run("nvidia-smi --query-gpu=name --format=csv,noheader", shell=True, capture_output=True, text=True).stdout, flush=True)
import torch
x = torch.randn(4096, 4096, device="cuda", dtype=torch.float16)
print("cuda ok", torch.cuda.get_device_name(0), flush=True)
last = 0
while time.time() - t0 < 180:
    for _ in range(50):
        y = x @ x
    torch.cuda.synchronize()
    if time.time() - last > 10:
        last = time.time()
        print(f"alive {time.time() - t0:.0f}s  mem {torch.cuda.memory_allocated() >> 20} MB", flush=True)
print("probe done", flush=True)
