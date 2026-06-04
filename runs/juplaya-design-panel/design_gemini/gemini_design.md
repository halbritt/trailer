---
author: operator
---

# Design pass — Gemini lane (third and final full pass)

## Posture: Devil's Advocate, Spec Falsification, and Physical Integration

This is the third and final pass in the design relay (Claude → Codex → Gemini). I carry forward the core architecture of the single 24 V house bus and the deletion of the central 48→12 V converter. However, I identify and correct major integration errors in both predecessor passes:
1. **The Fridge:** Falsified both predecessor fridge choices (ICECO VL60 and Dometic CFX2 57). The owner has **already purchased** the Dometic CFX3 95DZ (95 L dual-zone) as an accepted fact (D005). Re-recommending other units is a failure to respect settled project constraints. I integrate the actual owned unit.
2. **The Awning Mount:** Falsified the wall-mount recommendation above the curbside personnel door. The 78" wall height and 72" door frame height leave a 6" margin, which is further reduced by the door frame trim (to 4.5"). A 5.35" high wall-mounted Fiamma case would physically block the door frame. Furthermore, when deployed, the sloping fabric would obstruct the outward door swing. I resolve this with a roof-mount strategy.
3. **The 24 V Converter:** Replaced the industrial, open-terminal Mean Well RSD-500C-24 converter with the RV-optimized, enclosed **Victron Orion-Tr 48/24-16A (380W) Isolated** converter to enable safe remote switching and clean installation.

---

## 1. DC House Bus
**Committed Recommendation:** Run a **single regulated 24 V DC house bus** off **one Victron Orion-Tr 48/24-16A (380W) Isolated DC-DC converter**. Delete the central 48→12 V house converter and the 12 V fuse block. Protect the converter input with a **Blue Sea 7443 20 A UL-489 DC breaker (80 V rated)**. Distribute 24 V power via a **Blue Sea 5026 12-circuit ST Blade fuse block**.

### Why the Victron Orion-Tr over the Mean Well RSD-500:
* **Remote On/Off switching:** The Victron Orion-Tr features a low-current remote on/off jumper. A thin 2-conductor wire can run from this jumper to a toggle switch in the cabin (near the entrance or bed), allowing the owner to switch off the entire 24 V house bus to eliminate quiescent draw during storage. The industrial Mean Well RSD-500 has no-load draw and requires a high-current switch on the 48 V input or a custom control circuit to turn off.
* **Enclosed, RV-Safe Design:** The Orion-Tr is fully enclosed with a mounting flange and covered screw terminals. The Mean Well RSD-500 has open screw terminals, which are a safety hazard in a moving cargo trailer unless mounted inside a secondary electrical enclosure.
* **Adequate Power capacity:** 16 A continuous at 24 V (380 W continuous, up to 430 W at 25 °C) provides a >60% safety margin over the peak simultaneous load: Dometic CFX3 95DZ (4.6 A compressing) + lighting (2 A) + USB-C PD (3 A) = 9.6 A.

### Falsifying the 48→12 V Converter:
All house loads are 24 V native, 12/24 V auto-sensing, or signal-level. The running, brake, and marker lights are powered by the tow vehicle's 7-way harness and must stay isolated from the house DC system. The factory 12 V dome light will be retired or run on a local $10 point-of-load (POL) 24→12 V buck converter. USB-C PD outlets (Scanstrut Flip Pro Max) run on 24 V, which is superior because it unlocks the 20 V/3 A (60 W) charging profile that is unavailable on a 12 V input.

### Rail Map:

| Load | Voltage | Implementation |
|---|---|---|
| **LiTime AIO / AC Out / Solar Charger** | 48 V (Nominal 51.2 V) | Directly connected to the battery stack via ANL 250 A fuse. |
| **Velit Mini 2000R AC** | 48 V (Nominal 51.2 V) | Connected directly to the 48 V battery bus with a dedicated inline fuse. |
| **Victron Orion-Tr 48/24-16A Converter** | 48 V Input / 24 V Output | Fused on the 48 V bus with a Blue Sea 7443 20 A breaker. |
| **Blue Sea 5026 Fuse Block** | 24 V | Fed from the Orion-Tr output; 32 V max block rating is safe on regulated 24 V. |
| **Dometic CFX3 95DZ Fridge** | 24 V | Connected directly to the 24 V fuse block (10 A fuse, 14 AWG wire). |
| **Yuji LED Strips** | 24 V | Connected to the 24 V fuse block via 24 V dimmers/zones (5 A fuse, 14 AWG wire). |
| **Scanstrut SC-USB-F3 USB-C Outlets** | 24 V | Connected to the 24 V fuse block; native 24 V input enables 60 W charging (7.5 A fuse). |
| **LandAirSea 54 GPS Tracker** | 24 V | Wired using the LandAirSea hardwire cable (6-24 V input) (3 A fuse). |
| **Door Switch** | 24 V | Dry contact switch routing 24 V signal to lighting controllers. |
| **Trailer Brakes & Running Lights** | 12 V (Tow Vehicle) | Powered exclusively by the F-150 7-way connector. Isolated from the house DC. |
| **Diesel Heater (Future)** | 24 V | Future heater will be a 24 V DC model, avoiding any 12 V rail requirement. |

---

## 2. Fridge Integration
**Committed Recommendation:** Integrate the **already purchased Dometic CFX3 95DZ (95 L dual-zone, 12/24 VDC)**, wired natively to the **24 V house bus**. Mount it **on the floor curbside, immediately aft of the 32"×72" personnel door**, secured to the floor E-track with heavy-duty straps.

### Why Predecessor Fridge Recommendations are Falsified:
* **D005 is Accepted:** The decision log states the owner purchased the Dometic CFX3 95DZ, superseding the 50-55 L recommendation. Recommending the CFX2 57 (Codex) or ICECO VL60 (Claude) ignores the physical reality that the owner owns this specific 95 L unit.
* **Energy Fit:** The CFX3 95DZ draws 4.6 A rated at 24 V (≈110 W while compressing). Daily consumption in July desert heat is estimated at **1.0–1.3 kWh/day**. Combined with AIO ECO idle (~0.72 kWh/day) and the Velit AC (~2.4 kWh/day), the total load is ~4.45 kWh/day. This is fully sustainable off the 5.12 kWh ComFlex battery with 910 W roof solar (~4.0 kWh/day yield) and easily cleared when the 1820 W 2S2P camped solar array is deployed (~8.0 kWh/day yield).

### Physical Integration & Bike Clearance:
* **The Dimensions:** 37.9" W (including handles) × 20.9" D × 18.6" H.
* **The Bike Interference Solution:** The WR250R and CRF450RL (~86" length, ~33" handlebar width) are loaded side-by-side, nose-forward, on the left (roadside) of the trailer. By **staggering the front wheel chocks by 12–18"**, the handlebars clear each other. Because the motorcycle bodies are only ~12-15" wide at their midpoints, they do not block the 20.9" deep fridge on the curbside. With the trailer's 81" interior width: `81" - 20.9" (fridge) - 15" (Bike 2 body) - 15" (Bike 1 body) = 30.1" of clearance` in the center aisle, ensuring the bikes easily clear the fridge.
* **Lid Clearance:** The CFX3 95DZ has a split top-loading lid. Placing it aft of the side door leaves the top completely clear of the 34" bed deck (which is assembled in the rear after the bikes are unloaded), allowing easy access. Its placement near the side door allows the owner to reach inside for drinks directly from outside the trailer under the awning.

---

## 3. Awning & Mount
**Committed Recommendation:** Install a **Fiamma F45s 350 (Polar White case / Royal Grey fabric, part 06280B01R)** manual winch cassette awning, **roof-mounted on the curbside edge** using **Fiamma Flat Roof Adapter Brackets (part 98655-316)** through-bolted into the steel roof bows (24" on center). Secure it on the playa using the **Fiamma Tie Down S Black kit (part 98655-133)** anchored to **3/8" × 12" steel lag bolts** driven into the hardpan with an impact driver.

### Falsification of Wall Mounting:
* **Door Frame Collision:** The interior height is 78" and the door cutout is 72" high. The door frame trim extends ~1.5" above the cutout, leaving only **4.5" of clear wall space** below the roofline. The Fiamma F45s case is **5.35" high**. Wall-mounting the case using standard brackets is mathematically impossible without overlapping and blocking the door frame trim.
* **Door Swing Collision:** If wall-mounted, the bottom of the awning case sits at 72.65" (78" wall height - 5.35" case). The 72" door swinging outward 180 degrees would strike the case (which projects 3.35" from the wall) and fail to open. When deployed, the sloping fabric of a wall-mounted awning would hang below 72" at the door's 32" swing radius, hitting the door panel.

### The Roof-Mount Resolution:
* Mounting the awning on the roof using the flat-roof adapters raises the bottom of the awning case to **~78.5"** (completely above the 78" wall line and 73.5" door trim). The door can swing a full 180 degrees flat against the trailer wall under the retracted case.
* When extended, the fabric starts at 78.5" and slopes down. Even at a 10-degree pitch, the fabric at 32" from the wall is at **72.9"**, allowing the 72" door to swing freely underneath it.
* **Co-existence with Solar:** The 2 × LG455 solar panels (41.02" wide) are centered on the roof bows, leaving `(84" exterior width - 41.02") / 2 = 21.49"` of clear space on both the curbside and roadside roof. The Fiamma F45s case is 3.35" wide and its roof brackets are 3.15" wide. Roof-mounting the awning on the curbside edge leaves an ~18" gap to the solar panels, eliminating all mounting and shading conflicts.

### Desert Tie-Down and Operating Discipline:
* Deploy the support legs vertically to the ground (never wall-foot mode).
* Clip the **Tie Down S** hooks into the front rail slot. Tension the heavy-duty straps to **3/8" × 12" steel lag bolts** driven into the playa hardpan. In soft silt, back them up with deadman bags.
* **Strict De-rig Discipline:** The awning is a sun shade, not a storm shelter. It must be wound in and locked before sleeping, leaving camp, or when wind gusts exceed 20 mph.

---

## 4. Doc Divorce Map
I execute the split of `docs/juplaya-trailer-context.md` into four domain files under `docs/build/` and a slim index file. No content is lost.

### Section-by-Section Migration Map:

| Section in Original Context Doc | Destination File | Notes |
|---|---|---|
| **Title, Target Date, Handoff Warning** | `docs/juplaya-trailer-context.md` (Slim Index) | Retained to frame the index. |
| **Settled / Trailer** | `docs/juplaya-trailer-context.md` (Slim Index) | Kept as core identity. Cross-links added to `fastrac-specs.md` and `wells-cargo-ft712s2-d-work-order.md`. |
| **Settled / Tow Vehicle** | `docs/juplaya-trailer-context.md` (Slim Index) | Kept as core identity. |
| **Settled / Power system (48V)** | `docs/build/power.md` | Moves to power build doc. |
| **Settled / Envelope & cooling** | `docs/build/climate.md` | Moves to climate build doc. |
| **Settled / Use case & on-hand** | Split: `docs/build/interior.md` (bikes/E-track details) & `docs/build/systems.md` (gear details) | |
| **Recommendations / Power / electrical** | `docs/build/power.md` | #3 (converter) and #4-6 (rails/wiring) are updated to reflect the 24 V-only house bus decision. |
| **Recommendations / Climate / envelope** | `docs/build/climate.md` | #11 (awning) updated to reflect the Fiamma roof-mount and tie-down decisions. |
| **Recommendations / Interior / layout** | `docs/build/interior.md` | Staggered bike mounting layout and E-track heights move here. |
| **Recommendations / Systems / gear** | `docs/build/systems.md` | #17 (fridge) updated to reflect the CFX3 95DZ 24 V native integration and physical clearance. |
| **Still open / Solar / MPPT floor** | `docs/build/power.md` | Closed. Documented as 2S roof + 2S2P ground expansion. |
| **Still open / 48V→12V vs 24V bus** | `docs/build/power.md` | Closed. Resolved as 24 V-only bus with local POL bucks. |
| **Still open / Top-rail contention** | `docs/build/climate.md` | Closed. Resolved by roof-mounting the awning. |
| **Still open / Interior floor plan** | `docs/build/interior.md` | Kept as open, waiting for final tape-measure pass on stud/rail steel. |
| **Still open / Measurements** | Split: `docs/build/climate.md` (window/awning), `docs/build/interior.md` (studs/chocks), `docs/juplaya-trailer-context.md` (curb weight) | |
| **Weight** | `docs/juplaya-trailer-context.md` (Slim Index) | Kept in index. Cross-linked from `interior.md`. |
| **Standing Preferences** | `docs/juplaya-trailer-context.md` (Slim Index) | Kept in index. |

### The Slim Index Keeps:
1. Trailer VIN, serial, models, and dimensions.
2. Tow vehicle specs, Pro Trailer Backup Assist details, and camera integration.
3. The actual curb weight (to be filled in after weighing) and the 10–12% tongue weight rule.
4. Standing preferences.
5. A **link table** directing the reader to the four new domain files, `docs/trailer-mission.md`, `docs/DECISION_LOG.md`, and all spec sheets.

---

## 5. Risks and Immediate Actions

### Key Risks:
* **Roof Bow Loading:** Roof-mounting the 55.1 lb awning places a structural load on the roof bows. We must use backing plates under the roof bows inside the trailer to sandwich the steel bows and distribute the shear and pull-out forces.
* **Side-Door Trim Thickness:** The 0.65" vertical clearance between the door panel and the roof-mounted awning fabric assumes standard door trim. The door frame trim must be measured before final bracket placement to ensure it does not exceed 1.5" height.

### Immediate Action Plan (July 4 Deadline):
1. **Order Hardware (Long-lead):**
   * Fiamma F45s 350 (#06280B01R) and Flat Roof Adapter Brackets (#98655-316).
   * Fiamma Tie Down S Black kit (#98655-133).
   * Victron Orion-Tr 48/24-16A Isolated DC-DC converter.
2. **Perform the Tape-Measure Pass:**
   * Measure the exact exterior height of the door frame trim above the 72" cutout.
   * Verify the position of the curbside roof bows relative to the door opening.
3. **Build the 24 V Distribution:**
   * Mount the Victron Orion-Tr in the nose cabinet.
   * Wire the Blue Sea 7443 20 A breaker on the 48 V feed.
   * Wire the Blue Sea 5026 fuse block on the 24 V output.
   * Route the low-current remote on/off switch wires from the Orion-Tr to the cabin entryway.
4. **Install the Awning:**
   * Through-bolt the Fiamma Flat Roof brackets into the steel roof bows with backing plates, butyl tape, and Dicor lap sealant.
   * Mount the F45s case, adjust the arm pitch to ~10 degrees, and verify the door swings open without contact.
5. **Execute the Doc Split:**
   * After the owner ratifies these recommendations, create the new files under `docs/build/` and slim down the index. Update the `DECISION_LOG.md` with the new decisions.
