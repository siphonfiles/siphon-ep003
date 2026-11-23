"""Episode 002 (Bitget) visuals, cut to the sound timeline from sound/ep002/ep002_mix.py.

Usage:
  python3 ep002.py <timeline.json> <audio|none> <out.mp4> [--still T out.png ...] [--from S --to E]
Scenes are anchored on the voice-line ids, so a new audio mix re-times the picture automatically.

Thomas: only ever as moving video (rule 18b). Every Thomas line has a non-Thomas picture underneath
(illustration / card); the LongCat clips listed in presenter/clips/inputs/ep002_clip_plan.json are laid
over it when their frames exist (presenter/clips/frames/<name>/*.png at 30 fps). A clip that was not
generated simply leaves the picture underneath.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine  # noqa: E402
import scenes as S  # noqa: E402
import scenes_ep002 as E  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
THOMAS_REF = os.path.join(ROOT, "presenter", "reference", "thomas_ref_ep002_1920x1080.png")   # ep. 002 outfit
if not os.path.exists(THOMAS_REF):
    THOMAS_REF = os.path.join(ROOT, "presenter", "reference", "thomas_ref_v1_centered_1920x1080.png")
S.ILL_DIR = os.path.join(ROOT, "illustrations", "ep002", "img")
CLIPS = os.path.join(ROOT, "presenter", "clips", "frames")
CLIP_PLAN = os.path.join(ROOT, "presenter", "clips", "inputs", "ep002_clip_plan.json")
CLOSE = (1.3, 960.0, 440.0)          # second camera: the same moving clip, tighter
FIT720 = dict(scale=1920 / 1312, ox=0.0, oy=25.0)   # 720p LongCat frame laid over the reference (ep. 001)

WARM = (1.0, 0.72, 0.35)
REDL = (1.0, 0.15, 0.12)
COOL = (0.55, 0.75, 1.0)


def thomas_shots(tl):
    """[(a, b, frames_dir, clip_t0, camera)] for every generated clip. clip_t0 = episode time of frame 0."""
    if not os.path.exists(CLIP_PLAN):
        return []
    v = {e["id"]: (e["t"], e["t"] + e["dur"]) for e in tl["events"] if e["kind"] == "voice"}
    out = []
    for c in json.load(open(CLIP_PLAN))["clips"]:
        fr = os.path.join(CLIPS, c["name"])
        if not (os.path.isdir(fr) and any(f.endswith(".png") for f in os.listdir(fr))):
            continue
        if c["first"] not in v or c["last"] not in v:
            continue
        t0 = v[c["first"]][0] - c["lead"]
        a = v[c["first"]][0] - min(c["lead"], 0.35)
        b = v[c["last"]][1] + c.get("tail", 0.35)
        cut = c.get("close_from")           # second camera from this line on
        if cut and cut in v:
            k = v[cut][0] - 0.12
            out += [(a, k, fr, t0, "M"), (k, b, fr, t0, "C")]
        else:
            out.append((a, b, fr, t0, c.get("camera", "M")))
    return out


def _clip_len(fr):
    return len([f for f in os.listdir(fr) if f.endswith(".png")]) / 30.0


def _absorb_slivers(T, shots):
    """A scene left with < 1 s right after a shot would flash (e.g. 1:23). Hold the shot over it instead,
    as long as the clip still has frames there."""
    shots = [list(x) for x in shots]
    for a, b, fn, p in T:
        for sh in shots:
            sa, sb, fr, t0 = sh[0], sh[1], sh[2], sh[3]
            if a < sb < b and b - sb < 1.0 and not any(o[0] <= sb < o[1] for o in shots if o is not sh):
                n = _clip_len(fr)
                if b <= t0 + (n if n > 1 else 5.0) - 0.02:
                    sh[1] = b
    return [tuple(x) for x in shots]


def overlay_thomas(T, shots):
    """Cut the shots into the picture: what they cover is removed; a scene resuming after a shot continues
    where it was. Slivers under 1 s right after a shot are covered by holding the shot (no flash)."""
    shots = _absorb_slivers(T, shots)
    out = []
    for a, b, fn, p in T:
        pieces = [(a, b)]
        for sa, sb, *_ in shots:
            nxt = []
            for pa, pb in pieces:
                if sb <= pa or sa >= pb:
                    nxt.append((pa, pb))
                    continue
                if pa < sa:
                    nxt.append((pa, sa))
                if sb < pb:
                    nxt.append((sb, pb))
            pieces = nxt
        for pa, pb in pieces:
            if pb - pa < 1.0 and (pa, pb) != (a, b):
                fill = S.black if fn is S.black else fn
                out.append((pa, pb, _off(fill, pa - a), p))   # keep continuity, it is short anyway
            elif pa == a:
                out.append((pa, pb, fn, p))
            else:
                out.append((pa, pb, _off(fn, pa - a), p))
    first = min((x[0] for x in shots), default=None)
    for a, b, fr, t0, cam in shots:
        clip = dict(frames=fr, start=t0 - a, **FIT720)
        lt = 0.6 if a == first else 99     # name card on his first appearance only
        out.append((a, b, S.presenter, dict(image_path=THOMAS_REF, lower_third_at=lt, clip=clip,
                                             zoom=CLOSE if cam == "C" else None)))
    return out


def _off(fn, off):
    def g(ctx, t, d, **p):
        return fn(ctx, t + off, d + off, **p)
    return g


_IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "illustrations", "ep002", "img")


def pick(new, old):
    """New Kaggle illustration if it (and its depth map) is in the repo, otherwise the old one."""
    ok = all(os.path.exists(os.path.join(_IMG, f)) for f in (f"{new}.jpg", f"{new}_depth.png"))
    return new if ok else old


def build(tl):
    ev = tl["events"]
    v = {e["id"]: (e["t"], e["t"] + e["dur"]) for e in ev if e["kind"] == "voice"}
    hits = [e["t"] for e in ev if e["kind"] == "hit"]
    cards = [e["t"] for e in ev if e["kind"] == "card"]
    total = tl["total"]
    T = []

    def nxt(lst, after):
        return min(x for x in lst if x >= after - 1e-6)

    def add(a, b, fn, **p):
        T.append((a, b, fn, p))

    def IL(a, b, name, move="in", **p):
        T.append((a, b, S.illus, dict(name=name, move=move, **p)))

    def frac(k, f):
        return v[k][0] + f * (v[k][1] - v[k][0])

    def s(k):
        return v[k][0]

    def e(k):
        return v[k][1]

    C = iter(cards)

    # ---------------- TEASER ----------------
    IL(s("t1"), nxt(hits, e("t1") - .01), "b01_empty_trading_office", "in", fi=0.15, fo=0.0,
       kicker="BITGET · 02:31 IN ASIA", glows=[dict(kind="flicker", x=1150, y=470, r=220, color=WARM, base=0.30)])
    h0 = nxt(hits, e("t1") - .01)
    c0 = next(C)
    add(h0, c0, S.black)
    add(c0, s("t2"), E.explorer_line, cols=["93 TRX", "24 SEP 2026", "18:31 UTC", "→ attacker wallet"],
        source="[S6]", cut=True)
    add(s("t2"), nxt(hits, e("t2") - .01), S.kinetic,
        line="Less than three hours later, about $388 million is gone. Not a single key was stolen.",
        highlight=("$388", "key"), source="[S2]")
    h1 = nxt(hits, e("t2") - .01)
    c1 = next(C)
    add(h1, c1, S.black)
    add(c1, s("t3"), S.quote_card, quote="Nobody stole a key.", who="DFNS · ANALYSIS OF THE BITGET HACK",
        source="[S8]")
    IL(s("t3"), nxt(hits, e("t3") - .01), "b12_alarm_control_room", "in", fo=0.0, kicker="19:05 UTC",
       line="The alarm. And the money kept leaving.", warm=False, source="[S2]",
       glows=[dict(kind="pulse", x=930, y=106, r=300, color=REDL, min=0.10, max=0.65, hz=1.1),
              dict(kind="beam", poly=[(900, 180), (1000, 180), (1120, 660), (760, 660)], color=(1.0, 0.35, 0.25), base=0.12)])
    h2 = nxt(hits, e("t3") - .01)
    add(h2, s("t4"), S.black)
    add(s("t4"), nxt(hits, e("t4")), S.kinetic,
        line="The first sign that someone was inside? Dated twenty-four days earlier—",
        highlight=("inside?", "twenty-four"))
    h3 = nxt(hits, e("t4"))
    c2 = next(C)
    add(h3, c2, S.black)
    c3 = next(C)
    add(c2, c3, S.title_card, title="THE GUARD WAS THE DOOR")

    # ---------------- THE RESCUER ----------------
    add(c3, s("r1"), E.chapter, title="The rescuer", kicker="FEBRUARY 2025")
    IL(s("r1"), e("r1") + .35, "b02_two_towers", "up", kicker="BYBIT · 21 FEB 2025",
       line="~$1.5 billion stolen. The FBI blames North Korea.", source="[S31][S28]",
       fog=dict(density=0.22, color=(0.45, 0.50, 0.58), speed=10, far=0.45))
    add(e("r1") + .35, s("r3"), E.loan_towers, mode="loan", source="[S27][S28]")
    IL(s("r3"), s("r4"), "b03_lifebuoy_dock", "in", statement="Remember that loan.",
       glows=[dict(kind="flicker", x=790, y=216, r=300, color=WARM, base=0.38)],
       fog=dict(density=0.30, color=(0.45, 0.52, 0.60), speed=12, floor=0.45))
    IL(s("r4"), nxt(hits, e("r4") - .01), "b10_empty_trading_floor", "left", kicker="24 SEPTEMBER 2026",
       line="The one that came to help became the one robbed.", source="[S2][S29]",
       glows=[dict(kind="flicker", x=950, y=70, r=260, color=WARM, base=0.25)])
    c4 = next(C)
    add(c4, s("i1"), S.big_number, value=388_000_000, suffix="", caption="24 SEP 2026 · BITGET · hot + warm wallets",
        count_for=1.4, source="[S2]")
    # Thomas i1..i5 (clips laid over when generated); underneath, no still of him:
    add(s("i1"), s("i2"), S.statement, line="Thomas Archer · the AI narrator of Siphon Files", color=S.GREY)
    add(s("i2"), s("i3"), S.statement, line="Every claim has a source. They're all in the description.", color=S.GREY)
    add(s("i3"), s("i4"), S.kinetic, line="Bitget says not a single private key was compromised.",
        highlight=("not", "single"), cut=False, source="[S2][S3]")
    add(s("i4"), s("i5"), S.question, q="How do you steal $388M without the keys?")
    add(s("i5"), nxt(hits, e("i5") - .01) + .6, S.statement, line="You make the exchange sign it for you.")

    # ---------------- HOW AN EXCHANGE PAYS YOU ----------------
    c5 = next(C)
    add(nxt(hits, e("i5") - .01) + .6, c5, S.black)
    add(c5, s("p1"), E.chapter, title="How an exchange pays you", kicker="THE MACHINE")
    add(s("p1"), s("p3"), E.wallet_tiers, source="[S2][S8]")
    add(s("p3"), s("p4"), E.pipeline, title="WHEN YOU PRESS ‘WITHDRAW’")
    IL(s("p4"), s("p5"), "b20_two_locks_door", "in", kicker="THE SIGNATURE",
       line="Without it, nothing leaves. With it, anything does.")
    IL(s("p5"), nxt(hits, e("p6") - .01), "b08_corridor_door", "in", kicker="THE PLAN",
       line="Get close to the machine that signs.",
       glows=[dict(kind="flicker", x=780, y=516, r=340, color=WARM, base=0.25)])

    # ---------------- T-MINUS 24 DAYS ----------------
    c6 = next(C)
    add(nxt(hits, e("p6") - .01), c6, S.black)
    add(c6, s("a1"), S.countdown, label="24 DAYS", sub="31 AUGUST 2026")
    IL(s("a1"), s("a3"), "b04_security_appliance", "in", kicker="31 AUG 2026 · EARLIEST ACTIVITY FOUND",
       line="Inside a security product. Not the wallets.", warm=False, source="[S3][S4][S7]",
       glows=[dict(kind="pulse", x=1230, y=566, r=230, color=REDL, min=0.10, max=0.70, hz=0.9),
              dict(kind="pulse", x=1050, y=112, r=120, color=REDL, min=0.05, max=0.40, hz=1.3)])
    add(s("a3"), s("a5"), S.explainer, name="PRODUCT A · PRODUCT B",
        lines=[(0.6, "Two third-party security tools · vendor not named"),
               (frac("a4", 0.2) - s("a3"), "Product A: a zero-day → a hidden script")], source="[S4][S8]")
    add(s("a5"), s("a6"), E.explorer_line, cols=["db_password=", "********", "(plain text)"],
        label="FOUND BY THE SCRIPT · ILLUSTRATIVE", source="[S4][S8]", cut=False)
    add(s("a6"), s("a7"), E.key_appliance, statement="A spare key under the doormat — inside the security office.",
        source="[S4][S8]")
    IL(s("a7"), nxt(hits, e("a7") - .01) + 1.0, "b06_empty_guard_booth", "in", kicker="FROM HERE ON",
       line="We know someone is inside. Bitget doesn't.",
       glows=[dict(kind="flicker", x=730, y=100, r=300, color=WARM, base=0.30)])
    add(nxt(hits, e("a7") - .01) + 1.0, s("a9"), S.explainer, name="ONE CAVEAT",
        lines=[(0.5, "SlowMist: first activity 31 August"), (1.6, "Mandiant: privileged access dated 24 September"),
               (3.0, "The two reports haven't been reconciled")], source="[S3][S7]")
    IL(s("a9"), s("a10"), pick("b21_two_appliances", "b06_empty_guard_booth"), "out")
    add(s("a10"), nxt(hits, e("a10") - .01) + .5, S.statement, line="A name. A real one.")

    # ---------------- BRIDGE (Thomas) ----------------
    hb = nxt(hits, e("a10") - .01) + .5
    IL(hb, s("d2"), pick("b23_server_cable", "b06_empty_guard_booth"), "right", line="Let me stop here for a second.",
       glows=[dict(kind="flicker", x=730, y=100, r=300, color=WARM, base=0.30)])
    IL(s("d2"), s("d3"), "b04_security_appliance", "left", kicker="SECURITY PRODUCTS",
       line="Deep access. They see everything.", warm=False,
       glows=[dict(kind="pulse", x=1230, y=566, r=200, color=(1.0, 0.6, 0.2), min=0.1, max=0.4, hz=0.5)])
    IL(s("d3"), e("d4") + .6, "b08_corridor_door", "in", statement="Take over the guard, and you're already in every corridor.",
       glows=[dict(kind="flicker", x=780, y=516, r=340, color=WARM, base=0.25)])

    # ---------------- T-MINUS 2 HOURS 24 MINUTES ----------------
    c7 = next(C)
    add(e("d4") + .6, c7, S.black)
    add(c7, s("b1"), S.countdown, label="2H 24M", sub="24 SEP 2026 · 16:07 UTC")
    add(s("b1"), s("b2"), S.timeline, points=[("31 AUG", "machine 1"), ("23 SEP", "machine 2"),
                                              ("24 SEP", "machine 3 · night of the theft")],
        title="THE SCRIPT SPREADS", source="[S4][S7]")
    add(s("b2"), s("b4"), E.borrowed_badge, clone_at=s("b3") - s("b2") + 0.3, source="[S4][S7][S15]")
    add(s("b4"), s("b5"), S.explainer, name="THE EMPLOYEE",
        lines=[(0.6, "Wasn't there"), (1.8, "Credentials stolen via the zero-day"),
               (3.4, "Insider collusion ruled out, for now (Bitget)")], source="[S15]")
    add(s("b5"), nxt(hits, e("b8") - .01), E.path_to_money, t_server=s("b6") - s("b5"), t_vault=s("b7") - s("b5"),
        t_barrier=s("b8") - s("b5") + 0.4, source="[S3][S4]")

    # ---------------- T-MINUS 42 MINUTES ----------------
    c8 = next(C)
    add(nxt(hits, e("b8") - .01), c8, S.black)
    add(c8, s("c1"), S.countdown, label="42 MIN", sub="24 SEP 2026 · 17:49 UTC")
    add(s("c1"), s("c2"), S.explainer, name="17:49 UTC · WALLET HOST",
        lines=[(0.6, "A tool starts"), (2.0, "Later recovered from deleted files (SlowMist)")], source="[S4][S7]")
    add(s("c2"), s("c4"), E.risk_form, stamp_at=99, label="risk checks answered by the attacker's tool",
        source="[S4][S7]")
    add(s("c4"), s("c5"), E.pipeline, forged=True, title="ACCORDING TO ONE ANALYSIS", source="[S8]")
    IL(s("c5"), nxt(hits, e("c6") - .01) + .5, "b09_stamp_form", "in", statement="Try it.",
       glows=[dict(kind="flicker", x=700, y=100, r=260, color=WARM, base=0.25)])

    # ---------------- 18:31 ----------------
    c9 = next(C)
    add(nxt(hits, e("c6") - .01) + .5, c9, S.black)
    add(c9, s("e1"), S.countdown, label="18:31 UTC", sub="02:31 IN ASIA")
    add(s("e1"), s("e2"), E.explorer_line, cols=["18:31", "93 TRX", "· then ·", "0.84 ETH"],
        label="THE TEST TRANSFERS", source="[S6]", cut=False)
    add(s("e2"), s("e3"), E.risk_form, stamp_at=0.6, label="below the risk threshold · no alert", source="[S15]")
    IL(s("e3"), s("e4"), "b13_fingerprint_glass", "in", kicker="HOLD ON TO THIS",
       line="Something odd about these transfers.",
       glows=[dict(kind="flicker", x=620, y=310, r=220, color=(0.95, 0.95, 1.0), base=0.30)])
    IL(s("e4"), s("e5"), "b10_empty_trading_floor", "in", kicker="18:31 → 18:58",
       line="Nothing. For almost half an hour.",
       glows=[dict(kind="flicker", x=950, y=70, r=260, color=WARM, base=0.25)])
    add(s("e5"), s("e6"), S.big_number, value=34.75, prefix="", suffix="M USDT", decimals=2, count_for=1.0,
        caption="18:58 UTC · one transfer", source="[S6]")
    IL(s("e6"), nxt(cards, e("e7")), pick("b28_guard_monitors", "b12_alarm_control_room"), "out", kicker="STILL NO ALARM", warm=False,
       glows=[dict(kind="pulse", x=930, y=106, r=160, color=(0.4, 0.1, 0.1), min=0.02, max=0.08, hz=0.3)])

    # ---------------- LOCKED OUT ----------------
    c10 = next(C)
    add(c10, s("f2"), E.burst, clock="19:01", n=7, chains=5, seconds=15, source="[S6]")
    add(s("f2"), s("f3"), E.explorer_line, cols=["19:03", "small test", "different wallet"],
        label="ONE MORE TEST", source="[S6][S8]", cut=False)
    IL(s("f3"), s("f4"), "b12_alarm_control_room", "in", kicker="19:05 UTC", line="Reconciliation flags the gap.",
       warm=False, source="[S2]",
       glows=[dict(kind="pulse", x=930, y=106, r=320, color=REDL, min=0.15, max=0.85, hz=1.6),
              dict(kind="beam", poly=[(900, 180), (1000, 180), (1120, 660), (760, 660)], color=(1.0, 0.35, 0.25), base=0.16)])
    add(s("f4"), s("f5"), E.locked_phone_split, note="If you had money on Bitget", source="[S2]")
    if pick("b24_crisis_room", "") == "b24_crisis_room":
        IL(s("f5"), s("f6"), "b24_crisis_room", "in", kicker="19:14 UTC", line="Highest-level emergency.", warm=False, source="[S2]")
    else:
        add(s("f5"), s("f6"), S.explainer, name="19:14 UTC", lines=[(0.4, "Highest-level emergency")], source="[S2]")
    add(s("f6"), s("f9"), E.burst, clock="19:16", n=5, chains=5, seconds=9, red=True,
        caption="≈ $203 million", source="[S6]")
    add(s("f9"), nxt(hits, e("f10") - .01) + .6, E.locked_phone_split, source="[S2][S8]")

    # ---------------- WHY DIDN'T IT STOP? ----------------
    c11 = next(C)
    add(nxt(hits, e("f10") - .01) + .6, c11, S.black)
    add(c11, s("g1"), E.chapter, title="Why didn't it stop?", kicker="THE WRONG SWITCH")
    add(s("g1"), s("g2"), E.locked_phone_split, source="[S2][S8]")
    add(s("g2"), s("g3"), E.pipeline, steps=("FORGED REQUEST", "SECOND PERSON?", "ALLOW-LIST?", "SIGNATURE"),
        forged=False, title="WARM WALLETS · ACCORDING TO ONE ANALYSIS", source="[S8]")
    add(s("g3"), nxt(cards, e("g3")), S.statement, line="The signing service kept running.")
    c12 = next(C)
    add(c12, s("g4"), E.big_text, value="2 h 39 min", caption="of signing after the first alert",
        source="[S2][S8]")
    add(s("g4"), s("g5"), S.big_number, value=238_000_000, suffix="", prefix="~$", caption="left after the alarm · two estimates",
        count_for=1.2, source="[S7][S20]")
    IL(s("g5"), s("g7"), pick("b25_vault_closing", "b19_vault_half_full"), "out", kicker="20:40 UTC",
       line="Funds move to cold storage. Last traced transfer: 21:23.", source="[S2][S6][S7]",
       glows=[dict(kind="flicker", x=790, y=90, r=320, color=WARM, base=0.35)])
    add(s("g7"), s("g8"), S.explainer, name="AFTER 21:23",
        lines=[(0.6, "Attempts to rewrite withdrawal records"), (2.4, "Two fake Bitcoin orders → errors"),
               (4.0, "Covering tracks, or going for more? The reports don't say.")], source="[S4][S7]")
    add(s("g8"), s("g9"), E.clock_span, marks=[(0.19, "19:05", "alarm"), (0.97, "21:23", "last transfer")],
        source="[S2][S6]")
    IL(s("g9"), nxt(cards, e("g10")), pick("b22_recovered_drive", "b13_fingerprint_glass"), "in", kicker="THE NEXT MORNING",
       line="Root cause found. Reported to law enforcement.", source="[S2]",
       glows=[dict(kind="flicker", x=620, y=310, r=220, color=(0.95, 0.95, 1.0), base=0.30)])

    # ---------------- THE TELL ----------------
    c13 = next(C)
    add(c13, s("h1"), E.chapter, title="The tell", kicker="FINGERPRINTS")
    add(s("h1"), s("h3"), E.gas_bars, source="[S6]")
    add(s("h3"), s("h4"), S.big_number, value=35678, prefix="", suffix=" transactions", count_for=1.0,
        caption="in the 8 days before · not one customer payout used those limits", source="[S6]")
    if pick("b27_coin_crowd", "") == "b27_coin_crowd":
        IL(s("h4"), s("h5"), "b27_coin_crowd", "in", kicker="ZCASH · ~1,000 INPUTS PER TRANSFER",
           line="The wallet's previous maximum: 54.", source="[S7]")
    else:
        add(s("h4"), s("h5"), S.explainer, name="ZCASH",
            lines=[(0.6, "~1,000 inputs per stolen transfer"), (2.4, "previous maximum for that wallet: 54")], source="[S7]")
    IL(s("h5"), nxt(hits, e("h6") - .01) + .5, "b13_fingerprint_glass", "in", kicker="COMMANDS DELETED",
       line="The fingerprints weren't.", source="[S8][S16]",
       glows=[dict(kind="flicker", x=620, y=310, r=240, color=(0.95, 0.95, 1.0), base=0.35)])
    add(nxt(hits, e("h6") - .01) + .5, nxt(cards, e("h7")), S.statement, line="And a new problem: how to keep it.")

    # ---------------- WHERE DID IT GO? ----------------
    c14 = next(C)
    add(c14, s("w1"), E.chapter, title="Where did it go?", kicker="THE MONEY")
    add(s("w1"), s("w3"), E.flow_split, title="WITHIN HOURS", rows=[
        ("USDT", "ETH", "swapped within ~20 min · stablecoins can be frozen"),
        ("XRP", "THORChain → BTC", ""),
        ("ZEC", "private pool", "can't be followed")], source="[S6][S7]")
    IL(s("w3"), s("w5"), "b18_open_barrier", "in", kicker="THORCHAIN",
       line="Asked to block the addresses. Declined.", source="[S7][S9]",
       fog=dict(density=0.35, color=(0.45, 0.52, 0.60), speed=12, far=0.5),
       glows=[dict(kind="flicker", x=600, y=360, r=260, color=(0.5, 0.9, 0.9), base=0.20)])
    add(frac("w4", 0.0), s("w5"), S.big_number, value=0.3, prefix="< ", suffix="%", decimals=1, count_for=0.8,
        caption="of the stolen funds frozen", source="[S7][S9]")
    IL(s("w5"), s("w6"), "b16_river_split", "in", kicker="NOVEMBER 2026 · COINJOIN",
       line="~$161M of Bitcoin moved in 11 days", source="[S21][S22]",
       fog=dict(density=0.35, color=(0.50, 0.57, 0.65), speed=18, floor=0.30))
    IL(s("w6"), nxt(cards, e("w8")), "b14_launderer_laptop", "in", kicker="ZACHXBT",
       line="Launderers asking for support in public chats.", source="[S23][S30]",
       glows=[dict(kind="flicker", x=380, y=330, r=260, color=WARM, base=0.30),
              dict(kind="pulse", x=880, y=560, r=380, color=COOL, min=0.06, max=0.16, hz=0.4)])

    # ---------------- WHO? ----------------
    c15 = next(C)
    add(c15, s("x1"), E.chapter, title="Who?", kicker="ATTRIBUTION")
    IL(s("x1"), next(iter([c for c in cards if c > s("x2")])), "b15_investigation_wall", "in", kicker="NIGHT OF THE HACK",
       line="IP addresses matching VPNs used by a North Korean group (CEO)", source="[S19]",
       glows=[dict(kind="flicker", x=40, y=786, r=300, color=WARM, base=0.35)])
    c16 = next(C)
    add(c16, s("x3"), S.quote_card, quote="The pattern looks very much like what the North Korean team did before.",
        who="GRACY CHEN · BITGET CEO · X LIVESTREAM", source="[S19]")
    add(s("x3"), s("x5"), S.explainer, name="FOUR DAYS LATER",
        lines=[(0.5, "“Preliminary indicators”"), (frac("x4", 0.1) - s("x3"), "Chainalysis · Elliptic · TRM: lean North Korea")],
        source="[S10][S11][S12][S13]")
    add(s("x5"), s("x6"), S.big_number, value=6_300_000_000, caption="Binance · ~5 weeks later", count_for=1.2,
        source="[S17][S25]")
    x6b = s("x6")
    if pick("b26_rivers_meet", "") == "b26_rivers_meet":
        IL(s("x6"), s("x7"), "b26_rivers_meet", "in", kicker="CHAINALYSIS",
           line="The Binance money met the Bitget money on-chain.", source="[S24]")
        x6b = s("x7")
    add(x6b, s("x8"), E.flow_split, title="ON-CHAIN", rows=[
        ("BINANCE $", "same address", "via THORChain (ZachXBT)"),
        ("BITGET $", "same address", "commingled (Chainalysis)")], source="[S24][S26]")
    add(s("x8"), s("x9"), S.explainer, name="FBI · 31 OCT 2026",
        lines=[(0.6, "Binance: North Korea's TraderTraitor")], source="[S17][S25]")
    add(s("x9"), e("x10") + .5, S.dossier, stamp="BITGET\nNO OFFICIAL ATTRIBUTION",
        lines=[(0.6, "No government statement"), (1.8, "Mandiant names no one")], source="[S3][S8]")

    # ---------------- THE LOAN (Thomas) ----------------
    add(e("x10") + .5, s("l3"), E.loan_towers, mode="loan", source="[S27][S28]")
    add(s("l3"), s("l4"), S.explainer, name="FBI · FEB 2025", lines=[(0.5, "Bybit: North Korea")], source="[S31]")
    add(s("l4"), s("l5"), E.loan_towers, mode="leaving", source="[S2][S6]")
    add(s("l5"), nxt(cards, e("l5")), S.statement, line="No government has named anyone. The analysts point the same way.")

    # ---------------- AFTERWARDS ----------------
    c17 = next(C)
    add(c17, s("k1"), E.chapter, title="Afterwards", kicker="THE CUSTOMERS")
    IL(s("k1"), s("k3"), "b11_phone_nightstand", "out", kicker="BITGET",
       line="Losses covered from its own protection fund · withdrawals back by 2 Oct", source="[S2][S16]",
       glows=[dict(kind="pulse", x=920, y=696, r=260, color=WARM, min=0.10, max=0.30, hz=0.3)])
    IL(s("k3"), s("k4"), "b19_vault_half_full", "in", kicker="PROTECTION FUND",
       line="Rebuilt to just over $300M. Less than before.", source="[S2][S16]",
       glows=[dict(kind="flicker", x=790, y=90, r=320, color=WARM, base=0.35)])
    IL(s("k4"), s("k5"), "b20_two_locks_door", "in", kicker="SINCE THEN",
       line="Critical operations need more than one approval.", source="[S2][S16]")
    add(s("k5"), s("z1"), S.explainer, name="THE VENDOR", lines=[(0.6, "Under review"), (2.0, "Still not named")],
        source="[S2][S16]")
    IL(s("z1"), s("z2"), "b01_empty_trading_office", "out", kicker="93 TRX · 02:31 IN ASIA",
       line="Nobody looked at it.", glows=[dict(kind="flicker", x=1150, y=470, r=220, color=WARM, base=0.30)])
    IL(s("z2"), s("z3"), "b06_empty_guard_booth", "in", statement="Someone else may have been holding the guard.",
       glows=[dict(kind="flicker", x=730, y=100, r=300, color=WARM, base=0.30)])
    add(s("z3"), s("z4"), E.locked_phone_split, source="[S2]")
    add(s("z4"), e("z4") + .6, S.statement, line="This was Siphon Files.", color=S.GREY)
    add(e("z4") + .6, total, S.end_card)
    T = [x for x in T if x is not None]
    out = overlay_thomas(T, thomas_shots(tl))
    check_no_flash(out)
    return out, total


def check_no_flash(T):
    """Montage guard (lesson 23 Nov 2026): no non-black scene may show for < 1 s (it reads as a flash)."""
    bad = [(round(a, 2), round(b, 2)) for a, b, fn, p in T
           if b - a < 1.0 and fn is not S.black and fn is not S.presenter]
    if bad:
        raise SystemExit(f"FLASH: scenes shorter than 1 s at {bad} - fix the cut before rendering")


def main():
    args = sys.argv[1:]
    tl = json.load(open(args[0]))
    T, total = build(tl)
    if "--still" in args:
        i = args.index("--still")
        for k in range(i + 1, len(args), 2):
            if args[k].startswith("--"):
                break
            engine.still(T, float(args[k]), args[k + 1])
            print("still", args[k], args[k + 1])
        return
    frames = None
    if "--from" in args:
        a = float(args[args.index("--from") + 1])
        b = float(args[args.index("--to") + 1])
        frames = range(int(a * engine.FPS), int(min(b, total) * engine.FPS))
    audio = None if args[1] == "none" else args[1]
    engine.render(T, total, args[2], audio=audio, frames=frames)
    print("wrote", args[2])


if __name__ == "__main__":
    main()
