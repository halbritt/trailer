---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
---

# Corrected 3-Panel House-Charger Verdict

Corrected premise is binding: three LG455 roof panels fit, and the Velit 2000R fits in the nose. The prior geometry objection is superseded.

Post-run correction from owner: the 5 kW LiTime AIO is the accidentally ordered unit to return; the 3.5 kW LiTime is **not owned yet** and is only a candidate replacement house charger. Five LG455 panels are available total. Ground panels are optional margin, not a house-charger requirement.

Owner read after the corrected run: the verdict should be **Victron**, because once roof 3S is handled by a dedicated SmartSolar controller and ground solar is optional, the house charger should be selected on inverter/charger quality, idle draw, monitoring/programming, support, and battery fit rather than on the LiTime AIO's extra MPPT input.

## Final Recommendation

**Revise D002 around the Victron house-charger purchase.** Return the mistaken **LiTime 48 V 5 kW AIO** and buy the **Victron MultiPlus-II 48/3000/35-50 120V** as the house inverter/charger. Buy a **Victron SmartSolar MPPT 250/60-Tr** for the three-panel roof array.

July architecture:

```
3 x LG455 roof panels in 3S -> 250 V-class PV disconnect -> Victron SmartSolar MPPT 250/60 -> 48 V bus/battery

optional deployable 2S ground pair -> separate small 150 V-class MPPT, if used

Victron MultiPlus-II 48/3000/35-50 120V -> 120 VAC loads
48 V battery -> fused Velit branch + Orion-Tr 48/24 house bus
```

Panel plan: put **three LG455s on the roof** as the primary array. The remaining two panels can be used as an optional deployable 2S ground pair when the extra margin is worth the setup; if used with the Victron house charger, they need their own MPPT. If that extra controller is not worth the schedule/cost, skip ground solar for July.

Buy/return now:

1. Return the LiTime 5 kW AIO.
2. Buy the Victron MultiPlus-II 48/3000/35-50 120V.
3. Buy a Victron SmartSolar MPPT 250/60-Tr.
4. Buy DC-rated roof PV disconnect/breaker hardware rated above worst-case cold 3S Voc, plus SmartSolar battery-side output protection and conductors.
5. Optional: buy a small 150 V-class MPPT for the deployable 2S ground pair if camped ground solar remains worth it.

## 3S Ruling

Confirmed roof 3S **does not require a high-voltage AIO**. It **does require split MPPT solar**.

Three LG455s in series are invalid on 145/150 V-class AIO inputs because cold Voc exceeds that ceiling. The same 3S string is also a poor fit for 120 V-min high-voltage AIOs: LG455 3S is already about 118.8 V Vmpp at NMOT, and hot roof conditions push the true MPP below the 120 V operating floor during the hours when AC load is highest. The reviewers classify that as a reliability problem, not acceptable clipping.

The reliable 3S-positive answer is roof 3S on a 250 V-class Victron controller. Once that is accepted, the inverter/charger can be chosen separately. The MultiPlus-II wins on idle behavior, charger/inverter quality, ecosystem, programming, and monitoring. The LiTime 3500 W remains the budget fallback, not the primary recommendation.

## Options Considered

| Option | Verdict | Reason |
|---|---|---|
| Victron MultiPlus-II 48/3000 + SmartSolar 250/60 | **Recommended house-charger verdict** | Best ecosystem, idle draw, charging/programming, and monitoring. Lower sustained AC output and higher cost/weight are accepted tradeoffs. |
| LiTime 3500 W + Victron SmartSolar 250/60 | Budget fallback | Makes roof 3S electrically real and provides more rated AC watts for less money, but loses to Victron on idle, ecosystem, docs/support, and serviceability. |
| LiTime 3500 W AIO only | Fallback only | Simple 2S/2S2P box, but wastes the confirmed third roof panel unless the roof SmartSolar is added. |
| Keep LiTime 5 kW AIO | Reject | 120 V MPPT floor is weak with hot LG455 3S, idle heat is worse, 2S ground is stranded, and 5 kW output exceeds a single ComFlex pack's comfortable continuous limit. |
| EG4 / 120 V-min HV AIO class | Reject | Better ecosystem than LiTime does not fix the 120 V floor or the 2S ground incompatibility. |
| Victron EasySolar-II GX | Reject | Integrated 250 V MPPT package is not a clean US 120 VAC trailer replacement. |
| 145/150 V AIO class | Reject | LG455 3S has no cold-Voc margin. |

## Reasoning Matrix

| Factor | Decision pressure |
|---|---|
| PV fit | 3S roof fits physically, but only a 250 V-class MPPT fits it electrically across cold and hot conditions. |
| Battery fit | One 48 V 100 Ah ComFlex pack favors the ~2.5-3.5 kW inverter class. MultiPlus-II 48/3000 fits comfortably; the 5 kW LiTime does not. |
| Idle | MultiPlus-II wins clearly: 11 W normal, 7 W AES, 2 W Search versus the LiTime 3500 W's <30 W ECO / <50 W normal. |
| Load fit | MultiPlus-II sustained AC output is lower: 2400 W at 25 C and 2200 W at 40 C. That is acceptable because the Velit is a DC load, but it requires high-draw AC discipline. |
| Cost | Victron costs more and adds modular wiring. That is the primary argument for the LiTime 3500 W fallback. |
| Schedule | The roof SmartSolar path should be installed during the same bare-roof campaign as the panel mounts. The optional ground MPPT can slip without blocking the house charger. |
| Install risk | Modular Victron adds boxes and protection hardware, but removes the weak AIO MPPT compromise and gives better settings/visibility. |
| Ground compatibility | Roof 3S and ground 2S must not share one tracker. Under the Victron verdict, the ground pair either gets its own MPPT or is skipped. |

## Required D002 / Build-Sheet Change

Replace D002's house-charger and solar wording:

- Remove "LiTime 3500 W is the proposed replacement purchase" as the primary recommendation.
- Add "Victron MultiPlus-II 48/3000/35-50 120V is the proposed house inverter/charger purchase."
- Keep "return the ordered LiTime 5 kW."
- Add "roof 3 x LG455 in 3S through Victron SmartSolar MPPT 250/60-Tr."
- Change "never 3S" to **"never 3S into any 145/150 V-class AIO input"**.
- State the five-panel inventory: 3 roof panels primary, 2 deployable ground panels optional.
- State that optional ground 2S needs a separate small MPPT if used with the Victron house charger.

## Gates That Remain

- Never connect roof 3S to a 145/150 V-class AIO PV input.
- Physically segregate and label the roof 3S PV path and any optional ground 2S inlet so MC4 mis-plugging is not plausible.
- Use DC-rated PV disconnect/OCP above worst-case cold 3S Voc; do not use 150 V gear if the cold string can exceed it.
- Fuse/breaker the SmartSolar battery-side output for controller current and conductor ampacity.
- Keep battery-terminal main OCP explicit and DC interrupt-rated; no 32 V automotive fuse gear on the 48 V side.
- Program Victron LiFePO4 charge settings consistently and disable temperature compensation where appropriate.
- Cap combined charge current at or below the ComFlex 100 A continuous limit.
- Ventilate and temperature-test the nose cabinet with MultiPlus, SmartSolar, Orion, and Velit branch wiring installed.
- Treat ~2200 W at 40 C as the sustained 120 VAC design envelope.
- Keep roof drawing and weigh-in gates: panel feet into roof bows, Velit shadow clearance, awning standoff stations, curb/tongue weight, and shakedown PV verification.

## One-Line Verdict

**REVISE D002:** return the ordered LiTime 5 kW; buy the Victron MultiPlus-II 48/3000/35-50 120V as the house inverter/charger; pair the confirmed roof 3S array with a Victron SmartSolar MPPT 250/60-Tr; treat the 2S ground pair as optional margin on its own MPPT.
