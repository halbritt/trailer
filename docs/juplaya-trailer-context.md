# Juplaya Trailer — Build Sheet
*Target: ready for Juplaya (~July 4, 2026).*

> **Settled** items are firm. **Decisions** are DECISION_LOG rows (`proposed` until the owner ratifies). **Gates** are pass/fail checks that must pass before drilling, fabricating, or ordering. Provenance: D002–D008 come from the cross-examined striatum runs (artifacts under `runs/`); don't infer decisions that aren't written here or in a D-row.
>
> **Web-validation (2026-06-05):** all 7 falsifiable decisions were fact-checked against public sources — [docs/research/build-decision-validation.md](research/build-decision-validation.md) (`[web-val]` below). It flipped 4/7 to caution; the material deltas are folded into the gates here.

---

## Trailer (settled)
- **FasTrac Deluxe FT712S2-D, 7×12, single axle** (ACG-built), **Silverfrost** exterior. The Trailer Specialist, Acampo CA. **VIN 7V0W11214TU444163**, serial 444163.
- **Interior 81" W × 157" L × 78" H**; overall ~16'0". Rear **5,000 lb ramp door**; side **32"×72" personnel door, RH**. **2"×4" tube main rails**; 76½" steel tube posts 16" OC; 4× factory 5,000 lb D-rings; ¾" PlexCore floor.
- Specs: [reference/fastrac-specs.md](reference/fastrac-specs.md) · [factory work order](reference/wells-cargo-ft712s2-d-work-order.md) · **[dimension sheet](dimensions.md)** (incl. the mm measurement-pass table) · vision: [trailer-mission.md](trailer-mission.md).

## Tow vehicle (settled)
- **2021 Ford F-150 EcoBoost, Max Tow.** Pro Trailer Backup Assist; integrated trailer backup camera + TPMS ordered.

---

## Power / electrical

### 48 V stack (settled)
- **AIO: LiTime 48V 3500W** (5 kW returned) — PV 60–145 V op / 60–115 V rec / 4400 W / 50 A; no-load <50 W (<30 W ECO); AC 3500 W, surge 6000 W/5 s; ~75 A max battery draw. **Commissioning: cap total charge ≤100 A.** ECO/off when idle. **Cold floor: AIO rated to −10 °C — that, not PV Voc, is the binding cold limit; keep it in the conditioned nose cabinet `[web-val]`.** ([specs](reference/litime-48v-3500w-aio-specs.md) · [manual](manuals/litime-48v-3500w-inverter-charger-manual.md))
- **Battery: LiTime 48V 100Ah Smart ComFlex** — 5.12 kWh, ~97 lb, 100 A continuous; mount low/centered. ([specs](reference/litime-48v-100ah-battery-specs.md))
- **LiTime 500A Bluetooth shunt; ANL 250A fuses.** AIO + electronics live in the **nose cabinet — ventilate it** (131 °F ceiling + converter waste heat).

### Solar (resolved)
- **Roof: 2 × LG455N2W-E6 in 2S (910 W)** — mid-window at all temps (Vmpp 84/79/~71 V; Voc ≤ ~117 V cold). **Never 3S** (cold Voc 157–163 V > 145 V max); a 3rd panel would need its own MPPT. ([datasheet](reference/lg455n2w-e6-datasheet.md))
  - **`[web-val]`:** owners report this LiTime AIO nuisance-faults on PV overvoltage *below* its rated 145 V with 49 V-class panels — 2S (~113 V cold, re-derived) clears it, so treat the headroom as real and **reinforce never-3S**. Reconcile LG's page (Voc 49.9 V, −0.26 %/°C, Vmpp 42.1 V) against the −0.24 %/°C / 41.7 V in the spec sheet.
- **Camped: ground 2S pair parallels in → 2S2P (1820 W)** — ~21.7 A Impp, in-spec vs 50 A/4400 W. Hardware: MC4 Y-branch/mini-combiner, per-string protection ≤20 A, PV disconnect, weatherproof inlet, 10 AWG extension. Guy/anchor the ground pair (playa wind).
- **Mounting:** rails on tilt/Z-brackets through the 24"-OC steel roof bows, butyl + Dicor. **Roof fit — MEASURED ✓ (2026-06-04):** width **84-7/8" rail-edge to rail-edge, minimal crown — the landscape pair fits** (~0.9"/side margin → under-panel feet/rails, not side clamps); rectangle length **145.5"** → the two rows take 82", leaving **~63" + the nose**. Remaining for the **roof drawing**: bow stations, the **Velit 2000R AC + its roof opening** (still unplaced), awning standoff stations, panel feet layout.

### 24 V house bus — D006
- **One Victron Orion-Tr 48/24-16A isolated** (nose cabinet, **remote on/off to a cabin toggle**). **48→12 V converter deleted; no 12 V house rail.**
- **Conditions:** 16 A is sized for current loads (~12–15 A realistic worst case). The named winter heater (**LF Bros N4 24 V** — glow draw unpublished, est. ~4–11 A for 2–3 min) **reopens converter sizing** if measured glow stacks past 16 A with fridge + lights; cheap out is glow-window load-shedding. Cabinet venting must cover converter waste heat.
- **48 V-side protection:** Blue Sea 7443 20 A UL-489 (80 V-class) ahead of the converter — **no 32 V automotive fuse gear on the 48 V side**. Required outputs: feed-conductor ampacity, converter output OCP, breaker interrupt-rating sanity, dedicated fuse/breaker on the Velit 48 V branch.
  - **`[web-val]`:** UL-489 / 80 VDC / 10 kA AIC confirmed (clears ABYC's 5 kA-per-100 Ah by 2×). Two follow-ups: **make the battery-terminal main OCP explicit** (Class-T at the battery per standard LiFePO4 practice, *or* document the close-mounted 7443 as the main OCP); **verify the exact Blue Sea SKU** — "7443" in these docs vs the 20 A / 80 V UL-489 part that surfaced as 7463 (7465 = 30 A). Each 24→12 V POL buck also needs its own DC-rated input OCP (not 32 V automotive) on the ~29 V rail.
- **24 V block: Blue Sea 5026.** Rail map: fridge 10 A/14 AWG · Yuji strip zones 5 A (Klus, dimmed) · Scanstrut SC-USB-F3 PD 7.5 A (24 V in → 60 W profiles) · LandAirSea GPS 3 A · door switch (dry contact) · **heater branch (winter): 15 A / 12 AWG to an exterior-reachable outlet — N4 glow est. 4–11 A / run ~1–2 A** · stray 12 V-only fixtures via POL 24→12 bucks.
- **Converter stack check (heater in the calc):** fridge 4.6 + lights ~2–3 + N4 glow up to ~11 ≈ **18–19 A worst case vs the Orion-Tr's 16 A** — winter operation requires **glow-window load-shedding** (lights off for the 2–3 min glow) or the parallel-second-Orion path. Bench measurement of actual glow decides which; July is unaffected.
- **Tow-vehicle 12 V (7-way: running/marker/brake) is never a house load.** Single-point ground at the shunt.

### Truck charging
- **Deferred**; **pre-wire 4 AWG + Anderson tongue connector now.** Future charger: ~480–600 W 12→48 V DC-DC, ignition-gated.

### Energy budget (July, camped)
- Fridge 1.0–1.3 + AIO ECO idle ~0.7 + Velit duty ~2.4 ≈ **4.1–4.45 kWh/day** vs roof-only ~4.0 → **the ground pair is required margin on AC-heavy days**; ECO/off discipline stands.

---

## Climate / envelope

### Settled
- **Closed-cell spray foam**; **elastomeric roof coating**; **Velit Mini 2000R AC (48 VDC) — ordered** (own fused 48 V branch).
- **Roof sandwich `[web-val]`:** building science *endorses* foam-inside + coating-outside on steel **provided the steel is dry/clean/rust-free at closure** (the one condition the endorsement rests on) and the foam is air-sealed at every bow/fastener/penetration. **Spec a cold-rated/silicone coating — standard summer-cure acrylics go brittle and "zipper" off in deep cold.** Run a 48-hr adhesion patch on the actual galvanized/aluminized skin; confirm foaming under the roof doesn't void any panel warranty; schedule periodic exterior blister inspections (hidden-steel corrosion is otherwise invisible).

### Windows — placement decided
- **2 × RecPro 12"×22" frameless (RP-FRMWIN-1222-TRM, portrait), directly opposite each other in the REAR (bed) zone — roadside + curbside, same bay station, sills ~36".** The 12" cutout fits inside one 16"-OC bay (~14.5" clear) — no post cut, no sub-frame. The 36–58" window band sits **between the bed track (~27") and shelf track (60")**; cross-breeze over the bed; roadside-rear is behind the bikes' handlebar sweep (bars live in the front half, nose-forward); curbside-rear clears the 18.6" fridge and the roofline-mounted awning case.
- **Door: RecPro 20"×15" frameless (RP-FRMWIN-2015-TRM) in the 32"×72" personnel door** — forward-zone light, see-out at the entry, third vent point for front-to-back flow.
- **Gates before cutting:** clear bay width at both chosen stations + RecPro cutout/RO spec; frameless clamp-ring range vs the wall build-up (liner + FRP); door-window RO vs the door's internal frame; keep the curbside bay clear of awning-riser backing-plate spans.
- **`[web-val]` — clamp ring is a single 1.5" spec, not a range.** RecPro publishes the trim ring only as "for 1-1/2" wall thickness" (no min/max). The built-up wall is ~1"–1.4", so **it won't clamp tight as specified → fur the opening up to 1.5"** (that step is currently missing from the wall sandwich). **Cutouts confirmed:** 1222-TRM → **11-5/8" × 21-5/8"**; 2015-TRM → **19-5/8" × 14-5/8"** (dim rows 13). The 20×15 cut in the ~20-ga steel door **removes a structural panel → add perimeter re-framing.** Isolate galvanic contact (aluminum frame/screws vs steel skin) with butyl + stainless/nylon.

### HRV / diesel heater (deferred, rough-in now)
- HRV: rough-in paired 4" wall penetrations + power string.
- **Heater identified: LF Bros N4, 24 V variant — operates OUTSIDE the space** ([specs](reference/lf-bros-n4-specs.md)): 5 kW all-in-one pedestal, integrated 3.5 L tank, 17"×13"×14.8", 15.9 lb, −40 °F rated. **No heater aboard for July** (D003). Combustion/tank/exhaust never enter the envelope — **fuel rough-in and exhaust gland both deleted**. Rough-in: **2 × 3" duct ports** (supply + return, capped/plugged until winter — place low, clear of the bed zone and fridge bay), a **24 V feed reachable at the heater's exterior station**, CO detector (cheap insurance on the supply duct). Inside E-track spot = transport/storage only. **On the rail map for the power calc now** — glow unpublished (est. 4–11 A @ 24 V, 2–3 min), run ~1–2 A; bench-measure on arrival.

### Awning — D007
- **Fiamma F45s 350** (06280B01R; 11'6" case, ~55 lb) on **owner-fabricated standoffs at the perimeter aluminum top rail**, **case at/above the roofline (~78.5")** — wall-mount dead **by tape (2026-06-04)**: 5-1/8" measured drip-rail-top → trailer-top-edge vs the 5.35" case (0.225" short; fabric would also foul the swing). Flat-roof mount dead (panels own the roof width).
- **Stations & load path:** the rail's existing bolts mark the uprights — **but they sit at the center of the extrusion**, and a single centered bolt can't react the standoff's prying moment. **Each standoff base runs down the wall face and takes ≥2 fasteners into its steel tube upright** (vertical couple — maximize the spread), picking up the rail bolt as a bonus, not the load path. Fasten into the tube by drill-and-tap or through-bolt **while the interior is open — before FRP**; butyl-seal every skin penetration. Design for deployed wind + tie-down + travel vibration.
- **Required outputs before fab:** standoff count/stations along the 138" case (F45s wants 3–4 brackets → pick uprights that bracket the span + mid-span); fastener size/grade + **post tube wall thickness** (tap vs through-bolt); couple-arm spacing; documented load case.
- **Gates:** rail-section 3D scan (dimension row 16); the shared measured roof drawing; **deployed-fabric vs open-door at actual pitch** (paper margin ~0.9"). **Fallback:** freestanding shade (Moonshade-class).
- **Discipline `[web-val]`:** Tie Down S (98655-133) + 3/8"×12" lags / deadman bags; legs to ground. **Retract threshold depends on deployment mode: wall-only (load through fasteners, no legs/tie-down) → wind in by ~10 mph; legs staked + tie-down → ~20–25 mph.** The old flat ">20 mph" rule assumed legs+tie-down and is ~2× too loose for the wall-only case. Note the limiting failure is the **awning's own arms/extrusions bending, not fastener pull-out** — and an over-rigid standoff can defeat the arms' intended wind/water release, so don't over-constrain. Always wound in before sleep, departure, or gusts.

---

## Interior / layout

### Bikes & floor E-track
- **WR250R + CRF450RL (~590 lb), side-by-side nose-forward (roadside), staggered chocks 12–18"**; flush-recessed E-track bolted through to steel; reuse the 4 factory D-rings.
- **⚠ Floor plan rework gate:** ~24" centerline spacing fails (~9" handlebar interference; the 2×4 rails run at the **perimeter**, and a ½" recess leaves ~¼" ply between crossmembers). Re-derive against measured steel locations + bar width. **Aisle reality:** nominal ~30" shrinks to **~20" effective** at bar height — plan fridge access/egress accordingly.
- **E-track footage short: ~73 ft needed vs ~60 on hand — order more.** (~(6) 10 ft black sections believed ordered; confirm.)

### Fridge bay
- **Curbside, immediately aft of the personnel door**, E-track strapped. 37.9"×20.9"×18.6" + **lid-swing clearance (verify hinge orientation)**.
- **⚠ Thermal gate — HARDENED `[web-val]`:** the Dometic CFX3 manual requires a **50 mm (~2") gap on all four sides** and states **"do not place the cooling device in closed compartments."** An *enclosed* bay is non-compliant as worded → **the bay must give 50 mm all-sides clearance + forced through-flow ventilation**, not just "shaded." Then field-measure in-bay air under desert sun with the awning out: **<43 °C (110 °F) to run at all; <30 °C (86 °F) to hold both dual-zone setpoints.** Keep it off the nose-cabinet heat plume. (Warning 34 = high ambient / blocked vent; Warning 33 = low incoming voltage — see D008 below for the wiring check.)

### Wall tracks, bed, walls, stairs
- **Bed row ~27" (revised from 34" — owner challenge upheld), shelf row ~60"**, backed onto the 16"-OC tube posts. At 34" the sleeping surface (~38.5") left only ~1–3" of seated headroom for a 6'+ adult; at 27" (surface ~31") it's ~46". Bikes-out means nothing needs the taller under-deck. **Gate: mock a 31" surface and sit-test before drilling.** **Bed shoring: E-track sockets taking 2×4 lumber.**
- **Walls — D009 (proposed): pull the factory OSB during the foam job and re-skin in 3/8" birch ply, FRP textured panel over the birch, no paint.** 3/8 matches the factory thickness — wall sandwich geometry (window clamp range, door reveals) unchanged; birch holds fasteners and FRP adhesive far better than OSB; walls are already open for the spray foam, so the swap is nearly free labor. **Skip 1/4"** (flex between the 16"-OC posts, thins the window clamp sandwich); the on-hand **1/2" sheet goes to interior fixtures** (fridge-bay partition, shelving), not walls. ¼" XPS behind the bed zone only; backing in before finish. **Gates: verify factory OSB is actually 3/8" (dimension row 19); D009 must be ratified before the window RO cuts (row 12 feeds the clamp-range check); FRP trim system still open (see design freeze).** **`[web-val]` — moisture is the real hazard:** impermeable FRP inside + <1-perm closed-cell foam outside leaves the ply *no drying path* in a non-climate-controlled box (the build's own cited birch "precedent" was actually a condensation-failure story). → **Spec exterior/marine-glue birch, not interior-glue**; seal all FRP seams/edges + the window clamp sandwich so liquid water never enters the cavity; confirm the chosen FRP brand (Crane/Marlite/Glasbord) warranties Baltic birch + the adhesive grade. 3/8" sits near the structural floor (7/16" at 16" OC) — adequacy leans on the bonded FRP composite, so the lamination must be sound.
- **Stairs: folding/telescoping aluminum RV step stowed on the E-track grid.**
- **Panel transport slot:** the ground-pair LG455s (83" > 81" interior width) ride **lengthwise** in a padded E-track wall slot.

---

## Systems / gear

### Fridge — D008
- **Dometic CFX3 95DZ (purchased)** — 95 L dual-zone, 12/24 VDC, 24 V @ 4.6 A, 66.4 lb ([specs](reference/dometic-cfx3-95dz-specs.md)). Native **24 V** off the 5026; bay + thermal gate above. **`[web-val]`:** electrical sizing is sound/conservative (10 A fuse ≈ 2× the 4.6 A draw; VMSO3 soft-start, no big inrush; 14 AWG well-protected). Verify 14 AWG round-trip voltage drop holds the fridge above its low-voltage cutoff (<3 %), and check the unit's build date vs the **Nov 2019–Jun 2020 recall** window. The real risk is the bay thermal/compliance gate above, not the wiring.

### Order list
- **Long-lead now:** Fiamma F45s 350 + Tie Down S + lag anchors/deadman bags · Victron Orion-Tr 48/24-16A · Blue Sea 7443 · riser-bracket + backing steel (owner fab) · E-track top-up.
- **Accessories:** Proven 2516 coupler lock · 2× Abloy/Paclock pucks **keyed-alike** · Trimax TCL65 · LandAirSea 54 (hardwired, 24 V block) · Blue Sea 5026 · Scanstrut SC-USB-F3 · 14 AWG runs + fuse assortment + 2–3 POL 24→12 bucks · dome/task lights (24 V or POL).
- **Windows order:** RecPro frameless — 2× **RP-FRMWIN-1222-TRM** (12×22, walls) + 1× **RP-FRMWIN-2015-TRM** (20×15, door). Placement decided — see Climate/Windows.

---

## Design freeze — definition of done

**The design is DONE when every row below is checked.** Then the build phase starts: order everything, foam, walls, cuts, fab. Each row names what closes it.

| # | Item | Closes when | Status |
|---|---|---|---|
| 1 | **D006–D008 ratified** (24 V bus · awning standoffs · fridge integration) | owner ratifies in the DECISION_LOG | ☐ |
| 2 | **D009 wall substrate** — 3/8" birch re-skin over pulled OSB | owner ratifies + factory OSB thickness verified (row 19) | ☐ |
| 3 | **Track heights final** — bed ~27", shelf 60" | 31"-surface mock sit-test passes; shelf checked against the 36–58" window band | ☐ |
| 4 | **Window locations final** — exact bay stations, both walls + door | clear bay at chosen stations (row 7) + RecPro ROs (row 13) + clamp range vs birch+FRP build-up (row 12) + door frame (row 14) | ☐ |
| 5 | **Roof drawing** — panel feet, Velit station + opening, standoff stations on the measured 84⅞" × 145.5" field | rows 5a, 6, 15 measured and drawn | ☐ |
| 6 | **Awning standoff design** — section + fasteners | rail 3D scan + post tube wall thickness (row 16) → drawn part, ≥2 fasteners per upright | ☐ |
| 7 | **Floor plan final** — bike stagger, fridge bay, E-track rows | floor steel + bar widths + bay depth measured (rows 10, 11, 17) | ☐ |
| 8 | **Flooring material** | committed choice (lean: rubber coin roll — fuel/oil-proof, hose-out, relieved over the recessed E-track) | ☐ |
| 9 | **FRP trim system** | corner/seam/edge/reveal profiles + adhesive picked (color-matched vinyl moldings; FRP adhesive on birch) | ☐ |
| 10 | **Order list frozen** — every SKU + E-track footage recount | rows 1–9 closed | ☐ |

Post-freeze (build-phase, not design): fridge-bay ventilation check + lid hinge orientation · deployed-fabric vs open-door at pitch · **curb-weight weigh-in** (row 18).

## Weight
- **GVWR 3,500 lb** (confirmed). Payload = 3,500 − actual curb; **will be weighed**. Single axle is nose-sensitive — ~**10–12% tongue weight** when loading.

## Standing preferences (for whoever picks this up)
- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
