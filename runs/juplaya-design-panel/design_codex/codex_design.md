---
author: operator
---

# Design pass - Codex lane (second full pass)

Posture: feasibility and spec rigor. I kept Claude's correct architecture move - delete the central 12 V house rail - but changed the fridge and awning recommendations where the draft was thin or mismatched to the prompt.

## What I changed from Claude

- **Kept:** one 24 V house bus fed from the 48 V pack, with no central 48->12 V converter and no 12 V house fuse block. That is the right answer.
- **Corrected:** the solar math references. The local LG sheet gives 2S Voc = 99.8 V at STC; at -40 C it is about 116.7 V nominal, and about 122.6 V if the +5% Voc tolerance is included. Still below the LiTime 145 V hard PV max, but not the old "~109 V cold" shortcut. 3S is invalid even before cold/tolerance because 3 x 49.9 V = 149.7 V > 145 V.
- **Changed fridge:** replaced the ICECO VL60 ProD with **Dometic CFX2 57, SKU 97000040398**. Reason: the VL60 overshoots the requested 50-55 L class and Claude's exact footprint/compressor-current claims were not supported by the provided docs. The CFX2 57 is current, 12/24 V, lighter, and has official dimensions/current.
- **Changed awning:** replaced Carefree Fiesta/Festival-style patio awning language with **Fiamma F45s 350, Polar White/Royal Grey, 06280B01R**. Reason: the prompt asks for a manual lateral-arm/top-rail solution. The F45s is a wall/top-rail cassette winch awning with reinforced arms and telescopic support legs; the Carefree Fiesta family has wall arms and lower brackets that add door-placement risk.
- **Tightened protection:** ordinary 32 V automotive fuse gear is not acceptable on the 48 V side. The 48 V->24 V converter branch gets an 80 V DC breaker. The Blue Sea 5026 is acceptable only downstream on regulated 24 V because its max rating is 32 V DC.
- **Extended the doc-divorce map:** the split below maps every current context-doc section to a destination and states what the slim index keeps.

## Spec receipts

Local sheets checked:

- LiTime 48 V 3500 W AIO: 3500 W AC, 6000 W/5 s surge, battery range 40-60 V, PV 60-145 V operating / 60-115 V recommended / <=4400 W / <=50 A, max combined charge 120 A, no-load <50 W normal / <30 W ECO.
- LiTime 48 V 100 Ah ComFlex: 51.2 V nominal, 5120 Wh, 100 A max continuous charge, 100 A max continuous discharge, 200 A for 2 min, charge voltage 57.6 +/- 0.8 V, 97.44 lb.
- LG455N2W-E6: 455 W, Vmpp 42.1 V, Voc 49.9 V +/-5%, Impp 10.83 A, Isc 11.39 A, Voc temp coefficient -0.26 %/C, size 83.07 x 41.02 in, weight 48.5 lb.
- Trailer: FT712S2-D, 81 x 157 x 78 in interior, 32 x 72 in curbside personnel door, 3,500 lb GVWR, single 3.5K electric-brake axle, 2 x 4 tube main rails, 24 in OC roof bows, 16 in OC vertical posts, 16 in OC crossmembers.

External product checks used for concrete part specs:

- Dometic CFX2 57 product/manual: https://www.dometic.com/product/cfx2-57-electric-cooler-97000040398 and https://media.dometic.com/externalassets/07-0703-070327-070327003_97000040397_112266.pdf
- Fiamma F45s: https://fiammausa.com/en/f45s-en.html
- Fiamma Tie Down S: https://www.fiammausa.com/en/products/fiammastore-en/fiammastore-accessories/anchoring-straps.html
- Mean Well RSD-500 series: https://www.meanwell.co.uk/power-supplies/dc-dc-power-supplies/rsd-500-series
- Blue Sea 5026 fuse block: https://www.bluesea.com/products/5026
- Blue Sea 7443/UL-489 breaker family: https://www.bluesea.com/products/7442/UL-489_Circuit_Breaker_-_15A_Flat_Rocker
- Scanstrut SC-USB-F3: https://www.scanstrut.com/rv/power/usb/flip-pro/flip-pro-max
- LandAirSea 54 hardwire cable: https://landairsea.com/products/hardwire-power-adapter-cable-for-gps-trackers-usb-c

## Decision 1 - DC house bus

**Recommendation:** build a **single regulated 24 V house bus** from the 48 V battery stack. Install **one Mean Well RSD-500C-24 isolated DC-DC converter** and **delete the 48->12 V house converter**. Do not install a 12 V house fuse block.

Concrete bus parts:

- **48->24 converter:** Mean Well **RSD-500C-24**, 33.6-67.2 VDC input, 24 V / 19.2 A / 460.8 W output, isolated, fanless, railway shock/vibration class.
- **48 V branch protection:** Blue Sea **7443** 20 A UL-489 DC breaker, 80 V DC class, ahead of the converter input. Use 48 V-rated protection here; do not use 32 V ATO/ATC hardware on the 48 V side.
- **24 V distribution:** Blue Sea **5026** 12-circuit ST Blade fuse block with negative bus and cover. Its 32 V DC max rating is fine on a regulated 24 V bus and not fine on the 48 V battery bus.
- **USB-C PD outlets:** Scanstrut **SC-USB-F3 Flip Pro Max**, 10-32 V input, 2x USB-C, full 60 W profiles only on 24 V. Fuse at 10 A on the 24 V block.
- **Legacy 12 V-only point loads:** only if an unavoidable accessory appears, use one local **Victron Orion-Tr 24/12-5A** or equivalent point-of-load converter at that accessory. This is not a rail and does not get a 12 V fuse block.

Rail map:

| Load | Rail | Implementation |
|---|---:|---|
| LiTime AIO AC output / charging | 48 V battery domain | Existing AIO wiring, shunt, main DC protection. |
| Velit Mini 2000R AC | 48 V battery domain | Direct 48 V fused branch, not through the 24 V bus. |
| Yuji LED strips | 24 V | Native 24 V from the Blue Sea 5026, zoned/dimmed. |
| Dometic CFX2 57 fridge | 24 V | Native 12/24 V DC input; fuse at the 24 V block. |
| LandAirSea 54 GPS | 24 V | Use the LandAirSea hardwire cable; it accepts 6-24 V external input. |
| Door switch | 24 V signal | Dry contact into the 24 V lighting/control circuit. |
| USB-C PD | 24 V | Scanstrut SC-USB-F3; this is a direct payoff of choosing 24 V because it unlocks 20 V/3 A USB-C output. |
| Awning | no electrical load for July | Fiamma F45s is manual. Future LEDs get 24 V native strip lighting or a local 24->12 point converter at the awning. |
| Running, marker, brake, tail lights | tow-vehicle 12 V | Leave on the OEM 7-way/trailer harness. Do not merge with house DC. |
| Factory 12 V dome light | OEM/tow only or retire | House lighting is the Yuji 24 V system. Do not create a 12 V rail to preserve this dome. |
| Generic cigarette sockets | do not install | They invite plugging 12 V devices into a 24 V bus. Use USB-C PD instead. |

Why this kills the 48->12 question:

- The real committed house loads are either 24 V native, 12/24 V auto-sensing, or dry contacts.
- The OEM legal trailer-lighting/brake harness is tow-fed and must stay isolated from house DC.
- A central 48->12 converter would add idle draw, weight, protection complexity, and a second fuse block for loads that do not need it.
- The 24 V bus is already required for Yuji strips. Consolidating the fridge, GPS hardwire adapter, USB-C PD, and controls onto it reduces parts and halves current versus 12 V for the same wattage.

Power sanity check:

- AIO at full 3500 W output draws roughly 3500 W / (51.2 V x 0.91) = 75 A from the pack, below the ComFlex 100 A continuous discharge rating. The 6000 W/5 s surge is roughly 129 A, below the pack's 200 A/2 min surge allowance.
- AIO ECO idle <30 W is still about 0.72 kWh/day, about 14% of the 5.12 kWh pack. The fridge stays on DC so the inverter can sleep.
- The RSD-500C-24 converter gives 19.2 A at 24 V. That covers fridge peak, USB-C PD, GPS/controls, and realistic lighting diversity. Fuse branches by wire/load; do not size the bus by adding every branch fuse as simultaneous load.

## Decision 2 - Fridge

**Recommendation:** buy the **Dometic CFX2 57 Electric Cooler, SKU 97000040398**, and run it directly from the 24 V house bus.

Why this unit:

- Official Dometic spec: **57 L**, 12/24 V DC or 100-240 V AC, **4.0 A rated at 24 V**, -22 C to 20 C cooling range, 40.4 lb.
- Dimensions are **27.91 W x 19.80 H x 18.03 D in** including handles. That fits the 81 in interior width without stealing the bike centerline plan.
- It is a DC compressor fridge/freezer, not an inverter-fed Midea. This preserves D005's inverter-idle decision.
- It is lighter than the 55 L ICECO APL55 and closer to the requested class than the 60 L ICECO VL60 ProD in Claude's pass.
- Price class: about **$990** from Dometic's current product line. This is not the cheapest cooler, but it is a clean current-product recommendation with official 24 V numbers.

Mounting:

- Put it on the **curbside forward floor zone just aft of the nose cabinet**, strapped to floor/wall E-track with a removable base plate.
- Keep it out from under the 34 in bed deck unless it sits on a slide-out tray; the lid needs vertical swing clearance.
- Leave compressor ventilation space on the vent end; do not bury it inside the warm AIO nose cabinet.
- Wire as a dedicated 24 V branch from the Blue Sea 5026. Use a locking two-pole DC connector rather than a loose cigarette plug.

What this changes from D005/Claude:

- D005 said "12 VDC compressor fridge" because the earlier open question assumed a 12 V accessory rail. Recast it as **12/24 VDC compressor fridge on 24 V**.
- Claude's ICECO VL60 ProD recommendation works electrically, but it is a 60 L answer to a 50-55 L prompt and its stated dimensions/current were not documented in the repo. I would not carry that forward.

## Decision 3 - Awning

**Recommendation:** install a **Fiamma F45s 350, Polar White case / Royal Grey fabric, part 06280B01R**, curbside, through-bolted to the trailer's upper side/top rail structure with backing plates. Use the **Fiamma Tie Down S Black kit, 98655-133**, plus playa screw anchors/deadmen.

Why this unit:

- It is a manual winch/cassette awning for wall installation, with reinforced arms and telescopic legs. That matches the prompt's manual lateral-arm/top-rail intent better than a traditional RV patio awning with lower wall brackets.
- Size is right for the 12 ft box: **11 ft 6 in case length**, **10 ft 10 in canopy length**, **8 ft 2 in extension**, **55.1 lb**. It shades the personnel door and curbside work area without running past the 12 ft body.
- MSRP/current price class is about **$1.4k-$1.7k** before brackets, freight, backing plates, and install supplies. This is the long-lead July item.
- The awning is manual, so it adds no July electrical load and no motor failure path.

Mounting:

- Mount curbside at the **highest practical top-rail/upper-wall line**, not to the sheet skin. Through-bolt brackets into structure with interior backing plates tied across the upper rail/vertical-post line.
- Use butyl under brackets and compatible exterior sealant over fasteners. No peel-loaded skin screws.
- Solar stays on roof-bow rails. The top rail is reserved for awning brackets; there is no solar/awning conflict.
- Door clearance is tight and must be treated as geometry, not assumption. Interior height is 78 in and the side door is 72 in, so the nominal header margin is about 6 in. The F45s case is roughly 5.4 in tall in installation drawings. The install must hold the case high/outboard enough that the **bottom of the case and crank/lead hardware clear the outward-swinging 32 x 72 door through its full travel**.

Desert tie-down scheme:

- Use the Fiamma legs deployed to the ground, not wall-foot mode, on playa.
- Clip **Tie Down S** hooks into the lead-bar guide and run the two 300 cm straps to ground.
- Replace or supplement the included pegs with impact-driven screw anchors rated for hard playa, backed up by deadman bags when the surface is powdery.
- Add a short safety tether from each lead-bar corner to the trailer-side E-track/top-rail anchor only as a backup, not as the primary wind load path.
- Operating rule: if leaving camp, sleeping, or seeing a front/dust wall, roll it in. This awning is shade, not a storm structure.

What this changes from Claude:

- The Carefree Fiesta Lite concept is a good RV awning family, but it uses sidewall arms and lower brackets. That is worse around a cargo trailer personnel door and weaker against the prompt's "lateral-arm/top-rail" requirement.
- Fiamma's cassette also reduces deadline risk: one self-contained unit plus structural brackets and tie-downs, not an awning rail/bag/patio-arm layout that depends on clean lower wall real estate.

## Decision 4 - Doc divorce

**Recommendation:** split `docs/juplaya-trailer-context.md` into four domain docs under `docs/build/` and leave the original file as a slim index. Move content verbatim first, then edit only for links/headings so no content disappears.

Target files:

| Current content | Destination |
|---|---|
| Title, Juplaya target date, warning that only Settled is firm | Keep in `docs/juplaya-trailer-context.md` index. |
| Settled / Trailer | Keep summary in index; detailed trailer facts also link to `docs/fastrac-specs.md` and `docs/wells-cargo-ft712s2-d-work-order.md`. |
| Settled / Tow vehicle | Keep in index. |
| Settled / Power system (48V - current/up to date) | Move to `docs/build/power.md`. Index keeps one-line pointer. |
| Settled / Envelope & cooling | Move to `docs/build/climate.md`. |
| Settled / Use case & on-hand | Split: bike/use-case facts to `docs/build/interior.md`; mission framing stays linked to `docs/trailer-mission.md`; E-track on-hand note to `docs/build/interior.md`. |
| Recommendations intro and provenance | Keep short provenance note in index; each domain doc keeps the relevant run links. |
| Recommendations #1-#7 Power / electrical | Move to `docs/build/power.md`; replace #3-#6 with this bus decision after owner ratifies. |
| Recommendations #8-#11 Climate / envelope | Move to `docs/build/climate.md`; awning section references the Fiamma decision and links to mounting details. |
| Recommendations #12-#16 Interior / layout and E-track footage note | Move to `docs/build/interior.md`. |
| Recommendations #17-#18 Systems / gear | Move to `docs/build/systems.md`; fridge and accessories live there, with electrical cross-link back to `power.md`. |
| Still open / Solar / MPPT floor resolved | Move to `docs/build/power.md` as a closed note, not an open question. |
| Still open / 48V->12V converter vs 24V bus | Move to `docs/build/power.md` as resolved by this pass: no 48->12 house converter. |
| Still open / Top-rail contention | Move to `docs/build/climate.md` as resolved: awning top rail, solar roof bows. |
| Still open / Interior floor plan | Move to `docs/build/interior.md` as still open. |
| Still open / Measurements | Split by domain: window RO to `climate.md`, tire centerlines/E-track to `interior.md`, actual curb/payload to the index Weight section. |
| Weight | Keep in index and cross-link from `interior.md`. Do not optimize against estimated payload until the trailer is weighed. |
| Standing preferences | Keep in index. |

What the slim index keeps:

- Trailer identity and dimensions, tow vehicle, Juplaya target, real-weight warning, standing preferences.
- A link table to `docs/build/power.md`, `docs/build/climate.md`, `docs/build/interior.md`, `docs/build/systems.md`, `docs/trailer-mission.md`, `docs/DECISION_LOG.md`, and all local spec sheets.
- A "current open gates" list with only truly unresolved items: actual curb weight, interior steel/handlebar tape pass, window rough opening, and any owner ratification pending in the decision log.

New domain-doc responsibilities:

- `docs/build/power.md`: 48 V stack, AIO settings, battery limits, solar string math, truck-charging prewire, 24 V bus decision, DC protection rules, electrical load map.
- `docs/build/climate.md`: insulation/roof coating, Velit 48 V AC, window, HRV rough-in, diesel-heater deferral, awning decision and tie-down discipline.
- `docs/build/interior.md`: bike transport geometry, E-track floor/wall rows, bed/shelf rows, wall finish, removable step, fridge physical placement constraint, actual measurement gates.
- `docs/build/systems.md`: fridge product decision, security/accessory order, GPS hardwire, USB-C PD parts, locks, labeling conventions, removable gear.

## Immediate order/install sequence

1. Order long-lead items now: Fiamma F45s 350, Fiamma Tie Down S, Mean Well RSD-500C-24, Dometic CFX2 57, Scanstrut SC-USB-F3.
2. Tape-check before drilling: curbside door swing against the F45s case/bracket line; fridge lid clearance against the bed-row plan; AIO cabinet converter ventilation.
3. Build the 24 V panel: 48 V breaker to converter, converter to Blue Sea 5026, branch fuses/labels, USB-C PD, fridge connector, GPS hardwire.
4. Through-bolt awning brackets into structure with backing plates, then deploy and tie down once in calm conditions before Juplaya.
5. After owner ratification, convert this pass into D006+ decision-log rows and execute the doc split.

## Remaining risks

- The F45s door clearance is tight but manageable only with a high/outboard bracket layout. This must be verified on the actual trailer before drilling.
- Payload remains to-be-weighed. These choices are weight-conscious, but the awning is still about 55 lb high on the curbside and should be included in the tongue/side balance check.
- The RSD-500C-24 is enough for the intended 24 V loads, but lighting design should be fused and dimmed as zones. Do not make the Yuji strips a single all-on decorative load that consumes the whole converter.
