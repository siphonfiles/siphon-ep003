"""Dump the gradio API of the Spaces we plan to call, so callers can be written against real signatures."""
import os, sys, io, contextlib
from gradio_client import Client

SPACES = sys.argv[1:] or ["Tongyi-MAI/Z-Image-Turbo", "Qwen/Qwen-Image-Edit-2511"]
os.makedirs("out", exist_ok=True)
for sp in SPACES:
    buf = io.StringIO()
    try:
        c = Client(sp, token=os.environ.get("HF_TOKEN"))
        with contextlib.redirect_stdout(buf):
            c.view_api(all_endpoints=True)
    except Exception as e:
        buf.write(f"ERROR: {type(e).__name__}: {e}\n")
    txt = buf.getvalue()
    print(f"===== {sp} =====\n{txt}")
    open(f"out/api_{sp.replace('/','__')}.txt", "w").write(txt)
