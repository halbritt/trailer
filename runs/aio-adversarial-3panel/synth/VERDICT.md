---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
---

# Corrected 3-Panel AIO Verdict

Corrected premise is binding: three LG455 roof panels fit, and the Velit 2000R fits in the nose. The prior geometry objection is superseded.

## Final Recommendation

**Revise D002, but do not reopen the inverter/charger purchase.** Keep/order the **LiTime 48 V 3500 W AIO** as the inverter, AC charger, and optional ground-string MPPT. Return the mistaken **LiTime 48 V 5 kW AIO**. Add a **Victron SmartSolar MPPT 250/60-Tr** now for the roof array.

July architecture:

```
3 x LG455 roof panels in 3S -> 250 V-class PV disconnect -> Victron SmartSolar MPPT 250/60 -> 48 V bus/battery

optional deployable 2S ground pair -> LiTime 3500 W AIO PV input

LiTime 3500 W AIO -> 120 VAC loads
48 V battery -> fused Velit branch + Orion-Tr 48/24 house bus
```

Cost-sensitive panel plan: put **three owned LG455s on the roof** and keep the fourth panel as a home/damage spare for July. A single leftover panel has no good electrical home on this 48 V system. Buy a fifth matched or current-compatible panel only if you want the deployable 2S ground pair live for July or if shakedown shows the Velit energy duty needs the extra margin.

Buy/return now:

1. Return the LiTime 5 kW AIO.
2. Keep/order the LiTime 48 V 3500 W AIO.
3. Buy a Victron SmartSolar MPPT 250/60-Tr.
4. Buy DC-rated roof PV disconnect/breaker hardware rated above worst-case cold 3S Voc, plus SmartSolar battery-side output protection and conductors.
5. Defer a fifth panel unless preserving a deployable 2S pair is a July requirement.

## 3S Ruling

Confirmed roof 3S **does not change the inverter/charger decision**. It **does change the solar topology**.

Three LG455s in series are invalid on the LiTime 3500 W AIO because cold Voc exceeds its 145 V PV ceiling. The same 3S string is also a poor fit for 120 V-min high-voltage AIOs: LG455 3S is already about 118.8 V Vmpp at NMOT, and hot roof conditions push the true MPP below the 120 V operating floor during the hours when AC load is highest. The reviewers classify that as a reliability problem, not acceptable clipping.

The reliable 3S-positive answer is split MPPT: roof 3S on a 250 V-class Victron controller, with the LiTime 3500 W retained for inverter/charger duties and optional 2S ground charging.

## Options Considered

| Option | Verdict | Reason |
|---|---|---|
| LiTime 3500 W AIO only | Fallback only | Best simple 2S/2S2P box, but wastes the confirmed third roof panel. |
| LiTime 3500 W + Victron SmartSolar 250/60 | **Recommended** | Makes roof 3S electrically real, keeps the inverter sized to one 100 A battery, and preserves the AIO PV input for optional ground 2S. |
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
| Cost | Hybrid adds the SmartSolar and protection hardware; using the fourth panel as a spare avoids a fifth-panel purchase unless ground solar is required. |
| Schedule | Roof row 3 should be installed during the same bare-roof campaign as rows 1-2. If the MPPT slips, wire two roof panels as 2S into the AIO and park panel 3 temporarily. |
| Install risk | Added controller means added OCP, disconnects, charge settings, and cabinet heat. This is manageable and less risky than swapping to a 120 V-min AIO. |
| Ground compatibility | Roof 3S and ground 2S must not share one tracker. The AIO PV input is the ground 2S tracker if a matched pair exists. |

## Required D002 / Build-Sheet Change

Replace D002's solar wording:

- Remove "roof 2S only", "camped 2S2P", and "no external MPPT for July" as the primary design.
- Add "roof 3 x LG455 in 3S through Victron SmartSolar MPPT 250/60-Tr".
- Keep "LiTime 3500 W AIO, 5 kW returned".
- Change "never 3S" to **"never 3S into the LiTime AIO"**.
- State the fourth-panel/fifth-panel rule: current four-panel inventory means 3 roof panels plus one spare; a live deployable 2S pair requires a fifth current-compatible panel.

## Gates That Remain

- Never connect roof 3S to the LiTime 3500 W PV input.
- Physically segregate and label the roof 3S PV path and the optional ground 2S inlet so MC4 mis-plugging is not plausible.
- Use DC-rated PV disconnect/OCP above worst-case cold 3S Voc; do not use 150 V gear if the cold string can exceed it.
- Fuse/breaker the SmartSolar battery-side output for controller current and conductor ampacity.
- Keep battery-terminal main OCP explicit and DC interrupt-rated; no 32 V automotive fuse gear on the 48 V side.
- Program LiTime and Victron LiFePO4 charge settings consistently and disable temperature compensation.
- Cap combined charge current at or below the ComFlex 100 A continuous limit.
- Ventilate and temperature-test the nose cabinet with AIO, SmartSolar, Orion, and Velit branch wiring installed.
- Keep roof drawing and weigh-in gates: panel feet into roof bows, Velit shadow clearance, awning standoff stations, curb/tongue weight, and shakedown PV verification.

## One-Line Verdict

**REVISE D002:** keep the LiTime 3500 W inverter/charger and return the 5 kW, but replace the July solar architecture with roof 3S on a Victron SmartSolar MPPT 250/60-Tr; reserve the AIO PV input for optional deployable 2S, and never route 3S into the AIO.
