---
title: Systems / gear draft — fridge + accessories ordering list
author: operator
kind: handoff
date: 2026-06-03
run_id: run_5b03c224aa588d85eb949f5bd4dee3cc
domain: systems-gear
status: draft-for-cross-examination
---

# Systems / gear — committed recommendations

Scope: the two Systems/gear open questions (context Q17, Q18). One committed
recommendation per question. Grounded in the settled build: 48V LiTime stack
(5kW split-phase AIO + one 48V 100Ah / 5.12 kWh LiFePO4, AIO in the nose
cabinet), off-grid Juplaya (~July 4 2026), single axle, payload weighed not
guessed, interior 81" W × 157" L × 78" (6'6") tall. North star: E-track grid is
the OS, interior is software, reconfigurable across moto/fab/kayak/offroad.

Convention below: **REC** = the committed call. **Why** = one-line rationale.
**Depends on** = the spec/constraint it rides on. **Action** = measure-or-buy
flag.

---

## Q17 — Fridge

**REC: One 12 VDC DC-compressor fridge/freezer, dual-zone, ~50–55 L chest/drawer
form, powered from a dedicated 12V branch off the 48→12 converter. Specific
unit: a Secop/Danfoss-BD35-class compressor box (e.g. Dometic CFX3 55IM or ICECO
VL60 ProD dual-zone). Buy the 12V model, NOT a 24V or 48V variant, and NOT a
Midea AC unit on the inverter.**

- **Why:** A BD35-compressor box pulls ~0.7–1.0 A at 12V running, duty-cycles to
  ~30–45 Ah/day in desert heat, and runs straight from DC — no inverter idle
  tax. A Midea (or any 120VAC mini-fridge) forces the 5kW AIO to stay powered
  for a ~60–100 W load, adding ~25–50 W of pure inverter overhead 24/7
  (~0.6–1.2 kWh/day wasted) and removing the ability to let the inverter sleep
  overnight. Over an off-grid week that overhead alone is a meaningful fraction
  of the 5.12 kWh pack.
- **Why 12V not 48V/24V:** DC-compressor fridges are a mature 12/24V market;
  true 48V-native compressor fridges are rare, expensive, and a sourcing risk
  before July 4. We already need a 48→12 converter for other 12V loads (see the
  power run's Q3), so the fridge becomes just another 12V branch. A 24V tap is
  possible (lighting is 24V) but the fridge market and accessory ecosystem is
  12V; keep the fridge on 12V and keep 24V reserved for lighting.
- **Depends on:** 48V pack 5.12 kWh; a 48→12 converter sized to carry fridge +
  other 12V loads (coordinate with the power-electrical run — fridge is the
  single largest sustained 12V load and should drive the converter's continuous
  rating, budget ~10 A continuous headroom for the fridge branch). Interior 81"
  wide — a 55 L chest fits under a wall-track shelf or against the nose cabinet
  without blocking E-track rows.
- **Action (measure):** Confirm chosen unit's running + startup draw on the
  spec sheet and confirm the 48→12 converter (power run) covers it with margin.
  Confirm physical footprint against the chosen interior layout (systems run
  does not own layout — flag to interior run).
- **Action (buy):** 1× DC-compressor 12V dual-zone fridge/freezer, ~50–55 L.
  Order by mid-June to clear shipping before the July 4 trip.

**Tradeoff conceded up front:** A chest unit means opening from the top; if the
layout wants a front-opening drawer fridge that is fine, same compressor class,
slightly higher draw and price. The DC-vs-Midea call is the load-bearing
decision and it is firmly DC-compressor.

---

## Q18 — Accessories ordering list

**REC: Order the list below as the Juplaya-readiness accessory set. Quantities
and the bus they land on are committed; swap-equivalent brands are noted only
where sourcing risk is real.**

### Security (theft is the real Juplaya/parking-lot risk)
| Qty | Item | Notes / bus |
|---|---|---|
| 1 | **Proven Industries 2516** puck-style coupler lock | Fits the 2" coupler (work order confirms 2" 5,000 lb coupler). Best-in-class against coupler theft. |
| 2 | **Abloy PL340/PL321** (or Paclock 90A-series) puck padlocks, **keyed alike** | One for the ramp door hasp, one for the side personnel door. Keyed-alike so one key runs the trailer. Abloy preferred over Paclock for disc-detainer pick/pull resistance; either acceptable. |
| 1 | **Trimax TCL65** wheel/tire boot | Single axle = one wheel each side; boot the curb-side wheel when parked unattended. Visual deterrent + hard stop. |

### Tracking
| Qty | Item | Notes / bus |
|---|---|---|
| 1 | **LandAirSea 54** GPS tracker, **hardwired to 12V** (not the magnetic battery puck) | Hardwire to a switched-or-constant 12V branch so it never dies; hidden mount. Constant 12V preferred so it reports even with the trailer "off." Sips mA. |

### 12V distribution + outlets
| Qty | Item | Notes / bus |
|---|---|---|
| 1 | **Blue Sea Systems 5026 ST-Blade fuse block, 12 circuits, with negative bus + cover** | The 12V load center. Fed from the 48→12 converter output. Lands: fridge, GPS, dome/task lights, USB-C PD, door switch, awning, spares. |
| 1 | **Blue Sea push-button reset breaker or ANL on the converter feed** | Protect the converter→fuse-block feed (coordinate sizing with power run). |
| 2 | **12V 15A panel-mount sockets** (Blue Sea 1011-class) | One nose, one rear-quarter, for accessory power. |
| 1 | **USB-C PD + USB-A panel charger, 12V input** (Blue Sea 1045-class or equivalent 30W+ PD) | Device charging without spinning up the inverter. |

### Lighting (12V task/dome — distinct from the 24V Yuji strip system)
| Qty | Item | Notes / bus |
|---|---|---|
| 2 | **12V LED dome lights with integrated switch** (e.g. Lumitronics RV puck domes) | Entry/utility lighting independent of the 24V Klus strips. On the 12V fuse block. |
| 1 | **12V LED task/scene light, switched** (e.g. magnetic or rail-mount work light) | Bike loading at the ramp after dark. |

### Notes that pin the list to this build
- The factory unit already ships a **12V dome light, license light, and full LED
  clearance/tail lighting** (work order) — those run off the 7-way tow circuit
  and are NOT in this list; this list is the *house* 12V system only.
- Everything 12V lands on **one Blue Sea fuse block** fed by the single 48→12
  converter — keeps the 12V side to one documented load center, which is what
  the wiring-diagram question (power run Q6) will reference.
- Lighting strips (24V Yuji/Klus) and the Velit AC (48V) are explicitly **not**
  on this 12V list — they are their own buses. This list only covers 12V house
  loads + physical security + tracking.

### Validation of the "no other 12V wiring foreseen" claim (context Q4)
Context Q4 says: other than strip lights (24V), a door switch, and the AC (48V),
no other 12V wiring is foreseen — and asks to validate that. **This list
falsifies that as written:** the fridge (12V), GPS tracker (12V), house dome/
task lights (12V), and 12V/USB-C outlets are all real 12V house loads. So the
12V load list is NOT just "a door switch." The committed 12V load set is:
fridge + GPS + 2 dome + 1 task light + 2 sockets + 1 USB-C panel + door switch
(+ awning controller if the awning is 12V). That is what should size the 48→12
converter. (Hand this to the power run.)

### Action flags
- **Buy now (long-lead / shipping before July 4):** fridge, Proven 2516, Abloy
  pucks keyed-alike, Blue Sea 5026 fuse block, LandAirSea 54. Order by mid-June.
- **Buy local/late OK:** sockets, USB-C panel, dome/task lights, boot.
- **Measure before mounting:** GPS hidden-mount location + 12V tap point; fuse
  block mount location in the nose cabinet near the AIO; dome light positions
  (depends on interior layout — flag to interior run).

---

## Cross-domain handoffs (so the adjudicator can see the seams)
1. **Power-electrical run:** the 48→12 converter must be sized to the 12V house
   load set above (fridge is the dominant sustained draw). The fridge DC-vs-AC
   call here assumes a 48→12 converter exists; if power run kills the converter,
   re-open this.
2. **Interior run:** fridge footprint and dome/task light positions depend on
   the E-track layout; this draft commits the *what*, not the *where*.

## Open weakness I expect to be cross-examined on
- Exact fridge model/draw is committed to a *class* (BD35 12V dual-zone), not a
  single SKU, pending spec-sheet confirmation of draw vs converter rating.
- Whether the trip even needs a 12V converter at all is a power-run dependency;
  if 12V is killed, the fridge could be re-specced 24V — but the market makes
  that worse, not better.
