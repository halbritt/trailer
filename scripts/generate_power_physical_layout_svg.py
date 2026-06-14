#!/usr/bin/env python3
"""Generate the Juplaya trailer POWER SYSTEM PHYSICAL LAYOUT diagram (SVG).

This is a *physical layout* (where the gear sits), not the electrical schematic
(see docs/diagrams/power-overview.* for the schematic). Three scale plan panels:

  * Roof plan   - Velit 2000R + the roof 3x LG455 (3S) string and PV gland drop.
  * Floor plan  - footprint with the nose power cabinet, fridge bay, exterior
                  flood/awning positions, and the 24 V load locations.
  * Cabinet     - the nose-cabinet contents and the 48 V spine (contents +
                  required connections; exact internal stationing is an open gate).

Per the owner's request the standalone Anker SOLIX C1000 + PS400 AC island and the
optional ground-mounted 2S LG PV (with its SmartSolar 150/35) are intentionally
omitted. Dimensions trace to docs/dimensions.md and docs/power.md.

Hand-authored geometry; render to PNG with PyMuPDF:
    python3 scripts/generate_power_physical_layout_svg.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_OUT = ROOT / "docs" / "diagrams" / "power-physical-layout.svg"
PNG_OUT = ROOT / "docs" / "diagrams" / "power-physical-layout.png"

W, H = 1480, 1260
S = 4  # px per inch for the plan panels

# ---- palette ---------------------------------------------------------------
C = {
    "page": "#ffffff",
    "sheet": "#f8fafc",
    "sheet_stroke": "#cbd5e1",
    "wall": "#111827",
    "ink": "#0f172a",
    "slate": "#334155",
    "muted": "#64748b",
    "pv": "#ecfeff", "pv_s": "#0891b2",
    "bat": "#f0fdf4", "bat_s": "#16a34a",
    "conv": "#eef2ff", "conv_s": "#6366f1",
    "load": "#fff7ed", "load_s": "#ea580c",
    "prot": "#fef2f2", "prot_s": "#dc2626",
    "bus": "#fef9c3", "bus_s": "#ca8a04",
    "omit": "#94a3b8",
    "cab": "#f1f5f9", "cab_s": "#475569",
    "w48": "#b91c1c", "w24": "#2563eb", "w12": "#7c3aed",
}

out: list[str] = []
def e(s: str) -> None: out.append(s)

def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def text(x, y, t, size=14, fill=C["ink"], weight=400, anchor="start",
         rot=None, family="system-ui, -apple-system, 'Segoe UI', sans-serif"):
    tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    e(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
      f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{tr}>{esc(t)}</text>')

def rect(x, y, w, h, fill="none", stroke=C["ink"], sw=1.5, rx=0, dash=None, op=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{op}"' if op is not None else ""
    e(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
      f'stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')

def line(x1, y1, x2, y2, stroke=C["ink"], sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    e(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
      f'stroke-width="{sw}"{d}/>')

def poly(pts, fill="none", stroke=C["ink"], sw=1.5, dash=None, op=None):
    p = " ".join(f"{x},{y}" for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    o = f' fill-opacity="{op}"' if op is not None else ""
    e(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')

def path(d, fill="none", stroke=C["ink"], sw=1.5, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    e(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}/>')

def block(x, y, w, h, label, fill, stroke, size=12, sub=None, rx=4):
    rect(x, y, w, h, fill=fill, stroke=stroke, sw=1.6, rx=rx)
    cx = x + w / 2
    if sub:
        text(cx, y + h / 2 - 2, label, size=size, weight=700, anchor="middle", fill=C["ink"])
        text(cx, y + h / 2 + 14, sub, size=size - 2, anchor="middle", fill=C["slate"])
    else:
        # vertically center single line
        text(cx, y + h / 2 + size / 3, label, size=size, weight=700, anchor="middle", fill=C["ink"])

def dimv(x, y1, y2, label, side="left", tick=6):
    """Vertical dimension with end ticks."""
    line(x, y1, x, y2, stroke=C["ink"], sw=1.4)
    line(x - tick, y1, x + tick, y1, stroke=C["ink"], sw=1.4)
    line(x - tick, y2, x + tick, y2, stroke=C["ink"], sw=1.4)
    ym = (y1 + y2) / 2
    text(x + (10 if side == "right" else -10), ym, label, size=13, weight=700,
         anchor="middle", rot=-90)

def dimh(y, x1, x2, label, above=True, tick=6):
    line(x1, y, x2, y, stroke=C["ink"], sw=1.4)
    line(x1, y - tick, x1, y + tick, stroke=C["ink"], sw=1.4)
    line(x2, y - tick, x2, y + tick, stroke=C["ink"], sw=1.4)
    xm = (x1 + x2) / 2
    text(xm, y - 6 if above else y + 16, label, size=13, weight=700, anchor="middle")

def flood(x, y, tag, lx, ly, anchor="middle"):
    """Exterior flood marker (filled diamond) + label."""
    r = 7
    poly([(x, y - r), (x + r, y), (x, y + r), (x - r, y)],
         fill=C["load"], stroke=C["load_s"], sw=1.6)
    text(lx, ly, tag, size=10.5, weight=700, anchor=anchor, fill=C["load_s"])

def chip(x, y, fill, stroke, label):
    rect(x, y, 22, 14, fill=fill, stroke=stroke, sw=1.4, rx=2)
    text(x + 30, y + 11, label, size=12, fill=C["slate"])

# ===========================================================================
e(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
  f'viewBox="0 0 {W} {H}">')
rect(0, 0, W, H, fill=C["page"], stroke="none")
rect(20, 20, W - 40, H - 40, fill=C["sheet"], stroke=C["sheet_stroke"], sw=1.5, rx=10)

# Title
text(45, 60, "Juplaya trailer - power system physical layout", size=27, weight=700)
text(45, 86, "Plan view, looking down. Nose/front at left, rear/ramp at right. "
             "Curbside = passenger / awning / door side. Scale 1 in = 4 px (plan panels).",
     size=14, fill=C["muted"])

# Shared datum
REAR_X = 690

# ---------------------------------------------------------------------------
# PANEL A - ROOF PLAN
# ---------------------------------------------------------------------------
rt, rb = 118, 118 + 84.875 * S          # roof top / bottom
rmid = (rt + rb) / 2
r_taper = REAR_X - 145.5 * S            # taper start
r_tip = r_taper - 60                    # nose point

text(45, 110, "A  Roof plan", size=17, weight=700, fill=C["pv_s"])

# roof outline (rectangle + V-nose point)
poly([(REAR_X, rt), (REAR_X, rb), (r_taper, rb), (r_tip, rmid), (r_taper, rt)],
     fill="#ffffff", stroke=C["wall"], sw=4)

# 3x LG455 panels (landscape), aft field, each 41.02 in fore-aft x 83.07 in across
p_across = 83.07 * S
py0 = rmid - p_across / 2
p_len = 41.02 * S
x_right = REAR_X - 6
for i in range(3):
    x0 = x_right - (i + 1) * p_len
    rect(x0, py0, p_len, p_across, fill=C["pv"], stroke=C["pv_s"], sw=1.6, rx=2)
    text(x0 + p_len / 2, rmid, f"LG455 #{i+1}", size=12, weight=700,
         anchor="middle", fill=C["pv_s"])
text((x_right - 3 * p_len + x_right) / 2, py0 - 10,
     "Roof PV - 3x LG455 in 3S (1365 W) -> SmartSolar 250/60-Tr",
     size=12.5, weight=700, anchor="middle", fill=C["pv_s"])

# Velit at the nose section of the roof (26.4 across x 26 fore-aft)
v_aft = REAR_X - 125 * S                 # 125 in aft clearance line to rear rail
v_len = 26 * S
v_w = 26.4 * S
vx = v_aft - v_len
rect(vx, rmid - v_w / 2, v_len, v_w, fill=C["load"], stroke=C["load_s"], sw=1.6, rx=2)
text(vx + v_len / 2, rmid - 4, "Velit", size=12, weight=700, anchor="middle", fill=C["load_s"])
text(vx + v_len / 2, rmid + 12, "2000R", size=11, anchor="middle", fill=C["load_s"])

# 125 in aft clearance dimension (AC back edge -> rear rail = solar field)
dimh(rb + 26, v_aft, REAR_X,
     '125" AC-aft -> rear rail = solar field  (3 panels need ~123-124")', above=False)
# roof width
dimv(REAR_X + 26, rt, rb, '84-7/8" roof', side="right")

# PV gland + drop to cabinet
gx, gy = vx - 14, rmid
e(f'<circle cx="{gx}" cy="{gy}" r="7" fill="#ffffff" stroke="{C["pv_s"]}" stroke-width="2"/>')
line(x_right - 3 * p_len, py0 + 8, gx, gy, stroke=C["pv_s"], sw=2.2)
text(gx - 10, gy - 12, "PV gland", size=11, weight=700, anchor="end", fill=C["pv_s"])
# drop arrow toward floor plan cabinet
line(gx, gy, gx, rb + 8, stroke=C["pv_s"], sw=2.2, dash="6 5")
poly([(gx - 5, rb + 8), (gx + 5, rb + 8), (gx, rb + 18)], fill=C["pv_s"], stroke="none")
text(gx + 8, rb + 16, "3S down-lead to nose cabinet (250/60 MPPT)",
     size=11, weight=700, fill=C["pv_s"])

# orientation labels
text(r_tip - 6, rmid, "NOSE", size=11, weight=700, anchor="end", fill=C["muted"])
text(REAR_X + 6, rt - 6, "REAR", size=11, weight=700, fill=C["muted"])

# ---------------------------------------------------------------------------
# PANEL B - FLOOR PLAN
# ---------------------------------------------------------------------------
ft, fb = 600, 600 + 81 * S               # top-down view: curbside = top, roadside = bottom
fmid = (ft + fb) / 2
f_taper = REAR_X - 141 * S               # straight-wall length 141
f_tip = f_taper - 60

text(45, 525, "B  Floor plan  (top-down: curbside = top · roadside = bottom)",
     size=17, weight=700, fill=C["slate"])

# footprint (symmetric about the centerline)
poly([(REAR_X, ft), (REAR_X, fb), (f_taper, fb), (f_tip, fmid), (f_taper, ft)],
     fill="#ffffff", stroke=C["wall"], sw=4)

# centerline (the two bike rows straddle it)
line(f_tip + 6, fmid, REAR_X, fmid, stroke=C["muted"], sw=1, dash="9 7")
text(520, fmid + 13, "centerline", size=9, anchor="middle", fill=C["muted"])

# --- nose power BENCH: ~18" tall, fills the nose, holds ALL power gear + battery (on edge) ---
bench_back = f_taper + 8 * S
poly([(f_tip, fmid), (f_taper, ft), (bench_back, ft), (bench_back, fb), (f_taper, fb)],
     fill=C["cab"], stroke=C["cab_s"], sw=1.6, dash="5 3", op=0.95)
cab_out = (bench_back, fmid)               # 24 V feed origin
line(168, 856, bench_back, fmid + 22, stroke=C["cab_s"], sw=1, dash="3 3")
text(168, 862, "NOSE POWER BENCH (~18\" tall) - all power gear + battery on edge -> detail C",
     size=10, weight=700, anchor="start", fill=C["cab_s"])

# --- side door (curbside / top), 30 in opening, 98 in from rear ---
door_aft = REAR_X - 98 * S
door_fwd = REAR_X - 128 * S
line(door_fwd, ft, door_aft, ft, stroke=C["w24"], sw=5)
path(f"M {door_aft} {ft} A {30*S} {30*S} 0 0 1 {door_aft - 22*S} {ft - 22*S}",
     stroke=C["w24"], sw=2, dash="7 6")
text((door_fwd + door_aft) / 2, ft - 28, "side door 30\"", size=11.5, weight=700,
     anchor="middle", fill=C["w24"])

# --- fridge bay (curbside / top, aft of door) ---
frx = door_aft
frw = 37.9 * S
frd = 20.9 * S
rect(frx, ft, frw, frd, fill=C["load"], stroke=C["load_s"], sw=1.6, rx=2)
fcy = ft + frd / 2
text(frx + frw / 2, fcy - 8, "Dometic CFX3-95DZ", size=12, weight=700, anchor="middle", fill=C["load_s"])
text(frx + frw / 2, fcy + 6, "37.9\" x 20.9\" (24 V)", size=10, anchor="middle", fill=C["load_s"])
text(frx + frw / 2, fcy + 20, "+ lid swing", size=9, anchor="middle", fill=C["muted"])

# --- bikes: 26" OC straddling the centerline (one rail roadside, one curbside), near rear ---
def draw_bike(x_front, x_rear, y, bar_x, bar_w, label):
    rect(x_front, y - 18, x_rear - x_front, 36, fill="#eef2f7",
         stroke=C["omit"], sw=1.3, dash="5 3", rx=10)
    rect(x_front, y - 8, 24, 16, fill=C["slate"], stroke="none", rx=3)        # front wheel
    rect(x_rear - 24, y - 8, 24, 16, fill=C["slate"], stroke="none", rx=3)    # rear wheel
    poly([(x_front - 11, y), (x_front, y - 6), (x_front, y + 6)],
         fill=C["muted"], stroke="none")                                      # nose tick
    line(bar_x, y - bar_w / 2, bar_x, y + bar_w / 2, stroke=C["slate"], sw=4) # handlebar
    for gy in (y - bar_w / 2, y + bar_w / 2):
        e(f'<circle cx="{bar_x}" cy="{gy}" r="4" fill="{C["slate"]}"/>')
    text((x_front + x_rear) / 2 + 30, y + 4, label, size=11, weight=700,
         anchor="middle", fill=C["slate"])

bikeA_y = fb - 27.5 * S                      # roadside rail (~27" off the roadside/bottom wall)
bikeB_y = fb - 53.5 * S                      # curbside rail, 26" OC (~27" off the curbside/top wall)
draw_bike(322, 666, bikeA_y, 402, 32 * S, "WR250R")
draw_bike(258, 602, bikeB_y, 338, 34 * S, "CRF450RL")
line(322, bikeA_y, 246, bikeA_y, stroke=C["muted"], sw=1)
line(258, bikeB_y, 246, bikeB_y, stroke=C["muted"], sw=1)
dimv(246, bikeA_y, bikeB_y, '26" OC', side="left")
text(404, fb - 6, "bikes: nose-forward, via rear ramp - one rail roadside, one curbside (straddle CL)",
     size=10, anchor="middle", fill=C["muted"])
# bar-overlap callout (the curbside bike's bars sweep up over the top-mounted fridge)
line(470, fcy + frd / 2 + 4, 392, fcy + frd / 2 - 16, stroke=C["slate"], sw=1, dash="3 3")
text(560, fcy + frd / 2 + 2, "bars sweep over fridge", size=9.5, weight=700, anchor="middle", fill=C["slate"])
text(560, fcy + frd / 2 + 16, "(clear at bar height ~30\"+ vs 18.6\")", size=8.5, anchor="middle", fill=C["muted"])

# --- interior loads ---
usb_x, usb_y = frx + frw + 40, ft + 24
e(f'<circle cx="{usb_x}" cy="{usb_y}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(usb_x + 12, usb_y + 4, "USB-C PD / GPS (24 V)", size=10.5, fill=C["slate"])
led_x, led_y = 650, fmid
e(f'<circle cx="{led_x}" cy="{led_y}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(led_x - 12, led_y + 4, "interior LED (24 V)", size=10.5, anchor="end", fill=C["slate"])

# --- exterior floods (7x VAL2-NW9): curbside on top, roadside on bottom ---
flood(430, ft - 8, "F curb", 430, ft - 16)
flood(555, ft - 8, "F curb", 555, ft - 16)
flood(430, fb + 8, "F road", 430, fb + 24)
flood(555, fb + 8, "F road", 555, fb + 24)
# nose-face floods on the exterior of each V-nose flank
flood(90, (ft + fmid) / 2, "F nose", 52, (ft + fmid) / 2 - 12, anchor="end")
flood(90, (fb + fmid) / 2, "F nose", 52, (fb + fmid) / 2 + 12, anchor="end")
# rear flood
flood(REAR_X + 8, fb - 70, "F rear", REAR_X + 18, fb - 66, anchor="start")

# --- awning (curbside / top, at roofline) + warm strip ---
aw_x1, aw_x2 = REAR_X - 138 * S, REAR_X
line(aw_x1, ft - 46, aw_x2, ft - 46, stroke=C["load_s"], sw=4)
line(aw_x1, ft - 50, aw_x2, ft - 50, stroke="#f59e0b", sw=2.5, dash="4 4")
text((aw_x1 + aw_x2) / 2, ft - 62,
     "Fiamma F45s awning case 138\" + warm 24 V LED strip (curbside, at roofline)",
     size=10.5, weight=700, anchor="middle", fill=C["load_s"])

# --- winter heater outlet (exterior, curbside/top) ---
e(f'<circle cx="{REAR_X - 40}" cy="{ft - 8}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(REAR_X - 40, ft - 18, "heater (ext.)", size=10, anchor="middle", fill=C["load_s"])

# --- 24 V feed hints from cabinet to loads ---
line(cab_out[0], cab_out[1], frx + frw / 2, ft + frd + 4, stroke=C["w24"], sw=1.4, dash="3 4")
line(cab_out[0], cab_out[1], led_x, led_y, stroke=C["w24"], sw=1.4, dash="3 4")
text(cab_out[0] + 26, cab_out[1] + 8, "24 V branches", size=10, fill=C["w24"])

# floor dimensions
dimv(REAR_X + 26, ft, fb, '81" interior', side="right")
dimh(fb + 100, f_tip, REAR_X, '156" centerline (141" straight + 15" nose)', above=False)

# orientation
text(f_tip - 6, fmid, "NOSE", size=11, weight=700, anchor="end", fill=C["muted"])
text(REAR_X + 6, fb - 6, "REAR / RAMP", size=11, weight=700, fill=C["muted"])

# ---------------------------------------------------------------------------
# PANEL C - NOSE POWER BENCH: TOP-DOWN PLAN + centerline SECTION
# ---------------------------------------------------------------------------
CX, CY, CW, CH = 770, 118, 668, 720
rect(CX, CY, CW, CH, fill="#ffffff", stroke=C["cab_s"], sw=1.8, rx=8)
text(CX + 16, CY + 28, "C  Nose power bench - plan + section", size=17, weight=700, fill=C["cab_s"])
text(CX + 16, CY + 47,
     "Wall-to-wall bench; V-nose adds depth at the centerline.",
     size=11, fill=C["muted"])
text(CX + 16, CY + 63,
     "Battery sits in the deepest part. Components to scale.",
     size=11, fill=C["muted"])

# ---- TOP-DOWN PLAN of the bench (nose up) ----
sc = 6.5
PX0, PYb = 800, 372                          # plan: left edge, back edge (cabin face)
WB, BAND, NOSE = 78, 8, 15                    # bench width, back band aft of taper, nose depth
def PXx(wx): return PX0 + wx * sc             # across-width
def PYd(d): return PYb - d * sc               # depth fwd from the back edge
apex_x = PX0 + WB * sc / 2
poly([(PX0, PYb), (PX0 + WB * sc, PYb), (PX0 + WB * sc, PYd(BAND)),
      (apex_x, PYd(BAND + NOSE)), (PX0, PYd(BAND))],
     fill="#fbfdfe", stroke=C["cab_s"], sw=1.6)
line(PX0, PYb, PX0 + WB * sc, PYb, stroke=C["cab_s"], sw=4)   # cabin face (seat front)
text(apex_x, PYd(BAND + NOSE) - 8, "NOSE (front) ^", size=10, weight=700, anchor="middle", fill=C["muted"])
text(PX0 + WB * sc / 2, PYb + 16, "cabin face (seat front) - bench runs wall-to-wall", size=9.5, anchor="middle", fill=C["muted"])

# plan components: (n, wx, d, ww, dd, fill, stroke, label, lsize)  wx across, d depth from back
pcomps = [
    (1, 29.06, 1.0, 19.88, 9.25, C["bat"],   C["bat_s"],  "battery (on edge)|transverse", 8),
    (7,  2.0,  0.8, 7.28, 3.74,  C["pv"],    C["pv_s"],   "MPPT", 7.5),
    (8, 10.0,  0.8, 7.3,  2.8,   C["conv"],  C["conv_s"], "Orion 48/24", 7),
    (2, 19.5,  0.8, 4.72, 1.81,  C["sheet"], C["cab_s"],  "", 6.5),
    (4,  2.0,  5.2, 6.0,  1.3,   C["bus"],   C["bus_s"],  "- bus", 6.5),
    (5, 10.0,  5.2, 6.0,  1.3,   C["bus"],   C["bus_s"],  "+ bus", 6.5),
    (9, 49.5,  0.8, 7.3,  2.8,   C["conv"],  C["conv_s"], "Orion 48/12", 7),
    (13,61.0,  6.7, 6.06, 3.07,  C["sheet"], C["cab_s"],  "", 6.5),
    (11,58.0,  0.8, 5.5,  2.0,   C["load"],  C["load_s"], "", 6.5),
    (12,65.0,  0.5, 6.49, 1.4,   C["sheet"], C["cab_s"],  "", 6.5),
    (3, 49.5,  5.0, 4.3,  2.5,   C["prot"],  C["prot_s"], "", 6.5),
    (6, 55.0,  5.0, 3.4,  2.4,   C["prot"],  C["prot_s"], "", 6.5),
    (10,61.0,  4.8, 5.74, 1.6,   C["load"],  C["load_s"], "", 6.5),
]
for n, wx, d, ww, dd, fill, stroke, lab, lsize in pcomps:
    x, y = PXx(wx), PYd(d + dd)
    rect(x, y, ww * sc, dd * sc, fill=fill, stroke=stroke, sw=1.3, rx=2)
    cxb, cyb = x + ww * sc / 2, y + dd * sc / 2
    parts = lab.split("|")
    if len(parts) == 1:
        text(cxb, cyb + lsize / 3, parts[0], size=lsize, weight=700, anchor="middle", fill=C["ink"])
    else:
        text(cxb, cyb - 1, parts[0], size=lsize, weight=700, anchor="middle", fill=C["ink"])
        text(cxb, cyb + lsize, parts[1], size=lsize - 1, anchor="middle", fill=C["ink"])
    e(f'<circle cx="{x + 8}" cy="{y + 8}" r="6.5" fill="#ffffff" stroke="{stroke}" stroke-width="1.1"/>')
    text(x + 8, y + 11, str(n), size=8, weight=700, anchor="middle", fill=stroke)
# centerline of the deepest part
line(apex_x, PYb, apex_x, PYd(BAND + NOSE), stroke=C["muted"], sw=1, dash="6 5")

# ---- centerline SECTION (fore-aft cut) - shows the ~18" height; battery shown end-on ----
sxL, sy0 = 800, 560                           # section: left edge, floor datum
sDEP, sHGT = 23, 18
def SXd(d): return sxL + d * sc               # d = depth from cabin face (0) toward nose (23)
def SYh(h): return sy0 - h * sc
rect(sxL, SYh(sHGT), sDEP * sc, sHGT * sc, fill="#fbfdfe", stroke=C["cab_s"], sw=1.5)
line(sxL, SYh(sHGT), sxL + sDEP * sc, SYh(sHGT), stroke=C["cab_s"], sw=4)   # seat top
line(sxL, sy0, sxL + sDEP * sc, sy0, stroke=C["cab_s"], sw=3)               # floor
rect(SXd(1), SYh(12.32), 9.25 * sc, 12.32 * sc, fill=C["bat"], stroke=C["bat_s"], sw=1.4, rx=2)
text(SXd(1) + 9.25 * sc / 2, SYh(12.32) + 12.32 * sc / 2 - 3, "battery", size=8, weight=700, anchor="middle", fill=C["ink"])
text(SXd(1) + 9.25 * sc / 2, SYh(12.32) + 12.32 * sc / 2 + 8, "on edge", size=7, anchor="middle", fill=C["ink"])
rect(SXd(11), SYh(9.84), 3.74 * sc, 9.84 * sc, fill=C["pv"], stroke=C["pv_s"], sw=1.2, rx=2)
text(sxL + sDEP * sc / 2, SYh(sHGT) - 8, "Section (fore-aft) - ~18\" bench; battery end-on (runs transverse)", size=9.5, weight=700, anchor="middle", fill=C["cab_s"])
text(sxL, sy0 + 16, "cabin", size=8.5, weight=700, fill=C["muted"])
text(sxL + sDEP * sc, sy0 + 16, "NOSE (deep)", size=8.5, weight=700, anchor="end", fill=C["muted"])
# scale bar (12 in)
line(sxL, sy0 + 34, sxL + 12 * sc, sy0 + 34, stroke=C["ink"], sw=1.6)
for sx in (sxL, sxL + 12 * sc):
    line(sx, sy0 + 30, sx, sy0 + 38, stroke=C["ink"], sw=1.6)
text(sxL + 6 * sc, sy0 + 49, "12 in", size=9.5, anchor="middle", fill=C["slate"])

# ---- component list + notes (right of the section) ----
comps = [
    (1, "LiTime 48V 100Ah ComFlex", "19.88x12.32x9.25 - on edge", C["bat"], C["bat_s"]),
    (2, "Victron SmartShunt 500A", "4.72x1.81x2.13", C["sheet"], C["cab_s"]),
    (3, "Main Class-T OCP", "~4.3x2.4 (on +)*", C["prot"], C["prot_s"]),
    (4, "- busbar", "~6x1.3*", C["bus"], C["bus_s"]),
    (5, "+ busbar", "~6x1.3*", C["bus"], C["bus_s"]),
    (6, "Velit 48V branch breaker", "~3.4x2.4*", C["prot"], C["prot_s"]),
    (7, "SmartSolar 250/60-Tr", "7.28x9.84x3.74", C["pv"], C["pv_s"]),
    (8, "Orion-Tr 48/24-16A", "7.3x5.1x2.8", C["conv"], C["conv_s"]),
    (9, "Orion-Tr 48/12-20A", "7.3x5.1x2.8", C["conv"], C["conv_s"]),
    (10, "Blue Sea 5026 (24V)", "5.74x3.31*", C["load"], C["load_s"]),
    (11, "12V receptacles", "~5.5x2.2*", C["load"], C["load_s"]),
    (12, "Switch + dimmer (8260)", "6.49x2.3 (cabin face)", C["sheet"], C["cab_s"]),
    (13, "Victron Cerbo GX Mk2", "6.06x3.07x1.89", C["sheet"], C["cab_s"]),
]
lx = 1085
text(lx, 548, "Components  (W x H x D, in):", size=11, weight=700)
for k, (n, name, dims, fill, stroke) in enumerate(comps):
    yy = 570 + k * 21
    rect(lx, yy - 9, 11, 11, fill=fill, stroke=stroke, sw=1.1, rx=2)
    text(lx + 16, yy, f"{n}. {name}", size=9, weight=700, fill=C["ink"])
    text(lx + 16, yy + 10, dims, size=8, fill=C["muted"])

text(800, 690, "All gear in one ~18\" bench; battery transverse, low and centered.", size=9, fill=C["slate"])
text(800, 705, "SmartShunt/Cerbo add Victron monitoring.", size=9, fill=C["slate"])
text(800, 720, "Hinged top; low intake + fan exhaust; confirm depth.", size=9, fill=C["slate"])
text(800, 735, "* nominal/catalog; battery/SmartSolar/Orions = datasheet.", size=9, fill=C["slate"])

# ---------------------------------------------------------------------------
# LEGEND + omissions (bottom strip)
# ---------------------------------------------------------------------------
ly = H - 196
rect(45, ly, 690, 150, fill="#ffffff", stroke=C["sheet_stroke"], sw=1.4, rx=8)
text(60, ly + 26, "Legend", size=15, weight=700)
legend = [
    (C["pv"], C["pv_s"], "PV source / MPPT"),
    (C["bat"], C["bat_s"], "Battery"),
    (C["prot"], C["prot_s"], "Protection / OCP"),
    (C["conv"], C["conv_s"], "DC-DC converter"),
    (C["bus"], C["bus_s"], "Busbar"),
    (C["load"], C["load_s"], "Load / fixture"),
]
for i, (f, s, lab) in enumerate(legend):
    col = i % 2
    rowi = i // 2
    chip(60 + col * 330, ly + 48 + rowi * 30, f, s, lab)
# wire color key
text(60, ly + 144 - 6, "Wire spine:", size=12, weight=700)
line(150, ly + 138, 185, ly + 138, stroke=C["w48"], sw=3); text(190, ly + 142, "48 V", size=11, fill=C["slate"])
line(245, ly + 138, 280, ly + 138, stroke=C["w24"], sw=3); text(285, ly + 142, "24 V", size=11, fill=C["slate"])
line(340, ly + 138, 375, ly + 138, stroke=C["w12"], sw=3); text(380, ly + 142, "12 V", size=11, fill=C["slate"])
line(430, ly + 138, 465, ly + 138, stroke=C["pv_s"], sw=3); text(470, ly + 142, "PV", size=11, fill=C["slate"])

# omissions
rect(755, ly, 680, 150, fill="#ffffff", stroke=C["sheet_stroke"], sw=1.4, rx=8)
text(770, ly + 26, "Intentionally omitted (per request)", size=15, weight=700)
rect(770, ly + 40, 16, 16, fill="#ffffff", stroke=C["omit"], sw=1.5, dash="5 4", rx=2)
text(794, ly + 53, "Anker SOLIX C1000 + PS400 - standalone 120 VAC camp island.",
     size=12, fill=C["slate"])
rect(770, ly + 66, 16, 16, fill="#ffffff", stroke=C["omit"], sw=1.5, dash="5 4", rx=2)
text(794, ly + 79, "Optional ground-mounted 2S LG PV (910 W) + SmartSolar 150/35.",
     size=12, fill=C["slate"])
text(770, ly + 108, "Sources: docs/power.md, docs/dimensions.md. This is the physical",
     size=11, fill=C["muted"])
text(770, ly + 125, "layout; the electrical schematic is docs/diagrams/power-overview.*.",
     size=11, fill=C["muted"])

e("</svg>")

SVG_OUT.write_text("\n".join(out))
print(f"wrote {SVG_OUT} ({SVG_OUT.stat().st_size} bytes)")

try:
    import fitz
    doc = fitz.open(str(SVG_OUT))
    pix = doc[0].get_pixmap(dpi=110)
    pix.save(str(PNG_OUT))
    print(f"wrote {PNG_OUT} ({pix.width}x{pix.height})")
except Exception as exc:  # pragma: no cover
    print(f"PNG render skipped: {exc!r}")
