"""LongCat-Video-Avatar 1.6 on Kaggle's free T4 x2: several chained clips in one run
(each clip = 93 frames @25 fps = 3.72 s). v2 after the first run's OOM (21 nov 2026):
FFN computed in token chunks (exact, per-token op), blocks rebalanced across the two GPUs,
expandable CUDA segments, VAE decoded separately with tiling, chained clips continue from the exact
(uncompressed) frame of the previous clip. Each finished clip is written to /kaggle/working/out at
once; the run stops at the first failed clip and keeps everything finished before it.

Runs as a Kaggle "script" kernel. Inputs come from the private dataset siphon-longcat-inputs
(job.json + reference image + wav). Everything is written to /kaggle/working/out.

T4 (sm75) adaptations vs. the official demo:
- fp16 instead of bf16 for the DiT/VAE (T4 has no native bf16); attention through PyTorch SDPA
  (a tiny `flash_attn` shim), since FlashAttention-2 does not support T4.
- INT8 weight-only DiT (base_model_int8), split across the two T4s (blocks 0..SPLIT-1 on cuda:0,
  the rest on cuda:1); built on the meta device so it never needs 54 GB of RAM.
- UMT5 text encoder (bf16) and Whisper run first on cuda:1, results cached, then freed.
- No vocal separation (the TTS audio is already clean, like the Space's "Clean speech" mode).
Guards: aborts if a denoising step produces NaN/inf or if the first step takes too long, so a
broken run does not burn the weekly quota.
"""
import os, sys, json, time, math, glob, shutil, subprocess, types, datetime
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

T0 = time.time()
LOG = []
def log(*a):
    msg = f"[{time.time()-T0:7.1f}s] " + " ".join(str(x) for x in a)
    print(msg, flush=True)
    LOG.append(msg)

OUT = "/kaggle/working/out"
os.makedirs(OUT, exist_ok=True)
def save_log(extra=None):
    meta = {"log": LOG, "elapsed_s": round(time.time() - T0, 1)}
    if extra:
        meta.update(extra)
    json.dump(meta, open(os.path.join(OUT, "run_log.json"), "w"), indent=2)

def sh(cmd):
    log("$", cmd)
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        log(r.stdout[-3000:], r.stderr[-3000:])
        raise RuntimeError(f"command failed: {cmd}")
    return r.stdout

try:
    # ---------------- inputs ----------------
    inp = glob.glob("/kaggle/input/**/job.json", recursive=True)
    assert inp, "job.json not found in /kaggle/input"
    IN_DIR = os.path.dirname(inp[0])
    job = json.load(open(inp[0]))
    JOBS = job["jobs"]
    log(len(JOBS), "clips; inputs in", IN_DIR)
    SPLIT = int(job.get("split", 22))
    FFN_CHUNK = int(job.get("ffn_chunk", 4096))
    MAX_FIRST_STEP_S = float(job.get("max_first_step_s", 1500))
    log(sh("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader"))
    log(sh("df -h /tmp /kaggle/working | tail -2"))
    log(sh("free -g | head -2"))
    if not shutil.which("ffmpeg"):
        sh("pip install -q imageio-ffmpeg && ln -sf $(python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())') /usr/local/bin/ffmpeg")

    # ---------------- code + deps ----------------
    W = "/tmp/lcv"
    if not os.path.isdir(W):
        sh(f"git clone -q --depth 1 -b dev/lcavatar_v1d6 https://github.com/meituan-longcat/LongCat-Video {W}")
    sh(f"cd {W} && git log -1 --format=%H")
    sh("pip install -q diffusers==0.35.1 loguru ftfy einops pyloudnorm librosa imageio imageio-ffmpeg regex hf_transfer 2>&1 | tail -2")
    # fp16 everywhere in the LongCat code (T4 has no native bf16)
    n = 0
    for f in glob.glob(f"{W}/longcat_video/**/*.py", recursive=True):
        s = open(f).read()
        if "torch.bfloat16" in s:
            open(f, "w").write(s.replace("torch.bfloat16", "torch.float16"))
            n += 1
    log("patched bf16->fp16 in", n, "files")
    # flash_attn shim on top of SDPA
    shim = os.path.join("/tmp/shim")
    os.makedirs(os.path.join(shim, "flash_attn"), exist_ok=True)
    open(os.path.join(shim, "flash_attn", "__init__.py"), "w").write('''
import torch
import torch.nn.functional as F

def flash_attn_func(q, k, v, dropout_p=0.0, softmax_scale=None, causal=False, **kw):
    # q,k,v: [B, S, H, D]
    dt = q.dtype
    q, k, v = (t.transpose(1, 2).to(torch.float16) for t in (q, k, v))
    o = F.scaled_dot_product_attention(q, k, v, scale=softmax_scale, is_causal=causal)
    return o.transpose(1, 2).to(dt)

def flash_attn_varlen_func(q, k, v, cu_seqlens_q, cu_seqlens_k, max_seqlen_q=None, max_seqlen_k=None,
                           dropout_p=0.0, softmax_scale=None, causal=False, **kw):
    # q: [Nq_total, H, D], k/v: [Nk_total, H, D]
    dt = q.dtype
    outs = []
    cq = cu_seqlens_q.tolist(); ck = cu_seqlens_k.tolist()
    for i in range(len(cq) - 1):
        qi = q[cq[i]:cq[i+1]].transpose(0, 1)[None].to(torch.float16)
        ki = k[ck[i]:ck[i+1]].transpose(0, 1)[None].to(torch.float16)
        vi = v[ck[i]:ck[i+1]].transpose(0, 1)[None].to(torch.float16)
        o = F.scaled_dot_product_attention(qi, ki, vi, scale=softmax_scale, is_causal=causal)
        outs.append(o[0].transpose(0, 1))
    return torch.cat(outs, 0).to(dt)
''')
    sys.path.insert(0, shim)
    sys.path.insert(0, W)
    os.chdir(W)

    # ---------------- weights ----------------
    os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
    from huggingface_hub import snapshot_download
    CK = "/tmp/weights"
    t = time.time()
    snapshot_download("meituan-longcat/LongCat-Video", local_dir=f"{CK}/LongCat-Video",
                      allow_patterns=["tokenizer/*", "text_encoder/*", "vae/*"])
    snapshot_download("meituan-longcat/LongCat-Video-Avatar-1.6", local_dir=f"{CK}/LongCat-Video-Avatar-1.6",
                      allow_patterns=["base_model_int8/*", "loraA/*", "loraB/*", "scheduler/*",
                                      "whisper-large-v3/*", "*.json"])
    log("weights downloaded in", round(time.time() - t), "s;", sh(f"du -sh {CK}/* | tr '\\n' ' '"))
    AV = f"{CK}/LongCat-Video-Avatar-1.6"
    BASE = f"{CK}/LongCat-Video"

    import numpy as np
    import torch
    import torch.distributed as dist
    import librosa
    from PIL import Image

    os.environ.update(RANK="0", WORLD_SIZE="1", LOCAL_RANK="0", MASTER_ADDR="127.0.0.1", MASTER_PORT="29511")
    torch.cuda.set_device(0)
    dist.init_process_group(backend="nccl", timeout=datetime.timedelta(hours=6))
    from longcat_video.context_parallel import context_parallel_util
    context_parallel_util.init_context_parallel(context_parallel_size=1, global_rank=0, world_size=1)
    cp_split_hw = context_parallel_util.get_optimal_split(1)

    from transformers import AutoTokenizer, UMT5EncoderModel
    from longcat_video.pipeline_longcat_video_avatar import LongCatVideoAvatarPipeline
    from longcat_video.modules.scheduling_flow_match_euler_discrete import FlowMatchEulerDiscreteScheduler
    from longcat_video.modules.autoencoder_kl_wan import AutoencoderKLWan
    from longcat_video.modules.quantization import QuantizedLinear, DEFAULT_SKIP_PATTERNS
    from longcat_video.modules.avatar.longcat_video_dit_avatar import LongCatVideoAvatarTransformer3DModel
    from longcat_video.audio_process import get_audio_encoder, get_audio_feature_extractor
    from longcat_video.audio_process.torch_utils import save_video_ffmpeg
    DT = torch.float16
    D0, D1 = torch.device("cuda:0"), torch.device("cuda:1")
    import longcat_video.modules.blocks as lc_blocks
    _ffn_fwd = lc_blocks.FeedForwardSwiGLU.forward
    def ffn_chunked(self, x):
        # per-token op: chunking along the sequence gives the exact same result with far less memory
        if x.dim() != 3 or x.shape[1] <= FFN_CHUNK:
            return _ffn_fwd(self, x)
        return torch.cat([_ffn_fwd(self, x[:, i:i + FFN_CHUNK]) for i in range(0, x.shape[1], FFN_CHUNK)], 1)
    lc_blocks.FeedForwardSwiGLU.forward = ffn_chunked
    torch.backends.cuda.enable_flash_sdp(False)
    torch.backends.cuda.enable_mem_efficient_sdp(True)

    prompt = job["prompt"]
    negative_prompt = ("Close-up, Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, "
        "images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, "
        "poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy "
        "background, three legs, many people in the background, walking backwards")
    save_fps, num_frames = 25, 93
    image_path = os.path.join(IN_DIR, os.path.basename(job["image"]))

    # ---------------- phase A: text + audio on cuda:1 ----------------
    tokenizer = AutoTokenizer.from_pretrained(BASE, subfolder="tokenizer")
    te = UMT5EncoderModel.from_pretrained(BASE, subfolder="text_encoder", torch_dtype=torch.bfloat16).eval()
    TE_DEV = D1
    try:
        te.to(D1)
        with torch.no_grad():
            _ = te(torch.ones(1, 8, dtype=torch.long, device=D1), torch.ones(1, 8, dtype=torch.long, device=D1))
        log("text encoder: bf16 on cuda:1")
    except Exception as e:
        log("bf16 text encoder on T4 failed (", repr(e)[:200], ") -> CPU bf16")
        te.to("cpu"); torch.cuda.empty_cache(); TE_DEV = torch.device("cpu")
    cache = {}

    class TE(torch.nn.Module):
        dtype = DT
        def __init__(self, real):
            super().__init__()
            self.real = real
        def forward(self, ids, mask):
            key = (tuple(ids.flatten().tolist()))
            if key not in cache:
                assert self.real is not None, "text embedding cache miss after encoder was freed"
                with torch.no_grad():
                    h = self.real(ids.to(TE_DEV), mask.to(TE_DEV)).last_hidden_state.float()
                if not torch.isfinite(h).all():
                    raise RuntimeError("text encoder produced NaN/inf")
                cache[key] = h.to(DT).to(D0)
            return types.SimpleNamespace(last_hidden_state=cache[key])

    vae = AutoencoderKLWan.from_pretrained(BASE, subfolder="vae", torch_dtype=DT).to(D0).eval()
    scheduler = FlowMatchEulerDiscreteScheduler.from_pretrained(AV, subfolder="scheduler")
    te_wrap = TE(te)
    pipe = LongCatVideoAvatarPipeline(tokenizer=tokenizer, text_encoder=te_wrap, vae=vae, scheduler=scheduler,
                                      dit=None, model_type="avatar-v1.5")
    with torch.no_grad():
        pipe.encode_prompt(prompt=prompt, negative_prompt=negative_prompt, do_classifier_free_guidance=True,
                           num_videos_per_prompt=1, max_sequence_length=512, device=D0, dtype=DT)
    te_wrap.real = None
    del te
    torch.cuda.empty_cache()
    log("text encoded and cached:", len(cache), "entries")

    audio_encoder = get_audio_encoder(f"{AV}/whisper-large-v3", "avatar-v1.5").to(D1)
    fe = get_audio_feature_extractor(f"{AV}/whisper-large-v3", "avatar-v1.5")
    fake = types.SimpleNamespace(audio_encoder=audio_encoder, audio_feature_extractor=fe)
    AUDIO = {}
    for jb in JOBS:
        speech, sr = librosa.load(os.path.join(IN_DIR, jb["audio"]), sr=16000, mono=True)
        need = math.ceil((num_frames / save_fps + 1.0) * sr) - len(speech)
        if need > 0:
            speech = np.append(speech, np.zeros(need, dtype=speech.dtype))
        with torch.no_grad():
            emb = LongCatVideoAvatarPipeline.get_audio_embedding_whisper(
                fake, speech, fps=save_fps, device=D1, sample_rate=sr, use_loudness_norm=False)
        assert torch.isfinite(emb).all(), "audio embedding NaN " + jb["name"]
        idx = torch.arange(5) - 2
        center = torch.clamp(torch.arange(0, num_frames).unsqueeze(1) + idx.unsqueeze(0), min=0, max=emb.shape[0] - 1)
        AUDIO[jb["name"]] = emb[center][None].cpu()
    del audio_encoder, fake
    torch.cuda.empty_cache()
    log("audio embeddings for", len(AUDIO), "clips", tuple(next(iter(AUDIO.values())).shape))

    # ---------------- phase B: INT8 DiT on meta, loaded shard by shard ----------------
    from accelerate import init_empty_weights
    from safetensors.torch import load_file
    qdir = f"{AV}/base_model_int8"
    cfg = json.load(open(f"{qdir}/config.json"))
    for k in ("_class_name", "architectures", "_diffusers_version", "model_max_length"):
        cfg.pop(k, None)
    cfg.update(cp_split_hw=cp_split_hw, enable_flashattn3=False, enable_flashattn2=True,
               enable_xformers=False, enable_bsa=False)
    with init_empty_weights(include_buffers=False):
        dit = LongCatVideoAvatarTransformer3DModel(**cfg)
    repl = {}
    for name, m in dit.named_modules():
        if isinstance(m, torch.nn.Linear) and not any(p in name for p in DEFAULT_SKIP_PATTERNS):
            with init_empty_weights(include_buffers=True):
                repl[name] = QuantizedLinear(m.in_features, m.out_features, bias=m.bias is not None)
    for name, ql in repl.items():
        parent = dit
        *path, last = name.split(".")
        for p in path:
            parent = getattr(parent, p)
        setattr(parent, last, ql)
    loaded = set()
    for shard in sorted(glob.glob(f"{qdir}/*.safetensors")):
        sd = load_file(shard, device="cpu")
        sd = {k: (v.to(DT) if v.dtype in (torch.float32, torch.bfloat16) and not k.endswith("weight_scale") else v)
              for k, v in sd.items()}
        dit.load_state_dict(sd, strict=False, assign=True)
        loaded |= set(sd)
        del sd
    expected = set(dit.state_dict().keys())
    missing = [k for k in expected if k not in loaded]
    still_meta = [n for n, p in list(dit.named_parameters()) + list(dit.named_buffers()) if p.is_meta]
    log("dit keys loaded", len(loaded), "missing", len(missing), missing[:5], "meta", still_meta[:5])
    assert not still_meta, "some DiT tensors were never loaded"
    for m in dit.modules():
        if isinstance(m, QuantizedLinear):
            continue
        for pn, p in m.named_parameters(recurse=False):
            if p.dtype == torch.float32:
                p.data = p.data.to(DT)
    dit.eval()

    # distillation LoRAs (DMD + OPSD), as recommended for 1.6: mix_steps=4, mix_alpha=1.0
    dit.load_lora(f"{AV}/loraA/lora.safetensors", "dmd", multiplier=1.0, lora_network_dim=128, lora_network_alpha=64)
    dit.load_lora(f"{AV}/loraB/lora.safetensors", "opsd", multiplier=1.0, lora_network_dim=128, lora_network_alpha=64)
    dit.enable_lora_mix("dmd", "opsd", float(job.get("mix_alpha", 1.0)), int(job.get("mix_steps", 4)))

    # place: everything on cuda:0, blocks SPLIT.. on cuda:1
    nb = len(dit.blocks)
    for cname, child in dit.named_children():
        if cname != "blocks":
            child.to(D0)
    for pn, p in list(dit._parameters.items()):
        if p is not None:
            p.data = p.data.to(D0)
    for bn, b in list(dit._buffers.items()):
        if b is not None:
            dit._buffers[bn] = b.to(D0)
    for i in range(nb):
        dit.blocks[i].to(D0 if i < SPLIT else D1)
    # LoRA modules follow their target layer
    def owner_device(module_name):
        mod = dit
        for part in module_name.split("."):
            mod = getattr(mod, part)
        for t_ in list(mod.buffers()) + list(mod.parameters()):
            return t_.device
        return D0
    for net in dit.lora_dict.values():
        for lora in net.loras:
            mn = lora.lora_name.replace("lora___lorahyphen___", "").replace("___lorahyphen___", ".")
            lora.to(owner_device(mn), dtype=DT)

    def move(x, dev):
        if torch.is_tensor(x):
            return x.to(dev) if x.device != dev else x
        if isinstance(x, (list, tuple)):
            return type(x)(move(y, dev) for y in x)
        if isinstance(x, dict):
            return {k: move(v, dev) for k, v in x.items()}
        return x
    def pre_hook(mod, args, kwargs):
        dev = next(iter(list(mod.buffers()) + list(mod.parameters()))).device
        return move(args, dev), move(kwargs, dev)
    for i, b in enumerate(dit.blocks):
        b.register_forward_pre_hook(pre_hook, with_kwargs=True)
    dit.final_layer.register_forward_pre_hook(pre_hook, with_kwargs=True)
    torch.cuda.empty_cache()
    log("DiT placed: blocks 0-%d cuda:0, %d-%d cuda:1;" % (SPLIT - 1, SPLIT, nb - 1),
        "mem GB:", round(torch.cuda.memory_allocated(0) / 2**30, 2), round(torch.cuda.memory_allocated(1) / 2**30, 2))

    # step timing + NaN guard (wrap the DiT forward)
    step_t = {"t": time.time(), "n": 0}
    orig_forward = dit.forward
    def guarded_forward(*a, **k):
        out = orig_forward(*a, **k)
        o = out[0] if isinstance(out, tuple) else out
        step_t["n"] += 1
        dt_ = time.time() - step_t["t"]
        step_t["t"] = time.time()
        bad = not torch.isfinite(o).all().item()
        log(f"DiT forward {step_t['n']}: {dt_:.1f}s", "NaN/inf!" if bad else "ok",
            "peak GB", round(torch.cuda.max_memory_allocated(0) / 2**30, 1), round(torch.cuda.max_memory_allocated(1) / 2**30, 1))
        save_log()
        if bad:
            raise RuntimeError("NaN/inf in DiT output (fp16 overflow) - aborting")
        if step_t["n"] == 1 and dt_ > MAX_FIRST_STEP_S:
            raise RuntimeError(f"first step took {dt_:.0f}s > {MAX_FIRST_STEP_S:.0f}s - aborting to save quota")
        return out
    dit.forward = guarded_forward

    pipe.dit = dit
    vae.enable_tiling()
    REF = Image.open(image_path).convert("RGB")
    FRAMES = {}
    done = []
    for n_, jb in enumerate(JOBS):
        name = jb["name"]
        cf = jb.get("continue_from")
        if cf:
            prev = FRAMES[cf["job"]]
            fi = min(len(prev) - 1, int(round(cf["at"] * save_fps)))
            image = Image.fromarray(prev[fi])
            log(f"[{n_+1}/{len(JOBS)}] {name}: continuing from {cf['job']} frame {fi}")
        else:
            image = REF
            log(f"[{n_+1}/{len(JOBS)}] {name}: from the reference image")
        generator = torch.Generator(device=D0)
        generator.manual_seed(int(job.get("seed", 42)))
        step_t["t"] = time.time(); step_t["n"] = 0
        torch.cuda.reset_peak_memory_stats(0); torch.cuda.reset_peak_memory_stats(1)
        t_gen = time.time()
        with torch.no_grad():
            latent = pipe.generate_ai2v(
                image=image, prompt=prompt, negative_prompt=negative_prompt,
                resolution=job.get("resolution", "480p"), num_frames=num_frames, num_inference_steps=8,
                text_guidance_scale=1.0, audio_guidance_scale=1.0, output_type="latent",
                generator=generator, audio_emb=AUDIO[name].to(D0), use_distill=True)
            torch.cuda.empty_cache()
            lat = pipe.denormalize_latents(latent.to(vae.dtype).to(D0))
            try:
                vid = pipe._decode_video_latents(lat)
            except torch.OutOfMemoryError:
                log("VAE decode OOM on cuda:0 -> parking the cuda:0 DiT blocks on the CPU for the decode")
                torch.cuda.empty_cache()
                parked = [b for b in dit.blocks if next(b.parameters()).device == D0]
                for b in parked:
                    b.to("cpu")
                torch.cuda.empty_cache()
                vid = pipe._decode_video_latents(lat)
                for b in parked:
                    b.to(D0)
            frames = pipe.video_processor.postprocess_video(vid)
        video = (np.clip(np.asarray(frames[0]), 0, 1) * 255).round().astype(np.uint8)
        del latent, lat, vid
        torch.cuda.empty_cache()
        gen_s = time.time() - t_gen
        FRAMES[name] = video
        save_video_ffmpeg(torch.from_numpy(video), os.path.join(OUT, name), os.path.join(IN_DIR, jb["audio"]),
                          fps=save_fps, quality=10)
        Image.fromarray(video[0]).save(os.path.join(OUT, name + "_f0.png"))
        Image.fromarray(video[-1]).save(os.path.join(OUT, name + "_flast.png"))
        done.append({"name": name, "generate_s": round(gen_s, 1), "frames": int(video.shape[0]),
                     "size": list(video.shape[1:3])})
        log(f"{name} OK in {gen_s:.0f}s, frames {video.shape}, peak GB",
            round(torch.cuda.max_memory_allocated(0) / 2**30, 1), round(torch.cuda.max_memory_allocated(1) / 2**30, 1))
        save_log({"status": "running", "done": done})
    save_log({"status": "ok", "done": done})
    log("DONE", len(done), "clips")
except Exception as e:
    import traceback
    log("FAILED:", repr(e))
    log(traceback.format_exc()[-4000:])
    save_log({"status": "failed", "error": repr(e), "done": globals().get("done", [])})
    sys.exit(1)
