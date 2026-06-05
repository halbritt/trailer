---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
---

# AIO Inverter/Charger Purchase Verdict

Final recommendation: **buy the LiTime 48 V 3500 W AIO replacement and return the mistaken LiTime 48 V 5 kW unit.** Keep D002's July architecture: 48 V ComFlex battery, LiTime 3500 W AIO for AC loads and the main MPPT, two LG455 roof panels in 2S, and the two deployable LG455 panels joining as a second 2S string for 2S2P when camped.

The adversarial run did not find a better buy-now replacement. It did find one valid future fork: if a measured roof drawing later proves three roof panels plus the Velit station really fit, add a separate 250 V-class MPPT for that roof string. Do not change the inverter/charger purchase to chase 3S.

## 1. Buy / Return Now

- **Buy now:** LiTime 48 V 3500 W solar inverter charger.
- **Return now:** LiTime 48 V 5 kW solar inverter charger ordered by mistake.
- **Do not buy now:** EG4/Growatt/MPP-style high-voltage AIO, full Victron stack, or a separate MPPT.
- **Keep installed architecture:** roof 2S into the LiTime 3500 W; camped deployable 2S pair paralleled as 2S2P; Velit remains a fused 48 V DC branch, not an inverter load.

Why: the single 48 V 100 Ah battery and the roof geometry are the controlling constraints. The 3500 W LiTime fits both. The 5 kW and high-voltage AIO class do not.

## 2. 3S / Three-Roof-Panel Ruling

The third roof panel is not a reason to change the inverter.

Physical fit is not frozen: the measured roof rectangle is 84-7/8" x 145.5". Three landscape LG455 rows consume about 123.1" of length, leaving about 22.4" of rectangle before the nose. The Velit exterior unit is about 26" square, so a three-panel roof requires a still-unproven nose placement for the AC and clear awning/standoff stations.

Electrical fit is worse:

| String | Practical result |
|---|---|
| 1S | Too low to charge a 48 V battery through a normal buck MPPT. |
| 2S | Correct for the LiTime 3500 W: mid-window in the 60-145 V operating range and 60-115 V recommended band. |
| 3S | Invalid on the LiTime 3500 W: 149.7 V STC Voc before cold correction, above the 145 V ceiling. |
| 3S on 120 V-min AIO | Marginal to bad: 3S NMOT Vmpp is 118.8 V before hotter-roof derating, so the MPPT floor is the wrong side of the real operating voltage. |

Conclusion: **3S is electrically homeless on the AIO choices.** It is too high for the LiTime 3500 W and too low under hot operating conditions for the high-voltage AIO class. If three roof panels become real later, the clean path is LiTime 3500 W plus a separate Victron SmartSolar 250-class MPPT, not a different AIO.

## 3. Options Considered

| Option | PV fit | Battery fit | Idle / heat | Load fit | Cost / schedule | Verdict |
|---|---|---|---|---|---|---|
| **LiTime 48 V 3500 W AIO** | Best AIO fit for 2S/2S2P; never 3S | Best one-box fit for one 100 A pack; ~75 A max inverter draw class | Real idle tax, but lower than 5 kW; requires ECO/off discipline | 3500 W AC covers tools/induction; Velit is DC-native | Cheapest and simplest replacement | **Buy now** |
| LiTime 48 V 5 kW AIO | 120 V MPPT floor breaks 2S and makes 3S hot-roof marginal | Sustained 5 kW is beyond the single pack's comfortable continuous output | Higher idle and more nose-cabinet heat | Extra AC output does not help the DC rooftop AC | Already wrong order; more cost | **Return** |
| EG4 3000EHV / HV AIO class | Same 120 V floor trap; cannot use 2S | Better than 5 kW on output size, but no battery-vendor advantage | Idle still material | Lower AC output than LiTime 3500 | More churn; does not solve roof | **Reject now** |
| Full Victron MultiPlus-II + SmartSolar 250 | Electrically best for 3S with real MPPT margin | Strong ecosystem and configurability | Best idle/support posture | Lower continuous AC than LiTime 3500 | More boxes, cost, protection design, and schedule risk | **Best long-term purist option, not the buy-now answer** |
| LiTime 3500 W + later SmartSolar 250-class MPPT | Best hybrid: 2S/2S2P stays valid; 3S roof becomes valid only if roof fit proves out | Keeps the sane inverter/battery sizing | Adds heat/parts only if the third panel is real | Preserves 3500 W AC | Deferrable; no July dependency | **Allowed future fork** |

## 4. Required D002 / Build-Sheet Change

D002 stays **accepted** with the LiTime 48 V 3500 W AIO as the committed replacement. The doc should record the adversarial review result and add this explicit escape hatch:

> A third roof panel does not change the inverter/charger purchase. If the roof drawing later proves three roof panels plus the Velit and awning stations fit, only then consider a separate 250 V-class MPPT for the roof string. Never route 3S into the LiTime 3500 W, and do not replace the AIO with a 120 V-min high-voltage unit for this trailer.

## 5. Gates That Remain Binding

- **Never 3S into the LiTime 3500 W.**
- **Do not use a 120 V-min high-voltage AIO as the replacement** unless the panel/string plan is completely different from the current LG455 roof.
- **Cap total charge current to <=100 A** for the single LiTime 48 V 100 Ah ComFlex battery.
- **Use ECO/off discipline** because AIO idle draw remains a real energy-budget line.
- **Make battery-terminal main OCP explicit** and use DC-rated PV disconnect/OCP.
- **Ventilate and temperature-check the nose cabinet** with AIO, Orion, and Velit branch wiring installed.
- **Gate any third-panel/external-MPPT purchase behind the measured roof drawing and weigh-in.**

## One-Line Verdict

**KEEP D002:** buy the LiTime 48 V 3500 W AIO now, return the 5 kW unit, stay 2S roof / 2S2P camped for July, and allow only a future separate 250 V-class MPPT if measured roof geometry later proves a three-panel roof.

## Source Pack

- Review lanes: [solar](../review_solar/SOLAR.md), [integration](../review_integration/INTEGRATION.md), [budget](../review_budget/BUDGET.md).
- Evidence brief: [aio-inverter-evidence-2026-06-05.md](../../../docs/research/aio-inverter-evidence-2026-06-05.md).
- Current product pages checked: [LiTime 3500 W](https://www.litime.com/products/48v-3500w-solar-converter-charger), [LiTime 5 kW](https://www.litime.com/products/48v-5kw-solar-inverter-charger), [EG4 3000EHV spec sheet](https://eg4electronics.com/backend/wp-content/uploads/2022/07/EG4-3000EHV-48-Spec-Sheet.pdf), [Victron SmartSolar 250-class specs](https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-60_up_to_250-70/en/technical-specifications.html), [Victron MultiPlus-II 120 V datasheet](https://www.victronenergy.com/upload/documents/Datasheet-MultiPlus-II-120V-EN.pdf).
