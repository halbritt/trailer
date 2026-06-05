---
author: operator
---

# D002 Adversarial Review — Solar / Roof-Geometry Posture

**Charge:** attack D002 from the roof-geometry and PV-string angle. Decide whether
three roof panels and 3S support are real enough to change the inverter/charger choice.

**Finding up front:** they are not. The third roof panel fails *two independent gates*
— it doesn't fit the measured rectangle, and even if it did, a 3S string is electrically
homeless on every AIO offered. The honest steelman for switching inverters collapses on
the evidence, so this posture's attack on D002 fails. Keep the LiTime 3500 W.

---

## 1. The string-voltage map is the whole argument

LG455N2W-E6, load-bearing figures (LG web page, repo datasheet): Vmpp **42.1 V** STC /
**39.60 V** NMOT; Voc **49.9 V** (±5%), coeff **−0.26 %/°C**; Impp 10.83 A; max series fuse 20 A.

| String | Vmpp STC | Vmpp NMOT | Vmpp hot-roof¹ | Voc STC | Voc −10 °C² | Where it lives |
|---|---:|---:|---:|---:|---:|---|
| **1S** | 42.1 | 39.6 | ~36 | 49.9 | 54.4 | Below every 48 V MPPT floor — **cannot charge.** |
| **2S** | 84.2 | 79.2 | ~71 | 99.8 | **108.9** | Mid-window on the **3500 W (60–145 V)**. Invisible to any 120 V-min AIO. |
| **3S** | 126.3 | **118.8** | **~108–115** | **149.7** | **163** | Over the 3500 W's 145 V ceiling; under the 120 V-min floor when hot. **Homeless.** |
| **2S2P** | 84.2 | 79.2 | ~71 | 99.8 | 108.9 | Camped 4-panel config; 21.7 A Impp, far inside the 50 A / 4400 W input. |

¹ Hot-roof Vmpp extrapolated past NMOT (~−0.35 %/°C on V): a black playa roof at 60–70 °C
cell temp pulls 3S to ~108–115 V. ² Voc cold = STC × (1 + 0.0026·ΔT); matches the brief's
~109 V (2S) / ~163 V (3S).

**Two facts fall straight out of this table and decide everything:**

- **3S over-volts the 3500 W before any cold correction.** 3 × 49.9 = 149.7 V > 145 V hard
  max at STC; 163 V at −10 °C, 169 V at −25 °C. Owners further report this unit
  *nuisance-faulting on PV overvoltage below its rated 145 V* with 49 V-class panels — the
  exact LG class ([web-val](../../../docs/research/build-decision-validation.md)). 3S is dead
  on the chosen AIO, twice over.
- **The roof's only safe string (2S, 71–84 V Vmpp) is below the 120 V floor of every
  high-voltage AIO.** That is the trap the 3-panel idea walks into: you cannot keep 2S *and*
  buy a 120 V-min inverter. The high-voltage box would **force** you onto 3S — and 3S NMOT
  Vmpp is already 118.8 V (< 120 V floor at a mild 42 °C module temp), dropping to ~108–115 V
  on a hot roof. The MPPT starves precisely when July sun is strongest. A 120 V-min AIO is not
  a "3S enabler"; it is a downgrade that breaks the string the roof actually carries.

---

## 2. The roof can't carry a third panel anyway (measured geometry)

Roof rectangle **MEASURED 84-7/8" × 145.5"** (2026-06-04) + nose trapezoid. Panels mount
landscape: 83.07" across the width (~0.9"/side margin → under-panel feet), each row eats
**41.02"** of length.

| Layout | Length used | Rectangle left | Verdict |
|---|---:|---:|---|
| 2 rows (D002) | 82.0" | ~63.5" + nose | Velit station competes for it; **roof drawing not yet done.** |
| 3 rows | 123.1" | **~22.4"** + nose | Less than the **Velit body (~26")**; AC must vacate the rectangle. |

The Velit 2000R Mini exterior unit is **~26.4" × 26" × 6.5"** with a ~14-1/4" roof opening
*plus* edge/obstruction clearance. Three rows leave 22.4" — the AC body doesn't fit the
remnant. Survival depends on relocating a 26"-square unit entirely onto the **tapering V-nose**
(roof nose ~18–24" long, narrowing to a flat tip) while sharing it with awning riser stations
and walk space. That is unproven on paper — **design-freeze item 5 (the roof drawing) has not
placed the Velit even for the two-panel case.** You cannot freeze an inverter purchase on a
third panel whose home is a rectangle remnant smaller than the appliance it must dodge.

Secondary geometry cost: a third roof panel is **+48.5 lb mounted high and forward** on a
single-axle, nose-sensitive trailer with a payload that will be **weighed, not estimated**.
That is real tongue-weight spend for a panel that — see §1 — produces nothing roof-only on the
chosen AIO.

---

## 3. Does a third panel actually raise roof-only harvest? No — not on any AIO.

The owner's real motive is harvest: roof-only 910 W makes ~4.0 kWh/day in July vs a
4.1–4.45 kWh budget — break-even on AC-heavy days. But a third panel **adds zero roof-only
harvest through any AIO**, because the only way to wire 3 panels is 3S (1S can't charge; 2S+1S
is invalid), and 3S is homeless (§1). The third panel produces only through a *separate*
wide-window MPPT — which is an add-on to the AIO, never a reason to change the inverter.

D002 already answers the harvest gap correctly: the **deployable ground 2S pair → 2S2P
(1820 W)** is the designed camped margin. Chasing +455 W of *roof-only* harvest costs roof
geometry, tongue weight, a second charge controller, PV disconnect/OCP, and roof-drawing risk —
to partially duplicate margin the ground pair already supplies, against a July deadline.

---

## 4. Candidate scoring (solar-relevant axes)

Scored on this posture's two decisive axes. Non-solar axes (idle, AC fit, battery comms,
wiring, heat, vendor, cost, timing) belong to the integration and budget reviewers; one-line
notes only.

| Candidate | Roof-only harvest if 3 panels "fit" | PV safety & hot-roof MPPT-floor margin | Solar verdict |
|---|---|---|---|
| **LiTime 3500 W (D002)** | 910 W (2S) firm; 3S over-volts so no roof-only gain from a 3rd panel | **Best fit:** 2S/2S2P sit mid-window (60–145 V op, 60–115 V rec); never 3S | **Correct.** Only window that matches the string the roof carries. |
| LiTime 5 kW (returned) | Needs 3S to do *anything* (2S 71–84 V < 120 V floor); 3S starves hot | **Bad:** can't track 2S at all; forces marginal 3S; +idle on a break-even budget | Return stands. Wrong window for this roof. |
| EG4 3000EHV-48 | Same — 120 V floor can't see 2S; 3S only, starves hot | **Bad:** identical floor problem; better ecosystem doesn't fix physics | Reject on solar. |
| Growatt/MPP/Sungold 5–6 kW HV | Same 120 V-min floor trap | **Bad:** spec-sheet 3S, hot-roof dropout in practice | Reject on solar. |
| Victron MultiPlus-II + SmartSolar 250/60 | True 3S harvest (250 V max, low start threshold) **if a 3rd panel fits** | **Best electrically:** real wide-window MPPT, tracks 2S and 3S | Solar-clean, but the geometry gate (§2) still gates the 3rd panel; not an AIO. |
| **LiTime 3500 W + separate SmartSolar 250-class MPPT** | 2S2P on AIO + 3S roof on external MPPT — the *only* way a 3rd panel produces | **Best hybrid:** keeps the correct AIO window, adds a 3S-safe controller | The right escape hatch **only if** the roof drawing proves 3 rows + Velit. |

---

## Required outputs

**1. Recommended architecture and exact next purchase.**
Keep D002's power core unchanged. **Buy the LiTime 48 V 3500 W AIO** ($629.99, LiTime) for the
2S roof / 2S2P-camped architecture. Do **not** let the 3-panel idea pull the purchase toward a
120 V-min high-voltage AIO — that would force a 3S string the roof can't fit and the hot MPPT
floor can't track. From the solar angle the AIO choice is independent of the 3-panel question.

**2. Should the mistaken 5 kW LiTime still be returned?**
**Yes — return it.** On solar grounds alone: its 120–500 V window cannot track the 2S string
(71–84 V Vmpp) the roof actually carries, so it *forces* 3S, which over-volts cold and starves
on the hot floor — plus a heavier idle tax against a break-even budget. Wrong inverter for this
roof regardless of the order mistake.

**3. Should 3 roof panels change the inverter decision?**
**No.** The third panel fails geometry (3 rows leave 22.4" < the 26" Velit body; roof drawing
unfinished; +48.5 lb forward on a nose-sensitive axle) *and* electrics (3S is over the 145 V
ceiling on the 3500 W and under the 120 V floor on every HV AIO when hot). The only device that
harvests a third panel is a *separate* 250 V-class MPPT — an add-on, not an inverter swap.
The inverter decision stands on the 2S/2S2P architecture that is physically real.

**4. Strongest counterargument to this recommendation.**
The most honest attack on my own call: roof-only is *break-even*, and a third roof panel would
let the owner hit the budget without the ritual of deploying and guying the ground pair every
camp — a real ergonomic win at a windy playa. If the measured roof drawing genuinely places the
Velit on the nose, three rows *might* fit, and a Victron SmartSolar 250/60 cleanly harvests a
3S roof string (~1365 W roof-only) while preserving the 3500 W AIO and the 24 V bus. So the
*hybrid* (AIO + external MPPT) is defensible. **Why it still loses now:** it spends a second
controller, PV disconnect/OCP, charge coordination, tongue weight, and roof-drawing risk before
the geometry is even proven, to chase margin the ground pair already supplies — all against the
July deadline. It is a *post-measurement option*, not a reason to change today's buy.

**5. Required gates / install notes.**
- **NEVER 3S** on any AIO. 3S = 149.7 V STC (> 145 V) and ~163 V cold on the 3500 W; ~108–119 V
  Vmpp (< 120 V floor) on HV units when hot. Treat the 2S ~109 V cold-Voc headroom as
  load-bearing, not unlimited (the unit nuisance-faults below 145 V).
- **Binding cold limit is the AIO's −10 °C operating floor, not PV Voc** — keep the unit in the
  conditioned nose cabinet.
- **Gate any third-panel/external-MPPT decision behind design-freeze item 5 (the roof drawing):**
  it must place all panel rows *and* the Velit station *and* awning risers on the measured
  84-7/8" × 145.5" field, and the weigh-in (row 18) must absorb +48.5 lb forward, *before* a
  third panel or a SmartSolar is bought. Until then the AIO purchase proceeds on 2S/2S2P.
- Ground 2S2P: keep both deployed strings at the **same tilt/orientation** (single MPP);
  per-string fusing not required at 2 strings (Isc ~11.4 A < 20 A), but mandatory if a further
  parallel string is ever added.
- Reconcile the minor datasheet delta when convenient (LG web: Voc 49.9 V / −0.26 %/°C / Vmpp
  42.1 V vs an older PDF's 41.7 V / −0.24 %/°C); the web figures used here are the conservative,
  load-bearing ones and do not change any verdict.

**6. One-line verdict for D002.**
**KEEP** — buy the LiTime 48 V 3500 W AIO; the third roof panel is geometrically marginal and
electrically homeless on every AIO, so it does not change the inverter choice; allow a *future*
separate 250 V-class MPPT only if the measured roof drawing later proves three rows plus the Velit.
