"""LatentSync 1.5 lip re-sync on Kaggle's free T4 (Siphon Files, ep. 001 extra Thomas time).

Takes existing Thomas footage (LongCat clips already generated on Hugging Face, chained into
continuous takes) and redraws only the mouth area so it speaks new lines of the episode.
Inputs (private dataset siphon-latentsync-inputs): job.json, footage_*.mp4, resync_*.wav.
Output: /kaggle/working/out/<name>.mp4 (+ first/last frame png, run_log.json).

Licensing: LatentSync code Apache-2.0, weights OpenRAIL++ (commercial use allowed with use
restrictions); sd-vae-ft-mse MIT. The InsightFace detector used upstream is replaced by OpenCV's
YuNet (MIT, opencv_zoo), because InsightFace's pretrained models are non-commercial.
T4: fp16 (SD-family UNet, safe in fp16), DeepCache on.
"""
import os, sys, json, time, glob, subprocess, shutil

T0 = time.time()
LOG = []
OUT = "/kaggle/working/out"
os.makedirs(OUT, exist_ok=True)


def log(*a):
    m = f"[{time.time() - T0:7.1f}s] " + " ".join(str(x) for x in a)
    print(m, flush=True)
    LOG.append(m)


def save_log(extra=None):
    d = {"log": LOG, "elapsed_s": round(time.time() - T0, 1)}
    d.update(extra or {})
    json.dump(d, open(os.path.join(OUT, "run_log.json"), "w"), indent=2)


def sh(cmd, cwd=None):
    log("$", cmd)
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if r.returncode != 0:
        log(r.stdout[-3000:], r.stderr[-3000:])
        raise RuntimeError("command failed: " + cmd)
    return r.stdout


done = []
try:
    jf = glob.glob("/kaggle/input/**/job.json", recursive=True)
    assert jf, "job.json missing"
    IN = os.path.dirname(jf[0])
    job = json.load(open(jf[0]))
    log(len(job["jobs"]), "clips; inputs in", IN)
    log(sh("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader"))
    if not shutil.which("ffmpeg"):
        sh("pip install -q imageio-ffmpeg && ln -sf $(python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())') /usr/local/bin/ffmpeg")

    W = "/tmp/ls"
    sh(f"git clone -q https://github.com/bytedance/LatentSync {W}")
    sh(f"git -C {W} log -1 --format=%H")
    sh("pip install -q diffusers==0.32.2 'transformers<5' 'huggingface_hub<1' omegaconf python_speech_features kornia DeepCache einops more_itertools tiktoken ffmpeg-python imageio imageio-ffmpeg librosa soundfile 2>&1 | tail -2")
    # 1) no decord on this Python: the pipeline reads video with OpenCV anyway
    u = f"{W}/latentsync/utils/util.py"
    s = open(u).read().replace("from decord import AudioReader, VideoReader",
                               "try:\n    from decord import AudioReader, VideoReader\nexcept Exception:\n    AudioReader = VideoReader = None")
    # decord's AudioReader is gone too: read the (already 16 kHz mono) wav with librosa instead
    s = s.replace("    ar = AudioReader(audio_path, sample_rate=audio_sample_rate, mono=True)\n\n    # To access the audio samples\n    audio_samples = torch.from_numpy(ar[:].asnumpy())\n    audio_samples = audio_samples.squeeze(0)",
                  "    import librosa\n    y, _ = librosa.load(audio_path, sr=audio_sample_rate, mono=True)\n    audio_samples = torch.from_numpy(y)")
    assert "librosa.load" in s, "read_audio patch did not apply"
    open(u, "w").write(s)
    # 2) fp16 on T4 (sm75)
    p = f"{W}/scripts/inference.py"
    s = open(p).read().replace("get_device_capability()[0] > 7", "get_device_capability()[0] >= 7")
    open(p, "w").write(s)
    # 3) face detector: OpenCV YuNet (MIT) instead of InsightFace (non-commercial models)
    sh(f"mkdir -p {W}/checkpoints && curl -sL -o {W}/checkpoints/yunet.onnx "
       "https://media.githubusercontent.com/media/opencv/opencv_zoo/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx")
    open(f"{W}/latentsync/utils/face_detector.py", "w").write('''
import cv2, numpy as np

class FaceDetector:
    """YuNet face + 5 landmarks. Returns (bbox, lmk106) where only the indices the ImageProcessor
    uses are filled: brows (43,48,49,50,51 = image-left brow; 101..105 = image-right brow) and
    nose (74,77,83,86). Brows are placed above the eyes by a fixed fraction of the eye distance,
    so the affine crop stays consistent from frame to frame."""
    def __init__(self, device="cuda"):
        self.det = None
    def __call__(self, frame, threshold=0.5):
        h, w = frame.shape[:2]
        if self.det is None or self.size != (w, h):
            self.det = cv2.FaceDetectorYN.create("checkpoints/yunet.onnx", "", (w, h), 0.6, 0.3, 5000)
            self.size = (w, h)
        img = cv2.cvtColor(np.ascontiguousarray(frame), cv2.COLOR_RGB2BGR)
        _, faces = self.det.detect(img)
        if faces is None or len(faces) == 0:
            return None, None
        f = max(faces, key=lambda r: r[2] * r[3])
        x, y, bw, bh = f[:4]
        re_, le_, nose = np.array(f[4:6]), np.array(f[6:8]), np.array(f[8:10])
        a, b = (re_, le_) if re_[0] < le_[0] else (le_, re_)     # a = image-left eye
        d = np.linalg.norm(b - a)
        up = np.array([0.0, -0.20 * d])
        lmk = np.zeros((106, 2), dtype=np.float64)
        for i in (43, 48, 49, 50, 51):
            lmk[i] = a + up
        for i in (101, 102, 103, 104, 105):
            lmk[i] = b + up
        for i in (74, 77, 83, 86):
            lmk[i] = nose
        x1, y1, x2, y2 = int(max(0, x)), int(max(0, y)), int(min(w, x + bw)), int(min(h, y + bh))
        return (x1, y1, x2, y2), np.round(lmk).astype(np.int_)
''')
    os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"
    from huggingface_hub import hf_hub_download, snapshot_download
    hf_hub_download("ByteDance/LatentSync-1.5", "latentsync_unet.pt", local_dir=f"{W}/checkpoints")
    hf_hub_download("ByteDance/LatentSync-1.5", "whisper/tiny.pt", local_dir=f"{W}/checkpoints")
    snapshot_download("stabilityai/sd-vae-ft-mse")      # MIT; the script loads it by name
    log("weights ready")

    for n, jb in enumerate(job["jobs"]):
        name = jb["name"]
        vid = os.path.join(IN, jb["video"])
        aud = os.path.join(IN, jb["audio"])
        out = os.path.join(OUT, name + ".mp4")
        log(f"[{n + 1}/{len(job['jobs'])}] {name}: {jb['video']} + {jb['audio']}")
        t = time.time()
        sh(f"python -m scripts.inference --unet_config_path configs/unet/stage2.yaml "
           f"--inference_ckpt_path checkpoints/latentsync_unet.pt --inference_steps {job.get('steps', 20)} "
           f"--guidance_scale {job.get('guidance', 1.5)} --enable_deepcache --seed {job.get('seed', 1247)} "
           f"--video_path {vid} --audio_path {aud} --video_out_path {out}", cwd=W)
        sh(f"ffmpeg -v error -y -i {out} -frames:v 1 {OUT}/{name}_f0.png")
        done.append({"name": name, "seconds": round(time.time() - t, 1)})
        log(f"{name} OK in {time.time() - t:.0f}s")
        save_log({"status": "running", "done": done})
    save_log({"status": "ok", "done": done})
    log("DONE", len(done))
except Exception as e:
    import traceback
    log("FAILED:", repr(e))
    log(traceback.format_exc()[-3000:])
    save_log({"status": "failed", "error": repr(e), "done": done})
    sys.exit(1)
