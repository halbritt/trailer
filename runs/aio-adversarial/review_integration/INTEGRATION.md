---
author: operator
---

# Integration / Reliability Review: D002

Posture: boring reliability over spec-sheet wins. The Velit is a 48 V DC load, not an inverter load; the single LiTime 48 V 100 Ah battery is the system limit; the nose cabinet is a heat-constrained electronics bay. Bigger AIOs mostly buy idle heat, battery overdraw, and PV-voltage fragility.

Committed recommendation: **revise D002 narrowly, but keep the exact next purchase as the [LiTime 48 V 3500 W AIO](https://www.litime.com/products/48v-3500w-solar-converter-charger).** Return the mistaken 5 kW unit. If the roof drawing proves three LG455 panels plus the Velit really fit, do not switch to a 120 V-min high-voltage AIO; add a separate Victron 250 V-class MPPT for the roof string later, behind explicit charge-current and protection gates.

Scoring: 5 = best reliability fit, 1 = poor fit. Battery, idle heat, and deadline risk are weighted harder than spec-sheet PV watts.

| Candidate | 3-roof harvest | PV margin / hot floor | Single-battery fit | Idle / ECO | AC output fit | Wiring / deadline | Nose heat / weight | Vendor / support | Cost / timing | Net |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LiTime 48 V 3500 W AIO | 2 | 5 | 5 | 3 | 5 | 5 | 4 | 3 | 5 | **35** |
| Keep/repurchase LiTime 48 V 5 kW AIO | 2 | 1 | 1 | 1 | 2 | 3 | 2 | 2 | 2 | **15** |
| [EG4 3000EHV-48](https://eg4electronics.com/categories/inverters/eg4-3000ehv-48-all-in-one-off-grid-inverter) or similar 120 V-min AIO | 2 | 1 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | **30** |
| [Victron MultiPlus-II 48/3000](https://www.victronenergy.com/upload/documents/Datasheet-MultiPlus-II-120V-EN.pdf) + [SmartSolar 250-class MPPT](https://www.victronenergy.com/upload/documents/Manual_SmartSolar_MPPT_150-60_up_to_250-70/29694-MPPT_solar_charger_manual-pdf-en.pdf) | 5 | 5 | 4 | 5 | 3 | 2 | 4 | 5 | 1 | **36** |
| LiTime 3500 W + separate Victron 250-class MPPT if 3 roof panels prove real | 5 | 5 | 5 | 3 | 5 | 3 | 3 | 4 | 2 | **37** |

## Findings

- **The 5 kW LiTime is a reliability regression.** Its 120 V PV floor breaks the current 2S/2S2P plan; three LG455s are only barely plausible by open-circuit ceiling but weak by operating voltage, with 3S NMOT Vmpp at 118.8 V before a hot roof drags it lower. Its <=55 W ECO idle is a 1.3 kWh/day tax, and 5 kW sustained output exceeds the single battery's 100 A continuous comfort zone once inverter losses and any simultaneous 48 V DC load are counted. Source: [LiTime 5 kW](https://www.litime.com/products/48v-5kw-solar-inverter-charger), [LG455 repo reference](../../../docs/reference/lg455n2w-e6-datasheet.md), [battery reference](../../../docs/reference/litime-48v-100ah-battery-specs.md).
- **High-voltage AIOs do not solve this roof cleanly.** EG4/Growatt/MPP-style 120 V-min units make 3S look attractive on a spec sheet, but the LG455 3S hot/NMOT MPP voltage sits at or below the floor. A mobile hot roof is exactly where MPPT floor margin disappears. They also do not improve the actual load fit because the rooftop AC bypasses the inverter.
- **The LiTime 3500 W is the least-bad immediate one-box fit.** 2S roof and 2S2P camped strings sit in the 60-145 V operating window and the 60-115 V recommended band; 3500 W AC draw is about 75 A class instead of 100+ A class; weight and heat are lower than the 5 kW. Its idle still matters: <30 W ECO is roughly 0.72 kWh/day, so ECO/off discipline is not optional.
- **Victron is the strongest engineering alternative, not the immediate buy.** MultiPlus-II + SmartSolar gives the best support ecosystem, very low idle, modular serviceability, and real 3S MPPT compatibility. The penalty is higher cost, more protection/wiring design, more install time, and lower continuous inverter output than the LiTime 3500 W. That is a real counterargument, but it misses the near-term deadline unless the owner is willing to reopen the whole power install.
- **Three roof panels should change only the solar sub-architecture.** If the measured roof drawing proves three panels plus the [Velit 2000R](https://www.tecvan.com/products/velit-2000r-mini-rooftop-air-conditioner-12-48v) fit, run the roof as 3S into a separate Victron 250 V-class MPPT. Leave the LiTime 3500 W as inverter/charger and use its internal MPPT for the deployable 2S ground pair or leave it unused when roof-only.

## Required Outputs

1. **Recommended architecture and exact next purchase:** buy the LiTime 48 V 3500 W AIO now; keep the existing 48 V battery, 24 V Orion house bus, Velit on its own fused 48 V branch, roof 2S plus deployable 2S ground pair for July. Revise D002 to allow a later separate Victron 250 V-class MPPT only if the roof drawing proves three roof panels.

2. **Whether the mistaken 5 kW LiTime should still be returned:** yes. Return it. It is worse for this single-battery trailer: higher idle, more nose-cabinet heat, worse 2S compatibility, marginal 3S hot-roof tracking, more AC output than the battery can continuously support, and no benefit to the DC rooftop AC.

3. **Whether 3 roof panels should change the inverter decision:** no. Three roof panels may justify a separate 250 V-class MPPT; they do not justify a 120 V-min AIO. Do not let roof-panel optimism drag the inverter into a worse battery/idle/heat fit.

4. **Strongest counterargument:** full Victron is the reliability purist answer. It has better support, lower idle, better configurability, and a 250 V MPPT path that actually likes 3S LG455. If the owner can absorb cost, parts count, and schedule churn, it is the better long-term ecosystem than LiTime.

5. **Required gates or install notes:** cap total charge current <=100 A; set and test ECO/off discipline; never connect 3S to the LiTime 3500 W PV input; make battery-terminal main OCP explicit, preferably Class-T; use DC-rated PV disconnects and OCP; ventilate the nose cabinet and verify cabinet temperature under desert sun with AIO + Orion + Velit branch wiring installed; keep the battery low/centered and re-weigh tongue; if adding external MPPT, coordinate charge limits so AIO AC/PV plus external MPPT cannot exceed the battery cap.

6. **One-line verdict for D002:** **revise**: keep the LiTime 3500 W purchase and 5 kW return, but add a gated external-250 V-MPPT fork for a proven three-panel roof and harden the charge-current, idle, OCP, and nose-cabinet heat gates.
