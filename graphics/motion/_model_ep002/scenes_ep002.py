"""Scene templates added for ep. 002 (Bitget). Same visual language as scenes.py (dark, amber accents)."""
import math

import cairo

from engine import (W, H, BG, AMBER, INK, GREY, DIM, RED, GREEN, HEAD, MONO, SERIF,
                    clamp, ease_out, ease_in_out, prog, fade_io, rgba, text, text_width,
                    wrap, rrect, source_tag)
from scenes import _panel

COLD = (0.45, 0.62, 0.85)


def chapter(ctx, t, d, title, kicker="CHAPTER"):
    """Short chapter break: kicker + title over the episode backdrop with a growing accent rule."""
    a = fade_io(t, d, 0.25, 0.3)
    p = ease_out(prog(t, 0.1, 0.6))
    text(ctx, kicker, W / 2, 470, AMBER, a, align="center", face=MONO, size=30, bold=False, tracking=10)
    text(ctx, title, W / 2, 590 + (1 - p) * 14, INK, a * p, align="center", size=88)
    rgba(ctx, AMBER, a)
    ctx.rectangle(W / 2 - 160 * p, 640, 320 * p, 4)
    ctx.fill()


def explorer_line(ctx, t, d, cols, label="ON-CHAIN · ILLUSTRATIVE LAYOUT", source=None, cut=True):
    """A block-explorer row typing itself out over the backdrop (teaser). cols = list of strings."""
    a = prog(t, 0, 0.2) if cut else fade_io(t, d)
    text(ctx, label, 200, 420, GREY, a, face=MONO, size=26, bold=False, tracking=6)
    rgba(ctx, DIM, a)
    ctx.rectangle(200, 450, W - 400, 2)
    ctx.fill()
    s = "   ".join(cols)
    n = int(len(s) * clamp(t / max(d * 0.55, 0.01)))
    shown = s[:n]
    size = 56
    while size > 30 and text_width(ctx, s, MONO, size, False) > W - 440:
        size -= 2
    text(ctx, shown, 200, 560, INK, a, face=MONO, size=size, bold=False)
    if int(t * 2.2) % 2 == 0 or n < len(s):
        w = text_width(ctx, shown, MONO, size, False)
        rgba(ctx, AMBER, a)
        ctx.rectangle(206 + w, 560 - size * 0.8, size * 0.46, size * 0.95)
        ctx.fill()
    rgba(ctx, DIM, a)
    ctx.rectangle(200, 610, W - 400, 2)
    ctx.fill()
    if source:
        source_tag(ctx, source, a)


def wallet_tiers(ctx, t, d, source=None):
    """COLD / WARM / HOT stacked like a building; cold is sealed, hot is lit and busy."""
    a = fade_io(t, d)
    tiers = [("HOT", "pays withdrawals automatically, 24/7", AMBER, 0.2),
             ("WARM", "holds a reserve", (0.95, 0.62, 0.30), 1.4),
             ("COLD", "offline · slow · untouched", COLD, 2.6)]
    for i, (name, sub, col, at) in enumerate(tiers):
        q = ease_out(prog(t, at, 0.6))
        y = 230 + i * 230
        _panel(ctx, 560, y, 800, 190, a * q, 14)
        rgba(ctx, col, a * q * (0.55 + 0.45 * (0.5 + 0.5 * math.sin(t * 6))) if name == "HOT" else a * q)
        ctx.rectangle(560, y, 10, 190)
        ctx.fill()
        text(ctx, name, 620, y + 95, col, a * q, face=MONO, size=64)
        text(ctx, sub, 620, y + 150, GREY, a * q, face=MONO, size=30, bold=False)
        if name == "COLD":
            # a padlock
            x0, y0 = 1250, y + 60
            rgba(ctx, COLD, a * q)
            ctx.set_line_width(7)
            ctx.new_path()
            ctx.arc(x0 + 30, y0 + 20, 22, math.pi, 2 * math.pi)
            ctx.stroke()
            rrect(ctx, x0, y0 + 20, 60, 52, 6)
            ctx.fill()
    # money moving up from cold to hot
    for k in range(6):
        ph = (t * 0.35 + k / 6) % 1
        y = 860 - ph * 600
        rgba(ctx, AMBER, a * prog(t, 3.0, 0.6) * math.sin(ph * math.pi))
        ctx.arc(1440, y, 9, 0, 2 * math.pi)
        ctx.fill()
    if source:
        source_tag(ctx, source, a)


def pipeline(ctx, t, d, steps=("REQUEST", "RISK CHECKS", "SIGNING SERVICE", "MONEY OUT"),
             forged=False, title=None, source=None):
    """A withdrawal request travelling through the pipeline. forged=True: the risk box is answered by
    the attacker's tool (ticks appear by themselves, in red), the signature still comes."""
    a = fade_io(t, d)
    n = len(steps)
    xs = [260 + i * (1400 / (n - 1)) for i in range(n)]
    y = 540
    if title:
        text(ctx, title, 200, 300, AMBER, a, face=MONO, size=34, bold=False, tracking=6)
    rgba(ctx, DIM, a)
    ctx.set_line_width(4)
    ctx.move_to(xs[0], y)
    ctx.line_to(xs[-1], y)
    ctx.stroke()
    travel = clamp((t - 0.6) / max(d * 0.65, 0.5))
    px = xs[0] + (xs[-1] - xs[0]) * ease_in_out(travel)
    for i, (x, s) in enumerate(zip(xs, steps)):
        reached = px >= x - 5
        q = ease_out(prog(t, 0.15 * i, 0.5))
        col = AMBER if reached else GREY
        if forged and s.startswith("RISK") and reached:
            col = RED
        _panel(ctx, x - 150, y - 80, 300, 160, a * q, 16)
        rgba(ctx, col, a * q)
        ctx.set_line_width(3)
        rrect(ctx, x - 150, y - 80, 300, 160, 16)
        ctx.stroke()
        for j, ln in enumerate(wrap(ctx, s, 260, MONO, 32)):
            text(ctx, ln, x, y - 5 + j * 40, INK if reached else GREY, a * q, align="center", face=MONO, size=32)
        if forged and s.startswith("RISK") and reached:
            text(ctx, "✓ ✓ ✓  (forged)", x, y + 130, RED, a, align="center", face=MONO, size=30, bold=False)
        if s.startswith("SIGNING") and reached:
            text(ctx, "SIGNED", x, y - 110, AMBER, a, align="center", face=MONO, size=34, tracking=6)
    rgba(ctx, AMBER, a)
    ctx.arc(px, y, 14, 0, 2 * math.pi)
    ctx.fill()
    if source:
        source_tag(ctx, source, a)


def risk_form(ctx, t, d, boxes=("AML", "LIMIT", "RISK"), stamp_at=None, source=None, label=None):
    """A form with three checks ticked by an invisible hand; a SIGNED stamp hovers, then comes down."""
    a = fade_io(t, d)
    _panel(ctx, 560, 170, 800, 760, a, 10)
    rgba(ctx, (0.85, 0.83, 0.78), a)
    ctx.rectangle(600, 210, 720, 680)
    ctx.fill()
    text(ctx, "WITHDRAWAL REQUEST", 640, 290, (0.15, 0.15, 0.17), a, face=MONO, size=34, tracking=4)
    for i, b in enumerate(boxes):
        y = 400 + i * 120
        q = ease_out(prog(t, 0.8 + i * 0.6, 0.3))
        rgba(ctx, (0.25, 0.25, 0.28), a)
        ctx.set_line_width(4)
        rrect(ctx, 650, y - 50, 64, 64, 6)
        ctx.stroke()
        if q > 0:
            rgba(ctx, RED, a * q)
            ctx.set_line_width(9)
            ctx.move_to(662, y - 20)
            ctx.line_to(678, y - 2)
            ctx.line_to(662 + 46 * q, y - 2 - 38 * q)
            ctx.stroke()
        text(ctx, b, 750, y, (0.15, 0.15, 0.17), a, face=MONO, size=48)
    sa = d * 0.75 if stamp_at is None else stamp_at
    if t < sa:
        hover = 0.5 + 0.5 * math.sin(t * 2.5)
        rgba(ctx, (0, 0, 0), 0.25 * a)
        ctx.rectangle(860, 760 + 10 * hover, 380, 110)
        ctx.fill()
        text(ctx, "STAMP PENDING", 1050, 840 - 24 - 6 * hover, GREY, a * 0.8, align="center", face=MONO, size=26,
             bold=False, tracking=4)
    else:
        q = ease_out(prog(t, sa, 0.12))
        s = 1.25 - 0.25 * q
        ctx.save()
        ctx.translate(1050, 815)
        ctx.rotate(-0.08)
        ctx.scale(s, s)
        rgba(ctx, RED, a * q * 0.9)
        ctx.set_line_width(7)
        rrect(ctx, -190, -55, 380, 110, 8)
        ctx.stroke()
        text(ctx, "SIGNED", 0, 24, RED, a * q * 0.9, align="center", face=MONO, size=72, tracking=10)
        ctx.restore()
    if label:
        text(ctx, label, W / 2, 1000, GREY, a, align="center", face=MONO, size=28, bold=False)
    if source:
        source_tag(ctx, source, a)


def burst(ctx, t, d, clock, n, chains, seconds, caption=None, source=None, red=False):
    """A burst of withdrawals: n streaks across `chains` columns in `seconds` seconds (shown sped up)."""
    a = fade_io(t, d)
    col = RED if red else AMBER
    text(ctx, clock, W / 2, 230, col, a, align="center", face=MONO, size=110)
    cw = 1300 / chains
    for c in range(chains):
        x = 310 + c * cw
        rgba(ctx, DIM, a)
        ctx.rectangle(x + cw * 0.15, 330, cw * 0.7, 500)
        ctx.fill()
    span = max(min(d * 0.6, 3.5), 1.0)
    for k in range(n):
        at = 0.6 + span * k / max(n - 1, 1)
        q = prog(t, at, 0.45)
        if q <= 0:
            continue
        c = k % chains
        x = 310 + c * cw + cw * 0.5
        y = 830 - 500 * ease_out(q)
        g = cairo.LinearGradient(x, y, x, y + 160)
        g.add_color_stop_rgba(0, col[0], col[1], col[2], a)
        g.add_color_stop_rgba(1, col[0], col[1], col[2], 0)
        ctx.set_source(g)
        ctx.rectangle(x - 6, y, 12, 160)
        ctx.fill()
    cnt = sum(1 for k in range(n) if t >= 0.6 + span * k / max(n - 1, 1))
    text(ctx, f"{cnt} / {n} TRANSFERS · {chains} CHAINS · {seconds} SECONDS", W / 2, 920, INK, a, align="center",
         face=MONO, size=40)
    if caption:
        text(ctx, caption, W / 2, 985, GREY, a * prog(t, span, 0.5), align="center", face=MONO, size=30, bold=False)
    if source:
        source_tag(ctx, source, a)


def split_locked(ctx, t, d, source=None):
    """Left: a customer's app, withdrawals suspended. Right: the signing service keeps stamping."""
    a = fade_io(t, d)
    # phone
    rgba(ctx, (0.07, 0.08, 0.10), a)
    rrect(ctx, 330, 160, 420, 780, 46)
    ctx.fill()
    rgba(ctx, GREY, a * 0.6)
    ctx.set_line_width(3)
    rrect(ctx, 330, 160, 420, 780, 46)
    ctx.stroke()
    text(ctx, "Withdraw", 380, 290, INK, a, size=44)
    rgba(ctx, DIM, a)
    rrect(ctx, 370, 340, 340, 90, 14)
    ctx.fill()
    text(ctx, "Amount", 395, 398, GREY, a, face=MONO, size=28, bold=False)
    q = prog(t, 0.8, 0.4)
    rgba(ctx, (0.30, 0.31, 0.34), a * q)
    rrect(ctx, 370, 470, 340, 150, 14)
    ctx.fill()
    for j, ln in enumerate(["Withdrawals", "suspended"]):
        text(ctx, ln, 540, 535 + j * 46, INK, a * q, align="center", size=38)
    text(ctx, "CUSTOMERS · 19:05", 540, 1010, GREY, a, align="center", face=MONO, size=28, bold=False, tracking=4)
    # signing machine
    rgba(ctx, DIM, a)
    ctx.rectangle(W / 2 + 20, 160, 3, 780)
    ctx.fill()
    k = int(max(0, t - 0.6) / 0.55)
    for i in range(min(k, 9)):
        r, c = divmod(i, 3)
        x, y = 1080 + c * 230, 260 + r * 230
        ctx.save()
        ctx.translate(x + 90, y + 60)
        ctx.rotate(-0.08 + 0.05 * ((i * 7) % 3 - 1))
        rgba(ctx, RED, a * 0.85)
        ctx.set_line_width(5)
        rrect(ctx, -100, -38, 200, 76, 6)
        ctx.stroke()
        text(ctx, "SIGNED", 0, 16, RED, a * 0.85, align="center", face=MONO, size=40, tracking=6)
        ctx.restore()
    text(ctx, "SIGNING SERVICE · STILL RUNNING", 1380, 1010, AMBER, a, align="center", face=MONO, size=28,
         bold=False, tracking=4)
    if source:
        source_tag(ctx, source, a)


def clock_span(ctx, t, d, start="18:31", end="21:23", label="2 h 52 min", source=None, marks=()):
    """A sweeping arc from the first test to the last traced transfer. marks = [(frac, 'HH:MM', text)]."""
    a = fade_io(t, d)
    cx, cy, r = W / 2, 560, 300
    rgba(ctx, DIM, a)
    ctx.set_line_width(16)
    ctx.arc(cx, cy, r, 0, 2 * math.pi)
    ctx.stroke()
    p = ease_in_out(prog(t, 0.4, max(d * 0.6, 1.0)))
    rgba(ctx, AMBER, a)
    ctx.arc(cx, cy, r, -math.pi / 2, -math.pi / 2 + 2 * math.pi * 0.92 * p)
    ctx.stroke()
    text(ctx, start, cx, cy - r - 50, GREY, a, align="center", face=MONO, size=40)
    text(ctx, label, cx, cy + 30, INK, a * prog(t, 0.4 + max(d * 0.6, 1.0) * 0.8, 0.5), align="center",
         face=MONO, size=96)
    text(ctx, f"{start} → {end} UTC", cx, cy + 100, GREY, a, align="center", face=MONO, size=34, bold=False)
    for f, hhmm, s in marks:
        ang = -math.pi / 2 + 2 * math.pi * 0.92 * f
        x, y = cx + (r + 60) * math.cos(ang), cy + (r + 60) * math.sin(ang)
        q = 1.0 if p >= f else 0.0
        rgba(ctx, RED, a * q)
        ctx.arc(cx + r * math.cos(ang), cy + r * math.sin(ang), 14, 0, 2 * math.pi)
        ctx.fill()
        al = "left" if math.cos(ang) >= 0 else "right"
        text(ctx, hhmm, x, y, INK, a * q, align=al, face=MONO, size=32)
        text(ctx, s, x, y + 36, GREY, a * q, align=al, face=MONO, size=24, bold=False)
    if source:
        source_tag(ctx, source, a)


def gas_bars(ctx, t, d, source=None):
    """Gas limits: Bitget's normal payouts (~63,000) next to the attacker's exact 100,000 and 200,000."""
    a = fade_io(t, d)
    text(ctx, "GAS LIMIT PER ETHEREUM TRANSFER", 200, 250, AMBER, a, face=MONO, size=34, bold=False, tracking=6)
    rows = [("Normal customer payouts", 63000, GREY, 0.4), ("Attacker", 100000, RED, 1.6), ("Attacker", 200000, RED, 2.4)]
    for i, (lab, v, col, at) in enumerate(rows):
        q = ease_out(prog(t, at, 0.7))
        y = 400 + i * 190
        text(ctx, lab, 200, y, INK, a * prog(t, at, 0.3), size=44)
        rgba(ctx, col, a)
        ctx.rectangle(200, y + 30, 1300 * v / 200000 * q, 60)
        ctx.fill()
        s = "~63,000" if v == 63000 else f"{v:,}"
        text(ctx, s, 220 + 1300 * v / 200000 * q, y + 78, INK, a * q, face=MONO, size=40)
    if source:
        source_tag(ctx, source, a)


def flow_split(ctx, t, d, rows, title=None, source=None):
    """Where the money went: rows of (from, to, note), each with a stream of dots."""
    a = fade_io(t, d)
    if title:
        text(ctx, title, 200, 230, AMBER, a, face=MONO, size=34, bold=False, tracking=6)
    for i, (src, dst, note) in enumerate(rows):
        at = 0.4 + i * 1.1
        q = ease_out(prog(t, at, 0.5))
        y = 380 + i * 210
        _panel(ctx, 200, y - 60, 330, 120, a * q, 60)
        text(ctx, src, 365, y + 14, INK, a * q, align="center", face=MONO, size=40)
        _panel(ctx, 1260, y - 60, 460, 120, a * q, 60)
        text(ctx, dst, 1490, y + 14, INK, a * q, align="center", face=MONO, size=36)
        rgba(ctx, DIM, a * q)
        ctx.rectangle(540, y - 2, 710, 4)
        ctx.fill()
        for k in range(7):
            ph = (t * 0.5 + k / 7) % 1
            rgba(ctx, AMBER, a * q)
            ctx.arc(540 + ph * 710, y, 8, 0, 2 * math.pi)
            ctx.fill()
        text(ctx, note, 895, y + 70, GREY, a * q, align="center", face=MONO, size=26, bold=False)
    if source:
        source_tag(ctx, source, a)


def loan_line(ctx, t, d, label="40,000 ETH · 21 FEB 2025", left="BITGET", right="BYBIT", source=None):
    """Two exchanges; a line of light runs from the lender to the one that was robbed."""
    a = fade_io(t, d)
    for x, name, lit in ((520, left, True), (1400, right, False)):
        _panel(ctx, x - 180, 330, 360, 420, a, 12)
        rgba(ctx, AMBER if lit else DIM, a)
        for r in range(6):
            for c in range(4):
                if lit or (r * 4 + c) % 5 == 0:
                    ctx.rectangle(x - 140 + c * 75, 370 + r * 60, 45, 30)
        ctx.fill()
        text(ctx, name, x, 820, INK, a, align="center", face=MONO, size=48)
    p = ease_in_out(prog(t, 0.6, max(d * 0.5, 1.0)))
    rgba(ctx, AMBER, a)
    ctx.set_line_width(6)
    ctx.move_to(700, 540)
    ctx.line_to(700 + (1220 - 700) * p, 540)
    ctx.stroke()
    text(ctx, label, W / 2, 500, AMBER, a * prog(t, 0.6 + max(d * 0.5, 1.0), 0.5), align="center", face=MONO, size=38)
    if source:
        source_tag(ctx, source, a)


def big_text(ctx, t, d, value, caption="", source=None):
    """A big amber value that is not a counter (e.g. '2 h 39 min')."""
    a = fade_io(t, d, 0.2, 0.4)
    p = ease_out(prog(t, 0, 0.5))
    text(ctx, value, W / 2, H / 2 + 50 + (1 - p) * 20, AMBER, a * p, align="center", face=MONO, size=170)
    if caption:
        text(ctx, caption, W / 2, H / 2 + 150, GREY, a * prog(t, 0.4, 0.5), align="center", face=MONO, size=40,
             bold=False)
    if source:
        source_tag(ctx, source, a)


# ---------------- cutout scenes (BiRefNet, MIT) — objects cut from the ep. 002 illustrations ----------------
import os as _os
_CUT_DIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "illustrations", "ep002", "cutouts")
_CUTS = {}


def _cut(name):
    if name not in _CUTS:
        _CUTS[name] = cairo.ImageSurface.create_from_png(_os.path.join(_CUT_DIR, f"c_{name}.png"))
    return _CUTS[name]


def draw_cut(ctx, name, cx, cy, h, a=1.0, rot=0.0, shadow=True, tint=None, tint_a=1.0):
    """Paint a cutout centred on (cx, cy), scaled to height h. Returns (x0, y0, w, h) of its box (no rotation).
    shadow: soft drop shadow (stacked offset masks). tint: paint the silhouette in this colour instead."""
    s = _cut(name)
    k = h / s.get_height()
    w = s.get_width() * k
    if a <= 0:
        return cx - w / 2, cy - h / 2, w, h
    ctx.save()
    ctx.translate(cx, cy)
    ctx.rotate(rot)
    ctx.scale(k, k)
    x0, y0 = -s.get_width() / 2, -s.get_height() / 2
    if shadow and tint is None:
        for i in range(6):
            off = (10 + i * 7) / k
            ctx.set_source_rgba(0, 0, 0, 0.085 * a)
            ctx.mask_surface(s, x0 + off * 0.6, y0 + off)
    if tint is not None:
        ctx.set_source_rgba(tint[0], tint[1], tint[2], a * tint_a)
        ctx.mask_surface(s, x0, y0)
    else:
        ctx.set_source_surface(s, x0, y0)
        ctx.get_source().set_filter(cairo.FILTER_GOOD)
        ctx.paint_with_alpha(a)
    ctx.restore()
    return cx - w / 2, cy - h / 2, w, h


def _glow(ctx, x, y, r, col, a):
    g = cairo.RadialGradient(x, y, 0, x, y, r)
    g.add_color_stop_rgba(0, col[0], col[1], col[2], a)
    g.add_color_stop_rgba(1, col[0], col[1], col[2], 0)
    ctx.set_source(g)
    ctx.arc(x, y, r, 0, 2 * math.pi)
    ctx.fill()


def _wire(ctx, p0, p1, k, col, a, w=4):
    """A line drawing itself from p0 to p1 (k in 0..1) with a bright head."""
    if k <= 0 or a <= 0:
        return
    x = p0[0] + (p1[0] - p0[0]) * k
    y = p0[1] + (p1[1] - p0[1]) * k
    rgba(ctx, col, a * 0.9)
    ctx.set_line_width(w)
    ctx.move_to(*p0)
    ctx.line_to(x, y)
    ctx.stroke()
    _glow(ctx, x, y, 18, col, a * 0.6)
    rgba(ctx, col, a)
    ctx.arc(x, y, 7, 0, 2 * math.pi)
    ctx.fill()


def _node(ctx, x, y, label, sub, q, col=None, wid=470):
    """A system box (label + one line) fading in with q."""
    if q <= 0:
        return
    col = col or AMBER
    _panel(ctx, x, y - 52, wid, 104, q, 10)
    rgba(ctx, col, q)
    ctx.rectangle(x, y - 52, 8, 104)
    ctx.fill()
    text(ctx, label, x + 32, y - 6, col if col == RED else INK, q, face=MONO, size=34)
    if sub:
        text(ctx, sub, x + 32, y + 32, GREY, q, face=MONO, size=24, bold=False)


def key_appliance(ctx, t, d, statement, kicker="PRODUCT A", source=None):
    """The guard's own machine; a key slides out from under it and lights up (the plain-text password)."""
    a = fade_io(t, d)
    p = ease_out(prog(t, 0, 0.8))
    k = ease_in_out(prog(t, 0.9, 1.2))
    kx = 960 + 70 * (1 - k) + 300 * k
    if k > 0.05:
        _glow(ctx, kx, 600, 170, AMBER, a * 0.35 * prog(t, 1.6, 0.6) * (0.75 + 0.25 * math.sin(t * 3)))
    draw_cut(ctx, "b05_key_under_mat", kx, 600, 92, a * clamp(k * 3), rot=-0.06)
    draw_cut(ctx, "b04_security_appliance", 900, 470 + 24 * (1 - p), 330, a * p)
    text(ctx, kicker, 900, 250, AMBER, a * prog(t, 0.4, 0.4), align="center", face=MONO, size=30, bold=False, tracking=8)
    lines = wrap(ctx, statement, 1500, HEAD, 58)
    for i, ln in enumerate(lines):
        text(ctx, ln, W / 2, 860 + i * 72, INK, a * prog(t, 1.4, 0.5), align="center", size=58)
    if source:
        source_tag(ctx, source, a)


def borrowed_badge(ctx, t, d, clone_at=2.0, source=None):
    """A real employee's badge; at clone_at a cyan copy peels off and goes to Product B, the original dims."""
    a = fade_io(t, d)
    p = ease_out(prog(t, 0, 0.9))
    c = ease_in_out(prog(t, clone_at, 1.4))
    sway = 0.03 * math.sin(t * 0.9)
    draw_cut(ctx, "b07_badge_lanyard", 500 - 160 * (1 - p), 450, 820, a * p * (1 - 0.55 * c), rot=sway + 0.08 * (1 - p))
    if c > 0:
        cx, cy = 500 + (1140 - 500) * c, 450 + (740 - 450) * c
        h = 820 - 560 * c
        draw_cut(ctx, "b07_badge_lanyard", cx, cy, h, a * (0.25 + 0.5 * (1 - c)), rot=sway, tint=AMBER, shadow=False)
    text(ctx, "16:07 UTC · PRODUCT B", 960, 300, AMBER, a * prog(t, 0.5, 0.4), face=MONO, size=32, tracking=4)
    text(ctx, "A borrowed name", 960, 390, INK, a * prog(t, 0.8, 0.5), size=84)
    text(ctx, "a real Bitget employee's identity", 960, 455, GREY, a * prog(t, clone_at - 0.2, 0.5), face=MONO,
         size=30, bold=False)
    _node(ctx, 1260, 740, "PRODUCT B", "management platform", a * prog(t, clone_at + 0.9, 0.5))
    if source:
        source_tag(ctx, source, a)


def path_to_money(ctx, t, d, t_server=4.0, t_vault=12.0, t_barrier=15.0, source=None):
    """Appliance B -> web shell -> wallet job server -> the vault; then risk control drops in between."""
    a = fade_io(t, d)
    p = ease_out(prog(t, 0, 0.8))
    x0, y0, w, h = draw_cut(ctx, "b04_security_appliance", 300, 560 + 20 * (1 - p), 230, a * p)
    led = prog(t, 0.8, 0.3) * (0.7 + 0.3 * math.sin(t * 7))
    lx, ly = x0 + w * 0.828, y0 + h * 0.565
    _glow(ctx, lx, ly, 60, RED, a * led * 0.6)
    _glow(ctx, lx, ly, 14, RED, a * led)
    text(ctx, "APPLIANCE B", 300, 400, AMBER, a * prog(t, 0.3, 0.4), align="center", face=MONO, size=28, bold=False,
         tracking=6)
    _wire(ctx, (x0 + w + 16, ly), (560, 330), ease_out(prog(t, 1.0, 0.6)), RED, a)
    _node(ctx, 560, 330, "WEB SHELL", "a channel back to the attacker", a * prog(t, 1.4, 0.4), RED, 440)
    _wire(ctx, (780, 382), (780, 618), ease_out(prog(t, t_server - 0.3, 0.6)), AMBER, a)
    _node(ctx, 560, 670, "WALLET JOB SERVER", "builds withdrawal transactions", a * prog(t, t_server, 0.4), None, 440)
    v = ease_out(prog(t, t_vault, 0.9))
    if v > 0:
        _wire(ctx, (1000, 670), (1250, 600), ease_out(prog(t, t_vault, 0.7)), AMBER, a)
        draw_cut(ctx, "b19_vault_half_full", 1500, 560, 450 + 20 * v, a * v)
        text(ctx, "NEXT TO THE MONEY", 1500, 270, AMBER, a * v, align="center", face=MONO, size=30, tracking=6)
    b = ease_out(prog(t, t_barrier, 0.45))
    if b > 0:
        bx = 1150
        rgba(ctx, (0.10, 0.12, 0.15), a * b)
        ctx.rectangle(bx - 16, 380, 32, 520 * b)
        ctx.fill()
        for i in range(int(13 * b)):
            rgba(ctx, RED if i % 2 == 0 else INK, a * 0.9)
            ctx.rectangle(bx - 12, 384 + i * 40, 24, 36)
            ctx.fill()
        text(ctx, "RISK CONTROL", bx, 950, RED, a * prog(t, t_barrier + 0.3, 0.4), align="center", face=MONO,
             size=34, tracking=6)
    if source:
        source_tag(ctx, source, a)


def locked_phone_split(ctx, t, d, note=None, source=None):
    """Left: the customer's phone (cutout) with 'Withdrawals suspended'. Right: SIGNED keeps coming down."""
    a = fade_io(t, d)
    p = ease_out(prog(t, 0, 0.7))
    draw_cut(ctx, "b11_phone_nightstand", 520, 760 + 30 * (1 - p), 210, a * p)
    q = ease_out(prog(t, 0.6, 0.45))
    if q > 0:
        y = 330 + 30 * (1 - q)
        _panel(ctx, 170, y, 700, 190, a * q, 22)
        rgba(ctx, GREY, a * q * 0.5)
        rrect(ctx, 200, y + 40, 62, 62, 14)
        ctx.fill()
        text(ctx, "EXCHANGE APP · 19:05 UTC", 290, y + 62, GREY, a * q, face=MONO, size=24, bold=False)
        text(ctx, "Withdrawals suspended", 290, y + 112, INK, a * q, size=46)
        text(ctx, "for every customer on the platform", 290, y + 156, GREY, a * q, face=MONO, size=22, bold=False)
        rgba(ctx, GREY, a * q * 0.35)
        ctx.set_line_width(2)
        ctx.move_to(520, y + 190)
        ctx.line_to(520, 680)
        ctx.stroke()
    text(ctx, "CUSTOMERS", 520, 1010, GREY, a, align="center", face=MONO, size=28, bold=False, tracking=6)
    rgba(ctx, DIM, a)
    ctx.rectangle(W / 2 + 20, 160, 3, 780)
    ctx.fill()
    k = int(max(0, t - 0.8) / 0.55)
    for i in range(min(k, 9)):
        r, c = divmod(i, 3)
        x, y = 1080 + c * 230, 260 + r * 230
        s = 1.25 - 0.25 * ease_out(prog(t, 0.8 + i * 0.55, 0.12))
        ctx.save()
        ctx.translate(x + 90, y + 60)
        ctx.rotate(-0.08 + 0.05 * ((i * 7) % 3 - 1))
        ctx.scale(s, s)
        rgba(ctx, RED, a * 0.85)
        ctx.set_line_width(5)
        rrect(ctx, -100, -38, 200, 76, 6)
        ctx.stroke()
        text(ctx, "SIGNED", 0, 16, RED, a * 0.85, align="center", face=MONO, size=40, tracking=6)
        ctx.restore()
    text(ctx, "SIGNING SERVICE · STILL RUNNING", 1380, 1010, AMBER, a, align="center", face=MONO, size=28,
         bold=False, tracking=4)
    if note:
        text(ctx, note, W / 2, 120, INK, a * prog(t, 1.2, 0.5), align="center", size=48)
    if source:
        source_tag(ctx, source, a)


def loan_towers(ctx, t, d, mode="loan", source=None):
    """The two towers from the opening (left: Bybit, dark; right: Bitget, lit).
    mode='loan': light runs from Bitget to Bybit (40,000 ETH). mode='leaving': red runs out of Bitget, off-frame."""
    a = fade_io(t, d)
    p = ease_out(prog(t, 0, 0.9))
    x0, y0, w, h = draw_cut(ctx, "b02_two_towers", 960, 560 + 20 * (1 - p), 760, a * p, shadow=False)
    lt = (x0 + w * 0.40, y0 + h * 0.36)   # Bybit (left) facing side
    bt = (x0 + w * 0.60, y0 + h * 0.30)   # Bitget (right) facing side
    lab = a * prog(t, 0.6, 0.5)
    text(ctx, "BYBIT", x0 + w * 0.21, y0 + h + 52, GREY if mode == "leaving" else INK, lab, align="center", face=MONO, size=34)
    text(ctx, "BITGET", x0 + w * 0.78, y0 + h + 52, INK, lab, align="center", face=MONO, size=34)
    if mode == "loan":
        k = prog(t, 1.0, max(d * 0.45, 1.2))
        for j in range(14):
            u = (k * 1.6 - j / 14 * 0.6)
            if 0 < u < 1:
                x = bt[0] + (lt[0] - bt[0]) * u
                y = bt[1] + (lt[1] - bt[1]) * u - 90 * math.sin(math.pi * u)
                _glow(ctx, x, y, 46, AMBER, a * 0.55)
                _glow(ctx, x, y, 12, (1, 1, 1), a * 0.9)
        text(ctx, "40,000 ETH · 21 FEB 2025", W / 2, 150, AMBER, a * prog(t, 1.4, 0.5), align="center", face=MONO,
             size=40, tracking=4)
        text(ctx, "No interest. No collateral.", W / 2, 210, GREY, a * prog(t, 2.4, 0.5), align="center", face=MONO,
             size=30, bold=False)
    else:
        for j in range(18):
            u = ((t * 0.45 + j / 18) % 1) * prog(t, 0.8, 0.6)
            x = bt[0] + (W + 60 - bt[0]) * u
            y = bt[1] + 40 * math.sin(j * 1.7) * u
            _glow(ctx, x, y, 44, RED, a * 0.6 * math.sin(math.pi * u))
            _glow(ctx, x, y, 11, (1, 0.85, 0.85), a * 0.9 * math.sin(math.pi * u))
        text(ctx, "19 MONTHS LATER", W / 2, 150, RED, a * prog(t, 0.3, 0.4), align="center", face=MONO, size=40,
             tracking=6)
        text(ctx, "The money was leaving Bitget.", W / 2, 215, INK, a * prog(t, 0.6, 0.4), align="center", size=52)
    if source:
        source_tag(ctx, source, a)
