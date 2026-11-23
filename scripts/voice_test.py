"""Speed/quality test: ZONOS3-Mini on CPU, cloning Siphon Narrator v1 from presenter/voice_ref_v1.wav."""
import json, os, time
import soundfile as sf
import torch
from transformers import AutoModel

REF = "presenter/voice_ref_v1.wav"
OUT = "out"
TEXTS = [
    "On March twenty-third, twenty twenty-two, someone walked out of the Ronin bridge with a hundred and "
    "seventy-three thousand six hundred ether. Roughly six hundred and twenty-five million dollars. No alarms. "
    "Nobody noticed for six days. Six days. So how do you lose six hundred million dollars without noticing? "
    "You make it easy.",
    "Here's the thing about bridges. They hold more money than almost anything else in crypto, and they're "
    "guarded by a handful of keys. Get enough of those keys, and the bridge simply does what you tell it to. "
    "That's not a bug. That's the design.",
]

os.makedirs(OUT, exist_ok=True)
torch.set_num_threads(os.cpu_count() or 2)
t0 = time.time()
model = AutoModel.from_pretrained("Zyphra/ZONOS3-Mini-hf", trust_remote_code=True, dtype=torch.float32).to("cpu")
load_s = time.time() - t0

wav, sr = sf.read(REF, dtype="float32", always_2d=True)
emb = model.embed_speaker(wav.T, sr)
torch.save(emb, f"{OUT}/siphon_narrator_v1_embedding.pt")

report = {"load_seconds": round(load_s, 1), "cpu_threads": torch.get_num_threads(), "clips": []}
for i, text in enumerate(TEXTS, 1):
    t = time.time()
    out = model.generate(text, speaker_embedding=emb, language="en_us", seed=1)
    gen_s = time.time() - t
    audio = out.waveform.squeeze().numpy()
    dur = len(audio) / out.sampling_rate
    sf.write(f"{OUT}/test_{i}.wav", audio, out.sampling_rate)
    report["clips"].append({"clip": i, "audio_seconds": round(dur, 1), "gen_seconds": round(gen_s, 1),
                            "real_time_factor": round(gen_s / dur, 2)})
    print(report["clips"][-1], flush=True)

rtf = sum(c["gen_seconds"] for c in report["clips"]) / sum(c["audio_seconds"] for c in report["clips"])
report["avg_real_time_factor"] = round(rtf, 2)
report["est_cpu_minutes_per_12min_episode"] = round(rtf * 12, 1)
json.dump(report, open(f"{OUT}/report.json", "w"), indent=2)
print(json.dumps(report, indent=2))
