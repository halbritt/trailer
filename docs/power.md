# Power / Electrical

This is the detailed power source of truth for the Juplaya trailer build. The build sheet keeps only the abbreviated view; this document carries the wiring architecture, solar topology, component decisions, commissioning rules, and energy budget.

Related decisions: [D002](DECISION_LOG.md), [D006](DECISION_LOG.md), [D008](DECISION_LOG.md). Key receipts: [3-panel house-power verdict](../runs/aio-adversarial-3panel/synth/VERDICT.md), [SmartSolar 250/60 specs](reference/victron-smartsolar-mppt-250-60-tr-specs.md), [SmartSolar 150/35 specs](reference/victron-smartsolar-mppt-150-35-specs.md), [C1000/PS400 specs](reference/anker-solix-c1000-ps400-specs.md), [ComFlex battery specs](reference/litime-48v-100ah-battery-specs.md), [Orion-Tr 48/12-20A specs](reference/victron-orion-tr-48-12-20a-specs.md).

## Diagrams

![Juplaya power overview](diagrams/power-overview.svg)

![Solar string routing](diagrams/power-solar-strings.svg)

## Current Verdict

For Juplaya, the built-in inverter/charger is deferred. Critical trailer loads stay on DC:

- Roof solar charges the 48 V trailer battery through a Victron SmartSolar 250/60-Tr.
- The Velit 2000R runs directly from the 48 V battery on its own fused branch.
- One Victron Orion-Tr 48/24-16A feeds the 24 V house bus for fridge, lights, USB, GPS, and winter heater rough-in.
- One Victron Orion-Tr IP43 48/12-20A feeds fused cigarette-lighter receptacles in the power cabinet for occasional 12 V loads.
- Small 120 VAC loads run from the standalone Anker SOLIX C1000 + PS400 panel.
- The Victron MultiPlus-II 48/3000/35-50 120V remains the Phase 2 built-in inverter/charger choice, not a Juplaya blocker.

## Architecture

One high-voltage battery bus, one primary conversion step to 24 V house loads, and one local auxiliary 12 V converter for cabinet receptacles:

```text
Optional deployable LG ground PV (2S)
        |
   Victron SmartSolar MPPT 150/35
        |
        +-- 48 V bus

Roof PV (3 x LG455 in 3S)
        |
   Victron SmartSolar MPPT 250/60-Tr
        |
        +-- 48 V bus

48 V bus
        |
   LiTime 48V 100Ah ComFlex (5.12 kWh)
        | 500A shunt, main OCP
        +-- 48 V branch: Velit 2000R rooftop AC, own fused branch
        +-- Victron Orion-Tr 48/24-16A isolated -> Blue Sea 5026 24 V block
                                                        +-- fridge, 24 V native
                                                        +-- interior/exterior LED zones, USB-C PD, GPS
                                                        +-- winter heater outlet
        +-- Victron Orion-Tr IP43 48/12-20A isolated -> fused 12 V cabinet receptacles

Anker SOLIX C1000 + PS400 400 W panel -> standalone 120 VAC loads

Phase 2 optional:
LiTime 48 V battery -> Victron MultiPlus-II 48/3000/35-50 120V -> built-in 120 VAC / shore charging / transfer
```

Why 48 V: the Velit air conditioner is 48 V-native, and at 48 V the cables stay small. Why 24 V house loads: the fridge auto-senses 12/24 V, Yuji LED strips are 24 V, the Scanstrut USB-C takes 24 V input, and the selected exterior lights are 12-28 VDC wide-input fixtures. The 12 V converter is scoped narrowly: a switched, fused accessory outlet bank in the power cabinet for occasional 12 V devices, not a distributed house rail.

## Solar Topology

**Panels on hand:** 5 x LG455N2W-E6. Three live on the roof. Two can travel inside and deploy on the ground. Corrected review premise: the Velit fits in the nose section, so the roof has room for the permanent 3S string.

| Source | String | Power | Controller | Status |
|---|---:|---:|---|---|
| Deployable LG ground pair | 2S | 910 W | Victron SmartSolar MPPT 150/35 | ordered, optional use |
| Roof LG panels | 3S | 1365 W | Victron SmartSolar MPPT 250/60-Tr | primary |
| Anker PS400 | 1 panel | 400 W | Anker SOLIX C1000 input | separate AC island |

Rules:

- Roof 3S lands only on the SmartSolar 250/60-Tr.
- Never put roof 3S into a 145/150 V-class AIO or MPPT.
- Never combine roof 3S and ground 2S on one tracker.
- The PS400 feeds the C1000 only. Do not series or parallel it with LG panels.
- Physically label and segregate roof PV, LG ground PV, and Anker PV connectors so mis-plugging is not plausible.

## Roof Solar Mounting

Physical mount source: [solar panel mounting/backing research](research/solar-panel-mounting-backing-2026-06-06.md).

Mechanical verdict: the existing panel brackets attach the modules to a rail system; they do not define the trailer load path. Use two fore-aft structural rails spanning the roof array field, tied to multiple roof bows with discrete sealed feet/backing. Add a third rail only if dry-fit stiffness or bracket geometry requires it. Do not fasten the roof modules to roof skin alone.

Install the rail feet/backing, PV gland, and Velit curb before foam and before Henry 887 roof coating. Hose-test every penetration before the ceiling closes. Keep roof 3S wiring clipped to the rails, with service loops and labels so it cannot be confused with the optional ground 2S input.

Voltage checks:

- LG455 Voc is 49.9 V. Roof 3S is 149.7 V at STC and roughly 163-171 V cold signal, so it needs a 250 V-class controller.
- LG ground 2S is 99.8 V at STC and roughly 109-114 V cold signal, so the SmartSolar 150/35 is appropriate.
- The PS400 is 57.6 V Voc, intentionally close to the C1000's 60 V input ceiling. Use it as the matched Anker single-panel input.

## 48 V Stack

| Component | Role | Notes |
|---|---|---|
| LiTime 48 V 100 Ah Smart ComFlex | house battery | 5.12 kWh, 100 A continuous charge/discharge, Bluetooth BMS |
| LiTime 500 A Bluetooth shunt | instrumentation | single-point ground lives here |
| Main battery OCP | protection | make battery-terminal Class-T or equivalent main OCP explicit before final wiring |
| SmartSolar 250/60-Tr | roof MPPT | roof 3S only |
| SmartSolar 150/35 | ground MPPT | optional LG ground 2S only; connector variant pending |
| Velit 2000R | 48 V DC load | own fused branch |
| Orion-Tr 48/24-16A | house converter | isolated, remote on/off to cabin toggle |
| Orion-Tr IP43 48/12-20A | auxiliary 12 V converter | isolated, 240 W / 20 A, remote off; feeds only cabinet receptacles |

The battery, shunt, MPPTs, Orion converters, distribution, and protection live in the nose cabinet. Ventilate the cabinet; the SmartSolar and Orions add waste heat, and the fridge bay must stay away from this plume.

## Power Cabinet Ventilation

Active plan: **vent the power cabinet to the cabin and avoid exterior penetrations.** The cabinet gets filtered low intake from the cabin and high fan-assisted exhaust back to the cabin. This keeps tow rain and playa dust out of the electrical cabinet and avoids another wall hole in the nose.

Deferred fallback: if cabin-side ventilation cannot keep cabinet temperature under control during shakedown, reopen an exterior-vent path. The preferred exterior fitting remains the **[RecPro RP-2414 Exterior Wall Vent for Enclosed Trailers with 3" Hole](https://recpro.com/exterior-wall-vent-for-enclosed-trailers-with-3-hole/)**, color to match the trailer exterior. It is a low-profile 2-piece enclosed-trailer side vent over a 3" sidewall hole, with a UV-resistant polypropylene exterior cowl, interior round grille, weep path, and front-driver-side / rear-curb-side ram-air orientation guidance. Hardware and sealant are not included.

**Exterior-placement constraint:** do not use an unprotected, forward-facing high nose location as the normal vent path. The RecPro fitting is a sidewall vent with front-driver-side / rear-curb-side orientation guidance; a high nose vent sees ram wind, rain, and playa dust while towing and can become a forced intake when the fan is off. If a high nose location is unavoidable, treat it as a closable travel vent: interior shutter or backdraft damper, cowl/louver opening rearward or downward, drainage/weep path kept clear, and hose-test before the wall closes.

Recommended cabinet airflow:

- **Low intake:** filtered interior transfer vent in the lower cabinet face, pulling relatively clean cabin air.
- **High exhaust:** fan-assisted interior transfer vent near the upper cabinet face, exhausting back to the cabin. Keep intake and exhaust separated enough that the fan does not short-cycle hot air.
- **Fan:** 24 V, 120 mm, dust-resistant fan on the 24 V house bus; fuse at 1 A. A Noctua NF-F12 industrialPPC-24V-2000 SP IP67 PWM-class fan is enough airflow and survives dust better than a bare PC fan.
- **Control:** normally-open enclosure thermostat closing on temperature rise, set around 95 F on / 85 F off. Add a manual override if convenient.
- **Test:** with roof solar charging and both Orions enabled, verify cabinet air stays below 40 C / 104 F near the SmartSolars and Orions. Victron MPPTs are full-rated to 40 C and derate above that.

If cabin-side ventilation fails the shakedown temperature test, change course: add an exterior vent path using the RecPro sidewall fitting, with the exterior-placement constraint above.

## 24 V House Bus

One Victron Orion-Tr 48/24-16A isolated converter feeds a Blue Sea 5026 fuse block. Wire the Orion remote on/off to a cabin toggle so the house bus can be killed without opening the cabinet.

Approximate current is for planning and load-shedding. Fuses still size to the protected wire/device branch, not to these rough draw numbers.

| Branch | Approx current | Fuse | Wire | Notes |
|---|---:|---:|---|---|
| Fridge, Dometic CFX3 95DZ | ~4.6 A running | 10 A | 14 AWG | 24 V native; verify less than 3 percent round-trip voltage drop |
| LED lighting zones | ~4-10 A exterior depending on fixtures; ~2-3 A interior typical | 5 A per zone | TBD | 24 V interior strips plus exterior zones below |
| Scanstrut SC-USB-F3 | up to ~5 A at full USB-C load | 7.5 A | TBD | 24 V in to USB-C PD |
| LandAirSea 54 GPS | <0.1 A typical | 3 A | TBD | hardwired always-on security |
| Door switch | signal only | TBD | TBD | dry contact |
| Winter heater outlet | ~1-2 A run; glow up to ~11 A | 15 A | 12 AWG | exterior reachable; N4 glow may exceed current July converter margin |
| Optional C1000 top-up | up to 10 A, about 240 W | TBD | TBD | manual/fused branch only; disable before it starves critical 24 V loads |

Sizing honesty: current July loads fit the 16 A Orion. Winter heater glow can push the bus toward 18-19 A worst case, so winter use requires glow-window load shedding or a second Orion after bench measurement.

## Lighting And Switches

Switching plan: **put the lighting switches on the power cabinet**, not beside the entry door, for the Juplaya build. This keeps wiring shorter and serviceable. While the walls are open, leave a labeled pull string or spare low-current pair to the side-door bay only if it is easy; a future entry switch can be added later if real use proves it is worth the wire.

Switch hardware: use a **Blue Sea 8260 6-position Contura mounting panel** with **Blue Sea 8282 Contura III SPST OFF-ON black switches**. The 8282 is rated 15 A at 24 V DC, so it has ample margin for these fused lighting branches. The 8260 panel accepts 0.06" to 0.38" mounting thickness; if the power-cabinet face is 1/2" ply, mount the switches in a thin ABS/aluminum inset plate or back-rabbet the cutout. Wire each switch downstream of its Blue Sea 5026 branch fuse.

Recommended switch labels:

| Position | Label | Function |
|---:|---|---|
| 1 | INTERIOR | main/task lighting switch or dimmer enable |
| 2 | CURB FLOOD | two curbside `VAL2-NW9` fixtures |
| 3 | ROAD FLOOD | two roadside `VAL2-NW9` fixtures |
| 4 | NOSE FLOOD | both V-nose `VAL2-NW9` fixtures |
| 5 | REAR FLOOD | rear `VAL2-NW9` loading/work light |
| 6 | AWNING | hard enable for the awning dimmer/strip |

Use custom printed labels for those names; the Blue Sea 8214 label set is useful for generic DC labels but may not include the exact flood-zone names. For the awning strip dimmer, default to the low-cost **Super Bright LEDs `LDK-8A` 12-24 VDC / 8 A PWM dimmer** mounted inside or on the cabinet after the AWNING switch; it has enough margin for the 64 W / ~2.7 A strip. The premium marine alternative is **Blue Sea 7509 Deckhand Dimmer, 24 V DC / 12 A**, which is sealed and panel-integrated but much more expensive.

Use **24 V-native or 10-30 V DC exterior-rated LED fixtures**. The current selected fixture class is 12-28 VDC, so the lights run directly from the 24 V house bus. Do not build a 12 V exterior-lighting sub-bus for this plan, and do not run lighting through cigarette-lighter receptacles. House exterior lights stay completely separate from the OEM trailer lighting and the 7-way plug.

Active exterior layout: **2 curbside floods, 2 roadside floods, 1 flood on each V-nose face, 1 rear flood, plus separate awning lighting**. Count is seven flood fixtures plus the awning light circuit.

Panel verdict: **7 x Super Bright LEDs `VAL2-NW9` flood/scene fixtures are ordered**. It is the same 9" black 1450 lm / 18 W / 90 deg / IP67 / 12-28 VDC fixture class as `VAL2-WW9`, but 4000 K is more useful for work/security floods than 3000 K. `VAL2-WW9` remains the warm-white alternate if replacement stock is ever needed. For the awning, use a separate warm 24 V dimmable strip such as **Super Bright LEDs `RA-IP68-80CRI-5m`, 3000 K** under the case/rail rather than another glare flood.

| Zone | Fixture count | Approx current | Fuse | Wire | Notes |
|---|---:|---:|---|---|
| Interior main/task | TBD | ~2-3 A @ 24 V typical | 5 A | TBD | Yuji strips in aluminum channel; cabinet switch/dimmer |
| Awning/camp light | 1 x 5 m strip max | 64 W max / ~2.7 A @ 24 V before dimming | 5 A | 16-18 AWG | `RA-IP68-80CRI-5m` 3000 K or equivalent; dimmable, diffuse/downward, not a glare bar |
| Curbside floods | 2 x `VAL2-NW9` | 36 W / ~1.5 A @ 24 V | 5 A | 16 AWG | down/out aimed for camp/work; one switch labeled CURB FLOOD |
| Roadside floods | 2 x `VAL2-NW9` | 36 W / ~1.5 A @ 24 V | 5 A | 16 AWG | down/out aimed for roadside work; one switch labeled ROAD FLOOD |
| Nose floods | 2 x `VAL2-NW9` | 36 W / ~1.5 A @ 24 V | 5 A | 16 AWG | one fixture on each V-nose face; one switch labeled NOSE FLOOD unless separate control becomes useful |
| Rear flood | 1 x `VAL2-NW9` | 18 W / ~0.75 A @ 24 V | 5 A | 16 AWG | upper rear/down-aimed loading light, not tied to reverse/tow wiring |
| Optional step/courtesy | 1-2 small amber fixtures | <0.5 A | 3 A or shared 5 A branch | 18 AWG | optional low amber at personnel door/step; can share awning switch |
| Spare exterior/service | TBD | TBD | 5 A | 16-18 AWG | capped spare pair if the wall path is open |

Seven `VAL2-NW9` floods total **126 W / ~5.25 A @ 24 V**. Full awning strip adds **64 W / ~2.7 A @ 24 V** before dimming. That is fine as short-duration lighting, but do not combine all exterior lights with full USB-C load, optional C1000 top-up, and winter heater glow.

Voltage guardrail: because the selected flood fixtures are rated **12-28 VDC**, set and verify the Orion 48/24 output stays below 28 V under all charge/load states. Target normal 24 V output, not a 28+ V "24 V battery charge" profile.

Similar-spec panel considered `VAL2-WW9`, `VAL2-NW9`, the 13"/17"/22" Super Bright LEDs area lights, Optronics `UCL41CB`, TecNiq `P06`, Buyers `1492135`, Abrams Cobalt XS, Handxen 9" 20 W, STEDI/NAPA Mini LED Flood, Hella SM2000, Grote Trilliant, Scandvik E-500, ECCO EW2411, Primelux PX0415, and Home Depot low-voltage deck options. Verdict: `VAL2-NW9` wins the flood positions on 24 V compatibility, output, warm-enough work light, low profile, IP67 rating, and cost. Optronics `UCL41CB` is the best trailer-native fallback; TecNiq `P06` is the rugged premium fallback; Buyers/Abrams are budget fallbacks only if cool or unspecified CCT is acceptable. Oversized 13"/17"/22" fixtures waste too much power for seven positions. See [exterior-lighting panel verdict](../runs/exterior-lighting-panel/synth/VERDICT.md).

Load-shed rule: do not run every flood, full awning strip, full USB-C load, optional C1000 top-up, and winter heater glow at the same time on the 16 A 24 V converter. For Juplaya, all floods are short-duration work/security loads; normal camp mode should be awning/interior lighting only.

## Auxiliary 12 V Cabinet Receptacles

The added Victron Orion-Tr IP43 48/12-20A isolated converter feeds a small set of cigarette-lighter receptacles in the power cabinet. This is for occasional 12 V loads and adapters, not for the fridge, lighting, USB-C PD, GPS, tow-vehicle wiring, or OEM trailer lights.

| Item | Limit | Protection | Notes |
|---|---:|---|---|
| Orion-Tr IP43 48/12-20A | 20 A / 240 W at 12 V | DC-rated 48 V input OCP; output OCP sized to conductor/receptacle | 32-70 V input, 12.2 V nominal output, remote off when unused |
| Cigarette-lighter receptacles | per receptacle rating, total below 20 A | fuse each receptacle branch | install in power cabinet; label auxiliary 12 V only |

The converter's no-load input current is under 80 mA, roughly under 4 W on the 48 V bus. That is small, but still worth switching off by remote when the receptacles are not in use. IP43 protection only applies with the screw terminals facing down.

## C1000 AC Island

The Anker SOLIX C1000 + PS400 panel is portable camp gear, not trailer AC distribution.

Use it for:

- laptops, phones, radios, camera/tool battery chargers
- Starlink-class loads, if needed
- brief small-appliance hits

Do not use it for:

- sustained electric cooking
- electric space heating
- backfeeding trailer AC wiring

Optional 24 V trailer top-up:

- A fused/manual 24 V bus feed into the C1000 XT-60 input is acceptable as a discretionary auxiliary charge path.
- The C1000 accepts 11-32 V at 10 A, so call this about 240 W maximum.
- Enable it only when the trailer battery is healthy and the Orion has spare capacity.
- Keep this top-up on the 24 V bus if used; the 12 V cabinet receptacles would cut the charge rate roughly in half and burn an extra conversion stage.
- Do not direct-feed the C1000 from the 48 V battery unless a dedicated current-limited DC-DC charger is designed later.

## Phase 2 MultiPlus

The Victron MultiPlus-II 48/3000/35-50 120V remains the later integrated inverter/charger recommendation if the trailer needs built-in 120 VAC distribution, shore/generator charging, or automatic transfer.

Deferred because Juplaya does not need it:

- Critical loads are DC.
- The C1000 handles small 120 VAC loads.
- Skipping the built-in inverter removes idle draw, cabinet time, AC wiring, and commissioning risk.

If installed later, treat 2400 W at 25 C / 2200 W at 40 C as the sustained AC design envelope, and cap combined charge current at or below the ComFlex battery's 100 A continuous charge limit.

## Protection And Commissioning

Before energizing:

- Battery side first on MPPTs, then PV.
- Verify roof 3S lands only on the SmartSolar 250/60-Tr.
- Verify optional LG ground 2S lands only on the SmartSolar 150/35.
- Verify PS400 lands only on the C1000.
- Use DC-rated PV disconnect/OCP above worst-case cold roof 3S Voc.
- Fuse/breaker each MPPT battery-side output for controller current and conductor ampacity.
- Make the battery-terminal main OCP explicit; no 32 V automotive fuse gear on the 48 V side.
- Verify the Blue Sea UL-489 breaker SKU: docs have used 7443, web validation surfaced 7463 for the 20 A / 80 V part.
- Fuse/breaker both Orion converter inputs with DC-rated 48 V gear, fuse their outputs for conductor ampacity, and orient the 48/12 Orion screw terminals down if relying on IP43.
- Label the 12 V cabinet receptacles as auxiliary only; do not backfeed tow-vehicle 12 V, OEM trailer lighting, the 24 V bus, or C1000 charging through them.
- Configure LiFePO4 charge profiles: absorption 57.6 V, float about 55.2 V, equalization off, temperature compensation off.
- Cap combined trailer charge current at or below 100 A.
- Test the optional C1000 24 V top-up branch under fridge/lighting load before relying on it.

## Energy Budget

| Load | kWh/day |
|---|---:|
| Fridge, CFX3 95DZ desert duty | 1.0-1.3 |
| 24 V bus / controls overhead | 0.1-0.3 |
| Velit AC realistic duty | ~2.4 |
| **Trailer DC total** | **about 3.5-4.0** |

Roof-only 3S solar makes roughly 6.0 kWh/day before soiling/shading, enough for nominal July DC loads. The expected fridge + realistic Velit + small-DC load is about 3.8 kWh/day, leaving about 2.2 kWh/day clean-sun margin and staying positive through roughly a 25-33% solar derate. Detail: [roof-only 3S fridge + AC math](research/roof-3s-fridge-ac-energy-math-2026-06-05.md).

The optional 2S LG ground pair adds trailer-battery margin for AC-heavy days, dust, Velit shadow, or deficit recovery. The C1000 and PS400 form a separate small-AC budget.

## Open Gates

- Roof drawing: fore-aft solar rails tied into roof bows, panel bracket landings on those rails, Velit opening/shadow line, PV gland, and awning standoff stations.
- Battery-terminal main OCP selection.
- Exact Blue Sea 20 A / 80 V UL-489 breaker SKU.
- Ground MPPT connector variant and portable inlet/disconnect details.
- 12 V cabinet receptacle count, fuse sizes, wire gauge, and remote switch location.
- Exterior lighting final branch wire gauges and penetration/seal details.
- Optional C1000 24 V top-up branch test.
- Real shakedown energy use before leaving the generator home.
