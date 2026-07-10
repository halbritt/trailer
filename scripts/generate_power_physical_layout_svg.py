#!/usr/bin/env python3
"""Generate the trailer POWER SYSTEM PHYSICAL LAYOUT diagram (SVG).

This is a *physical layout* (where the gear sits), not the electrical schematic
(see docs/diagrams/power-wiring-*.tex for the protected wiring). It has three
panels:

  * Roof plan   - Velit 2000R + the roof 3x LG455 (3S) string and PV gland drop.
  * Floor plan  - footprint with the street-side battery bench, shallow high-wall
                  cabinet, fridge bay, exterior flood/awning positions, and loads.
  * Enclosure   - conceptual elevation of the split bench/cabinet and protected
                  feeder boundary; exact dimensions and component fit are G12.

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
text(45, 60, "Trailer - power system physical layout", size=27, weight=700)
text(45, 86, "Plan view, looking down. Nose/front at left, rear/ramp at right. "
             "Curbside = passenger / awning / door side. As-built overhang and split enclosure are conceptual pending measurements.",
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

# 3x LG455 panels (landscape), as-built array extends past the rear roof edge.
p_across = 83.07 * S
py0 = rmid - p_across / 2
p_len = 41.02 * S
# The exact overhang is an open as-built measurement; the offset is illustrative.
x_right = REAR_X + 12
for i in range(3):
    x0 = x_right - (i + 1) * p_len
    rect(x0, py0, p_len, p_across, fill=C["pv"], stroke=C["pv_s"], sw=1.6, rx=2)
    text(x0 + p_len / 2, rmid, f"LG455 #{i+1}", size=12, weight=700,
         anchor="middle", fill=C["pv_s"])
text((x_right - 3 * p_len + x_right) / 2, py0 - 10,
     "Roof PV - installed LG455 3S -> SmartSolar 250/60-Tr",
     size=12.5, weight=700, anchor="middle", fill=C["pv_s"])
line(REAR_X, py0 - 2, REAR_X, py0 + p_across + 2, stroke=C["prot_s"], sw=1.4, dash="5 4")
text(REAR_X - 6, py0 + 16, "rear roof edge", size=9.5, weight=700,
     anchor="end", fill=C["prot_s"])
text(REAR_X - 6, py0 + 31, "overhang: measure as-built", size=9,
     anchor="end", fill=C["prot_s"])

# Velit at the nose section of the roof. Station is illustrative until measured.
v_len = 26 * S
v_w = 26.4 * S
vx = r_tip + 38
rect(vx, rmid - v_w / 2, v_len, v_w, fill=C["load"], stroke=C["load_s"], sw=1.6, rx=2)
text(vx + v_len / 2, rmid - 4, "Velit", size=12, weight=700, anchor="middle", fill=C["load_s"])
text(vx + v_len / 2, rmid + 12, "2000R", size=11, anchor="middle", fill=C["load_s"])

# Field result supersedes the paper fit assumption.
text((vx + v_len + REAR_X) / 2, rb + 26,
     "As built: three panels did not fit fully behind the Velit; record exact overhang after wash",
     size=11, weight=700, anchor="middle", fill=C["prot_s"])
text(vx + v_len / 2, rmid + v_w / 2 + 18,
     "installed; roof-support repair pending", size=9.5, anchor="middle", fill=C["load_s"])
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
text(gx + 8, rb + 16, "3S down-lead to shallow high-wall cabinet (250/60 MPPT)",
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

# --- split power enclosure: low street-side battery bench + high shallow cabinet ---
bench_x, bench_y, bench_w, bench_h = f_taper + 8, fb - 70, 108, 54
rect(bench_x, bench_y, bench_w, bench_h, fill=C["bat"], stroke=C["bat_s"],
     sw=1.6, rx=3, dash="5 3", op=0.95)
text(bench_x + bench_w / 2, bench_y + 23, "BATTERY BENCH", size=10, weight=700,
     anchor="middle", fill=C["bat_s"])
text(bench_x + bench_w / 2, bench_y + 39, "street-side; size TBD", size=8.5,
     anchor="middle", fill=C["muted"])

cab_x, cab_y, cab_w, cab_h = f_taper + 8, fb - 15, 190, 10
rect(cab_x, cab_y, cab_w, cab_h, fill=C["cab"], stroke=C["cab_s"], sw=1.6,
     rx=2, dash="4 3")
text(cab_x + cab_w / 2, cab_y + 8, "HIGH CABINET - WALL PLANE", size=6.5,
     weight=700, anchor="middle", fill=C["cab_s"])

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
text(frx + frw * 0.66, fcy - 8, "Dometic CFX3-95DZ", size=12, weight=700, anchor="middle", fill=C["load_s"])
text(frx + frw * 0.66, fcy + 6, "37.9\" x 20.9\" (24 V)", size=10, anchor="middle", fill=C["load_s"])
text(frx + frw * 0.66, fcy + 20, "+ lid swing", size=9, anchor="middle", fill=C["muted"])

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
text(404, fb + 54, "bikes: nose-forward, via rear ramp - one rail roadside, one curbside (straddle CL)",
     size=10, anchor="middle", fill=C["muted"])
# bar-overlap callout (the curbside bike's bars sweep up over the top-mounted fridge)
line(470, fcy + frd / 2 + 4, 392, fcy + frd / 2 - 16, stroke=C["slate"], sw=1, dash="3 3")
text(560, fcy + frd / 2 + 2, "bars sweep over fridge", size=9.5, weight=700, anchor="middle", fill=C["slate"])
text(560, fcy + frd / 2 + 16, "verify loaded clearance", size=8.5, anchor="middle", fill=C["muted"])

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

# floor dimensions
dimv(REAR_X + 26, ft, fb, '81" interior', side="right")
dimh(fb + 100, f_tip, REAR_X, '156" centerline', above=False)

# orientation
text(f_tip - 6, fmid, "NOSE", size=11, weight=700, anchor="end", fill=C["muted"])
text(REAR_X + 6, fb - 6, "REAR / RAMP", size=11, weight=700, fill=C["muted"])

# ---------------------------------------------------------------------------
# PANEL C - SPLIT POWER ENCLOSURE: STREET-SIDE ELEVATION
# ---------------------------------------------------------------------------
CX, CY, CW, CH = 770, 118, 668, 720
rect(CX, CY, CW, CH, fill="#ffffff", stroke=C["cab_s"], sw=1.8, rx=8)
text(CX + 16, CY + 28, "C  Split power enclosure - street-side elevation", size=17, weight=700, fill=C["cab_s"])
text(CX + 16, CY + 47,
     "Battery low in a compact bench; active Victron gear higher in a shallow cabinet.",
     size=11, fill=C["muted"])
text(CX + 16, CY + 63,
     "Conceptual placement only. Bench/cabinet dimensions, backing, and clearances are G12.",
     size=11, fill=C["muted"])

# wall and floor datums
wall_x = CX + 42
floor_y = CY + 632
line(wall_x, CY + 90, wall_x, floor_y, stroke=C["wall"], sw=4)
line(wall_x, floor_y, CX + CW - 34, floor_y, stroke=C["wall"], sw=4)
text(wall_x - 8, CY + 108, "NOSE WALL", size=9, weight=700, anchor="end", fill=C["muted"], rot=-90)
text(wall_x + 8, floor_y + 18, "FLOOR / STREET-SIDE", size=9, weight=700, fill=C["muted"])

# low battery bench
bx, by, bw, bh = CX + 62, CY + 465, 245, 165
rect(bx, by, bw, bh, fill=C["cab"], stroke=C["cab_s"], sw=1.8, rx=4)
text(bx + 12, by + 23, "LOW BATTERY BENCH", size=12, weight=700, fill=C["bat_s"])
text(bx + 12, by + 41, "size / anchors / orientation: G12", size=9, fill=C["muted"])
block(bx + 18, by + 58, 138, 77, "LiTime battery", C["bat"], C["bat_s"],
      size=10, sub="low; orientation dry-fit")
block(bx + 166, by + 70, 64, 53, "Class-T", C["prot"], C["prot_s"],
      size=9, sub="TBD")

# high shallow cabinet
cx, cy, cw, ch = CX + 345, CY + 105, 270, 420
rect(cx, cy, cw, ch, fill=C["cab"], stroke=C["cab_s"], sw=1.8, rx=5)
text(cx + 12, cy + 23, "SHALLOW HIGH-WALL CABINET", size=12, weight=700, fill=C["cab_s"])
text(cx + 12, cy + 41, "post backing / W x H x D / airflow: G12", size=9, fill=C["muted"])

block(cx + 18, cy + 58, 112, 74, "SmartSolar", C["pv"], C["pv_s"],
      size=10, sub="250/60-Tr")
block(cx + 140, cy + 58, 112, 74, "Cerbo GX", C["sheet"], C["cab_s"],
      size=10, sub="3.15 A inline")
block(cx + 18, cy + 145, 112, 68, "Orion 48/24", C["conv"], C["conv_s"],
      size=9.5, sub="20 A input")
block(cx + 140, cy + 145, 112, 68, "Orion 48/12", C["conv"], C["conv_s"],
      size=9.5, sub="input TBD")
block(cx + 18, cy + 230, 92, 54, "SmartShunt", C["sheet"], C["cab_s"], size=9)
block(cx + 120, cy + 230, 60, 54, "+ bus", C["bus"], C["bus_s"], size=8.5)
block(cx + 190, cy + 230, 60, 54, "- bus", C["bus"], C["bus_s"], size=8.5)
block(cx + 18, cy + 301, 106, 58, "24 V fuses", C["load"], C["load_s"], size=9,
      sub="Blue Sea 5026")
block(cx + 136, cy + 301, 114, 58, "12 V fuses", C["load"], C["load_s"], size=9,
      sub="aux only")
block(cx + 18, cy + 372, 232, 32, "switch / dimmer / receptacle face", C["sheet"], C["cab_s"], size=9)

# protected positive feeder and shunted negative return
line(bx + 156, by + 96, bx + 166, by + 96, stroke=C["w48"], sw=3)
line(bx + 230, by + 96, cx + 150, cy + 230, stroke=C["w48"], sw=3)
text(bx + 225, by + 60, "+ protected before leaving bench", size=8.5, weight=700,
     fill=C["w48"])
line(bx + 87, by + 135, cx + 64, cy + 257, stroke=C["slate"], sw=3)
text(bx + 88, by + 151, "- only to SmartShunt battery side", size=8.5, weight=700,
     fill=C["slate"])

text(CX + 42, CY + 685, "Active DC gear only in the shallow cabinet; the deferred MultiPlus location is open.",
     size=10, weight=700, fill=C["prot_s"])
text(CX + 42, CY + 704, "See power-wiring-48v and power-wiring-low-voltage for fuse placement.",
     size=10, fill=C["muted"])

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
text(794, ly + 79, "Optional ground-mounted LG 2S PV + SmartSolar 150/35.",
     size=12, fill=C["slate"])
text(770, ly + 108, "Sources: docs/power.md, docs/dimensions.md. This is the physical",
     size=11, fill=C["muted"])
text(770, ly + 125, "layout; install schematics are power-wiring-48v.* and power-wiring-low-voltage.*.",
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
