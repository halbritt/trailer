# Juplaya Trailer — Build Sheet

*Target: ready for Juplaya (~July 4, 2026).*

This is the **source of truth** for the build. How to read it:

- **Settled** items are firm — bought, measured, or otherwise beyond debate.
- **Decisions** are DECISION_LOG rows (D001–D010), `proposed` until the owner ratifies them. Each major one was produced by a cross-examined striatum multi-model panel (claude/codex/gemini drafting, reviewing, and revising each other); the raw drafts, reviews, and verdicts are frozen under `runs/`. Don't infer decisions that aren't written here or in a D-row.
- **Gates** are pass/fail checks that must pass **before drilling, fabricating, or ordering** the thing they guard. Most close from the [measurement pass](dimensions.md#-measurement-pass--fill-in-mm-preferred-these-supersede-spec); measured values supersede spec everywhere.
- **`[web-val]`** marks findings from the 2026-06-05 web fact-check of the original 7 falsifiable decisions plus the D010 flooring addendum ([full report](research/build-decision-validation.md)). It flipped 4/7 original decisions to caution; the material deltas are folded into the gates below.

The north star is [trailer-mission.md](trailer-mission.md): **the E-track grid is the operating system; the interior is software.** (E-track: slotted steel tie-down track — fittings click in anywhere, no tools.) Nothing is built in permanently that could instead be a module strapped to track. The trailer must reconfigure between moto basecamp (two bikes in, gear walls), sleeping deck (bikes out, bed platform on the wall tracks), and empty box (cargo) without tools beyond a track fitting.

---

## The trailer (settled)

**Wells Cargo / ACG FasTrac Deluxe FT712S2-D** — 7×12 cargo trailer, single axle, V-nose, **Silverfrost** exterior. Bought from The Trailer Specialist, Acampo CA. **VIN 7V0W11214TU444163**, serial 444163.

| Fact | Value | Why it matters to the build |
|---|---|---|
| Interior | **81" W × 157" L × 78" H** (157" includes the tapering nose) — **tape-confirmed 2026-06-05: 81" W (to 81-3/32") × 156" L × 78" H**, see [interior footprint](#interior-footprint--measured-owner-tape-2026-06-05) | every layout number derives from this; the nose trapezoid is the electronics zone |
| Overall | ~16'0" L × 8'6" W × ~8'1" H | parking, clearance, panel reach for cleaning |
| Rear ramp | 78" × 72" opening, 5,000 lb rated | bike loading; 8' clearance with extension |
| Side door | **32" × 72" personnel door, RH hinge** | gets a window; defines the fridge bay's forward edge; the awning deploys over it |
| Structure | **2"×4" steel tube perimeter main rails · crossmembers 16" OC (on-center) · roof bows (tube) 24" OC · 76½" steel tube wall posts 16" OC** | the posts are the anchor grid: E-track rows, window bays (~14.5" clear), and awning standoffs all land on them |
| Floor | ¾" PlexCore (the factory's composite-ply floor sheathing) over the steel | flush E-track recesses are limited by what's between crossmembers |
| Anchors | 4× factory 5,000 lb D-rings | reused in the bike tie-down plan |
| Axle | 3,500 lb GVWR (gross vehicle weight rating), electric drum brakes | payload = 3,500 − curb (will be weighed); single axle is nose-sensitive |

References: [fastrac-specs.md](reference/fastrac-specs.md) (manufacturer line table + derived FT712S2 column) · [factory work order](reference/wells-cargo-ft712s2-d-work-order.md) (VIN-specific options) · **[dimension sheet](dimensions.md)** (every known dimension + the mm measurement-pass table).

## Tow vehicle (settled)

**2021 Ford F-150 EcoBoost, Max Tow package.** Pro Trailer Backup Assist on the truck; the integrated trailer backup camera + TPMS sensors are ordered. The 7-way connector (the standard trailer lighting plug) feeds running/marker/brake power only — **never house loads** (see Power).

---

## Power / electrical

### Architecture — why it looks like this

One high-voltage battery bus, one conversion step down, no legacy 12 V plumbing:

```
Roof PV (3 x LG455 in 3S)
        │
   Victron SmartSolar MPPT 250/60-Tr
        │
   LiTime 48V 100Ah ComFlex (5.12 kWh)  ←→  LiTime 48V 3500W AIO
        │ 500A shunt, main OCP               (inverter/charger + optional ground MPPT)
        │                                             │
        │                                             ├── optional deployable 2S ground pair
        │                                             └── 120 VAC out (3500 W / 6000 W surge)
        ├── 48 V branch: Velit 2000R rooftop AC (48 V native, own fused branch)
        └── Victron Orion-Tr 48/24-16A (isolated) ── Blue Sea 5026 24 V block
                                                        ├ fridge (24 V native)
                                                        ├ LED zones, USB-C PD, GPS
                                                        └ winter heater outlet (exterior)
```

**Why 48 V:** the two biggest loads — the Velit air conditioner and the inverter — are 48 V-native, and at 48 V the cables stay small. **Why a single 24 V house bus and no 12 V rail:** every chosen house load is 24 V-capable (fridge auto-senses 12/24, Yuji LED strips are 24 V, the Scanstrut USB-C takes 24 V in), so a second 48→12 converter would add a conversion stage, a quiescent draw, and a parts family for nothing. The rare 12 V-only stray gets a point-of-load (POL) 24→12 buck — a small DC-DC converter at the device, not a second house rail. The panel ruled this unanimously (D006).

**Why this AIO:** the original LiTime 5 kW unit had a 120 V MPPT floor; LG455 3S is already ~118.8 V at NMOT and drops lower on a hot playa roof. It went back. The **3500 W** unit remains the right inverter/charger for one 48 V 100 Ah ComFlex pack; the corrected 3-panel run revised the **solar** topology instead: roof 3S goes through a separate 250 V-class MPPT, and the AIO's own PV input is reserved for an optional deployable 2S ground pair. See the corrected [3-panel AIO verdict](../runs/aio-adversarial-3panel/synth/VERDICT.md).

### 48 V stack (settled)

- **AIO — "all-in-one": MPPT solar charge controller + inverter + battery charger in one box. This one: LiTime 48V 3500W** ([specs](reference/litime-48v-3500w-aio-specs.md) · [manual](manuals/litime-48v-3500w-inverter-charger-manual.md)) — PV 60–145 V operating / 60–115 V recommended, 4400 W / 50 A max; AC out 3500 W continuous, 6000 W / 5 s surge; no-load draw <50 W (<30 W in ECO); ~75 A max battery draw. Its PV input is **not** the roof input anymore; it is the optional deployable 2S ground input. **Commissioning: cap combined charge current ≤100 A** across the AIO and the SmartSolar (the ComFlex's continuous limit). ECO/off discipline when idle — the idle draw is a real line in the energy budget.
  - **Cold floor `[web-val]`: the AIO is rated to −10 °C, and that — not PV Voc — is the binding cold limit.** It lives in the conditioned nose cabinet, which keeps winter operation on the table.
- **Roof MPPT: Victron SmartSolar MPPT 250/60-Tr** ([specs](reference/victron-smartsolar-mppt-250-60-tr-specs.md)) — dedicated to the roof 3S string. 250 V-class PV ceiling gives cold-Voc margin; start/track threshold is compatible with hot 3S Vmpp. Requires its own DC-rated roof PV disconnect and battery-side output fuse/breaker.
- **Battery: LiTime 48V 100Ah Smart ComFlex** ([specs](reference/litime-48v-100ah-battery-specs.md)) — 5.12 kWh, ~97 lb, 100 A continuous, Bluetooth BMS. Mount **low and centered** (single-axle tongue-weight sensitivity).
- **Instrumentation & protection:** LiTime 500A Bluetooth shunt (single-point ground lives here), ANL 250 A fuses (bolt-down high-current fuse format) on the main run.
- **Location:** AIO + battery + SmartSolar + converter + distribution all live in the **nose cabinet** (the interior nose trapezoid). **Ventilate the cabinet** — the AIO's ceiling is 131 °F and the SmartSolar/Orion-Tr add waste heat; this same plume is why the fridge bay must stay away from the nose.

### Solar (resolved — D002 revised)

**Panels: 4 × LG455N2W-E6 on hand** (455 W, 83.07" × 41.02" × 1.57", 48.5 lb; Vmpp 42.1 V — voltage at max power; Voc 49.9 V ±5% — open-circuit voltage, the cold-morning worst case; [datasheet](reference/lg455n2w-e6-datasheet.md)). **Three live on the roof permanently.** The fourth stays home as a spare unless a fifth current-compatible panel is bought to make a real deployable 2S ground pair.

- **Roof: 3 panels in series — "3S", 1365 W — into the Victron SmartSolar 250/60-Tr only.** STC Vmpp 126.3 V; NMOT Vmpp ~118.8 V; hot-roof Vmpp roughly ~105–115 V; cold Voc signal ~163–171 V with tolerance/cold correction. This is invalid on the LiTime AIO but comfortably inside a 250 V-class MPPT.
- **NEVER 3S into the LiTime 3500 W AIO.** Three panels in series exceed the AIO's 145 V PV max in cold conditions, and owner reports already make that rail look touchy. Physically segregate and label the two PV paths: roof 3S terminates only at its own disconnect → SmartSolar; the exterior deployable inlet wires only to the AIO.
- **Do not chase 3S with a 120 V-min high-voltage AIO.** The LiTime 5 kW / EG4 class wakes on a 120 V MPPT floor while LG455 3S sits at or below that floor under NMOT/hot-roof conditions. The corrected panel run classifies that as a reliability problem, not acceptable clipping.
- **Optional camped ground: a 2S deployable pair can feed the AIO's MPPT.** With the current four-panel inventory, that requires buying/borrowing a fifth current-compatible panel because panel #4 alone is electrically homeless on a 48 V bank. Hardware: weatherproof exterior inlet dedicated to the AIO, DC-rated disconnect, 10 AWG extension run, and guy/anchor hardware. **Never combine roof 3S and ground 2S on one tracker.**
- **Mounting:** three landscape rows on rails/tilt/Z-brackets, fastened **through the 24"-OC steel roof bows** (never skin-only), bedded in butyl tape (non-hardening sealant) with Dicor — self-leveling lap sealant — over the fastener heads. If the SmartSolar path slips, fall back by wiring two mounted roof panels as 2S into the AIO and parking the third panel until the controller is installed.
- **Roof fit — MEASURED ✓ (2026-06-04) + corrected premise:** width **84-7/8" rail-edge to rail-edge with minimal crown — landscape rows fit** with ~0.9" per side to spare. That margin means **under-panel feet/rails, not side clamps.** Rectangle length **145.5"**: three panel rows take ~123", leaving ~22" of measured rectangle plus the nose; the corrected premise places the **Velit 2000R AC in the nose section**. The **roof drawing** (design-freeze item 5) still has to lock bow stations, Velit opening + shadow line, awning standoff stations, and exact panel-foot layout.

### 24 V house bus — D006

- **Converter: one Victron Orion-Tr 48/24-16A isolated** (380 W), in the nose cabinet, with its **remote on/off wired to a cabin toggle** so the whole house bus can be killed without opening the cabinet. The budget alternate considered was the Mean Well RSD-500C; the Victron won on reputation, isolation, and the remote pin.
- **Sizing honesty:** 16 A is sized for the **current** loads — realistic simultaneous worst case ~12–15 A (fridge 4.6 A + a lighting zone near its 5 A branch + USB-C PD at full profile). It is **not** sized for the winter heater:
  - **Converter stack check (heater now in the calc):** fridge 4.6 + lights 2–3 + **N4 glow up to ~11 A** ≈ **18–19 A worst case vs 16 A**. Winter operation therefore requires **glow-window load-shedding** (lights off for the 2–3 min glow) or a **parallel second Orion-Tr**. The bench-measured glow current decides which; **July is unaffected.**
- **48 V-side protection:** Blue Sea 7443-class 20 A UL-489 breaker (UL-489 = real branch-circuit breaker standard, not a supplemental protector; 80 V-class) ahead of the converter. **No 32 V automotive fuse gear anywhere on the 48 V side** — automotive ratings are meaningless at 51–58 V. Required engineering outputs for the install: feed-conductor ampacity, converter output OCP (overcurrent protection), breaker DC interrupt-rating sanity against pack fault current, and a correctly rated dedicated fuse/breaker on the Velit's 48 V branch.
  - **`[web-val]`:** the UL-489 / 80 VDC / 10 kA AIC (ampere interrupting capacity — the fault current it can break without welding shut) class is confirmed appropriate (clears the 5 kA-per-100 Ah guidance of ABYC — the American Boat & Yacht Council, the de facto mobile-DC standard — by 2×). Two follow-ups before ordering: **(1)** make the **battery-terminal main OCP explicit** — a Class-T fuse (the fast, high-interrupt class that's standard practice on lithium banks) at the battery, *or* document the close-mounted breaker as the main OCP; **(2) verify the exact Blue Sea SKU** — these docs say "7443" but the 20 A / 80 V UL-489 part that surfaced is **7463** (7465 = 30 A). Also: every 24→12 V POL buck needs its own DC-rated input OCP on the ~29 V rail (again, not 32 V automotive gear at the margin).
- **24 V distribution: Blue Sea 5026 fuse block.** The rail map:

  | Branch | Fuse | Wire | Notes |
  |---|---|---|---|
  | Fridge (CFX3 95DZ) | 10 A | 14 AWG | 24 V native, 4.6 A draw; verify <3 % round-trip drop |
  | LED lighting zones (Yuji high-CRI strips in Klus aluminum channel + diffuser) | 5 A per zone | — | dimmed; zones rather than one string |
  | Scanstrut SC-USB-F3 (USB-C PD) | 7.5 A | — | 24 V in → full 60 W profiles |
  | LandAirSea 54 GPS | 3 A | — | hardwired, always-on (security) |
  | Door switch | — | — | dry contact |
  | **Heater outlet (winter)** | **15 A** | **12 AWG** | exterior-reachable; N4 glow est. 4–11 A, run ~1–2 A |
  | Stray 12 V-only fixtures | per-device | — | point-of-load 24→12 bucks, each with DC-rated input OCP |

- **The tow vehicle's 12 V (7-way: running/marker/brake) is never a house load** — fully isolated systems. Single-point ground at the shunt.

### Truck charging (deferred — pre-wire now)

Charging from the F-150 while driving is a later phase, but the copper goes in while the walls are open: **4 AWG run + Anderson connector (high-current quick-disconnect) at the tongue.** The future charger is a ~480–600 W 12→48 V DC-DC, ignition-gated so it can never flatten the truck battery.

### Energy budget (July, camped)

| Load | kWh/day |
|---|---|
| Fridge (CFX3 95DZ, desert duty) | 1.0–1.3 |
| AIO idle, ECO discipline | ~0.7 |
| Velit AC at realistic duty | ~2.4 |
| **Total** | **≈ 4.1–4.45** |

Roof-only solar makes ~4.0 kWh/day in July — **break-even at best on AC-heavy days.** Conclusion: **the deployable ground pair is required margin, not a nice-to-have**, and the ECO/off discipline stands. (Lighting/USB are noise against these three.)

---

## Climate / envelope

The envelope strategy: **closed-cell spray foam inside the steel skin, elastomeric coating outside on the roof, three operable windows for cross-flow, a 48 V rooftop AC for July, ducted diesel heat for winter.** July needs cooling and airflow; heat is deliberately deferred (D003) because mild playa nights don't justify carrying the install risk into the deadline.

### Insulation & roof (settled)

- **Closed-cell spray foam** in the wall and ceiling cavities; **elastomeric roof coating** outside; **Velit Mini 2000R rooftop AC (48 VDC) — ordered**, fed by its own fused 48 V branch.
- **Roof sandwich `[web-val]`:** building science *endorses* foam-inside + coating-outside on steel, **on one condition: the steel is dry, clean, and rust-free at closure** — foam over damp steel seals the corrosion in where it can never be seen. Execution requirements: air-seal the foam at every bow, fastener, and penetration; **spec a cold-rated/silicone coating** (standard summer-cure acrylics go brittle in deep cold and "zipper" off); run a **48-hr adhesion patch** on the actual galvanized/aluminized skin before committing to a product; confirm foaming under the roof doesn't void the solar-panel warranty; put periodic exterior blister inspections on the maintenance calendar (a blister is the only visible symptom of hidden steel corrosion).

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
- **Clamp-ring vs wall build-up `[web-val]`: the RecPro trim ring is a single 1.5" spec, not a range.** The built-up wall (steel skin + PlexCore substrate + FRP — fiberglass-reinforced plastic, the wipe-clean interior skin) lands ~1"–1.4" — **it won't clamp tight as-is → fur the window openings up to 1.5"** (this step now lives in the wall plan).
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

**Fiamma F45s 350** (**06290B01R — Titanium case / Royal Grey fabric, manual**): 138" (11'6") case, 5.35" tall, ~55 lb, 130" canopy. The July deliverable for shade. **ORDERED 2026-06-05 — Campervan HQ** (Portland, OR; free LTL freight, ~2–3 wk → ~late June, confirm tracking).

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

Two configurations share one floor: **moto mode** (both bikes in, gear on the walls) and **camp mode** (bikes out, bed deck on the wall tracks). Everything below is a module on the E-track grid.

### Bikes & floor E-track

- **WR250R + CRF450RL (~590 lb pair), side-by-side, nose-forward, on the roadside half**, in staggered chocks (12–18" stagger so the bars interleave). Flush-recessed floor E-track bolted through to steel; the 4 factory D-rings get reused as backup tie points.
- **⚠ Floor plan rework gate:** the original ~24" centerline spacing **fails** — cross-exam found ~9" of handlebar interference, and the 2"×4" main rails run at the **perimeter** (not under the centerline), while a ½"-recessed track leaves only ~¼" of ply between crossmembers. The row positions must be re-derived against **measured** steel locations (row 10) + actual bar widths (row 11).
- **Aisle reality:** the nominal ~30" walking aisle shrinks to **~20" effective at bar height** — fridge access and egress are planned around that, not the floor-level number.
- **E-track footage: ~73 ft needed vs ~60 on hand — order more.** (~Six 10-ft black sections believed ordered; confirm before the freeze.)

### Flooring — D010 (accepted)

**Committed recommendation: Durabak-18 Outdoor Textured, light grey — ORDERED 2026-06-05, delivery window June 12–15, 2026.** It is a flexible polyurethane bed-liner coating rolled/brushed onto the ¾" PlexCore floor, the rear ramp deck, and **coved 3–4" up the lower walls before the FRP lands**. FRP laps over the cured cove, turning the floor into a hose-out tray; raise the tongue jack to sluice dust and wash water toward the rear ramp. The remembered "DuraLok" name is not the spec.

Why this replaces the old rubber-coin lean: common coin roll is usually SBR (styrene-butadiene rubber), and SBR is a poor fit for moto fuel/oil spills. A bonded polyurethane liner avoids the under-sheet playa-dust/water trap, keeps the floor seamless, and stays much lighter than a thick loose rubber mat. Do not use a rigid garage epoxy; the single-axle trailer floor will move.

**Web-validation correction:** say **fuel/oil spill-resistant, clean promptly**, not "fuel-proof." Durabak's product data supports a flexible, one-part, non-slip polyurethane coating; Durabak's wood-prep guidance warns that sanded wood dust causes delamination and calls for a patch test; Raptor's 2K polyurethane data validates the class on stable wood and shows diesel/hydraulic-oil resistance, but gasoline/petrol is listed as splash-resistant rather than immersion-proof. The build therefore requires a PlexCore adhesion patch and a small gasoline/diesel drip patch before coating the whole floor.

**Adversarial review:** [floor-coating verdict](../runs/floor-coating-adversarial/synth/VERDICT.md) considered Durabak, Raptor, Herculiner, Rust-Oleum, TotalBoat TotalTread, KiwiGrip, Pettit EZ-Decks, Interlux Interdeck, Tuff Coat, G-Floor, and Monstaliner. It keeps Durabak as the default because light grey, one-part DIY control, cove execution, and truck-bed-duty polyurethane fit beat the cheaper alternatives for this trailer; Raptor remains the tested fallback.

**Raptor schedule override closed:** owner checked local availability and shippers on 2026-06-05; the acceptable 2K tintable light-gray Raptor path has no local availability or reliable ETA, so it provides no schedule benefit over Durabak and keeps all of the 2K downsides. Raptor remains only a patch-failure fallback. If reopened, acceptable color is Raptor Color **Light Gray** (UP4855) or a matched solvent-based urethane/acrylic automotive toner in the same light-gray range, mixed per Raptor's tint guidance. White is technically acceptable but too glare/stain-prone to prefer; Basalt Gray, black, and the AutoZone-visible black 2K kit are not acceptable as the main floor color. Do not substitute the 1K aerosol or 1-part roll-on Raptor products for the 2K fallback.

**Quantity:** buy **4 gallons**: 3 gal for the base floor+cove+ramp coat plan, plus 1 reserve gallon committed to a third coat in the wear lanes (rear ramp deck and chock/E-track contact lanes). The interior floor is bounded by 81" × 157" (~88 ft²), the 3–4" wall cove adds ~12–14 ft², and the 78" × 72" ramp adds ~39 ft². Durabak textured coverage is ~50–60 ft²/gal for a standard two-coat application, so 3 gal is adequate but tight once the ramp and tie-down lanes get extra film; confirm final quantity against the patch-test coverage rate before order freeze.

**Install sequence:** finish the floor E-track layout first, then recess and bolt the floor E-track through to steel. Mask the E-track slots, fastener heads, D-ring pockets, ramp hinge/transition hardware, and any drain/edge details so fittings stay usable and hardware remains inspectable. Sand the PlexCore, vacuum hard, remove dust per the coating instructions, run the patch tests, coat the floor plus cove plus ramp, add the third wear-lane coat, cure fully, then land the FRP over the cove. If Durabak fails the patch, use a Raptor-class flexible polyurethane with the correct wood prep; if coating fails entirely, the only acceptable roll fallback is **fully glued G-Floor PVC trailer flooring**, not loose-lay.

### Bed & wall tracks

- **Bed row at ~27", shelf row at ~60"**, both lag-backed into the 16"-OC tube posts.
- **Why 27" (revised from 34", owner challenge upheld):** at 34" the sleeping surface (~38.5" with platform + pad) left **1–3" of seated headroom** under the 78" ceiling for a 6'+ adult; at 27" (surface ~31") it's ~46" — you can actually sit up in bed. Bikes are out in camp mode, so nothing needs the taller under-deck clearance. **Gate: mock a 31" surface and sit-test before drilling** (design-freeze item 3).
- **Bed shoring:** E-track sockets taking plain 2×4 lumber — legs under the deck when slept on, gone in moto mode.

### Fridge bay

- **Curbside, immediately aft of the personnel door**, fridge E-track-strapped. Footprint 37.9" × 20.9" × 18.6" tall **plus lid-swing clearance — verify which way the split lids hinge before fixing the bay's wall orientation.** The location survives: outside reach under the awning, lid access in both modes, clear of the door swing.
- **⚠ Thermal gate — HARDENED `[web-val]`:** the Dometic manual requires a **50 mm (~2") gap on all four sides** and flatly says **"do not place the cooling device in closed compartments."** An enclosed bay is non-compliant as worded. So: **the bay gives 50 mm all-sides clearance + forced through-flow ventilation** — "shaded" alone doesn't cut it. Then field-verify in-bay air temperature under desert sun with the awning out: **<43 °C (110 °F) to run at all, <30 °C (86 °F) to hold both dual-zone setpoints.** Keep the bay off the nose-cabinet heat plume. (Dometic error codes: Warning 34 = high ambient / blocked vent; Warning 33 = low supply voltage — see Systems for the wiring check.)

### Walls — D009 (proposed)

**Pull the factory PlexCore while the walls are open for foam; reinstall it (BC-pine fallback) and laminate FRP over it in place — screwless finish, no paint.** *(Evolved 2026-06-05 from the original "buy 3/8" birch + FRP": the factory board turned out to be moisture-resistant PlexCore, better reused than replaced — see Substrate sourcing below.)*

- **Why:** the foam job already has the walls stripped — the swap is nearly free labor. 3/8" matches the factory skin thickness, so the wall-sandwich geometry (window clamp range, door reveals) doesn't move. Ply holds screws and FRP adhesive far better than OSB.
- **Substrate sourcing (updated 2026-06-05 — reuse the factory PlexCore):** the factory wall/floor board is **PlexCore — a "special OSB": moisture-*resistant* engineered strand board** (upgraded resins/compression + a harder, smoother face; Wells Cargo/Haulmark, GP DryMax class — owner confirmed off the product sheet). It comes off for foam anyway, so **reinstall it as the FRP substrate**: free, pre-cut to the geometry, and **better-suited to the sealed FRP+foam sandwich than birch** (engineered to tolerate moisture; birch rots readily). This **supersedes the original "buy 3/8" birch over commodity OSB" premise — likely no wall substrate to buy.** Caveats: **scuff-sand + patch-test the FRP-adhesive bond** (the hard face may resist grip); reinstall intact, **seal old fastener holes/wiring cutouts**, cut out any swollen/damaged spots; it's still wood-strand (*resistant, not proof*) so keep the unpenetrated-FRP + sealed-edge mitigations below.
- **Fallback substrate (only for PlexCore sheets that tear up on removal):** **3/8" BC sanded pine, Exposure-1/exterior glue** (Home Depot **Plytanium 721715**, 11/32"≈3/8"; sanded B-face toward the FRP). **Not** the *pressure-treated* BCX (FRP won't bond) and **not** Sande ply (interior glue). The on-hand birch is a single interior-grade sheet — **not wall-eligible** — so route it to a **visible, dry interior fixture** (nose-cabinet face/shelving), not the walls.
- **Thickness ruling:** **3/8" for the walls.** 1/4" rejected — flexes between the 16"-OC posts and thins the window clamp sandwich. **Nicer interior-grade birch (incl. the on-hand sheet) goes to interior fixtures** (fridge-bay partition, shelving), not walls.
- **Install method — laminate in place for a screwless finish (owner, 2026-06-05):** **screw the 3/8" substrate panel (reused PlexCore / fallback BC pine) to the posts first, then laminate the 0.090" FRP over it in place.** The fasteners are captured under the FRP, so the **interior shows no screws** *and* the **FRP membrane is never penetrated — no screw holes through the moisture seal** (a direct win on the drying-path hazard below). **Countersink/set the screw heads flush** so they don't telegraph as dimples through the thin FRP; bond with notched-trowel FRP adhesive (Titebond GREENchoice Fast Grab 4059) and roll out. *One-piece faced FRP-plywood (NuFiber-type) was considered and set aside* — it keeps a wood core anyway, isn't a Home Depot shelf item, and forfeits the cheap 0.090" trim ecosystem; DIY lamination is cheaper, HD-sourced, and yields the same screwless result.
- **`[web-val]` — moisture is the real hazard:** impermeable FRP on the inside + <1-perm closed-cell foam on the outside leaves the ply **no drying path** in a box that isn't climate-controlled year-round (the one birch "precedent" the build had cited turned out to be a condensation-failure story). Mitigations are mandatory, not optional: **a fully waterproof (exterior/WBP) glue line is the gating spec — not interior-glue birch** (verify the on-hand sheets; much cabinet-grade Baltic birch is interior-glued and would fail here). *Marine grade* is the same waterproof glue **plus a void-free core/better veneers** — a step better but **neither grade is rot-proof** (both are still wood), so reserve true marine/void-free for the highest-wetting zones (**lower-wall cove/floor junction, window cutouts**); the unpenetrated laminated-in-place FRP + sealed edges are the real defense, the ply grade the second line. **Seal every FRP seam/edge and the window clamp sandwich** so liquid water never reaches the cavity; **confirm the chosen FRP brand** (Crane/Marlite/Glasbord) **warranties application over the chosen substrate** (the PlexCore face, or the BC-pine fallback) **with the chosen adhesive** — and that the glue-line/marine notes above govern the fallback ply, not the reused PlexCore. Note 3/8" sits near the structural floor (7/16" @ 16" OC) — stiffness leans on the bonded FRP composite, so the lamination must be sound.
- ¼" XPS (rigid extruded-polystyrene foam board) goes behind the bed zone only (back insulation against the cold wall). All backing plates go in **before** finish.
- **Gates:** confirm the factory PlexCore thickness ≈3/8" (row 19 — material confirmed) · **scuff + patch-test the FRP-adhesive bond to the PlexCore face** (decides reuse vs BC-pine fallback) · D009 ratified **before any window RO is cut** (the row-12 clamp check depends on the final sandwich) · FRP trim system selected (design-freeze item 9).

### Ceiling substrate — FRP over ply, laminated in place (proposed 2026-06-05)

**Same system as the walls:** screw the ply to the 24"-OC bows, then laminate the FRP over it → screwless finish, unpenetrated FRP membrane.

- **Thickness — 3/8" here too.** The **24"-OC bow spacing is wider than the 16"-OC wall posts**, so 1/4" is prone to oil-canning/sag overhead; the ~1/8" headroom saving isn't worth a wavy ceiling. (1/4" is viable *only* with one mid-span furring run to halve the span. The bonded FRP adds composite stiffness either way.)
- **Headroom:** 78" is to the **bow underside**, so finished ceiling ≈ 78" − (ply + FRP + any AC/wire drop). Carry the *finished* number into the bed sit-test (track-heights item 3), not 78".
- **Moisture — extra care overhead:** the ceiling is the #1 condensation surface, so the D009 mitigations apply harder — **exterior/marine-glue ply, sealed edges/seams.** The in-place lamination (no screw penetrations through the FRP) helps here too.
- **Decide stands before foam** (sequence step 5): the bow-mount method sets what installs when.

### Stairs & panel transport

- **Entry: folding/telescoping aluminum RV step**, stowed on the E-track grid (no permanent step).
- **Panel transport slot:** the ground-pair LG455s are 83" long vs the **81" interior width** — they ride **lengthwise** in a padded E-track wall slot. (One more reason the interior-width tape measurement matters: row 3.)

---

## Systems / gear

### Fridge — D008

**Dometic CFX3 95DZ (purchased)** — 95 L dual-zone, 12/24 VDC compressor, 24 V @ 4.6 A, 66.4 lb ([specs](reference/dometic-cfx3-95dz-specs.md)). Runs **native 24 V** off the 5026 — zero conversion stages between battery and compressor.

**`[web-val]`:** the electrical sizing is sound and conservative — 10 A fuse ≈ 2× the 4.6 A draw; the VMSO3 compressor (Dometic's variable-speed unit) soft-starts (no meaningful inrush); 14 AWG is well-protected. Two checks remain: verify the 14 AWG round-trip **voltage drop stays <3 %** so the fridge never sees its low-voltage cutoff, and check the unit's build date against the **Nov 2019–Jun 2020 recall window**. The real risk on this fridge is the bay thermal gate (Interior section), not the wiring.

### Security & tracking

- **Proven 2516 coupler lock** + **2× Abloy/Paclock pucks, keyed alike** + **Trimax TCL65** wheel lock — layered, because Juplaya.
- **LandAirSea 54 GPS**, hardwired to the 24 V block (3 A branch), always-on.

### Order list

- **Long-lead, order now:** Fiamma F45s 350 (**06290B01R Titanium**) — **ORDERED 2026-06-05 (Campervan HQ)** · Tie Down S + lag anchors/deadman bags · Victron Orion-Tr 48/24-16A · **Victron SmartSolar MPPT 250/60-Tr + 250 V-class roof PV disconnect/OCP** · the 48 V-side UL-489 breaker (**verify SKU: 7463 vs "7443"**, web-val) · standoff + backing steel stock (owner fab) · E-track top-up.
- **Coatings:** Henry 887 Tropi-Cool White 100% Silicone Roof Coating (HE887HS018, 4.75 gal pail) + Henry 884 Tropi-Cool silicone sealant · **Durabak-18 Outdoor Textured light grey, 4 gal — ORDERED, delivery June 12–15, 2026** (3 gal base floor+cove+ramp + 1 reserve for ramp/chock/E-track wear lanes).
- **Accessories:** Blue Sea 5026 · Scanstrut SC-USB-F3 · LandAirSea 54 · locks (above) · 14 AWG runs + fuse assortment + 2–3 POL 24→12 bucks · dome/task lights (24 V or POL).
- **Wall/ceiling finish (FRP, DIY laminate over 3/8" ply):** Glasliner 0.090" white FRP 4×8 (Home Depot, MFTF12IXA480009600) — **~3 sheets for the ceiling + wall count from the freeze** · Titebond GREENchoice Fast Grab FRP adhesive (4059, 3.5-gal pail) · HD PVC FRP trim — division bar `9290NL`, inside corner `9350NL`, outside corner `99400NL`, end cap `9460XA` + color-matched silicone · **substrate = reuse the factory PlexCore** (special moisture-resistant OSB; scuff + patch-test the FRP bond) — **3/8" BC sanded pine (HD Plytanium 721715) only as fallback** for sheets damaged on removal; optional true-marine only at the cove/window cutouts (lumberyard).
- **Windows:** 2× RP-FRMWIN-1222-TRM + 1× RP-FRMWIN-2015-TRM (placement decided — Climate section).

---

## Build sequence (dependency order)

The design freeze (below) gates step 3 onward. Within the sequence, **"while the walls are open" is the critical window** — five different systems need it.

1. **Measure & scan** — finish the [measurement pass](dimensions.md): interior tape (rows 3/3a, 7, 14, 17), roof stations (5a, 6), rail 3D scan + post wall thickness (16), floor steel + bar widths (10, 11), OSB thickness (19).
2. **Freeze** — close the 10 design-freeze items; ratify D006–D009; D010 is accepted; place remaining orders (long-lead first).
3. **Strip the interior** — factory PlexCore off and **set aside for reuse** as the FRP substrate (or template for any BC-pine fallback cuts); document factory wiring as found.
4. **Everything that needs open walls / bare roof:**
   - Awning standoff fasteners + any backing into the posts (≥2 per upright).
   - Window-bay furring (build openings out to the 1.5" clamp spec) + backing.
   - E-track backing at the 27"/60" rows.
   - Rough-ins: HRV 4" pair, heater 3" duct ports, wire chases, 4 AWG tongue pre-wire.
   - Roof: Velit opening cut + curb, panel rail feet through the bows, all penetrations sealed.
5. **Foam** — steel verified dry/clean/rust-free; every penetration already made (foam after cutting, never before); air-seal at bows/fasteners.
6. **Roof coating** — Henry 887 silicone, after the 48-hr adhesion patch passes.
7. **Floor liner + walls closed** — floor E-track recessed/bolted through to steel first; Durabak-18 floor+cove+ramp applied and cured; the 3/8" substrate (reused PlexCore / BC-pine fallback) + FRP land over the cove, seams/edges sealed, trim on.
8. **Window cuts + install** — after the row-12 clamp check against the real sandwich; door window gets perimeter re-framing.
9. **Tracks & remaining floor hardware** — wall E-track rows on the posts; floor E-track masks pulled and slots/hardware inspected.
10. **Nose cabinet** — battery, AIO, SmartSolar, shunt, breaker, Orion-Tr, 5026; rail wiring out to branches; cabinet venting.
11. **Systems** — fridge bay (50 mm clearance + through-flow), lights/USB/GPS, awning case onto the standoffs, tie-down anchors.
12. **Weigh & commission** — scale (curb + tongue, row 18); combined charge-current cap ≤100 A; verify roof 3S lands only on SmartSolar and optional ground 2S lands only on the AIO; shakedown camp before Juplaya.

---

## Design freeze — definition of done

**The design is DONE when every row below is checked.** Then the build phase starts (sequence above). Each row names what closes it.

| # | Item | Closes when | Status |
|---|---|---|---|
| 1 | **D006–D008 ratified** (24 V bus · awning standoffs · fridge integration) | owner ratifies in the DECISION_LOG | ☐ |
| 2 | **D009 wall/ceiling substrate** — reuse factory PlexCore + laminated FRP (BC-pine fallback) | owner ratifies + PlexCore thickness verified + FRP patch-test passes (row 19) | ☐ |
| 3 | **Track heights final** — bed ~27", shelf 60" | 31"-surface mock sit-test passes; shelf checked against the 36–58" window band | ☐ |
| 4 | **Window locations final** — exact bay stations, both walls + door | clear bay at chosen stations (row 7) + RecPro ROs (row 13 ✓) + clamp range vs substrate+FRP build-up (row 12) + door frame (row 14) | ☐ |
| 5 | **Roof drawing** — three panel rows/feet, Velit nose station + opening/shadow line, standoff stations on the measured 84⅞" × 145.5" field | rows 5a, 6, 15 measured and drawn | ☐ |
| 6 | **Awning standoff design** — section + fasteners | rail 3D scan + post tube wall thickness (row 16) → drawn part, ≥2 fasteners per upright | ☐ |
| 7 | **Floor plan final** — bike stagger, fridge bay, E-track rows | floor steel + bar widths + bay depth measured (rows 10, 11, 17) | ☐ |
| 8 | **Flooring material** | D010 accepted: Durabak-18 Outdoor Textured light grey, 4 gal ordered for June 12–15 delivery; PlexCore adhesion + fuel-drip patch required before coating | ☑ 2026-06-05 |
| 9 | **FRP trim system** | corner/seam/edge/reveal profiles + adhesive picked (color-matched vinyl moldings; FRP adhesive bond confirmed on the PlexCore substrate via patch-test — web-val). **Candidate set:** HD Glasliner PVC trim (division bar 9290NL / inside 9350NL / outside 99400NL / end cap 9460XA) + Titebond Fast Grab 4059 — laminated in place over the screwed-down 3/8" substrate (screwless finish) | ☐ |
| 10 | **Order list frozen** — every SKU (incl. the SmartSolar 250/60-Tr + 250 V-class PV disconnect/OCP, 7463-vs-7443 breaker check, Henry 887/884, Durabak quantity) + E-track footage recount | rows 1–9 closed | ☐ |

Post-freeze (build-phase, not design): fridge-bay ventilation check + lid hinge orientation · deployed-fabric vs open-door at pitch · **curb-weight weigh-in** (row 18).

## Interior footprint — measured (owner tape, 2026-06-05)

The owner tape-measured the **interior floor footprint** and sketched it ("structure layout"). Redrawn (plan view, not to scale) at [reference/structure-layout.svg](reference/structure-layout.svg); full numbers in the [dimension sheet](dimensions.md#interior-footprint--measured-2026-06-05-owner-tape). **This is the tape pass that closes measurement rows 3/3a** and supersedes the rejected magicplan scan.

- **Confirms spec:** **81" W** (varies 81" to 81-3/32" along the length) × **156" L** (rear → nose tip; spec was 157") × **78" H**.
- **Headroom caveat:** the **78" is to the underside of the steel roof bows**, not the finished ceiling. **Finished headroom = 78" − ceiling build-up** (ceiling panel + any furring/wire-or-AC drop). This tightens the bed sit-test (track-heights item 3) and any standing-height claim — carry the *finished* number, not 78".
- **V-nose, plan view:** straight side walls **141"** (rear → taper start), then a symmetric V-nose **~15" deep** to a **13" flat tip**; nose walls **~43" each** (the eyeballed 42"/43" pair resolved equal — they compute to ~43" from the reliable 81"/156"/13" numbers).
- **Personnel door:** curbside wall, ~**98"** forward of the rear wall, swing shown (the 30° arc is the door swing).

> Treat **81"** as the design width (the ~3/32" variation is within tolerance — watch the tight side for the 83" panel-transport slot and any full-width module). The nose-wall length and door station are derived/eyeballed — re-confirm on the next tape pass. This footprint is distinct from the design-freeze **roof drawing** (item 5), which lays panels/AC on the 84⅞" × 145.5" *exterior* roof field.

## Weight

**GVWR 3,500 lb** (gross vehicle weight rating — confirmed). Payload = 3,500 − actual curb; **the trailer will be weighed** rather than estimated — no paper weight budget. Single axle is nose-sensitive: load to ~**10–12 % tongue weight**, battery low and centered, bikes' mass forward of the axle.

## Standing preferences (for whoever picks this up)

- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
