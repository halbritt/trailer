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

text(45, 530, "B  Floor plan  (curbside = bottom)", size=17, weight=700, fill=C["slate"])

# footprint
poly([(REAR_X, ft), (REAR_X, fb), (f_taper, fb), (f_tip, fmid), (f_taper, ft)],
     fill="#ffffff", stroke=C["wall"], sw=4)

# --- nose power cabinet: ~8" deep, localized to the LEFT (roadside) nose flank ---
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
text(A_in[0] + 24, fmid - 89, "~8\" deep · left (roadside) nose flank", size=10, fill=C["muted"])
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

# --- bikes (roadside/top, nose-forward, near the rear; bars overlap the fridge) ---
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

bikeA_y = ft + 22 * S
bikeB_y = ft + 48 * S                       # 26" OC below bike A
draw_bike(322, 666, bikeA_y, 402, 32 * S, "WR250R")
draw_bike(258, 602, bikeB_y, 338, 34 * S, "CRF450RL")
line(322, bikeA_y, 246, bikeA_y, stroke=C["muted"], sw=1)
line(258, bikeB_y, 246, bikeB_y, stroke=C["muted"], sw=1)
dimv(246, bikeA_y, bikeB_y, '26" OC', side="left")
text(380, ft + 6, "bikes: nose-forward, roadside, loaded via rear ramp",
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
     "Front elevation of the ~8\"-deep left-flank cabinet. Components drawn to scale.",
     size=11, fill=C["muted"])

# elevation frame: 30 in W x 46 in H envelope, 1 in = sc_e px
sc_e = 12
EX0, EYb = 800, 760                       # cabinet interior bottom-left (svg)
CABW, CABH = 30, 46
rect(EX0, EYb - CABH * sc_e, CABW * sc_e, CABH * sc_e,
     fill="#fbfdfe", stroke=C["cab_s"], sw=1.6, rx=4)
line(EX0, EYb, EX0 + CABW * sc_e, EYb, stroke=C["cab_s"], sw=3)          # floor
text(EX0 + CABW * sc_e / 2, EYb - CABH * sc_e - 7,
     "Front elevation - 30\" W x 46\" H envelope (fit to components)",
     size=10.5, weight=700, anchor="middle", fill=C["cab_s"])

# components: (n, ex, ey, ew, eh, fill, stroke, name, dims)   ex/ey from bottom-left, inches
comps = [
    (1,  5.0,  0.0, 19.88, 12.32, C["bat"],   C["bat_s"],  "LiTime 48V 100Ah ComFlex", "19.88x12.32x9.25  (depth driver)"),
    (2,  2.0, 13.6, 3.5,   1.8,   C["sheet"], C["cab_s"],  "LiTime 500A shunt",         "~3.5x1.8  (on -)*"),
    (3, 23.7, 13.4, 4.3,   2.4,   C["prot"],  C["prot_s"], "Main Class-T OCP",          "~4.3x2.4  (on +)*"),
    (4,  2.0, 17.2, 6.0,   1.3,   C["bus"],   C["bus_s"],  "- busbar",                  "~6x1.3*"),
    (5, 10.0, 17.2, 6.0,   1.3,   C["bus"],   C["bus_s"],  "+ busbar",                  "~6x1.3*"),
    (6, 24.0, 17.0, 3.4,   2.2,   C["prot"],  C["prot_s"], "Velit 48V branch breaker",  "~3.4x2.2*"),
    (7,  1.5, 20.3, 7.28,  9.84,  C["pv"],    C["pv_s"],   "SmartSolar 250/60-Tr",      "7.28x9.84x3.74"),
    (8, 11.0, 20.3, 7.3,   5.1,   C["conv"],  C["conv_s"], "Orion-Tr 48/24-16A",        "7.3x5.1x2.8"),
    (9, 20.5, 20.3, 7.3,   5.1,   C["conv"],  C["conv_s"], "Orion-Tr 48/12-20A",        "7.3x5.1x2.8"),
    (10, 1.5, 31.5, 5.74,  3.31,  C["load"],  C["load_s"], "Blue Sea 5026 (24V)",       "5.74x3.31*"),
    (11, 9.5, 31.5, 5.5,   2.2,   C["load"],  C["load_s"], "12V receptacles",           "~5.5x2.2*"),
    (12, 1.5, 37.0, 6.49,  4.5,   C["sheet"], C["cab_s"],  "Switch + dimmer panel (8260)", "6.49x2.3 + dimmers"),
]
for n, ex, ey, ew, eh, fill, stroke, name, dims in comps:
    x = EX0 + ex * sc_e
    y = EYb - (ey + eh) * sc_e
    rect(x, y, ew * sc_e, eh * sc_e, fill=fill, stroke=stroke, sw=1.5, rx=2)
    cy = y + eh * sc_e / 2
    e(f'<circle cx="{x - 11}" cy="{cy}" r="7" fill="#ffffff" stroke="{stroke}" stroke-width="1.2"/>')
    text(x - 11, cy + 3.5, str(n), size=9, weight=700, anchor="middle", fill=stroke)

# orientation label (where roof PV enters)
text(EX0 + (1.5 + 7.28 / 2) * sc_e, EYb - 30.6 * sc_e, "PV in",
     size=9.5, weight=700, anchor="middle", fill=C["pv_s"])

# scale bar (12 in)
sb_y = EYb + 16
line(EX0, sb_y, EX0 + 12 * sc_e, sb_y, stroke=C["ink"], sw=1.6)
line(EX0, sb_y - 4, EX0, sb_y + 4, stroke=C["ink"], sw=1.6)
line(EX0 + 12 * sc_e, sb_y - 4, EX0 + 12 * sc_e, sb_y + 4, stroke=C["ink"], sw=1.6)
text(EX0 + 6 * sc_e, sb_y + 15, "12 in", size=10, anchor="middle", fill=C["slate"])

# depth + face/vent notes (under the elevation)
text(EX0, EYb + 50, "Cabinet ~8\" deep: electronics <=3.7\" (MPPT 3.74, Orions 2.8); "
     "battery is the depth driver (9.25\" min) - sits low on the floor at the base.",
     size=9.5, fill=C["slate"])
text(EX0, EYb + 66, "Cabin face: 8260 + 6x 8282 switches + 6x 24V dimmers. "
     "Vent: low cabin intake + high fan exhaust (24V fan + thermostat).",
     size=9.5, fill=C["slate"])

# component list (right column)
lx = EX0 + CABW * sc_e + 28
text(lx, CY + 92, "Components  (W x H x D, in):", size=12, weight=700)
for i, (n, ex, ey, ew, eh, fill, stroke, name, dims) in enumerate(comps):
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
