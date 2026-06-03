author: operator

# Power / Electrical — Committed Recommendations (DRAFT for cross-examination)

Run: `run_9e484dba594496a37346f2aa587e1924`
Job: `author_draft`
Branch: `striatum/juplaya-power-electrical`

Scope: the 7 Power/electrical open questions in `docs/juplaya-trailer-context.md`. One committed recommendation each, with rationale and the spec/constraint it leans on. Items needing a physical measurement or a purchase are flagged **[MEASURE]** / **[BUY]**.

Architecture is fixed by what's already owned: a **48 V LiTime 5 kW split-phase AIO** (inverter + charger + MPPT in one box, in the nose cabinet), a **48 V 100 Ah LiFePO4** pack (5.12 kWh, ~100 lb), a **500 A Bluetooth shunt**, **ANL fuses**. Loads are tiered by voltage: **48 V** (AC + inverter loads + battery charging), **24 V** (Yuji LED strip lighting), **12 V** (trailer running/marker lights + a few accessories). Target: Juplaya-ready ~July 4 2026; single axle, payload to be weighed.

---

## Q1. Solar count & string — **3 × LG455N2W-E6 in one 3S string**

**Recommendation:** Three LG455N2W-E6 panels (1365 W nameplate) wired **3 in series (3S), single string**, feeding the AIO's MPPT.

**Rationale / spec dependency:** The LG455N2W-E6 (NeON 2, 455 W bifacial) has roughly Voc ≈ 53.3 V, Vmp ≈ 41.8 V per panel (typical for this 144-half-cell class; **[MEASURE/CONFIRM]** exact Voc on the panel label before final string sizing). The LiTime 48 V 5 kW AIO's solar MPPT input is rated to **~145–150 V max PV open-circuit** with an MPPT operating window that needs to sit above the ~60 V battery-charging voltage. String math:

- **3S Voc cold:** 3 × 53.3 = 160 V nominal at STC, but Voc rises in cold. At Burning-Man-region pre-dawn lows (~5 °C) the temperature coefficient (~−0.0027/°C × ~25 °C below STC) lifts Voc only modestly above 160 V — **this is the one number that can exceed the 145–150 V ceiling, so it must be checked against the AIO's actual datasheet max PV voltage** **[MEASURE/CONFIRM]**. If the confirmed AIO PV max is 150 V, 3S is marginal-to-over at cold Voc and the safe call drops to **2S2P (4 panels)** or **2S (2 panels)**.
- **Vmp 3S:** 3 × 41.8 ≈ 125 V — comfortably inside a 60–145 V MPPT tracking window. Good.
- **Current:** ~11 A Imp single string — trivial for the controller and wiring.

**Committed call:** **3 panels, 3S**, contingent on the AIO datasheet PV-Voc-max being ≥ ~165 V; if the AIO is a 150 V-class MPPT, fall back to **2S (2 panels)** and accept ~910 W. 3 panels ≈ 1365 W into a 5.12 kWh pack is the right ratio for a "sips power" moto basecamp (full recharge in ~4 good solar hours). Four panels (2S2P) is the only way to add power without raising string voltage, but roof area on a 7-wide (≈81" interior, ~96" exterior shell) and weight argue against it for the Juplaya mission. **Do not exceed 3 panels** — payload and roof real estate don't justify it for the sip-power use case.

---

## Q2. Solar mounting — **Z-bracket + aluminum unistrut rails landing on the roof bows, NOT hung off the side rail**

**Recommendation:** Mount panels on **2 longitudinal aluminum rails (e.g. unistrut or solar mounting rail) bolted down through the 1-piece aluminum roof into the steel tube roof bows (24" on center per the work order)**, with stainless fasteners, butyl/EPDM sealing washers, and an elastomeric/Dicor lap-sealant overband. Panels sit flat-ish on Z-brackets or tilt-feet on those rails.

**Rationale / spec dependency:** The work order confirms **tube roof bows 24" on center** and a **1-piece aluminum roof**. That bow grid is the only real structure up there — the aluminum skin alone will not hold a panel against 70 mph tow loads. Owner's stated preference to **hang panels off the side aluminum top rail** is rejected as the primary method: a cantilevered side-mount loads the rail in a tipping/peel mode at highway speed and over the dirt road into Juplaya, and it puts the panels outside the 8'6" width envelope / in the airflow. **Land the load on the bows.** Every roof penetration gets butyl tape under the foot + self-leveling lap sealant on top; this is compatible with the planned elastomeric roof coating (coat first, then mount, then seal feet).

**[MEASURE]** Confirm bow positions from inside before drilling (mark centers). **[BUY]** Mounting rail, Z/tilt brackets, stainless bolts, butyl tape, Dicor self-leveling sealant.

---

## Q3. 48 V→12 V converter — **Yes. One 48 V→12 V DC-DC, 20–30 A (≈300 W)**

**Recommendation:** Install a dedicated **48 V→12 V DC-DC converter, 25 A continuous (~300 W) class** (e.g. an isolated 48→13.8 V unit), feeding a **Blue Sea fused 12 V distribution block**.

**Rationale / spec dependency:** The pack and AIO are 48 V; the AC is 48 V; lighting is 24 V. But the trailer's own running/marker/tail lights, the factory 12 V dome light, and the accessory list (GPS hardwire, 12 V sockets, USB-C PD, vent fans, door switch, awning controller) are all **12 V**. Running these off the 48 V pack requires a step-down. Do **not** abuse the inverter→12 V-wall-wart path (idle inverter draw). A 25 A/300 W DC-DC covers the realistic simultaneous 12 V load (Q4) with headroom. Mount it in the nose cabinet beside the AIO, fused on the 48 V input (ANL or appropriately-rated) and on the 12 V output block. **[BUY]** DC-DC converter + Blue Sea fuse block.

Note the 24 V lighting bus (Q5) is a **separate** question — see Q5; a 48→24 V converter is recommended there rather than running lights off this 12 V rail.

---

## Q4. 12 V load list — **Enumerated below; the "only strip lights + door switch + AC" assumption is FALSE**

**Committed 12 V load list:**
| Load | Draw (typ) | Notes |
|---|---|---|
| Factory trailer running/marker/clearance/tail/ID-bar lights | ~3–5 A | Already on the trailer; fed from 7-way when towing, but should also be on the 12 V house rail for yard use |
| 12 V dome light (factory) + added LED dome/task lights | ~1–2 A | |
| Roof/exhaust vent fan (e.g. Maxxair-class) | ~1–3 A | Pairs with the HRV/heat plan |
| 12 V accessory sockets + USB-C PD chargers | ~5–10 A peak | Phones, headlamps, tools |
| GPS tracker (LandAirSea 54, hardwired) | <0.1 A | Always-on |
| Door switch / interior light trigger | <0.1 A | |
| Awning motor/controller (if powered awning) | ~5 A intermittent | Most likely the 12 V awning load |
| Water pump (if any plumbing added later) | ~3–5 A | Reconfigurability allowance |

**Recommendation/validation:** The context's working assumption ("other than strip lights, a door switch, and the AC, no other wiring is foreseen") is **not safe to commit** — the trailer ships with a 12 V lighting harness and the accessory list already names several 12 V devices. Realistic simultaneous 12 V draw is ~10–15 A, peaks ~20 A. This sizes the Q3 converter. **Commit a 12 V house rail.**

---

## Q5. Lighting — **24 V Yuji strips on a dedicated 48 V→24 V DC-DC bus (250 W), Klus extrusions; awning/exterior on 12 V**

**Recommendation:** Run the Yuji 24 V LED strips off a **dedicated 48 V→24 V DC-DC converter (~10 A / 250 W)** feeding a small fused 24 V distribution, with strips in **Klus extrusions/diffusers** zoned (e.g. galley, bed deck, entry) on switches/dimmers rated for 24 V. Keep **exterior/awning lighting on the 12 V rail** (Q4) since most RV awning LED and porch fixtures are 12 V.

**Rationale / spec dependency:** Strips are confirmed 24 V (Yuji). Deriving 24 V from the 48 V pack via its own DC-DC keeps the lighting bus clean and independent of the 12 V accessory rail (so a 12 V fault or fan inrush doesn't dim the cabin). 250 W of 24 V LED is far more strip than this interior needs (sip-power), giving dimming headroom. Voltage drop on 24 V over the ~13 ft length is low; size strip feeder wire for <3% drop **[MEASURE]** once Klus runs are laid out. **[BUY]** 48→24 V DC-DC, 24 V dimmers, Yuji strips, Klus extrusion/diffuser, end caps.

---

## Q6. Wiring diagram — **Three-rail bus topology (48 V / 24 V / 12 V), star-grounded at the pack negative / shunt**

**Recommended bus design (the diagram to be drawn):**

```
[3S LG455 array] --PV--> [LiTime 48V 5kW AIO MPPT]
                                  |
        [F-150 12V] --DC/DC 48V charger (Q7)--> 48V BUS <--> [48V 100Ah LiFePO4]
                                  |                              (500A shunt on neg)
        +--- 48V: AIO inverter (120/240 split) -> Velit Mini 2000R AC, 120V outlets
        +--- 48V->24V DC-DC (250W) ----> 24V BUS -> Yuji strips (Klus zones)
        +--- 48V->12V DC-DC (300W) ----> 12V BUS (Blue Sea block)
                                            -> trailer lights, dome/task, vent fan,
                                               sockets/USB-C, GPS, door switch, awning
```

**Principles:** single-point DC ground at the pack negative / shunt; every converter input individually fused on the 48 V bus (ANL/MIDI per current); every output rail on its own fused block; 48 V battery cabling to ABYC ampacity for the AIO's 5 kW inverter draw (≈100 A at 48 V continuous → 2/0 to 4/0 short runs, **[MEASURE]** run lengths). **Conduit/ENT with pull strings** through the wall cavities (per mission doc) so the reconfigurable build can re-feed E-track-mounted modules later. **Do not draw final gauges until run lengths are measured.** This question is **deferred to a measured layout pass** but the topology above is committed.

---

## Q7. Truck charging — **DEFER the charger for Juplaya; PRE-WIRE the path now. Spec a ~480–600 W 12→48V DC-DC (~40–50 A @ 12 V in, ~10–12 A @ 48 V out) for later.**

> **REVISED after cross-examination (agy).** Original header committed a "30–40 A output (~2 kW)" unit — that was **internally contradictory** with this section's own input math and is **struck**. Corrected spec and a re-ranked necessity verdict below. See `runs/juplaya-power-electrical/dialogue/cross_examiner_1/CROSS_EXAM.md`.

**Recommendation:** For the **Juplaya/moto mission, do NOT install a truck-charge DC-DC** — 1365 W of solar + desert sun fully recharges the 5.12 kWh pack in <4 h, so an alternator line is redundant when leaving home at 100% SoC. **But pre-run a 4 AWG line + Anderson connector to the tongue NOW while the walls are open** (cheap, ~5 lb) so the charger can be added later for the shaded/winter Moab/offroad profiles without re-opening the build. When added, the charger is a **~480–600 W-class 12 V→48 V DC-DC: ~40–50 A on the 12 V input → ~10–12 A at 48 V output** (≈0.1C gentle top-up), gated by an **ignition-sensed relay/DC-DC enable** so it never drains the truck at rest.

**Sizing / spec dependency:**
- The F-150 EcoBoost alternator (~200+ A class) can spare ~40–50 A continuous while the engine runs. Pulling **~40–50 A at 12 V (~480–600 W)** into a 12→48 V DC-DC yields **~10–12 A at 48 V (~480–550 W usable)** into the pack — about 0.1C, a gentle, safe top-up that recovers ~1.5–2 kWh over a multi-hour tow. **This is the whole budget**: do NOT spec a "2 kW / 30–40 A-output" unit — that would draw ~160 A at 12 V, blow the fuse, overload the alternator's spare headroom, and crater the line voltage. The corrected unit is small. **Do not** try to push 100+ A down the trailer harness; the 7-way 12 V pin and standard trailer wiring cannot carry it.
- **Wire gauge:** the factory 7-way 12 V "house/charge" pin and its wiring are **not** rated for sustained 40–50 A over a ~25–30 ft truck-to-pack run. Commit to a **dedicated 4 AWG (or larger) charge line run alongside the harness**, with an **Anderson SB50/SB175 connector** at the tongue, **fused at both ends (50 A) near each battery**, and a **continuous-duty relay or the DC-DC's own ignition-enable** so it only charges with the engine running. **[BUY — defer to later profiles]** 12→48 V DC-DC charger (~480–600 W class, e.g. Victron Orion-class rated for 48 V output), 2× ANL/MIDI fuses + holders, ignition-trigger relay/wire tap. **[BUY NOW — pre-wire]** 4 AWG cable + Anderson SB50/SB175 connector, run while walls are open.
- **[MEASURE]** Actual truck-to-pack cable length to finalize gauge (4 AWG good to ~30 ft at 40–50 A / 12 V for ~3% drop; go 2 AWG if longer).

---

## Cross-cutting flags
- **[MEASURE/CONFIRM] before committing Q1 to 3S:** the LiTime AIO's exact PV max open-circuit voltage and MPPT window from its datasheet, and the LG455N2W-E6 label Voc — this is the single safety-relevant number (over-voltage can damage the MPPT).
- **[WEIGH]** 3 panels + rails + DC-DCs + truck-charge cable add ~60–90 lb high and forward; fold into the to-be-weighed payload budget, not a guessed one.
- All converters (48→24, 48→12, 12→48 charger) and the AIO live in/near the **nose cabinet** — confirm cabinet ventilation for ~3 converters + AIO heat.
