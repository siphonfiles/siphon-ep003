"""Scene templates for ep. 003 (Coldcard). Own look: graphite steel, entropy-green accent (AMBER = the
accent colour of the theme), red only for theft. Same engine and helpers as scenes.py."""
import math
import random

import cairo

from engine import (W, H, AMBER, INK, GREY, DIM, RED, HEAD, MONO, SERIF,
                    clamp, ease_out, ease_in_out, prog, fade_io, rgba, text, text_width,
                    wrap, rrect, source_tag)
from scenes import _panel

STEEL = (0.62, 0.68, 0.74)


def _label(ctx, s, x, y, a, col=GREY, size=26, align="left"):
    text(ctx, s, x, y, col, a, align=align, face=MONO, size=size, bold=False, tracking=6)


def chapter(ctx, t, d, title, kicker="CHAPTER", number=None):
    """Chapter break: a steel plate slides in, the kicker in mono, the title, a dial tick that turns."""
    a = fade_io(t, d, 0.25, 0.3)
    p = ease_out(prog(t, 0.05, 0.7))
    _panel(ctx, W / 2 - 520, 380 + (1 - p) * 30, 1040, 320, a * p, 10)
    _label(ctx, kicker, W / 2, 470, a, AMBER, 28, "center")
    text(ctx, title, W / 2, 590 + (1 - p) * 10, INK, a * p, align="center", size=84)
    cx, cy, r = W / 2, 650, 22
    ang = -math.pi / 2 + ease_out(prog(t, 0.3, 1.2)) * math.pi * 1.5
    rgba(ctx, AMBER, a)
    ctx.set_line_width(3)
    ctx.arc(cx, cy, r, 0, 2 * math.pi)
    ctx.stroke()
    ctx.move_to(cx, cy)
    ctx.line_to(cx + r * 0.8 * math.cos(ang), cy + r * 0.8 * math.sin(ang))
    ctx.stroke()
    if number:
        _label(ctx, number, W / 2 + 480, 420, a, GREY, 24, "right")


def seed_card(ctx, t, d, n=24, source=None):
    """A blank recovery-sheet with numbered lines; the words stay blurred bars (never readable)."""
    a = fade_io(t, d)
    p = ease_out(prog(t, 0, 0.6))
    x0, y0, w, h = 460, 150 + (1 - p) * 30, 1000, 760
    rgba(ctx, (0.88, 0.89, 0.86), 0.95 * a * p)
    rrect(ctx, x0, y0, w, h, 8)
    ctx.fill()
    text(ctx, "RECOVERY WORDS", x0 + 60, y0 + 80, (0.12, 0.14, 0.16), a * p, face=MONO, size=30, tracking=6)
    rnd = random.Random(5)
    for i in range(n):
        col, row = i // 12, i % 12
        x = x0 + 60 + col * 470
        y = y0 + 150 + row * 50
        q = prog(t, 0.4 + i * 0.05, 0.3)
        text(ctx, f"{i + 1:02d}", x, y, (0.35, 0.38, 0.42), a * q, face=MONO, size=24, bold=False)
        bw = rnd.uniform(130, 260)
        g = cairo.LinearGradient(x + 60, 0, x + 60 + bw, 0)
        g.add_color_stop_rgba(0, 0.15, 0.17, 0.2, 0.0)
        g.add_color_stop_rgba(0.15, 0.15, 0.17, 0.2, 0.55 * a * q)
        g.add_color_stop_rgba(0.85, 0.15, 0.17, 0.2, 0.55 * a * q)
        g.add_color_stop_rgba(1, 0.15, 0.17, 0.2, 0.0)
        ctx.set_source(g)
        rrect(ctx, x + 60, y - 18, bw, 18, 9)
        ctx.fill()
    _label(ctx, "ILLUSTRATIVE · WORDS HIDDEN", x0 + w, y0 + h + 50, a * 0.9, GREY, 22, "right")
    if source:
        source_tag(ctx, source, a)


def rng_switch(ctx, t, d, flip_at=1.5, zero_at=None, source=None):
    """'seed generation' asks for randomness; one setting routes it to the hardware generator or to a
    simple software substitute. At flip_at the switch shows 0 and the arrow goes to the substitute."""
    a = fade_io(t, d)
    on = t >= flip_at
    k = ease_in_out(prog(t, flip_at, 0.5))
    # source box
    _panel(ctx, 160, 470, 420, 150, a, 12)
    _label(ctx, "SEED GENERATION", 370, 535, a, INK, 26, "center")
    _label(ctx, "needs random numbers", 370, 580, a, GREY, 20, "center")
    # switch
    cx, cy = 820, 545
    _panel(ctx, cx - 110, cy - 90, 220, 180, a, 14)
    _label(ctx, "SETTING", cx, cy - 100 - 14, a, GREY, 20, "center")
    val = "0" if on else "?"
    text(ctx, val, cx, cy + 42, RED if on else GREY, a, align="center", face=MONO, size=120)
    # targets
    hw = (1340, 330)
    sw = (1340, 760)
    for (x, y), name, sub, col, lit in ((hw, "HARDWARE RANDOM GENERATOR", "built for the job", AMBER, not on),
                                         (sw, "SOFTWARE SUBSTITUTE", "factory ID + timers", GREY, on)):
        _panel(ctx, x - 20, y - 85, 560, 170, a * (1 if lit else 0.55), 12)
        _label(ctx, name, x + 260, y - 10, a * (1 if lit else 0.6), col if lit else GREY, 22, "center")
        _label(ctx, sub, x + 260, y + 35, a * (1 if lit else 0.5), GREY, 20, "center")
    # wires
    ctx.set_line_width(5)
    rgba(ctx, INK, 0.5 * a)
    ctx.move_to(580, 545)
    ctx.line_to(cx - 110, cy)
    ctx.stroke()
    ty = hw[1] + (sw[1] - hw[1]) * k
    col = AMBER if k < 0.5 else RED
    rgba(ctx, col, a)
    ctx.move_to(cx + 110, cy)
    ctx.curve_to(cx + 260, cy, 1180, ty, hw[0] - 20, ty)
    ctx.stroke()
    ctx.move_to(hw[0] - 40, ty - 14)
    ctx.line_to(hw[0] - 20, ty)
    ctx.line_to(hw[0] - 40, ty + 14)
    ctx.stroke()
    if zero_at is not None and t >= zero_at:
        q = prog(t, zero_at, 0.5)
        text(ctx, "Zero means: use the substitute.", W / 2, 990, INK, a * q, align="center", size=46)
    if source:
        source_tag(ctx, source, a)


def code_guard(ctx, t, d, pass_at=2.5, source=None):
    """The safety check in the build: it only asks whether the setting exists. It does (= 0), so it passes."""
    a = fade_io(t, d)
    _panel(ctx, 330, 230, 1260, 520, a, 14)
    _label(ctx, "BUILD CHECK · ILLUSTRATIVE EXCEPT THE QUOTED LINE", 360, 205, a, GREY, 20)
    rows = [("#ifndef  RNG_SETTING", GREY), ('#error  "get a HW TRNG plz"', AMBER), ("#endif", GREY)]
    for i, (s, c) in enumerate(rows):
        n = int(len(s) * clamp((t - 0.3 - i * 0.5) / 0.6))
        text(ctx, s[:n], 400, 360 + i * 90, c, a, face=MONO, size=46, bold=False)
    q = prog(t, pass_at, 0.4)
    if q > 0:
        _label(ctx, "SETTING EXISTS?", 400, 690, a * q, GREY, 26)
        text(ctx, "YES  (= 0)", 760, 692, INK, a * q, face=MONO, size=34)
        rgba(ctx, AMBER, a * q)
        rrect(ctx, 1240, 640, 300, 70, 10)
        ctx.fill()
        text(ctx, "PASSED", 1390, 690, (0.05, 0.08, 0.08), a * q, align="center", face=MONO, size=36)
    if source:
        source_tag(ctx, source, a)


def bits_compare(ctx, t, d, source=None):
    """40 bits against a proper seed's 128: the bars to scale make the gap obvious."""
    a = fade_io(t, d)
    rows = [("MK2 / MK3 · AFFECTED", 40, RED, 0.2), ("NEWER MODELS · AFFECTED", 72, (1.0, 0.7, 0.35), 0.9),
            ("A PROPER SEED · AT LEAST", 128, AMBER, 1.6)]
    for i, (name, bits, col, at) in enumerate(rows):
        q = ease_out(prog(t, at, 0.9))
        y = 330 + i * 190
        _label(ctx, name, 260, y, a * prog(t, at, 0.3), GREY, 24)
        w = 1300 * bits / 128 * q
        rgba(ctx, col, 0.9 * a)
        rrect(ctx, 260, y + 30, max(w, 2), 56, 8)
        ctx.fill()
        text(ctx, f"{int(bits * q)} bits", 260 + w + 30, y + 75, INK, a * prog(t, at, 0.3), face=MONO, size=44)
    if source:
        source_tag(ctx, source, a)


def sweep(ctx, t, d, n_total=1196, blocks=(960183, 960191), clock=("01:10", "01:51"), source=None,
          collectors=3):
    """The first wave: rows of addresses drain into a few collector points while a block counter and an
    address counter run. Positions are illustrative; counts and block range are from the sources."""
    a = fade_io(t, d)
    u = clamp(t / max(d * 0.85, 0.1))
    rnd = random.Random(9)
    cols, rows = 46, 18
    x0, y0, sx, sy = 120, 210, 26, 34
    done = int(cols * rows * u)
    order = list(range(cols * rows))
    rnd.shuffle(order)
    gone = set(order[:done])
    cx = [W - 260]
    cys = [330 + i * 220 for i in range(collectors)]
    for i in range(cols * rows):
        c, r = i % cols, i // cols
        x, y = x0 + c * sx, y0 + r * sy
        if i in gone:
            rgba(ctx, RED, 0.25 * a)
        else:
            rgba(ctx, AMBER, 0.75 * a)
        ctx.rectangle(x, y, 12, 12)
        ctx.fill()
    # streaks: recently drained boxes fly to a collector
    for k in range(max(0, done - 40), done):
        i = order[k]
        c, r = i % cols, i // cols
        x, y = x0 + c * sx + 6, y0 + r * sy + 6
        ty = cys[i % collectors]
        f = (done - k) / 40.0
        px, py = x + (cx[0] - x) * (1 - f), y + (ty - y) * (1 - f)
        rgba(ctx, RED, 0.5 * a * f)
        ctx.set_line_width(2)
        ctx.move_to(x, y)
        ctx.line_to(px, py)
        ctx.stroke()
    for y in cys:
        rgba(ctx, RED, 0.85 * a)
        ctx.arc(cx[0], y, 22 + 6 * math.sin(t * 4), 0, 2 * math.pi)
        ctx.fill()
    blk = int(blocks[0] + (blocks[1] - blocks[0]) * u)
    _label(ctx, f"BLOCK {blk:,}", 120, 150, a, GREY, 26)
    _label(ctx, f"{clock[0]} → {clock[1]} UTC", W - 120, 150, a, GREY, 26, "right")
    text(ctx, f"{int(n_total * u):,} addresses emptied", 120, 900, INK, a, size=52)
    _label(ctx, "POSITIONS ILLUSTRATIVE", W - 120, 900, a * 0.8, GREY, 20, "right")
    if source:
        source_tag(ctx, source, a)


def balance_lines(ctx, t, d, times=("9:36 PM", "9:39 PM", "9:43 PM"), total="≈ C$1.6 million",
                  starts=(0.6, 2.0, 3.4), source=None):
    """Three wallet balance lines on a dark screen turn red one after another (ILLUSTRATIVE)."""
    a = fade_io(t, d)
    _panel(ctx, 360, 200, 1200, 640, a, 16)
    _label(ctx, "WALLET VIEW · ILLUSTRATIVE", 400, 180, a, GREY, 20)
    for i, (tm, st) in enumerate(zip(times, starts)):
        y = 330 + i * 170
        q = prog(t, st, 0.5)
        col = RED if q > 0 else INK
        _label(ctx, f"WALLET {i + 1}", 420, y, a, GREY, 24)
        val = "0.00000000 BTC" if q >= 1 else "•••••• BTC"
        text(ctx, val, 1500, y + 6, col, a, align="right", face=MONO, size=48)
        if q > 0:
            _label(ctx, f"OUT · {tm}", 420, y + 50, a * q, RED, 22)
            rgba(ctx, RED, 0.25 * a * q)
            ctx.rectangle(400, y + 70, 1120 * q, 3)
            ctx.fill()
    if t > starts[-1] + 0.8:
        text(ctx, total, W / 2, 960, INK, a * prog(t, starts[-1] + 0.8, 0.5), align="center", face=MONO, size=58)
    if source:
        source_tag(ctx, source, a)


def tx_pattern(ctx, t, d, rows=7, highlight_at=1.0, title="WAVE 1 · EVERY TRANSACTION", source=None):
    """Identical rows: same fee rate, no change output. The repeating columns light up."""
    a = fade_io(t, d)
    _label(ctx, title, 260, 230, a, AMBER, 26)
    heads = ("TX", "INPUTS", "FEE RATE", "CHANGE BACK")
    xs = (260, 620, 980, 1360)
    for x, h in zip(xs, heads):
        _label(ctx, h, x, 300, a, GREY, 22)
    rnd = random.Random(4)
    q = prog(t, highlight_at, 0.6)
    for i in range(rows):
        y = 370 + i * 80
        p = prog(t, 0.15 + i * 0.12, 0.3)
        tx = "".join(rnd.choice("0123456789abcdef") for _ in range(8)) + "…"
        text(ctx, tx, xs[0], y, INK, a * p, face=MONO, size=34, bold=False)
        text(ctx, str(rnd.randint(1, 9)), xs[1], y, INK, a * p, face=MONO, size=34, bold=False)
        text(ctx, "same", xs[2], y, AMBER if q > 0 else INK, a * p, face=MONO, size=34)
        text(ctx, "none", xs[3], y, AMBER if q > 0 else INK, a * p, face=MONO, size=34)
    if q > 0:
        for x in (xs[2], xs[3]):
            rgba(ctx, AMBER, 0.6 * a * q)
            ctx.set_line_width(2)
            rrect(ctx, x - 24, 330, 260, rows * 80 + 20, 10)
            ctx.stroke()
    _label(ctx, "LAYOUT ILLUSTRATIVE · PATTERN PER GALAXY RESEARCH", W - 160, 990, a * 0.8, GREY, 20, "right")
    if source:
        source_tag(ctx, source, a)


def waves(ctx, t, d, source=None, total_at=None):
    """Four waves on a day axis, 30 Jul to 3 Aug: wave 1 big and still, later waves smaller."""
    a = fade_io(t, d)
    days = ("THU 30 JUL", "FRI 31 JUL", "SAT 1 AUG", "SUN 2 AUG", "MON 3 AUG")
    x0, x1, y = 220, W - 220, 760
    rgba(ctx, GREY, 0.6 * a)
    ctx.rectangle(x0, y, x1 - x0, 2)
    ctx.fill()
    for i, dd in enumerate(days):
        x = x0 + (x1 - x0) * i / 4
        _label(ctx, dd, x, y + 50, a, GREY, 20, "center")
    bars = [(0.02, 1.0, "WAVE 1", RED), (0.27, 0.45, "WAVE 2", (1.0, 0.55, 0.45)),
            (0.45, 0.35, "WAVE 3", (1.0, 0.55, 0.45)), (0.98, 0.3, "WAVE 4", (1.0, 0.55, 0.45))]
    for i, (fx, h, name, col) in enumerate(bars):
        q = ease_out(prog(t, 0.3 + i * 0.6, 0.6))
        x = x0 + (x1 - x0) * fx
        hh = 420 * h * q
        rgba(ctx, col, 0.85 * a)
        rrect(ctx, x - 40, y - hh, 80, hh, 6)
        ctx.fill()
        _label(ctx, name, x, y - hh - 20, a * q, INK, 22, "center")
    if total_at is not None and t >= total_at:
        q = prog(t, total_at, 0.5)
        text(ctx, "≈ 1,816 BTC · 5,200+ addresses", W / 2, 220, INK, a * q, align="center", face=MONO, size=52)
    _label(ctx, "HEIGHTS NOT TO SCALE", W - 220, 900, a * 0.7, GREY, 18, "right")
    if source:
        source_tag(ctx, source, a)


def rbf_race(ctx, t, d, replace_at=2.0, source=None):
    """A waiting transaction gets replaced by one paying a higher fee: the bait comes back."""
    a = fade_io(t, d)
    _label(ctx, "WAITING TO BE CONFIRMED", W / 2, 260, a, GREY, 24, "center")
    q = ease_in_out(prog(t, replace_at, 0.8))
    for k, (who, fee, col, y) in enumerate((("THIEF'S BOT", "fee: low", RED, 420), ("OWNER", "fee: higher", AMBER, 640))):
        vis = 1.0 if k == 0 else prog(t, replace_at - 0.6, 0.5)
        x = 460 + (k == 0) * 0 - (k == 0) * 600 * q
        al = a * vis * (1 - 0.85 * q if k == 0 else 1)
        _panel(ctx, x, y - 70, 1000, 140, al, 12)
        _label(ctx, who, x + 40, y - 5, al, col, 26)
        _label(ctx, fee, x + 40, y + 40, al, GREY, 22)
        text(ctx, "bait", x + 960, y + 20, INK, al, align="right", face=MONO, size=40, bold=False)
    if q >= 1:
        text(ctx, "Replaced. He wins the bait back.", W / 2, 900, INK, a * prog(t, replace_at + 0.8, 0.5),
             align="center", size=48)
    _label(ctx, "ILLUSTRATIVE", W - 160, 990, a * 0.7, GREY, 18, "right")
    if source:
        source_tag(ctx, source, a)


def lookup_log(ctx, t, d, match_at=2.5, source=None):
    """Left: guesses being looked up (the attack). Right: a provider's request log. They line up."""
    a = fade_io(t, d)
    rnd = random.Random(12)
    _label(ctx, "THE ATTACK · LOOKUPS", 220, 230, a, GREY, 22)
    _label(ctx, "A PAID DATA ACCOUNT · LOG", 1060, 230, a, GREY, 22)
    q = prog(t, match_at, 0.6)
    for i in range(10):
        y = 300 + i * 62
        p = prog(t, 0.2 + i * 0.12, 0.3)
        addr = "bc1q" + "".join(rnd.choice("acdefghjkmnpqrstuvwxyz023456789") for _ in range(10)) + "…"
        text(ctx, addr, 220, y, INK, a * p, face=MONO, size=30, bold=False)
        text(ctx, f"req {1000 + i * 7:,} · 01:0{i % 10}", 1060, y, INK, a * p, face=MONO, size=30, bold=False)
        if q > 0:
            rgba(ctx, AMBER, 0.45 * a * q)
            ctx.set_line_width(2)
            ctx.move_to(760, y - 10)
            ctx.line_to(1040, y - 10)
            ctx.stroke()
    if q > 0:
        text(ctx, "“with extraordinary specificity”", W / 2, 1000, AMBER, a * q, align="center",
             face=SERIF, size=46, italic=True)
    _label(ctx, "ILLUSTRATIVE", W - 120, 180, a * 0.7, GREY, 18, "right")
    if source:
        source_tag(ctx, source, a)


def status_board(ctx, t, d, rows, title="STATUS AS OF LATE NOVEMBER 2026", source=None):
    """The dated status card (rule 14a): what is known and not known as the video is made."""
    a = fade_io(t, d)
    _panel(ctx, 320, 200, 1280, 160 + len(rows) * 110, a, 14)
    _label(ctx, title, W / 2, 280, a, AMBER, 30, "center")
    for i, (k, v) in enumerate(rows):
        p = prog(t, 0.4 + i * 0.35, 0.4)
        y = 400 + i * 110
        _label(ctx, k, 380, y, a * p, GREY, 24)
        text(ctx, v, 1540, y + 4, INK, a * p, align="right", size=40)
    if source:
        source_tag(ctx, source, a)


def dice_finale(ctx, t, d, line="At least 50 dice rolls of their own.", source=None):
    """Dice tumble in, land, and the line appears: the owners the bug couldn't reach."""
    a = fade_io(t, d)
    rnd = random.Random(21)
    for i in range(9):
        x = 560 + i * 100 + rnd.uniform(-20, 20)
        land = 0.2 + i * 0.12
        q = ease_out(prog(t, land, 0.6))
        y = 300 + 260 * q + rnd.uniform(-20, 20)
        ang = (1 - q) * rnd.uniform(-3, 3)
        ctx.save()
        ctx.translate(x, y)
        ctx.rotate(ang)
        rgba(ctx, (0.93, 0.94, 0.92), a)
        rrect(ctx, -36, -36, 72, 72, 12)
        ctx.fill()
        rgba(ctx, (0.1, 0.12, 0.14), a)
        n = rnd.randint(1, 6)
        pos = {1: [(0, 0)], 2: [(-14, -14), (14, 14)], 3: [(-16, -16), (0, 0), (16, 16)],
               4: [(-15, -15), (15, -15), (-15, 15), (15, 15)],
               5: [(-15, -15), (15, -15), (0, 0), (-15, 15), (15, 15)],
               6: [(-15, -16), (15, -16), (-15, 0), (15, 0), (-15, 16), (15, 16)]}[n]
        for px, py in pos:
            ctx.arc(px, py, 6, 0, 2 * math.pi)
            ctx.fill()
        ctx.restore()
    q = prog(t, 1.6, 0.6)
    text(ctx, line, W / 2, 830, INK, a * q, align="center", size=56)
    if source:
        source_tag(ctx, source, a)
