---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
---

# Corrected 3-Panel AIO Verdict

Corrected premise is binding: three LG455 roof panels fit, and the Velit 2000R fits in the nose. The prior geometry objection is superseded.

Post-run correction from owner: the 5 kW LiTime AIO is the accidentally ordered unit to return; the 3.5 kW LiTime is **not owned yet** and is only a candidate replacement house charger. Five LG455 panels are available total. Ground panels are optional margin, not a house-charger requirement.

## Final Recommendation

**Revise D002 around the house-charger purchase.** The current recommendation is to **buy the LiTime 48 V 3500 W AIO** as the inverter/AC charger and return the mistaken **LiTime 48 V 5 kW AIO**. Add a **Victron SmartSolar MPPT 250/60-Tr** now for the roof array.

July architecture:

```
3 x LG455 roof panels in 3S -> 250 V-class PV disconnect -> Victron SmartSolar MPPT 250/60 -> 48 V bus/battery

optional deployable 2S ground pair -> LiTime 3500 W AIO PV input if LiTime is selected

LiTime 3500 W AIO -> 120 VAC loads
48 V battery -> fused Velit branch + Orion-Tr 48/24 house bus
```

Panel plan: put **three LG455s on the roof** as the primary array. The remaining two panels can be used as an optional deployable 2S ground pair when the extra margin is worth the setup. If the house charger changes away from the LiTime 3500 AIO, the ground pair either needs its own small MPPT or gets skipped.

Buy/return now:

1. Return the LiTime 5 kW AIO.
2. Buy the LiTime 48 V 3500 W AIO **if accepting this low-cost house-charger recommendation**.
3. Buy a Victron SmartSolar MPPT 250/60-Tr.
4. Buy DC-rated roof PV disconnect/breaker hardware rated above worst-case cold 3S Voc, plus SmartSolar battery-side output protection and conductors.
5. Treat the deployable 2S ground pair as optional margin, not as a requirement that controls the house-charger choice.

## 3S Ruling

Confirmed roof 3S **does not change the inverter/charger decision**. It **does change the solar topology**.

Three LG455s in series are invalid on the LiTime 3500 W AIO because cold Voc exceeds its 145 V PV ceiling. The same 3S string is also a poor fit for 120 V-min high-voltage AIOs: LG455 3S is already about 118.8 V Vmpp at NMOT, and hot roof conditions push the true MPP below the 120 V operating floor during the hours when AC load is highest. The reviewers classify that as a reliability problem, not acceptable clipping.

The reliable 3S-positive answer is split MPPT: roof 3S on a 250 V-class Victron controller, with the house charger selected primarily for 48 V battery fit, AC charging, inverter output, idle draw, cost, and schedule. The LiTime 3500 W remains the low-cost recommendation; its ability to accept optional 2S ground solar is a secondary benefit.

## Options Considered

| Option | Verdict | Reason |
|---|---|---|
| LiTime 3500 W AIO only | Fallback only | Best simple 2S/2S2P box, but wastes the confirmed third roof panel. |
| LiTime 3500 W + Victron SmartSolar 250/60 | **Recommended low-cost house-charger path** | Makes roof 3S electrically real, keeps the inverter sized to one 100 A battery, and optionally accepts ground 2S. |
| Keep LiTime 5 kW AIO | Reject | 120 V MPPT floor is weak with hot LG455 3S, idle heat is worse, 2S ground is stranded, and 5 kW output exceeds a single ComFlex pack's comfortable continuous limit. |
| EG4 / 120 V-min HV AIO class | Reject | Better ecosystem does not fix the 120 V floor or the 2S ground incompatibility. |
| Victron MultiPlus-II + SmartSolar | Strong but not July-best | Best ecosystem and idle behavior, but more cost, more wiring, and lower continuous 120 VAC output than the LiTime 3500 W. |
| Victron EasySolar-II GX | Reject | Integrated 250 V MPPT package is not a clean US 120 VAC trailer replacement. |
| 145/150 V AIO class | Reject | LG455 3S has no cold-Voc margin. |

## Reasoning Matrix

| Factor | Decision pressure |
|---|---|
| PV fit | 3S roof fits physically, but only a 250 V-class MPPT fits it electrically across cold and hot conditions. |
| Battery fit | One 48 V 100 Ah ComFlex pack favors a 3500 W inverter, not 5 kW continuous output. |
| Idle | LiTime 3500 W is materially better than the 5 kW; Victron modular is best but not enough to justify the July churn. |
| Load fit | 3500 W covers intended AC loads while Velit stays on DC. Avoid sustained full AC load plus Velit turbo plus max 24 V load on one battery. |
| Cost | Hybrid adds the SmartSolar and protection hardware. Five panels are available, but ground solar remains optional and should not dominate the house-charger decision. |
| Schedule | Roof row 3 should be installed during the same bare-roof campaign as rows 1-2. If the MPPT slips, wire two roof panels as 2S into the AIO and park panel 3 temporarily. |
| Install risk | Added controller means added OCP, disconnects, charge settings, and cabinet heat. This is manageable and less risky than swapping to a 120 V-min AIO. |
| Ground compatibility | Roof 3S and ground 2S must not share one tracker. The AIO PV input is the ground 2S tracker if a matched pair exists. |

## Required D002 / Build-Sheet Change

Replace D002's solar wording:

- Remove "roof 2S only", "camped 2S2P", and "no external MPPT for July" as the primary design.
- Add "roof 3 x LG455 in 3S through Victron SmartSolar MPPT 250/60-Tr".
- State "5 kW LiTime is ordered by mistake and should be returned; LiTime 3500 W is the proposed replacement purchase, not owned."
- Change "never 3S" to **"never 3S into the LiTime AIO"**.
- State the five-panel inventory: 3 roof panels primary, 2 deployable ground panels optional.

## Gates That Remain

- Never connect roof 3S to the LiTime 3500 W PV input.
- Physically segregate and label the roof 3S PV path and any optional ground 2S inlet so MC4 mis-plugging is not plausible.
- Use DC-rated PV disconnect/OCP above worst-case cold 3S Voc; do not use 150 V gear if the cold string can exceed it.
- Fuse/breaker the SmartSolar battery-side output for controller current and conductor ampacity.
- Keep battery-terminal main OCP explicit and DC interrupt-rated; no 32 V automotive fuse gear on the 48 V side.
- Program LiTime and Victron LiFePO4 charge settings consistently and disable temperature compensation.
- Cap combined charge current at or below the ComFlex 100 A continuous limit.
- Ventilate and temperature-test the nose cabinet with AIO, SmartSolar, Orion, and Velit branch wiring installed.
- Keep roof drawing and weigh-in gates: panel feet into roof bows, Velit shadow clearance, awning standoff stations, curb/tongue weight, and shakedown PV verification.

## One-Line Verdict

**REVISE D002:** return the ordered LiTime 5 kW; current house-charger recommendation is to buy the LiTime 3500 W and pair it with roof 3S on a Victron SmartSolar MPPT 250/60-Tr. Treat the 2S ground pair as optional margin, and never route 3S into any 145 V-class AIO input.
