# Juplaya Trailer — Build Sheet

*Target: ready for Juplaya (~July 4, 2026).*

This is the **source of truth** for the build. How to read it:

- **Settled** items are firm — bought, measured, or otherwise beyond debate.
- **Decisions** are DECISION_LOG rows (D001–D012), `proposed` until the owner ratifies them. Each major one was produced by a cross-examined striatum multi-model panel (claude/codex/gemini drafting, reviewing, and revising each other); the raw drafts, reviews, and verdicts are frozen under `runs/`. Don't infer decisions that aren't written here or in a D-row.
- **Gates** are pass/fail checks that must pass **before drilling, fabricating, or ordering** the thing they guard. Most close from the [measurement pass](dimensions.md#-measurement-pass--fill-in-mm-preferred-these-supersede-spec); measured values supersede spec everywhere.
- **`[web-val]`** marks findings from the 2026-06-05 web fact-check of the original 7 falsifiable decisions plus the D010 flooring addendum ([full report](research/build-decision-validation.md)). It flipped 4/7 original decisions to caution; the material deltas are folded into the gates below.

The north star is [trailer-mission.md](trailer-mission.md): **the track grid is the operating system; the interior is software.** Floor **L-track** handles low-profile motorcycle chocks/tie-downs; wall **E-track** handles bed/shelf shoring and modules. Per D011, wall E-track mounts directly to the 1" thin-wall steel tube uprights with steel 1/4-20 rivnuts, and the birch/FRP finish trims up to the track. Nothing is built in permanently that could instead be a module strapped to track. The trailer must reconfigure between moto basecamp (two bikes in, gear walls), sleeping deck (bikes out, bed platform on the wall tracks), and empty box (cargo) without tools beyond a track fitting.

---

## The trailer (settled)

**Wells Cargo / ACG FasTrac Deluxe FT712S2-D** — 7×12 cargo trailer, single axle, V-nose, **Silverfrost** exterior. Bought from The Trailer Specialist, Acampo CA. **VIN 7V0W11214TU444163**, serial 444163.

| Fact | Value | Why it matters to the build |
|---|---|---|
| Interior | **81" W × 157" L × 78" H** (157" includes the tapering nose) | every layout number derives from this; the nose trapezoid is the electronics zone |
| Overall | ~16'0" L × 8'6" W × ~8'1" H | parking, clearance, panel reach for cleaning |
| Rear ramp | 78" × 72" opening, 5,000 lb rated | bike loading; 8' clearance with extension |
| Side door | **32" × 72" personnel door, RH hinge** | gets a window; defines the fridge bay's forward edge; the awning deploys over it |
| Structure | **2"×4" steel tube perimeter main rails · crossmembers 16" OC (on-center) · roof bows (tube) 24" OC · 76½" steel tube wall posts 16" OC** | the posts are the anchor grid: wall E-track rows, window bays (~14.5" clear), and awning standoffs all land on them |
| Floor | ¾" PlexCore (the factory's composite-ply floor sheathing) over the steel | floor L-track recesses are limited by what's between crossmembers |
| Anchors | 4× factory 5,000 lb D-rings | reused in the bike tie-down plan |
| Axle | 3,500 lb GVWR (gross vehicle weight rating), electric drum brakes | payload = 3,500 − curb (will be weighed); single axle is nose-sensitive |

References: [fastrac-specs.md](reference/fastrac-specs.md) (manufacturer line table + derived FT712S2 column) · [factory work order](reference/wells-cargo-ft712s2-d-work-order.md) (VIN-specific options) · **[dimension sheet](dimensions.md)** (every known dimension + the mm measurement-pass table).

## Tow vehicle (settled)

**2021 Ford F-150 EcoBoost, Max Tow package.** Pro Trailer Backup Assist on the truck; the integrated trailer backup camera + TPMS sensors are ordered. The 7-way connector (the standard trailer lighting plug) feeds running/marker/brake power only — **never house loads** (see Power).

---

## Power / electrical

Detailed power design, diagrams, component tables, and commissioning rules now live in **[power.md](power.md)**.

Current Juplaya power verdict:

- **DC trailer core:** roof 3× LG455 in 3S → Victron SmartSolar 250/60-Tr → LiTime 48V 100Ah ComFlex. Velit 2000R runs from a fused 48 V branch. Fridge/lights/USB/GPS run from the 24 V bus through one Victron Orion-Tr 48/24-16A. A Victron Orion-Tr IP43 48/12-20A feeds fused cigarette-lighter receptacles in the power cabinet for occasional 12 V loads.
- **Optional trailer-battery margin:** deployable 2× LG455 in 2S → ordered Victron SmartSolar 150/35. Never combine roof 3S and ground 2S on one tracker.
- **Small 120 VAC / storage comms:** Anker SOLIX C1000 + PS400 is the Juplaya AC island. Optional C1000 top-up from the trailer is only a fused/manual 24 V branch, about 240 W max, and must not starve the Orion/fridge bus. Starlink Mini is optional storage/camp comms, not the primary tracker; run it from the C1000 first or from a fused 12 V cabinet receptacle with Starlink's 12-24 V car adapter after shakedown.
- **Deferred:** Victron MultiPlus-II 48/3000/35-50 120V remains the Phase 2 built-in inverter/shore-charger/transfer choice, not a Juplaya blocker.

Must-not-miss gates:

- Roof 3S lands only on the SmartSolar 250/60-Tr; never into a 145/150 V-class AIO or MPPT.
- Roof panel brackets do not need to align with bows; **the roof rail/backing structure does**. Use fore-aft rails tied to multiple roof bows, then mount the panels/brackets to those rails. Do not fasten panel brackets only to roof skin. See [solar mounting build sheet](solar_mounting.md) and [solar mounting research](research/solar-panel-mounting-backing-2026-06-06.md).
- PS400 feeds the C1000 only; do not mix it with LG strings.
- Battery side first on MPPTs, then PV.
- Make battery-terminal main OCP explicit; no 32 V automotive fuse gear on the 48 V side.
- Verify the Blue Sea 20 A / 80 V UL-489 SKU (`7443` vs `7463`) before ordering/install.
- Fuse both Orion inputs with DC-rated 48 V gear; label the 12 V cabinet receptacles auxiliary only and keep them isolated from tow-vehicle/OEM trailer wiring.
- Configure LiFePO4 charge settings and cap combined trailer charge current ≤100 A.

Energy budget: trailer DC loads are about **3.5–4.0 kWh/day** in July; roof-only 3S harvest is about **6.0 kWh/day before soiling/shading**. The LG ground pair adds recovery margin; the C1000/PS400 carries only small AC loads. A Starlink Mini left on continuously adds about **0.7–1.1 kWh/day** real-world, so it is acceptable as an optional managed storage/camp link but not free.

---

## Climate / envelope

The envelope strategy: **closed-cell spray foam inside the steel skin, elastomeric coating outside on the roof, three operable windows for cross-flow, a 48 V rooftop AC for July, ducted diesel heat for winter.** July needs cooling and airflow; heat is deliberately deferred (D003) because mild playa nights don't justify carrying the install risk into the deadline.

### Insulation & roof (settled)

- **Closed-cell spray foam** in the wall and ceiling cavities; **elastomeric roof coating** outside; **Velit Mini 2000R rooftop AC (48 VDC) — ordered**, fed by its own fused 48 V branch.
- **Roof sandwich `[web-val]`:** building science *endorses* foam-inside + coating-outside on steel, **on one condition: the steel is dry, clean, and rust-free at closure** — foam over damp steel seals the corrosion in where it can never be seen. Execution requirements: air-seal the foam at every bow, fastener, and penetration; **spec a cold-rated/silicone coating** (standard summer-cure acrylics go brittle in deep cold and "zipper" off); run a **48-hr adhesion patch** on the actual galvanized/aluminized skin before committing to a product; confirm foaming under the roof doesn't void the solar-panel warranty; put periodic exterior blister inspections on the maintenance calendar (a blister is the only visible symptom of hidden steel corrosion).

### Roof solar mounting — rail/backing structure

The solar-panel brackets do **not** need to land on roof bows. The rail fasteners do. Use two fore-aft NXT rails spanning the three panel rows, drilled through at bow crossings and tied into multiple 24" OC roof bows with backing/crush control; the existing panel brackets/clamps bolt to those rails. Use 1/4" aluminum spacer pads at bow stations only if needed for low-profile drainage/crown control; EPDM/neoprene is acceptable as an isolation layer or high-durometer spacer only with crush sleeves/hard stops. Add a third rail only if the dry-fit proves the bracket pattern or rail stiffness needs it. Do not use roof-skin-only screws as the load path for the panels.

Order of operations: measured roof drawing -> rail centerlines and bow tie-ins -> dry-fit panels/Velit/awning standoffs -> drill and seal rails/gland/curb -> hose test -> foam -> Henry 887 roof coating. Build sheet: [solar_mounting.md](solar_mounting.md). Full research and gates: [solar mounting backing note](research/solar-panel-mounting-backing-2026-06-06.md).

### Roof coating — picked

**Henry 887 Tropi-Cool White 100% Silicone Roof Coating** (HE887HS018, Home Depot) is the coating. Use the matching **Henry 884 Tropi-Cool 100% Silicone Roof Sealant** at roof penetrations, fastener heads, curbs, transitions, and other leak paths that will be top-coated. Henry lists 887 for metal roofs and RV/trailer/mobile-home roofs, with 35–120 °F application range, silicone chemistry, and permanent ponding-water resistance. The Home Depot product Q&A from Henry lists service temperature as **−40 to 180 °F**, which clears the winter-cold caution that killed generic acrylic elastomerics.

**Quantity:** the label rate is about 1.5 gal / 100 ft² for 22 mil dry film. The trailer roof field plus nose/curbs/penetrations makes a 0.90 gal can too tight; buy **one 4.75 gal pail** unless the measured roof drawing proves a smaller can-and-a-half job. This is compatible with the existing roof gate: **clean/dry/rust-free steel, silicone-compatible penetration sealant, then a 48-hr adhesion patch on the actual skin before the full coat.**

### Windows — placement decided

Three RecPro frameless units. Placement logic: the pair gives **cross-breeze directly over the bed**; the door window adds forward light and a third vent point for front-to-back flow when the AC is off.

| Window | SKU | Cutout `[web-val]` | Location |
|---|---|---|---|
| 12"×22" ×2 (portrait) | RP-FRMWIN-1222-TRM | **11-5/8" × 21-5/8"** | rear (bed) zone, **directly opposite each other**, roadside + curbside (roadside = driver side; curbside = passenger/awning side), same bay station, sills ~36" |
| 20"×15" ×1 | RP-FRMWIN-2015-TRM | **19-5/8" × 14-5/8"** | in the 32"×72" personnel door |

Why these spots survive every other system: the 12" cutout fits **inside one 16"-OC post bay (~14.5" clear) — no post gets cut, no sub-frame needed.** The 36–58" window band sits between the bed track (~27") and the shelf track (60"). Roadside-rear is behind the bikes' handlebar sweep (bars live in the front half, nose-forward). Curbside-rear clears the 18.6"-tall fridge and the roofline-mounted awning case above.

**Gates before cutting:**
- Clear bay width at both chosen stations (dimension row 7) against the confirmed cutouts (row 13 ✓).
- **Clamp-ring vs wall build-up `[web-val]`: the RecPro trim ring is a single 1.5" spec, not a range.** The built-up wall (steel skin + birch + FRP — fiberglass-reinforced plastic, the wipe-clean interior skin) lands ~1"–1.4" — **it won't clamp tight as-is → fur the window openings up to 1.5"** (this step now lives in the wall plan).
- Door window: the RO (rough opening) vs the door's internal frame (row 14) — and **the 20×15 cut in a ~20-ga steel door skin removes a structural panel → add perimeter re-framing** `[web-val]`.
- **Galvanic isolation** `[web-val]`: aluminum frames/screws against steel skin — butyl isolation + stainless/nylon hardware.
- Keep the curbside bay clear of awning-standoff backing spans.

### Heater — winter, operates OUTSIDE the space

**LF Bros N4, 24 V variant** ([specs](reference/lf-bros-n4-specs.md)): 5 kW all-in-one pedestal, integrated 3.5 L tank, 17"×13"×14.8", 15.9 lb, rated to −40 °F. **Not aboard for July** (D003).

The owner's call: the heater sits **outside**, heat comes in through **2 × 3" ducts** (supply + return). That single decision deletes the two worst parts of a diesel-heater install — **no fuel line, no combustion exhaust penetration; combustion never enters the envelope.**

What July pre-builds (cheap while everything is open):
- **2 × 3" duct ports**, capped/plugged — placed low, clear of the bed zone and the fridge bay.
- A **24 V feed reachable at the heater's exterior station** (the 15 A / 12 AWG rail-map branch).
- **CO detector** — cheap insurance on the supply duct path.
- An inside E-track spot for the unit is **transport/storage only**, not an operating position.

Open: glow-plug draw is unpublished — **bench-measure on arrival** (typical 5 kW units: ~90–260 W glow ≈ 4–11 A @ 24 V for 2–3 min; run ~1–2 A). The measured number decides load-shedding vs a second converter (see the 24 V bus section).

### HRV (deferred, rough-in now)

HRV = heat-recovery ventilator: fresh-air exchange without dumping the heat. Rough-in **paired 4" wall penetrations + a power string**; no unit for July. A future HRV solves winter condensation, which matters more once the heater is in play.

### Awning — D007

**Fiamma F45s 350** (06280B01R): 138" (11'6") case, 5.35" tall, ~55 lb, 130" canopy. The July deliverable for shade.

**How the mount was arrived at** (both stock options are dead, by measurement):
1. **Wall-mount: dead by tape (2026-06-04).** Measured clearance from drip-rail top to the trailer's top edge is **5-1/8"** — the case is 5.35" tall. Short by 0.225". Deployed fabric would also foul the door swing.
2. **Flat-roof-adapter mount: dead by arithmetic.** The two solar panels own the roof width (83.07" of 84-7/8"); there is no curbside roof strip.
3. **Therefore: owner-fabricated standoffs at the perimeter aluminum top rail**, holding the case **at/above the roofline (case bottom ≥ ~78.5")** — same door-swing math as a roof mount, zero roof width consumed.

**Stations & load path:** the rail's existing bolts mark the uprights — **but they sit at the center of the extrusion**, and a single centered bolt can't react the standoff's prying moment. So **each standoff base runs down the wall face and takes ≥2 fasteners into its steel tube upright** (a vertical couple — maximize the spread; the lower fastener kills the moment). The rail bolt gets picked up as a bonus, not as the load path. Fasten into the tube by drill-and-tap or through-bolt **while the interior is open — before FRP**; butyl-seal every skin penetration. Design for deployed wind + tie-down + travel vibration, not the 55 lb static case.

**Required outputs before fab:** standoff count/stations along the 138" case (the F45s wants 3–4 brackets — pick uprights that bracket the span plus mid-span; there are no uprights across the 32" door, so stations flank it); fastener size/grade + **post tube wall thickness** (decides tap vs through-bolt); couple-arm spacing; a documented load case.

**Gates:** the rail-section 3D scan (dimension row 16) · the shared measured roof drawing · **deployed-fabric vs open-door at actual pitch** (the paper margin is ~0.9": fabric ~72.9" at 32" out, 10° pitch, vs the 72" door). **Fallback if gates fail:** freestanding shade (Moonshade-class) anchored to trailer + ground — zero trailer structure.

**Deployment discipline `[web-val]`:** Fiamma Tie Down S (98655-133) + 3/8"×12" lag anchors / deadman bags (buried/weighted anchors for ground that lags can't bite); legs to ground. **The retract threshold depends on deployment mode:** wall-only (no legs, load through the fasteners) → wind in by **~10 mph**; legs staked + tie-down → **~20–25 mph**. The old flat ">20 mph" rule assumed legs+tie-down and is ~2× too loose for the wall-only case. Note the limiting failure is the **awning's own arms bending, not fastener pull-out** — and an over-rigid standoff can defeat the arms' designed give, so don't over-constrain. Always wound in before sleep, departure, or gusts.

---

## Interior / layout

Two configurations share one floor: **moto mode** (both bikes in, gear on the walls) and **camp mode** (bikes out, bed deck on the wall tracks). Everything below is a module on the track grid.

### Bikes & floor L-track

- **WR250R + CRF450RL (~590 lb pair), side-by-side, nose-forward, on the roadside half**, in **ordered Bolt It On 360 L-track wheel chocks** (12–18" stagger so the bars interleave). Starting floor geometry: **two lengthwise floor L-track rows, about 26" on center**, flush/recessed and bolted through to steel/backing; the 4 factory D-rings get reused as backup tie points. Primary motorcycle crash restraint stays on the floor L-track and factory 5,000 lb D-rings tied to the steel frame/crossmembers, not on the wall E-track.
- **⚠ Floor plan rework gate:** the original ~24" E-track centerline spacing **failed** — cross-exam found ~9" of handlebar interference, and the 2"×4" main rails run at the **perimeter** (not under the centerline), while a deep recess leaves limited ply between crossmembers. The final L-track row positions must be re-derived against **measured** steel locations (row 10), actual bar widths/front-tire centerlines (row 11), and the ordered chock hardware/studs. Evidence/options: [L-track floor chock options](research/l-track-floor-chock-options-2026-06-05.md).
- **Aisle reality:** the nominal ~30" walking aisle shrinks to **~20" effective at bar height** — fridge access and egress are planned around that, not the floor-level number.
- **Track/chock order status:** floor L-track = **2 × 8 ft flanged L-track sections ordered / on the way (2026-06-05)**; **Bolt It On 360 L-track wheel chocks ordered (2026-06-05)**. The ~50–60 ft of E-track on hand should be treated as wall-track stock first, not floor stock.

### Flooring — D010 (accepted)

**Committed recommendation: Durabak-18 Outdoor Textured, light grey — 3 gal ORDERED 2026-06-05, delivery window June 12–15, 2026; 4th gal conditional.** It is a flexible polyurethane bed-liner coating rolled/brushed onto the ¾" PlexCore floor, the rear ramp deck, and **coved 3–4" up the lower walls before the FRP lands**. FRP laps over the cured cove, turning the floor into a hose-out tray; raise the tongue jack to sluice dust and wash water toward the rear ramp. The remembered "DuraLok" name is not the spec.

Why this replaces the old rubber-coin lean: common coin roll is usually SBR (styrene-butadiene rubber), and SBR is a poor fit for moto fuel/oil spills. A bonded polyurethane liner avoids the under-sheet playa-dust/water trap, keeps the floor seamless, and stays much lighter than a thick loose rubber mat. Do not use a rigid garage epoxy; the single-axle trailer floor will move.

**Web-validation correction:** say **fuel/oil spill-resistant, clean promptly**, not "fuel-proof." Durabak's product data supports a flexible, one-part, non-slip polyurethane coating; Durabak's wood-prep guidance warns that sanded wood dust causes delamination and calls for a patch test; Raptor's 2K polyurethane data validates the class on stable wood and shows diesel/hydraulic-oil resistance, but gasoline/petrol is listed as splash-resistant rather than immersion-proof. The build therefore requires a PlexCore adhesion patch and a small gasoline/diesel drip patch before coating the whole floor.

**Adversarial review:** [floor-coating verdict](../runs/floor-coating-adversarial/synth/VERDICT.md) considered Durabak, Raptor, Herculiner, Rust-Oleum, TotalBoat TotalTread, KiwiGrip, Pettit EZ-Decks, Interlux Interdeck, Tuff Coat, G-Floor, and Monstaliner. It keeps Durabak as the default because light grey, one-part DIY control, cove execution, and truck-bed-duty polyurethane fit beat the cheaper alternatives for this trailer; Raptor remains the tested fallback.

**Raptor schedule override closed:** owner checked local availability and shippers on 2026-06-05; the acceptable 2K tintable light-gray Raptor path has no local availability or reliable ETA, so it provides no schedule benefit over Durabak and keeps all of the 2K downsides. Raptor remains only a patch-failure fallback. If reopened, acceptable color is Raptor Color **Light Gray** (UP4855) or a matched solvent-based urethane/acrylic automotive toner in the same light-gray range, mixed per Raptor's tint guidance. White is technically acceptable but too glare/stain-prone to prefer; Basalt Gray, black, and the AutoZone-visible black 2K kit are not acceptable as the main floor color. Do not substitute the 1K aerosol or 1-part roll-on Raptor products for the 2K fallback.

**Quantity:** start with **3 gallons ordered** for the base floor+cove+ramp coat plan. Keep a **4th gallon conditional** behind the PlexCore patch coverage and first full-area coverage rate, for a third coat in the wear lanes if needed (rear ramp deck and chock/L-track contact lanes). The interior floor is bounded by 81" × 157" (~88 ft²), the 3–4" wall cove adds ~12–14 ft², and the 78" × 72" ramp adds ~39 ft². Durabak textured coverage is ~50–60 ft²/gal for a standard two-coat application, so 3 gal is adequate but tight once the ramp and tie-down lanes get extra film; order the 4th gallon only if the patch/first-pass coverage says the wear-lane coat will be short.

**Install sequence:** finish the floor L-track/chock layout first, then recess and bolt the floor L-track through to steel/backing. Mask the L-track slots, fastener heads, D-ring pockets, ramp hinge/transition hardware, and any drain/edge details so fittings stay usable and hardware remains inspectable. Sand the PlexCore, vacuum hard, remove dust per the coating instructions, run the patch tests, coat the floor plus cove plus ramp, add the third wear-lane coat, cure fully, then land the FRP over the cove. If Durabak fails the patch, use a Raptor-class flexible polyurethane with the correct wood prep; if coating fails entirely, the only acceptable roll fallback is **fully glued G-Floor PVC trailer flooring**, not loose-lay.

### Bed & wall tracks — D011

- **Bed row at ~27", shelf row at ~60"**, both mounted directly to the 16"-OC, 1" thin-wall steel tube posts with steel 1/4-20 rivnuts. Do not depend on birch or FRP as the track structure.
- **Why 27" (revised from 34", owner challenge upheld):** at 34" the sleeping surface (~38.5" with platform + pad) left **1–3" of seated headroom** under the 78" ceiling for a 6'+ adult; at 27" (surface ~31") it's ~46" — you can actually sit up in bed. Bikes are out in camp mode, so nothing needs the taller under-deck clearance. **Gate: mock a 31" surface and sit-test before drilling** (design-freeze item 3).
- **Track finish detail:** install the rivnuts into the posts before foam/FRP; trim birch and FRP up to the E-track so the rail sits flush or slightly proud. Keep fastener heads visible and serviceable, and leave enough clearance at the FRP edge for fittings to rock into the E-track slots.
- **Use envelope:** wall E-track handles bed shoring, shelves, gear modules, anti-tip straps, and panel transport. It is not the primary motorcycle restraint system.
- **Bed shoring:** E-track sockets taking plain 2×4 lumber — legs under the deck when slept on, gone in moto mode.
- **Escalation path:** if a wall row shows movement after service testing, weld tabs or backing strips to the uprights and keep the E-track bolted to those welded features so the rail remains replaceable.

### Fridge bay

- **Curbside, immediately aft of the personnel door**, fridge E-track-strapped. Footprint 37.9" × 20.9" × 18.6" tall **plus lid-swing clearance — verify which way the split lids hinge before fixing the bay's wall orientation.** The location survives: outside reach under the awning, lid access in both modes, clear of the door swing.
- **⚠ Thermal gate — HARDENED `[web-val]`:** the Dometic manual requires a **50 mm (~2") gap on all four sides** and flatly says **"do not place the cooling device in closed compartments."** An enclosed bay is non-compliant as worded. So: **the bay gives 50 mm all-sides clearance + forced through-flow ventilation** — "shaded" alone doesn't cut it. Then field-verify in-bay air temperature under desert sun with the awning out: **<43 °C (110 °F) to run at all, <30 °C (86 °F) to hold both dual-zone setpoints.** Keep the bay off the nose-cabinet heat plume. (Dometic error codes: Warning 34 = high ambient / blocked vent; Warning 33 = low supply voltage — see Systems for the wiring check.)

### Walls — D009 (proposed)

**Pull the factory OSB while the walls are open for foam, re-skin in 3/8" birch ply, FRP textured panel over the birch, no paint.**

- **Why:** the foam job already has the walls stripped — the swap is nearly free labor. 3/8" matches the factory skin thickness, so the wall-sandwich geometry (window clamp range, door reveals) doesn't move. Birch holds screws and FRP adhesive far better than OSB. The owner has access to high-quality stock (one 3/8" and one 1/2" sheet on hand; 1/4" obtainable).
- **Thickness ruling:** **3/8" for the walls.** 1/4" rejected — flexes between the 16"-OC posts and thins the window clamp sandwich. The **1/2" sheet goes to interior fixtures** (fridge-bay partition, shelving), not walls.
- **`[web-val]` — moisture is the real hazard:** impermeable FRP on the inside + <1-perm closed-cell foam on the outside leaves the ply **no drying path** in a box that isn't climate-controlled year-round (the one birch "precedent" the build had cited turned out to be a condensation-failure story). Mitigations are mandatory, not optional: **exterior/marine-glue birch only** (not interior-glue); **seal every FRP seam/edge and the window clamp sandwich** so liquid water never reaches the cavity; **confirm the chosen FRP brand** (Crane/Marlite/Glasbord) **warranties application over Baltic birch with the chosen adhesive.** Note 3/8" sits near the structural floor (7/16" @ 16" OC) — stiffness leans on the bonded FRP composite, so the lamination must be sound.
- ¼" XPS (rigid extruded-polystyrene foam board) goes behind the bed zone only (back insulation against the cold wall). All backing plates go in **before** finish.
- **Gates:** verify the factory OSB is actually 3/8" (row 19) · D009 ratified **before any window RO is cut** (the row-12 clamp check depends on the final sandwich) · FRP trim system selected (design-freeze item 9).

### Stairs & panel transport

- **Entry: folding/telescoping aluminum RV step**, stowed on the track grid (no permanent step).
- **Panel transport slot:** the ground-pair LG455s are 83" long vs the **81" interior width** — they ride **lengthwise** in a padded E-track wall slot. (One more reason the interior-width tape measurement matters: row 3.)

---

## Systems / gear

### Fridge — D008

**Dometic CFX3 95DZ (purchased)** — 95 L dual-zone, 12/24 VDC compressor, 24 V @ 4.6 A, 66.4 lb ([specs](reference/dometic-cfx3-95dz-specs.md)). Runs **native 24 V** off the 5026 — zero conversion stages between battery and compressor.

**`[web-val]`:** the electrical sizing is sound and conservative — 10 A fuse ≈ 2× the 4.6 A draw; the VMSO3 compressor (Dometic's variable-speed unit) soft-starts (no meaningful inrush); 14 AWG is well-protected. Two checks remain: verify the 14 AWG round-trip **voltage drop stays <3 %** so the fridge never sees its low-voltage cutoff, and check the unit's build date against the **Nov 2019–Jun 2020 recall window**. The real risk on this fridge is the bay thermal gate (Interior section), not the wiring.

### Lighting

- **Switches live on the power cabinet for Juplaya.** Skip the entry-door light switch for now; it adds wall/door-area wiring and is easy to revisit later if use proves it matters. If convenient while walls are open, leave a labeled pull string or spare low-current pair toward the side-door bay.
- **Lighting controls — D012:** keep the six cabinet lighting switches and put a 24 V PWM dimmer downstream of each switched branch: INTERIOR, CURB FLOOD, ROAD FLOOD, NOSE FLOOD, REAR FLOOD, and AWNING. The switches are hard enables; the dimmers set brightness.
- **Exterior lighting layout:** **2 curbside floods, 2 roadside floods, 1 flood on each V-nose face, 1 rear flood, plus separate awning lighting**. Optional low amber step/courtesy can share the awning circuit if added. Run them from the **24 V house bus** using 12-28 VDC / 10-30 VDC IP67-ish fixtures, fused per branch, switched and dimmed at the cabinet. Keep all house exterior lighting isolated from the OEM trailer lights and 7-way tow plug.
- **Selected fixture class:** seven **Super Bright LEDs `VAL2-NW9`** floods (9", black, 1450 lm, 18 W, 4000 K, 90 deg, IP67, 12-28 VDC) are **ORDERED** per the [exterior-lighting panel](../runs/exterior-lighting-panel/synth/VERDICT.md). `VAL2-WW9` is the warm 3000 K alternate if replacement stock is ever needed. Use separate warm 24 V dimmable strip lighting for the awning, such as **`RA-IP68-80CRI-5m` 3000 K**, not another glare flood.
- **Switch/dimmer hardware:** use **Blue Sea 8260 6-position Contura mounting panel + 6x Blue Sea 8282 SPST OFF-ON black Contura switches** labeled INTERIOR, CURB FLOOD, ROAD FLOOD, NOSE FLOOD, REAR FLOOD, AWNING. The 8260 panel needs <=0.38" mounting thickness, so use a thin inset plate or rabbet a thicker cabinet face. Default dimmer is **6x Super Bright LEDs `LDK-8A` 12-24 V / 8 A PWM dimmers**, one after each switch. Blue Sea 7509 is the premium sealed/panel-integrated dimmer fallback if the cheap controls feel wrong.
- **Dimming gate:** bench-test one ordered `VAL2-NW9` flood/scene fixture with the selected PWM dimmer before final exterior mounting. Its public specs confirm 12-28 VDC, 18 W, and 1.5 A, but do not explicitly say dimmable. If it flickers, buzzes, shuts down, or runs hot on PWM, keep that exterior side switch-only or change to a dimmable exterior fixture.
- **Light quality/current:** seven `VAL2` floods are 126 W total, about 5.25 A on the 24 V bus; the full awning strip is about 64 W / 2.7 A before dimming. Floods should aim down/out, not at neighbors. Verify the Orion 48/24 output stays below the fixtures' 28 V input ceiling.

### Security & tracking

- **Proven 2178 coupler lock** for the documented 2" coupler + **2× PACLOCK 7-Series / UCS-7A flat-back puck locks, keyed alike to the truck's existing PACLOCK U-PICK code if cylinder family matches** + **Trimax TCL65** wheel lock — layered, because Juplaya. One keyed-alike puck goes on the rear ramp; one goes on the personnel-door hasp. Verify the truck locks are UCS before ordering UCS-7A pucks; PRO/SR/RD PACLOCK families do not automatically share codes. Do not order the Proven 2516 unless the trailer is upgraded to a 2-5/16" coupler.
- **Personnel door:** the factory latch/deadbolt is not enough as the security layer. **Nu-Set 8-1/4" high-security trailer-door puck hasp is ORDERED**; install it with six 3/8" carriage bolts/washers/nuts, backing plates, and sealant, tied into the door frame/jamb rather than thin door skin alone. External puck hasp is for unattended/travel/storage only; never use it as the occupied/sleeping latch because it cannot be opened from inside. Occupied mode needs an inside-operable latch/deadbolt.
- **Ramp door:** first choice is the matching keyed-alike PACLOCK 7-Series / UCS-7A puck if the ramp latch/hasp accepts a puck. Use the truck's existing U-PICK key code only after confirming the truck locks are UCS; otherwise contact PACLOCK for cross-family options or keep the trailer on its own U-PICK code. If the ramp only has a conventional shackle hole, either add a puck-compatible hasp or use a PACLOCK keyed-alike UCS shackle padlock as the fallback.
- **LandAirSea Overdrive Permanent GPS Tracker with hardwire cable — ORDERED**, expected June 12, 2026. Hardwire to the 24 V block (3 A branch), always-on. This is the primary hidden keepalive/tracking layer for Oakland storage; Starlink Mini is a secondary high-bandwidth path only if the storage spot has open sky and the power schedule works. A free/covered Oakland spot is still usable with cellular telemetry; choose an Alameda/open-sky spot only if physical security, access, solar exposure, or broadband telemetry are worth the delta.

### Order list

Dedicated ordering and budget ledger: **[order-sheet.md](order-sheet.md)**. The list below stays abbreviated so this build sheet remains the engineering source of truth instead of the purchasing ledger.

- **Long-lead, order now:** return LiTime 5 kW; **defer the Victron MultiPlus-II until Phase 2** · Fiamma F45s 350 + Tie Down S + lag anchors/deadman bags · Victron Orion-Tr 48/24-16A · **Victron Orion-Tr IP43 48/12-20A — ADDED for power-cabinet 12 V receptacles** · **Victron SmartSolar MPPT 250/60-Tr + 250 V-class roof PV disconnect/OCP** · **Victron SmartSolar MPPT 150/35 for deployable 2S LG ground — ORDERED, connector variant pending** · the 48 V-side UL-489 breaker (**verify SKU: 7463 vs "7443"**, web-val) · **power-cabinet interior transfer grilles/filter + 24 V cabinet fan + normally-open thermostat** · standoff + backing steel stock (owner fab) · **2 × 8 ft flanged floor L-track — ORDERED / on the way** · **Bolt It On 360 L-track wheel chocks — ORDERED**.
- **Coatings:** Henry 887 Tropi-Cool White 100% Silicone Roof Coating (HE887HS018, 4.75 gal pail) + Henry 884 Tropi-Cool silicone sealant · **Durabak-18 Outdoor Textured light grey, 3 gal — ORDERED, delivery June 12–15, 2026; 4th gal conditional** after patch/first-pass coverage for ramp/chock/L-track wear lanes.
- **Accessories:** Blue Sea 5026 · Scanstrut SC-USB-F3 · LandAirSea Overdrive Permanent GPS with hardwire cable — ORDERED · locks (above) including ordered Nu-Set personnel-door hasp/backing · 14 AWG runs + fuse assortment · fused cigarette-lighter receptacles for the power cabinet · optional Starlink Mini treated as storage/camp comms · dome/task lights (24 V preferred; 12 V only at the cabinet outlets) · **exterior lighting: 7 × Super Bright LEDs `VAL2-NW9` floods — ORDERED, 1 × warm 24 V awning strip such as `RA-IP68-80CRI-5m`, optional amber step/courtesy, Blue Sea 8260 switch panel + 6 × Blue Sea 8282 switches, 6 × `LDK-8A` PWM dimmers, and custom labels**.
- **Windows:** 2× RP-FRMWIN-1222-TRM + 1× RP-FRMWIN-2015-TRM (placement decided — Climate section).

---

## Build sequence (dependency order)

The design freeze (below) gates step 3 onward. Within the sequence, **"while the walls are open" is the critical window** — five different systems need it.

1. **Measure & scan** — finish the [measurement pass](dimensions.md): interior tape (rows 3/3a, 7, 14, 17), roof stations (5a, 6), rail 3D scan + post wall thickness (16), floor steel + bar widths (10, 11), OSB thickness (19).
2. **Freeze** — close the 10 design-freeze items; ratify D006–D009; D010 and D011 are accepted; place remaining orders (long-lead first).
3. **Strip the interior** — factory OSB off (it's the template stock for the birch cuts); document factory wiring as found.
4. **Everything that needs open walls / bare roof:**
   - Awning standoff fasteners + any backing into the posts (≥2 per upright).
   - Window-bay furring (build openings out to the 1.5" clamp spec) + backing.
   - Wall E-track steel 1/4-20 rivnuts into the 1" tube posts at the 27"/60" rows; use the track as the finish datum and keep fasteners inspectable.
   - Rough-ins: HRV 4" pair, heater 3" duct ports, wire chases, 4 AWG tongue pre-wire.
   - Roof: solar rail/backing structure first (fore-aft rails tied to multiple bows; brackets/panels attach to rails, not skin), then Velit opening + curb, PV gland, all penetrations sealed and hose-tested.
5. **Foam** — steel verified dry/clean/rust-free; every penetration already made (foam after cutting, never before); air-seal at bows/fasteners.
6. **Roof coating** — Henry 887 silicone, after the 48-hr adhesion patch passes.
7. **Floor liner + walls closed** — floor L-track recessed/bolted through to steel/backing first; Durabak-18 floor+cove+ramp applied and cured; 3/8" exterior-glue birch + FRP land over the cove, seams/edges sealed, and trimmed to the wall E-track edges.
8. **Window cuts + install** — after the row-12 clamp check against the real sandwich; door window gets perimeter re-framing.
9. **Tracks & remaining floor hardware** — wall E-track rows bolted to the rivnuts in the posts; floor L-track masks pulled and slots/hardware inspected.
10. **Nose cabinet** — battery, SmartSolar, shunt, breaker, Orion-Tr 48/24, Orion-Tr 48/12, 5026, fused 12 V receptacles; rail wiring out to branches; cabinet-to-cabin ventilation with low filtered intake, high fan-assisted exhaust, 24 V fan, and temperature switch. Avoid exterior penetrations for now; if shakedown heat becomes a real issue, reopen the exterior-vent fallback. MultiPlus mounting space can be reserved for Phase 2, but it is not a Juplaya install dependency.
11. **Systems** — fridge bay (50 mm clearance + through-flow), cabinet-switched interior/exterior lights, USB/GPS, awning case onto the standoffs, tie-down anchors.
12. **Weigh & commission** — scale (curb + tongue, row 18); combined charge-current cap ≤100 A; verify roof 3S lands only on SmartSolar and optional LG ground 2S lands only on its own MPPT path; verify the C1000 + PS400 covers small AC loads; if a 24 V C1000 top-up branch is added, test that it does not brown out or overload the Orion/fridge bus; shakedown camp before Juplaya.

---

## Design freeze — definition of done

**The design is DONE when every row below is checked.** Then the build phase starts (sequence above). Each row names what closes it.

| # | Item | Closes when | Status |
|---|---|---|---|
| 1 | **D006–D008 ratified** (24 V bus · awning standoffs · fridge integration) | owner ratifies in the DECISION_LOG | ☐ |
| 2 | **D009 wall substrate** — 3/8" birch re-skin over pulled OSB | owner ratifies + factory OSB thickness verified (row 19) | ☐ |
| 3 | **Track heights final** — bed ~27", shelf 60"; D011 wall-track mounting detail accepted | 31"-surface mock sit-test passes; shelf checked against the 36–58" window band; 1/4-20 rivnut-mounted E-track/FRP-edge fit confirmed on an offcut or first row | ☐ |
| 4 | **Window locations final** — exact bay stations, both walls + door | clear bay at chosen stations (row 7) + RecPro ROs (row 13 ✓) + clamp range vs birch+FRP build-up (row 12) + door frame (row 14) | ☐ |
| 5 | **Roof drawing** — three panel rows, fore-aft NXT rail/backing structure + through-rail bow tie-ins, Velit nose station + opening/shadow line, PV gland, standoff stations on the measured 84⅞" × 145.5" field | rows 5a, 6, 15 measured and drawn; through-rail fastener/backing/spacer detail selected | ☐ |
| 6 | **Awning standoff design** — section + fasteners | rail 3D scan + post tube wall thickness (row 16) → drawn part, ≥2 fasteners per upright | ☐ |
| 7 | **Floor plan final** — bike stagger, fridge bay, L-track rows | floor steel + bar widths/front-tire centerlines + bay depth measured (rows 10, 11, 17); 2×8 ft flanged L-track and Bolt It On 360 chocks received/fit-checked; chock hardware kit confirmed | ☐ |
| 8 | **Flooring material** | D010 accepted: Durabak-18 Outdoor Textured light grey, 3 gal ordered for June 12–15 delivery; 4th gal conditional after patch/first-pass coverage; PlexCore adhesion + fuel-drip patch required before coating | ☑ 2026-06-05 |
| 9 | **FRP trim system** | corner/seam/edge/reveal profiles + adhesive picked (color-matched vinyl moldings; FRP adhesive warranted on birch — web-val) | ☐ |
| 10 | **Order list frozen** — every SKU (incl. SmartSolar 250/60-Tr + 250 V-class PV disconnect/OCP, ordered SmartSolar 150/35 ground MPPT, roof solar rail/backing hardware, C1000/PS400 carried as the Juplaya AC island, 7463-vs-7443 breaker check, Henry 887/884, Durabak quantity, power-cabinet interior vent/fan/thermostat parts, exterior lighting + cabinet switch/dimmer parts, ordered floor L-track, ordered Bolt It On 360 chocks). MultiPlus-II remains Phase 2, not a freeze blocker. | rows 1–9 closed | ☐ |

Post-freeze (build-phase, not design): fridge-bay ventilation check + lid hinge orientation · deployed-fabric vs open-door at pitch · **curb-weight weigh-in** (row 18).

## Weight

**GVWR 3,500 lb** (gross vehicle weight rating — confirmed). Payload = 3,500 − actual curb; **the trailer will be weighed** rather than estimated — no paper weight budget. Single axle is nose-sensitive: load to ~**10–12 % tongue weight**, battery low and centered, bikes' mass forward of the axle.

## Standing preferences (for whoever picks this up)

- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
