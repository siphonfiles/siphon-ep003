"""Siphon Files: Z-Image-Turbo (Apache-2.0) illustrations on a Kaggle T4, same settings as the HF Space
(2048x1152, 8 DiT steps, shift 3, fixed seeds, same style suffix). No dataset: jobs are embedded below.
bf16 (emulated on T4; fp16 overflowed to NaN in run 1). A flat/NaN image is logged as an error. Output: /kaggle/working/<id>.png + run_log.json."""
import json, os, subprocess, sys, time, traceback
T0 = time.time(); LOG = []
def log(*a):
    s = f"[{time.time()-T0:7.1f}s] " + " ".join(map(str, a)); print(s, flush=True); LOG.append(s)
def save(status, err=None):
    json.dump({"status": status, "error": err, "log": LOG, "results": RES}, open("/kaggle/working/run_log.json", "w"), indent=1)
RES = []
try:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-U", "diffusers>=0.36", "transformers>=4.51,<5", "accelerate", "huggingface_hub<1"], check=True)
    import numpy as np, torch
    from diffusers import ZImagePipeline, FlowMatchEulerDiscreteScheduler
    JOBS = json.loads(r'''__JOBS__''')
    STYLE = (" Cinematic 3D render for a premium investigative documentary, stylized realism with clean matte materials, "
             "low-key lighting with deep navy and charcoal shadows, one warm amber key light as the only strong accent, "
             "a subtle cool teal rim light, soft volumetric haze, shallow depth of field, 35mm lens, "
             "clearly separated foreground, midground and background layers, calm restrained mood, fine film grain.")
    log("gpus", torch.cuda.device_count(), torch.cuda.get_device_name(0))
    def load(dtype):
        p = ZImagePipeline.from_pretrained("Tongyi-MAI/Z-Image-Turbo", torch_dtype=dtype)
        p.scheduler = FlowMatchEulerDiscreteScheduler.from_config(p.scheduler.config, shift=3.0)
        p.enable_model_cpu_offload(); p.vae.enable_tiling()
        return p
    dtype = torch.bfloat16; pipe = load(dtype)  # run 1: fp16 gave NaN (black image) at 78 s/image; reloading inside the script got OOM-killed (RAM); log("loaded", dtype)
    for j in JOBS["images"]:
        for attempt in range(2):
            t = time.time()
            try:
                g = torch.Generator("cpu").manual_seed(j["seed"])
                im = pipe(prompt=j["prompt"].strip() + STYLE, width=2048, height=1152, num_inference_steps=9,
                          guidance_scale=0.0, generator=g).images[0]
                a = np.asarray(im).astype(float)
                if a.std() < 3:  # NaN decodes to a flat (usually black) image
                    raise FloatingPointError(f"flat image (std {a.std():.2f}) - fp overflow")
                im.save(f"/kaggle/working/{j['id']}.png")
                RES.append({"id": j["id"], "seed": j["seed"], "dtype": str(dtype), "seconds": round(time.time() - t, 1)})
                log(j["id"], "ok", RES[-1]["seconds"], "s", dtype); save("running"); break
            except FloatingPointError as e:
                log(j["id"], "NaN/flat with", dtype, e)
                if dtype == torch.bfloat16: RES.append({"id": j["id"], "error": str(e)}); break
                del pipe; torch.cuda.empty_cache(); dtype = torch.bfloat16; pipe = load(dtype); log("reloaded", dtype)
            except Exception as e:
                log(j["id"], "ERROR", type(e).__name__, e); RES.append({"id": j["id"], "error": f"{type(e).__name__}: {e}"})
                torch.cuda.empty_cache(); break
    save("done")
except Exception as e:
    log("FATAL", traceback.format_exc()); save("error", f"{type(e).__name__}: {e}")
