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

# --- nose power cabinet zone (shaded) ---
cab_back = f_taper + 14 * S               # cabinet extends ~14 in aft of taper
poly([(f_tip, fmid), (f_taper, ft), (cab_back, ft), (cab_back, fb), (f_taper, fb)],
     fill=C["cab"], stroke=C["cab_s"], sw=1.6, dash="6 4", op=0.9)
text((f_tip + cab_back) / 2 + 6, fmid - 6, "NOSE POWER", size=12, weight=700,
     anchor="middle", fill=C["cab_s"])
text((f_tip + cab_back) / 2 + 6, fmid + 10, "CABINET", size=12, weight=700,
     anchor="middle", fill=C["cab_s"])
text((f_tip + cab_back) / 2 + 6, fmid + 28, "(detail C)", size=10.5,
     anchor="middle", fill=C["muted"])

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
text(frx + frw / 2, fb - frd / 2 - 4, "Fridge", size=12, weight=700, anchor="middle", fill=C["load_s"])
text(frx + frw / 2, fb - frd / 2 + 12, "CFX3 95DZ (24 V)", size=10, anchor="middle", fill=C["load_s"])

# --- bikes (roadside / top, context only) ---
for i in range(2):
    by = ft + 10 + i * 30
    rect(f_taper + 6, by, 86 * S, 24, fill="#ffffff",
         stroke=C["omit"], sw=1.3, dash="5 4", rx=3)
text(f_taper + 6 + 86 * S / 2, ft + 10 + 70, "bikes  (roadside, ~86\" - context only)",
     size=10.5, anchor="middle", fill=C["muted"])

# --- interior loads ---
usb_x, usb_y = frx + frw + 36, fb - 26
e(f'<circle cx="{usb_x}" cy="{usb_y}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(usb_x + 12, usb_y + 4, "USB-C PD / GPS (24 V)", size=10.5, fill=C["slate"])
led_x, led_y = 470, fmid - 36
e(f'<circle cx="{led_x}" cy="{led_y}" r="6" fill="{C["load"]}" '
  f'stroke="{C["load_s"]}" stroke-width="1.6"/>')
text(led_x + 12, led_y + 4, "interior LED zones (24 V)", size=10.5, fill=C["slate"])

# --- exterior floods (7x VAL2-NW9) ---
flood(430, fb + 8, "F curb", 430, fb + 24)
flood(555, fb + 8, "F curb", 555, fb + 24)
flood(430, ft - 8, "F road", 430, ft - 16)
flood(555, ft - 8, "F road", 555, ft - 16)
# nose-face floods on the two flanks
flood((f_tip + f_taper) / 2, (fmid + ft) / 2 - 12, "F nose", f_taper + 4, ft + 70, anchor="start")
flood((f_tip + f_taper) / 2, (fmid + fb) / 2 + 12, "F nose", f_taper + 4, fb - 60, anchor="start")
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
line(cab_back, fmid + 24, frx + frw / 2, fb - frd - 4, stroke=C["w24"], sw=1.4, dash="3 4")
line(cab_back, fmid - 24, led_x, led_y + 6, stroke=C["w24"], sw=1.4, dash="3 4")
text(cab_back + 8, fmid + 46, "24 V branches", size=10, fill=C["w24"])

# floor dimensions
dimv(REAR_X + 26, ft, fb, '81" interior', side="right")
dimh(fb + 100, f_tip, REAR_X, '156" centerline (141" straight + 15" nose)', above=False)

# orientation
text(f_tip - 6, fmid, "NOSE", size=11, weight=700, anchor="end", fill=C["muted"])
text(REAR_X + 6, fb - 6, "REAR / RAMP", size=11, weight=700, fill=C["muted"])

# ---------------------------------------------------------------------------
# PANEL C - NOSE CABINET DETAIL (contents + 48 V spine, bottom-up flow)
# ---------------------------------------------------------------------------
CX, CY, CW, CH = 770, 118, 668, 720
rect(CX, CY, CW, CH, fill="#ffffff", stroke=C["cab_s"], sw=1.8, rx=8)
text(CX + 16, CY + 28, "C  Nose power cabinet - contents & 48 V spine",
     size=17, weight=700, fill=C["cab_s"])
text(CX + 16, CY + 48,
     "Contents + required connections (flows bottom-up: battery -> bus -> converters -> loads).",
     size=11, fill=C["muted"])
text(CX + 16, CY + 64,
     "Exact internal stationing is an open gate - this is not a final placement.",
     size=11, fill=C["muted"])

inx = CX + 24
inw = CW - 48
bw = (inw - 3 * 14) / 4                  # 4 consumer columns
def col_x(i): return inx + i * (bw + 14)
def col_cx(i): return col_x(i) + bw / 2

out_y, out_h = 214, 54
con_y, con_h = 300, 60
manifold_y = 388
busL_x, busR_x, bus_w = inx, inx + 322, 298
bus_y, bus_h = 398, 40
so_y, so_h = 480, 48                      # shunt / OCP
bat_x, bat_w = CX + CW/2 - 150, 300
bat_y, bat_h = 576, 60

# --- battery (bottom, low & centered) ---
block(bat_x, bat_y, bat_w, bat_h, "LiTime 48 V 100 Ah ComFlex", C["bat"], C["bat_s"],
      size=13, sub="5.12 kWh - low & centered (tongue weight)")
bat_neg_x, bat_pos_x = bat_x + 44, bat_x + bat_w - 44
text(bat_neg_x, bat_y + bat_h - 6, "-", size=16, weight=700, anchor="middle", fill=C["w48"])
text(bat_pos_x, bat_y + bat_h - 6, "+", size=16, weight=700, anchor="middle", fill=C["w48"])

# --- shunt (on -) / main OCP (on +) ---
shunt_x, ocp_x, sow = inx + 50, inx + 390, 180
block(shunt_x, so_y, sow, so_h, "500 A shunt", C["sheet"], C["cab_s"], size=12,
      sub="on battery (-) / SoC")
block(ocp_x, so_y, sow, so_h, "Main Class-T OCP", C["prot"], C["prot_s"], size=12,
      sub="on battery (+) - TBD")

# --- busbars ---
block(busL_x, bus_y, bus_w, bus_h, "- busbar", C["bus"], C["bus_s"], size=12.5)
block(busR_x, bus_y, bus_w, bus_h, "+ busbar", C["bus"], C["bus_s"], size=12.5)

# --- consumer row (4 boxes off the 48 V bus) ---
block(col_x(0), con_y, bw, con_h, "SmartSolar", C["pv"], C["pv_s"], size=12,
      sub="250/60-Tr (PV in)")
block(col_x(1), con_y, bw, con_h, "Velit branch", C["prot"], C["prot_s"], size=12,
      sub="breaker -> roof AC")
block(col_x(2), con_y, bw, con_h, "Orion-Tr", C["conv"], C["conv_s"], size=12,
      sub="48/24-16A iso.")
block(col_x(3), con_y, bw, con_h, "Orion-Tr IP43", C["conv"], C["conv_s"], size=12,
      sub="48/12-20A iso.")

# --- outputs above the two Orions ---
block(col_x(2), out_y, bw, out_h, "Blue Sea 5026", C["load"], C["load_s"], size=12,
      sub="24 V fuse block")
block(col_x(3), out_y, bw, out_h, "12 V recept.", C["load"], C["load_s"], size=12,
      sub="aux only")

# --- 48 V protection links: battery -> shunt/OCP -> busbars ---
line(bat_neg_x, bat_y, shunt_x + sow/2, so_y + so_h, stroke=C["w48"], sw=2.4)
line(shunt_x + sow/2, so_y, busL_x + bus_w/2, bus_y + bus_h, stroke=C["w48"], sw=2.4)
line(bat_pos_x, bat_y, ocp_x + sow/2, so_y + so_h, stroke=C["w48"], sw=2.4)
line(ocp_x + sow/2, so_y, busR_x + bus_w/2, bus_y + bus_h, stroke=C["w48"], sw=2.4)

# --- 48 V manifold from + busbar up to the four consumers ---
line(col_cx(0), manifold_y, col_cx(3), manifold_y, stroke=C["w48"], sw=2.6)
line(busR_x + bus_w/2, bus_y, busR_x + bus_w/2, manifold_y, stroke=C["w48"], sw=2.6)
for i in range(4):
    line(col_cx(i), manifold_y, col_cx(i), con_y + con_h, stroke=C["w48"], sw=2.2)
text(col_cx(0) - 8, manifold_y - 6, "48 V bus", size=10.5, weight=700,
     anchor="end", fill=C["w48"])

# --- consumer -> output links ---
line(col_cx(2), con_y, col_cx(2), out_y + out_h, stroke=C["w24"], sw=2.2)
line(col_cx(3), con_y, col_cx(3), out_y + out_h, stroke=C["w12"], sw=2.2)
text(col_cx(2) + 6, (con_y + out_y + out_h) / 2, "24 V", size=10, fill=C["w24"])
text(col_cx(3) + 6, (con_y + out_y + out_h) / 2, "12 V", size=10, fill=C["w12"])

# --- PV in (from roof down-lead) into the SmartSolar ---
line(col_cx(0), out_y + 12, col_cx(0), con_y, stroke=C["pv_s"], sw=2.4, dash="6 4")
poly([(col_cx(0) - 5, con_y), (col_cx(0) + 5, con_y), (col_cx(0), con_y + 9)],
     fill=C["pv_s"], stroke="none")
text(col_cx(0), out_y + 6, "roof 3S", size=10.5, weight=700, anchor="middle", fill=C["pv_s"])
# --- Velit branch -> roof AC (up/out) ---
line(col_cx(1), con_y, col_cx(1), out_y + 18, stroke=C["prot_s"], sw=2.2, dash="6 4")
poly([(col_cx(1) - 5, out_y + 18), (col_cx(1) + 5, out_y + 18), (col_cx(1), out_y + 9)],
     fill=C["prot_s"], stroke="none")
text(col_cx(1), out_y + 6, "-> roof AC", size=10, weight=700, anchor="middle", fill=C["prot_s"])

# --- 5026 branch list + cabin-face / vent captions ---
cap_y = bat_y + bat_h + 28
text(inx, cap_y, "Blue Sea 5026 24 V branches: fridge - interior/exterior LED zones - "
     "USB-C PD - GPS - winter heater outlet.", size=10.5, fill=C["slate"])
text(inx, cap_y + 18, "Cabin face: Blue Sea 8260 + 6x 8282 switches + 6x 24 V dimmers "
     "(INTERIOR/CURB/ROAD/NOSE/REAR/AWNING).", size=10.5, fill=C["slate"])
text(inx, cap_y + 36, "Vent: low filtered cabin intake + high fan-assisted exhaust "
     "(24 V fan + thermostat); no exterior penetration.", size=10.5, fill=C["slate"])

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
