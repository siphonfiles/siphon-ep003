"""Kaggle LatentSync inputs for the ep. 003 Thomas lines that have no Hugging Face clip of their own.

Each line gets one 5 s shot: a 720p HF clip from a distant part of the episode, with only the mouth
redrawn to speak the new line. The audio has the same layout as the HF clips (0.3 s lead + line +
silence to 5 s), so the clip plan treats both kinds alike. Consecutive lines alternate cameras.

Usage: python3 scripts/make_ep003_resync_inputs.py <voice_dir>
Writes kaggle/latentsync_t4/inputs/{job.json, footage_*.mp4, resync_*.wav} and appends to
presenter/clips/inputs/ep003_clip_plan.json (names thomas_e3_rs_<id>).
"""
import json
import os
import shutil
import sys

import numpy as np
from scipy.io import wavfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "sound"))
from teaser_mix import load_voice  # noqa: E402
from sting_design import SR  # noqa: E402

LEAD, LEN = 0.3, 5.0
# line -> HF clip whose footage carries it (picked far away in the episode)
SRC = {"c3": "k3", "c4": "g9", "c13": "i2", "c14": "k6", "c15": "i3", "c16": "e8", "e9": "b8",
       "g1": "i1", "g2": "c12", "g3": "i4", "g4": "b10", "k4": "g8", "k5": "c12", "k7": "i1", "k10": "i4"}
CAM = {"c3": "C", "c4": "M", "c13": "M", "c14": "C", "c15": "M", "c16": "C", "e9": "M",
       "g1": "C", "g2": "M", "g3": "C", "g4": "M", "k4": "C", "k5": "M", "k7": "C", "k10": "M"}


def main(vdir):
    clips = os.path.join(ROOT, "presenter", "clips", "ep003")
    out = os.path.join(ROOT, "kaggle", "latentsync_t4", "inputs")
    os.makedirs(out, exist_ok=True)
    jobs, plan_add = [], []
    for line, src in SRC.items():
        v = os.path.join(clips, f"thomas_e3_{src}_720p.mp4")
        if not os.path.exists(v):
            print("missing footage", v)
            continue
        fv = f"footage_{src}.mp4"
        if not os.path.exists(os.path.join(out, fv)):
            shutil.copy(v, os.path.join(out, fv))
        a = np.concatenate([np.zeros(int(LEAD * SR)), load_voice(os.path.join(vdir, line + ".wav"))])
        if len(a) > LEN * SR:
            raise SystemExit(f"{line} too long")
        a = np.concatenate([a, np.zeros(int(LEN * SR) - len(a))]) * 0.89
        fa = f"resync_{line}.wav"
        wavfile.write(os.path.join(out, fa), SR, (a * 32767).astype(np.int16))
        name = f"thomas_e3_rs_{line}"
        jobs.append(dict(name=name, video=fv, audio=fa))
        plan_add.append(dict(name=name, first=line, last=line, lead=LEAD, camera=CAM[line], tail=0.35))
    json.dump(dict(jobs=jobs, steps=20, guidance=1.5, seed=1247), open(os.path.join(out, "job.json"), "w"), indent=1)
    pp = os.path.join(ROOT, "presenter", "clips", "inputs", "ep003_clip_plan.json")
    plan = json.load(open(pp))
    keep = [c for c in plan["clips"] if not c["name"].startswith("thomas_e3_rs_")]
    json.dump(dict(clips=keep + plan_add), open(pp, "w"), indent=1)
    print(len(jobs), "resync jobs")


if __name__ == "__main__":
    main(sys.argv[1])
