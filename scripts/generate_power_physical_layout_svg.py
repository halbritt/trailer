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

W, H = 1480, 1240
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
ft, fb = 548, 548 + 81 * S               # floor top / bottom (curbside = bottom)
fmid = (ft + fb) / 2
f_taper = REAR_X - 141 * S               # straight-wall length 141
f_tip = f_taper - 60

text(45, 530, "B  Floor plan  (roadside = top · curbside = bottom)", size=17, weight=700, fill=C["slate"])

# footprint
poly([(REAR_X, ft), (REAR_X, fb), (f_taper, fb), (f_tip, fmid), (f_taper, ft)],
     fill="#ffffff", stroke=C["wall"], sw=4)

# centerline (the two bike rows straddle it)
line(f_tip + 6, fmid, REAR_X, fmid, stroke=C["muted"], sw=1, dash="9 7")
text(520, fmid + 13, "centerline", size=9, anchor="middle", fill=C["muted"])

# --- nose power cabinet: ~8" deep, on the ROADSIDE nose flank ---
# Upper flank A(taper-start, top) -> B(nose tip); offset inward into the cabin by 8".
fdx, fdy = f_tip - f_taper, fmid - ft
flen = (fdx * fdx + fdy * fdy) ** 0.5
nx, ny = fdy / flen, -fdx / flen          # inward normal (+x,+y, into the cabin)
cdep = 8 * S
A_fl, B_fl = (f_taper, ft), (f_tip, fmid)
A_in = (A_fl[0] + nx * cdep, A_fl[1] + ny * cdep)
B_in = (B_fl[0] + nx * cdep, B_fl[1] + ny * cdep)
poly([A_fl, B_fl, B_in, A_in], fill=C["cab"], stroke=C["cab_s"], sw=1.6, dash="5 3", op=0.95)
cab_out = ((A_in[0] + B_in[0]) / 2, (A_in[1] + B_in[1]) / 2)   # 24 V feed origin
text(A_in[0] + 24, fmid - 104, "NOSE POWER CABINET", size=12, weight=700, fill=C["cab_s"])
text(A_in[0] + 24, fmid - 89, "~8\" deep · roadside nose flank", size=10, fill=C["muted"])
text(A_in[0] + 24, fmid - 74, "contents at real scale: detail C", size=10, fill=C["muted"])
line(A_in[0] + 18, fmid - 96, cab_out[0], cab_out[1], stroke=C["cab_s"], sw=1, dash="3 3")

# --- side door (curbside / bottom), 30 in opening, 98 in from rear ---
door_aft = REAR_X - 98 * S
door_fwd = REAR_X - 128 * S
line(door_fwd, fb, door_aft, fb, stroke=C["w24"], sw=5)
path(f"M {door_aft} {fb} A {30*S} {30*S} 0 0 0 {door_aft - 22*S} {fb + 22*S}",
     stroke=C["w24"], sw=2, dash="7 6")
text((door_fwd + door_aft) / 2, fb + 40, "side door 30\"", size=11.5, weight=700,
     anchor="middle", fill=C["w24"])

# --- fridge bay (curbside, aft of door) ---
frx = door_aft
frw = 37.9 * S
frd = 20.9 * S
rect(frx, fb - frd, frw, frd, fill=C["load"], stroke=C["load_s"], sw=1.6, rx=2)
text(frx + frw / 2, fb - frd / 2 - 8, "Dometic CFX3-95DZ", size=12, weight=700, anchor="middle", fill=C["load_s"])
text(frx + frw / 2, fb - frd / 2 + 6, "37.9\" x 20.9\" (24 V)", size=10, anchor="middle", fill=C["load_s"])
text(frx + frw / 2, fb - frd / 2 + 20, "+ lid swing", size=9, anchor="middle", fill=C["muted"])

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

bikeA_y = ft + 27.5 * S                     # roadside rail (~27" off the roadside wall)
bikeB_y = ft + 53.5 * S                     # curbside rail, 26" OC (~27" off the curbside wall)
draw_bike(322, 666, bikeA_y, 402, 32 * S, "WR250R")
draw_bike(258, 602, bikeB_y, 338, 34 * S, "CRF450RL")
line(322, bikeA_y, 246, bikeA_y, stroke=C["muted"], sw=1)
line(258, bikeB_y, 246, bikeB_y, stroke=C["muted"], sw=1)
dimv(246, bikeA_y, bikeB_y, '26" OC', side="left")
text(400, ft + 6, "bikes: nose-forward, via rear ramp - one rail roadside, one curbside (straddle CL)",
     size=10, anchor="middle", fill=C["muted"])
# bar-overlap callout
line(338, bikeB_y + 44, 472, fb - frd - 16, stroke=C["slate"], sw=1, dash="3 3")
text(480, fb - frd - 18, "handlebars sweep over the fridge", size=10, weight=700, fill=C["slate"])
text(480, fb - frd - 4, "(clears it at bar height: ~30\"+ vs 18.6\" fridge)", size=9, fill=C["muted"])

# --- interior loads ---
usb_x, usb_y = frx + frw + 40, fb - 24
e(f'<circle cx="{usb_x}" cy="{usb_y}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(usb_x + 12, usb_y + 4, "USB-C PD / GPS (24 V)", size=10.5, fill=C["slate"])
led_x, led_y = 470, ft + 14
e(f'<circle cx="{led_x}" cy="{led_y}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(led_x + 12, led_y + 4, "interior LED (ceiling, 24 V)", size=10.5, fill=C["slate"])

# --- exterior floods (7x VAL2-NW9) ---
flood(430, fb + 8, "F curb", 430, fb + 24)
flood(555, fb + 8, "F curb", 555, fb + 24)
flood(430, ft - 8, "F road", 430, ft - 16)
flood(555, ft - 8, "F road", 555, ft - 16)
# nose-face floods, on the exterior of each V-nose flank
flood(86, 624, "F nose", 52, 612, anchor="end")
flood(86, 796, "F nose", 52, 810, anchor="end")
# rear flood
flood(REAR_X + 8, ft + 70, "F rear", REAR_X + 18, ft + 74, anchor="start")

# --- awning (curbside, at roofline) + warm strip ---
aw_x1, aw_x2 = REAR_X - 138 * S, REAR_X
line(aw_x1, fb + 56, aw_x2, fb + 56, stroke=C["load_s"], sw=4, dash="2 0")
line(aw_x1, fb + 60, aw_x2, fb + 60, stroke="#f59e0b", sw=2.5, dash="4 4")
text((aw_x1 + aw_x2) / 2, fb + 80,
     "Fiamma F45s awning case 138\" + warm 24 V LED strip (curbside, at roofline)",
     size=10.5, weight=700, anchor="middle", fill=C["load_s"])

# --- winter heater outlet (exterior) ---
e(f'<circle cx="{REAR_X - 40}" cy="{fb + 8}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(REAR_X - 40, fb + 24, "heater (ext.)", size=10, anchor="middle", fill=C["load_s"])

# --- 24 V feed hints from cabinet to loads ---
line(cab_out[0], cab_out[1], frx + frw / 2, fb - frd - 4, stroke=C["w24"], sw=1.4, dash="3 4")
line(cab_out[0], cab_out[1], led_x, led_y + 8, stroke=C["w24"], sw=1.4, dash="3 4")
text(cab_out[0] + 26, cab_out[1] + 8, "24 V branches", size=10, fill=C["w24"])

# floor dimensions
dimv(REAR_X + 26, ft, fb, '81" interior', side="right")
dimh(fb + 100, f_tip, REAR_X, '156" centerline (141" straight + 15" nose)', above=False)

# orientation
text(f_tip - 6, fmid, "NOSE", size=11, weight=700, anchor="end", fill=C["muted"])
text(REAR_X + 6, fb - 6, "REAR / RAMP", size=11, weight=700, fill=C["muted"])

# ---------------------------------------------------------------------------
# PANEL C - NOSE CABINET: REAL-SCALE FRONT ELEVATION (components to scale)
# ---------------------------------------------------------------------------
CX, CY, CW, CH = 770, 118, 668, 720
rect(CX, CY, CW, CH, fill="#ffffff", stroke=C["cab_s"], sw=1.8, rx=8)
text(CX + 16, CY + 28, "C  Nose power cabinet - real-scale layout",
     size=17, weight=700, fill=C["cab_s"])
text(CX + 16, CY + 47,
     "Front elevation, to scale. Electronics on the ~8\"-deep wall cabinet; 48 V battery strapped to the floor.",
     size=11, fill=C["muted"])

# elevation frame: 30 in W x 46 in H envelope, 1 in = sc_e px
sc_e = 12
EX0, EYb = 800, 760                       # cabinet interior bottom-left (svg)
CABW, CABH = 30, 46
CAB_BOT = 13                              # wall cabinet bottom, in. off the floor (battery sits below)
# wall cabinet (electronics on the backboard) - bottom raised off the floor
rect(EX0, EYb - CABH * sc_e, CABW * sc_e, (CABH - CAB_BOT) * sc_e,
     fill="#fbfdfe", stroke=C["cab_s"], sw=1.6, rx=4)
line(EX0, EYb, EX0 + CABW * sc_e, EYb, stroke=C["cab_s"], sw=3)          # trailer floor
text(EX0 + CABW * sc_e / 2, EYb - CABH * sc_e - 7,
     "Front elevation - electronics on the ~8\" wall cabinet; battery on the floor below",
     size=10.5, weight=700, anchor="middle", fill=C["cab_s"])

# components: (n, ex, ey, ew, eh, fill, stroke, name, dims, in-box label, label size)
comps = [
    (1,  5.0,  0.0, 19.88, 12.32, C["bat"],   C["bat_s"],  "LiTime 48V 100Ah ComFlex", "19.88x12.32x9.25  (depth driver)", "LiTime 48V|100Ah ComFlex", 11),
    (2,  1.5, 13.6, 3.5,   1.8,   C["sheet"], C["cab_s"],  "LiTime 500A shunt",         "~3.5x1.8  (on -)*",  "shunt", 7),
    (3, 23.7, 13.4, 4.3,   2.4,   C["prot"],  C["prot_s"], "Main Class-T OCP",          "~4.3x2.4  (on +)*",  "Class-T", 7.5),
    (4,  1.5, 17.2, 6.0,   1.3,   C["bus"],   C["bus_s"],  "- busbar",                  "~6x1.3*",  "- bus", 8),
    (5, 10.0, 17.2, 6.0,   1.3,   C["bus"],   C["bus_s"],  "+ busbar",                  "~6x1.3*",  "+ bus", 8),
    (6, 17.5, 15.4, 3.4,   2.4,   C["prot"],  C["prot_s"], "Velit 48V branch breaker",  "~3.4x2.4*",  "Velit|brk", 7),
    (7,  1.5, 20.3, 7.28,  9.84,  C["pv"],    C["pv_s"],   "SmartSolar 250/60-Tr",      "7.28x9.84x3.74",  "SmartSolar|250/60-Tr", 9.5),
    (8, 11.0, 20.3, 7.3,   5.1,   C["conv"],  C["conv_s"], "Orion-Tr 48/24-16A",        "7.3x5.1x2.8",  "Orion-Tr|48/24-16A", 9),
    (9, 20.5, 20.3, 7.3,   5.1,   C["conv"],  C["conv_s"], "Orion-Tr 48/12-20A",        "7.3x5.1x2.8",  "Orion-Tr|48/12-20A", 9),
    (10,11.0, 27.5, 5.74,  3.31,  C["load"],  C["load_s"], "Blue Sea 5026 (24V)",       "5.74x3.31*",  "Blue Sea|5026", 8.5),
    (11,20.5, 27.5, 5.5,   2.2,   C["load"],  C["load_s"], "12V receptacles",           "~5.5x2.2*",  "12V recept.", 8),
    (12,11.0, 33.0, 6.49,  4.5,   C["sheet"], C["cab_s"],  "Switch + dimmer panel (8260)", "6.49x2.3 + dimmers",  "Switch +|dimmers", 9),
]
for n, ex, ey, ew, eh, fill, stroke, name, dims, lab, lsize in comps:
    x = EX0 + ex * sc_e
    y = EYb - (ey + eh) * sc_e
    bw_, bh_ = ew * sc_e, eh * sc_e
    rect(x, y, bw_, bh_, fill=fill, stroke=stroke, sw=1.5, rx=2)
    cxb, cyb = x + bw_ / 2, y + bh_ / 2
    e(f'<circle cx="{x - 11}" cy="{cyb}" r="7" fill="#ffffff" stroke="{stroke}" stroke-width="1.2"/>')
    text(x - 11, cyb + 3.5, str(n), size=9, weight=700, anchor="middle", fill=stroke)
    parts = lab.split("|")
    if len(parts) == 1:
        text(cxb, cyb + lsize / 3, parts[0], size=lsize, weight=700, anchor="middle", fill=C["ink"])
    else:
        text(cxb, cyb - lsize * 0.15, parts[0], size=lsize, weight=700, anchor="middle", fill=C["ink"])
        text(cxb, cyb + lsize * 0.95, parts[1], size=lsize, weight=700, anchor="middle", fill=C["ink"])

# battery is floor-mounted (strapped down to the floor), not on the wall/backboard
b_x, b_w, b_top = EX0 + 5.0 * sc_e, 19.88 * sc_e, EYb - 12.32 * sc_e
line(b_x + 6, b_top - 3, b_x + b_w - 6, b_top - 3, stroke=C["slate"], sw=2.5)   # hold-down bar
for sf in (0.12, 0.88):
    sxp = b_x + b_w * sf
    line(sxp, b_top - 3, sxp, EYb, stroke=C["slate"], sw=2.5)                   # strap
    line(sxp - 6, EYb, sxp + 6, EYb, stroke=C["slate"], sw=3)                   # floor anchor
text(b_x + b_w / 2, EYb - 24, "floor-mounted (strapped down)",
     size=9, anchor="middle", fill=C["slate"])

# ---- interconnecting wiring (red +48V, dark -48V, blue 24V, purple 12V, cyan PV) ----
NEG = "#374151"
def wire(pts, color, w=2.0):
    d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    e(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" '
      f'stroke-linejoin="round" stroke-linecap="round"/>')
def jdot(x, y, color):
    e(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="{color}"/>')

yCB, yRP, yRN = 516.4, 527.2, 534.4        # converter bottoms, + rail, - rail
yBT, yBM, yBB = 538.0, 545.8, 553.6        # busbar top / mid / bottom

# battery terminal marks
text(1064, 625, "+", size=12, weight=700, anchor="middle", fill=C["w48"])
text(896, 626, "-", size=13, weight=700, anchor="middle", fill=NEG)

# protection: battery -> shunt(-) / Class-T(+) -> busbars
wire([(896, 612.16), (896, 596.8), (839, 596.8)], NEG)
wire([(839, 575.2), (839, yBB)], NEG)
wire([(1064, 612.16), (1064, 599.2), (1110.2, 599.2)], C["w48"])
wire([(1110.2, 570.4), (1110.2, yBM), (992, yBM)], C["w48"])

# 48 V rails + busbar feeds
wire([(818, yRP), (1138.4, yRP)], C["w48"], 2.4)
wire([(818, yRN), (1138.4, yRN)], NEG, 2.4)
wire([(956, yBT), (956, yRP)], C["w48"]); jdot(956, yRP, C["w48"])
wire([(854, yBT), (854, yRN)], NEG); jdot(854, yRN, NEG)

# converter input stubs from the rails
for xp, xn in [(848, 872), (950, 980), (1064, 1094)]:
    wire([(xp, yRP), (xp, yCB)], C["w48"]); jdot(xp, yRP, C["w48"])
    wire([(xn, yRN), (xn, yCB)], NEG); jdot(xn, yRN, NEG)

# converter outputs -> loads (straight up; loads sit above their converter)
wire([(975.8, 455.2), (975.8, 430)], C["w24"], 2.2)     # Orion 48/24 -> 5026
wire([(1089.8, 455.2), (1089.8, 430)], C["w12"], 2.2)   # Orion 48/12 -> receptacles
wire([(966.44, 390.28), (966.44, 364)], C["w24"], 2.2)  # 5026 -> switch panel
text(982, 445, "24V", size=8, fill=C["w24"])
text(1096, 445, "12V", size=8, fill=C["w12"])

# roof PV in -> MPPT
wire([(861.68, 382.32), (861.68, 398.32)], C["pv_s"], 2.4)
poly([(856.68, 398.32), (866.68, 398.32), (861.68, 406.32)], fill=C["pv_s"], stroke="none")
text(861.68, 378, "roof PV in", size=9.5, weight=700, anchor="middle", fill=C["pv_s"])

# Velit 48 V branch: + busbar -> breaker -> roof AC
wire([(956, yBB), (956, 560.8), (1010, 560.8)], C["w48"], 2.0)
wire([(1050.8, 560.8), (1086, 560.8)], C["w48"], 2.0)
poly([(1086, 555.8), (1086, 565.8), (1095, 560.8)], fill=C["w48"], stroke="none")
text(1098, 564, "to Velit AC", size=8.5, weight=700, anchor="start", fill=C["w48"])

# scale bar (12 in)
sb_y = EYb + 16
line(EX0, sb_y, EX0 + 12 * sc_e, sb_y, stroke=C["ink"], sw=1.6)
line(EX0, sb_y - 4, EX0, sb_y + 4, stroke=C["ink"], sw=1.6)
line(EX0 + 12 * sc_e, sb_y - 4, EX0 + 12 * sc_e, sb_y + 4, stroke=C["ink"], sw=1.6)
text(EX0 + 6 * sc_e, sb_y + 15, "12 in", size=10, anchor="middle", fill=C["slate"])

# depth + face/vent notes (under the elevation)
text(EX0, EYb + 50, "Wall cabinet ~8\" deep (electronics <=3.7\"). The 48 V battery is "
     "floor-mounted - low & centered, not on the backboard.",
     size=9.5, fill=C["slate"])
text(EX0, EYb + 66, "Cabin face: 8260 + 6x 8282 switches + 6x 24V dimmers. "
     "Vent: low cabin intake + high fan exhaust (24V fan + thermostat).",
     size=9.5, fill=C["slate"])

# component list (right column)
lx = EX0 + CABW * sc_e + 28
text(lx, CY + 92, "Components  (W x H x D, in):", size=12, weight=700)
for i, (n, ex, ey, ew, eh, fill, stroke, name, dims, lab, lsize) in enumerate(comps):
    yy = CY + 116 + i * 23
    rect(lx, yy - 10, 13, 13, fill=fill, stroke=stroke, sw=1.3, rx=2)
    text(lx + 20, yy - 1, f"{n}. {name}", size=10, weight=700, fill=C["ink"])
    text(lx + 20, yy + 11, dims, size=9, fill=C["muted"])
text(lx, CY + 116 + 12 * 23 + 6,
     "* nominal/catalog. Battery, SmartSolar, Orions: datasheet.",
     size=9, fill=C["muted"])
text(lx, CY + 116 + 12 * 23 + 22,
     "Flow/topology: see schematic (power-overview).",
     size=9, fill=C["muted"])

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
