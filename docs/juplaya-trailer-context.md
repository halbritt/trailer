# Juplaya Trailer Build — Context & Open Questions
*Consolidated for handoff. Target: ready for Juplaya (~July 4, 2026).*

> This doc was reframed from an auto-generated draft that over-stated what was decided. Treat everything under **Open questions** as unresolved — they are the inputs for a striatum workflow. Only **Settled** items are firm. Do not infer decisions that aren't written here.

---

## Settled

### Trailer
- **FasTrac Deluxe FT712S2-D, 7×12, single axle** (ACG-built), **Silverfrost** exterior. Bought at The Trailer Specialist, Acampo CA. **VIN 7V0W11214TU444163**, serial 444163.
- **Interior 6'9" (81") W × 13'1" (157") L × 6'6" tall**; overall ~16'0". Rear **5,000 lb ramp door**; side **32"×72" personnel door, RH** ("RV-style"). **2"×4" tube main rails**; 4× factory 5,000 lb D-rings; 3/4" PlexCore floor.
- Full specs: [fastrac-specs.md](fastrac-specs.md) · factory build sheet: [work order](wells-cargo-ft712s2-d-work-order.md).

### Tow vehicle
- **2021 Ford F-150 EcoBoost, Max Tow package.** Has **Pro Trailer Backup Assist** (relevant to maneuvering/parking). Ordered: **integrated trailer backup camera + TPMS** (both integrate with the truck).

### Power system (48V — current/up to date)
- DIY 48V LiTime stack (F3800 is out):
  - **AIO: LiTime 48V 3500W (5 kW returned) — sheet verified** ([specs](litime-48v-3500w-aio-specs.md) · [manual](litime-48v-3500w-inverter-charger-manual.md)): PV **60–145 V op / 60–115 V rec / 4400 W / 50 A**; **no-load <50 W (<30 W ECO)**; AC 3500 W, surge 6000 W/5 s; ~75 A max battery draw (headroom under the pack's 100 A); 23 lb, 426×336×124 mm. **Commissioning: cap total charge ≤100 A** (unit does 120 A PV+AC; battery accepts 100 A). ECO/off when idle; ventilate the nose cabinet (131 °F ceiling). 5 kW docs kept for reference.
  - **LiTime 48V 100Ah Smart ComFlex** (LiFePO4) — 5.12 kWh, ~100 lb; mount low and centered ([specs](litime-48v-100ah-battery-specs.md)).
  - **LiTime 500A Bluetooth shunt**; **ANL 250A fuses**.
- The **AIO lives in the nose, in a cabinet**; anything that needs plugging in plugs in there.

### Envelope & cooling
- **Closed-cell spray foam** insulation — given.
- **Elastomeric roof coating** — given.
- **Velit Mini 2000R AC — ordered (48 VDC unit).** (No longer deferred.)

### Use case & on-hand
- Hauls two bikes — **WR250R + CRF450RL, ~590 lb** combined — convertible "bikes-out → sleeping deck."
- **~(6) 10 ft black powder-coated E-track sections** — believed ordered (confirm).

---

## Recommendations (from the cross-examined workflow runs)

Resolved 2026-06-03 by four striatum `cross_examination` runs (claude author + agy red-team). Full drafts, cross-exams, and the climate ledger/proposal are in `runs/<domain>/`. These are recommendations to ratify; genuinely-open items are under "Still open" below.

### Power / electrical
1. **Solar — RESOLVED by the 3500W-AIO swap: 2 × LG455N2W-E6 in 2S (910 W).** The 3500W AIO's PV window is **60–145 V** and 2S sits mid-window in every condition: Vmpp 84.2 V STC / 79.2 V NMOT / ~71 V desert-hot (≫ the 60 V floor); Voc 99.8 V STC, ≤ ~117 V even at −40 °C (< 145 V). The 5 kW unit's 120 V floor was unmeetable by any roof-fitting string (datasheet NMOT row: 3S = 118.8 V at 20 °C ambient). **Never wire 3S into this unit** — cold-morning Voc ≈ 157–163 V (Voc ±5%, cold) overshoots the 145 V PV max, and 3P (~42 V) is under the 60 V floor; a 3rd roof panel runs on **its own small MPPT** to the battery. 2 panels fit the roof easily (~97 lb vs 145). No external MPPT. Mounting unchanged: rails through the steel roof bows ([datasheet](lg455n2w-e6-datasheet.md)). *Expansion plan: a **ground-mounted 2S pair paralleled in → 2S2P, 1820 W** when camped. Voltage unchanged (still mid-window); current doubles to ~21.7 A Impp / ~22.8 A Isc — **gate closed: the 3500W takes 50 A / 4400 W of PV**, so 2S2P is comfortably in-spec (even a third pair would fit electrically). Hardware: MC4 Y-branch or mini-combiner, per-string inline protection (≤20 A), PV disconnect, weatherproof inlet, 10 AWG extension. Juplaya wind: guy/anchor the ground pair. Transport: panels are 83" vs the 81" interior width → they ride lengthwise; give them a padded E-track wall slot (feeds #12).*
2. **Solar mounting** — aluminum rails on tilt/Z-brackets **bolted through into the 24"-OC steel roof bows**, butyl + Dicor sealed. **The side-of-top-rail cantilever idea was rejected** (peel/tip load at tow speed).
3. **48V→12V converter** — ~25 A / 300 W isolated into a fused 12V block. *(May be deletable — see Still open.)*
4. **12V loads** — a real 12V house rail (~10–15 A typ): running/marker/tail, dome/task, vent fan, sockets/USB-C, GPS, door switch, awning. The earlier "only strips + door + AC" assumption was **false**.
5. **Lighting** — Yuji 24V strips on a dedicated **48V→24V DC-DC (~250 W)** + fused 24V bus, Klus extrusions/diffusers, zoned/dimmed; exterior/awning on 12V.
6. **Wiring** — three-rail bus (48V AC+charging / 24V lighting / 12V accessories), single-point ground at the shunt, per-converter fusing on the 48V bus, ENT + pull strings; gauges deferred to measured runs.
7. **Truck charging** — **defer the charger for Juplaya** (1365 W solar recharges 5.12 kWh in < 4 h) but **pre-wire 4 AWG + an Anderson tongue connector now**. Charger when added: ~480–600 W 12→48V DC-DC, ignition-gated.

### Climate / envelope  *(run completed; verdict: accept-with-findings)*
8. **Windows** — **one** framed curbside awning window sized to the **measured** clear opening (≤ ~26" RO), spanning two 16"-OC bays with a load-transfer sub-frame; fallback = no glass + a powered roof-vent fan. (agy falsified "two ~22" windows" — bays leave ~15" clear.)
9. **HRV** — defer the core; **rough-in the paired 4" wall penetrations + power string now**.
10. **Diesel heater** — **no heater for July**; rough-in through-floor exhaust/fuel penetrations + a hardwired-12V CO-detector string now, defer the unit to cold-weather profiles. (agy killed "install now": mild July nights vs under-floor-exhaust fire over dry scrub + nose-heavy fuel.)
11. **Awning** — **~12 ft manual lateral-arm RV awning, curbside, through-bolted to the aluminum top rail** (never the skin), desert tie-downs. The July deliverable.

### Interior / layout
12. **E-track floor** — bikes **side-by-side, both nose-forward**, flush-recessed, bolted through to steel; reuse the 4 factory D-rings. **⚠ NEEDS REWORK (agy):** the planned ~24" centerline spacing causes ~9" **handlebar interference** (32–34" bars need ~33" clear), and the **2"×4" main rails run at the perimeter, not ±12" off centerline** — centerline rows miss the steel, and a 1/2" recess leaves only ~1/4" ply between crossmembers. Re-derive spacing/position against the *actual* steel locations + measured bar width.
13. **Track heights** — **bed row ~34", shelf row ~60"**, both backed onto the 16"-OC vertical posts.
14. **Bed shoring** — **E-track sockets that accept 2×4 lumber** (not fixed aluminum) — reconfigurable, cheap/replaceable.
15. **Walls** — keep the factory liner; **FRP textured panel over it, no paint**; 1/4" XPS thermal break **only behind the bed zone**; FRP trim; backing in before finish.
16. **Door stairs** — a **folding/telescoping aluminum RV step that stows on the E-track grid** (not welded, not door-hung).
- **E-track footage** likely **short — ~73 ft needed vs ~60 on hand**; order more.

### Systems / gear
17. **Fridge** — a **12 VDC compressor fridge/freezer, ~50–55 L** (Dometic CFX3 55IM / ICECO VL60 ProD) — explicitly **not** a Midea on the inverter (avoids ~25–50 W of 24/7 inverter idle tax). *(BD35 units are 12/24V auto-sensing — see Still open.)*
18. **Accessories order** — Proven 2516 coupler lock; 2× Abloy/Paclock puck locks **keyed-alike**; Trimax TCL65 boot; LandAirSea 54 (hardwired 12V); Blue Sea 5026 12-circuit fuse block; 2× 12V sockets; 1× USB-C PD panel; 2× dome + 1× task light.

### Still open / to coordinate
- **Solar / MPPT floor — RESOLVED:** swap to the **3500W AIO (PV 60–145 V)** + **2 × LG455 in 2S** (see #1). **Verified against the 3500W sheet**: PV 60–145 V op (60–115 V rec) / 4400 W / 50 A → 2S and 2S2P both in-spec; idle <50/<30 W ECO. Only commissioning item: **cap total charge ≤100 A** for the battery. Harvest: roof 910 W rolling → 1820 W camped.
- **48V→12V converter vs the 24V bus** — both the power and systems red-teams noted the fridge + most 12V loads (12/24V auto-sensing) could run off the existing 24V lighting bus, **deleting the 48→12V converter**. Resolve #3 against this.
- **Top-rail contention** — the awning (#11) and the solar mounts (#2) both want the aluminum top rail. Coordinate placement.
- **Interior floor plan (#12)** — blocked on the steel-location + handlebar rework above; needs the tape-measure pass.
- **Measurements** — window RO, front-tire centerlines, and the to-be-weighed curb/payload still gate the above (the mm-measurement pass).
---

## Weight
- **GVWR 3,500 lb** (confirmed). Real payload = 3,500 − actual curb; **will be weighed**, not estimated. Single axle is nose-sensitive — aim ~**10–12% tongue weight** when positioning the bikes.

---

## Standing preferences (for whoever picks this up)
- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
