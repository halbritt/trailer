---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
---

# Corrected 3-Panel House-Power Verdict

Corrected premise is binding: three LG455 roof panels fit, and the Velit 2000R fits in the nose. The prior geometry objection is superseded.

Post-run corrections from owner:

- The 5 kW LiTime AIO is the accidentally ordered unit to return.
- The 3.5 kW LiTime is **not owned** and is only a fallback candidate.
- Five LG455 panels are available total.
- Ground panels are optional margin, not a house-charger requirement.
- The owner already has an **Anker SOLIX C1000** with its own **PS400 400 W solar panel**.

## Final Recommendation

**Revise D002 around Juplaya readiness, not a built-in inverter purchase.** Return the mistaken **LiTime 48 V 5 kW AIO**. Do **not** buy/install the MultiPlus-II for Juplaya unless a must-have built-in 120 VAC load appears. Use the **Anker SOLIX C1000 + PS400** as the standalone small-AC island and leave the generator home if sustained electric cooking/heating/tool loads are out of scope.

Build the trailer's DC power path now:

```
3 x LG455 roof panels in 3S -> 250 V-class PV disconnect -> Victron SmartSolar MPPT 250/60 -> 48 V bus/battery

optional 2 x LG455 deployable ground pair in 2S -> separate small 150 V-class MPPT, if used

48 V battery -> fused Velit branch + Orion-Tr 48/24 house bus

Anker PS400 400 W panel -> Anker SOLIX C1000 -> portable 120 VAC loads

optional manual 24 V bus top-up -> fused branch -> C1000 XT-60 input (~240 W max)
```

Buy/return now:

1. Return the LiTime 5 kW AIO.
2. Buy a Victron SmartSolar MPPT 250/60-Tr.
3. Buy DC-rated roof PV disconnect/breaker hardware rated above worst-case cold 3S Voc, plus SmartSolar battery-side output protection and conductors.
4. Buy/allocate the Orion-Tr 48/24, distribution, and trailer DC protection parts.
5. Use the ordered Victron SmartSolar MPPT 150/35 for the deployable 2S LG ground pair if extra trailer-battery margin remains worth it.
6. Defer the Victron MultiPlus-II 48/3000/35-50 120V to Phase 2.

## 3S Ruling

Confirmed roof 3S **does not require a high-voltage AIO**. It **does require split MPPT solar**.

Three LG455s in series are invalid on 145/150 V-class AIO inputs because cold Voc exceeds that ceiling. The same 3S string is also a poor fit for 120 V-min high-voltage AIOs: LG455 3S is already about 118.8 V Vmpp at NMOT, and hot roof conditions push the true MPP below the 120 V operating floor during the hours when AC load is highest. The reviewers classify that as a reliability problem, not acceptable clipping.

The reliable 3S-positive answer is roof 3S on a 250 V-class Victron controller. Once that is accepted, the inverter/charger decision can be separated from the solar decision. The C1000/PS400 now covers small 120 VAC loads for Juplaya, so the built-in trailer inverter/charger can wait.

## Options Considered

| Option | Verdict | Reason |
|---|---|---|
| Roof SmartSolar 250/60 + trailer DC loads + C1000/PS400 AC island | **Recommended Juplaya path** | Fastest, cheapest, lowest idle, leaves generator behind, and keeps critical loads on DC. |
| Victron MultiPlus-II 48/3000 + SmartSolar 250/60 | Phase 2 / ultimate integrated path | Best built-in inverter/charger ecosystem for later shore/generator charging, transfer, and trailer AC distribution. Not needed for Juplaya small AC loads because C1000 exists. |
| LiTime 3500 W + SmartSolar 250/60 | Budget integrated fallback | More rated AC watts for less money than Victron, but loses on idle, ecosystem, docs/support, and serviceability. |
| LiTime 3500 W AIO only | Fallback only | Simple 2S/2S2P box, but wastes the confirmed third roof panel unless the roof SmartSolar is added. |
| Keep LiTime 5 kW AIO | Reject | 120 V MPPT floor is weak with hot LG455 3S, idle heat is worse, 2S ground is stranded, and 5 kW output exceeds a single ComFlex pack's comfortable continuous limit. |
| EG4 / 120 V-min HV AIO class | Reject | Better ecosystem than LiTime does not fix the 120 V floor or the 2S ground incompatibility. |
| Victron EasySolar-II GX | Reject | It was considered. It integrates the right 250 V-class MPPT idea, but the EasySolar-II GX line is a 230 VAC / 50 Hz product, not a clean US 120 VAC trailer replacement; it also solves a built-in inverter/charger problem now deferred for Juplaya. |
| 145/150 V AIO class | Reject | LG455 3S has no cold-Voc margin. |

## Reasoning Matrix

| Factor | Decision pressure |
|---|---|
| Critical Juplaya loads | Velit is 48 V DC; fridge/lights/USB/GPS are 24 V DC. The trailer does not need built-in 120 VAC to run the mission-critical loads. |
| Small AC loads | C1000 supplies 1056 Wh and 1800 W AC output; PS400 gives it its own 400 W solar source. That is enough for chargers, laptops, radios, Starlink-class loads, and brief small-appliance use. |
| C1000 trailer top-up | Plausible from the 24 V bus because the C1000 accepts 11-32 V at 10 A, but it is a discretionary ~240 W load on the same 16 A Orion-Tr that feeds fridge/lights/USB. |
| Generator | Generator can stay home if sustained 120 VAC cooking/heating/tool loads are excluded and C1000/PS400 testing passes. |
| PV fit | 3S roof fits physically, but only a 250 V-class MPPT fits it electrically across cold and hot conditions. |
| Battery fit | One 48 V 100 Ah ComFlex pack is comfortable for the DC trailer loads and a later ~3 kVA inverter, but not for sustained 5 kW AC output. |
| Idle | Deferring a built-in inverter removes idle draw entirely. C1000 is powered only when small AC is needed. |
| Cost/schedule | Skipping MultiPlus for Juplaya saves money, cabinet time, wiring, AC distribution work, and commissioning risk. |
| Ground compatibility | Roof 3S and LG ground 2S must not share one tracker. Under the Juplaya path, the ordered SmartSolar 150/35 handles the LG ground pair if used. The Anker PS400 feeds only the C1000. |

## Required D002 / Build-Sheet Change

Replace D002's house-charger and solar wording:

- Remove "buy Victron MultiPlus-II now" as the Juplaya recommendation.
- Add "defer built-in inverter/charger for Juplaya; use Anker SOLIX C1000 + PS400 as the small 120 VAC island."
- Keep "return the ordered LiTime 5 kW."
- Keep "roof 3 x LG455 in 3S through Victron SmartSolar MPPT 250/60-Tr."
- Change "never 3S" to **"never 3S into any 145/150 V-class AIO input"**.
- State the five-LG-panel inventory: 3 roof panels primary, 2 deployable ground panels optional.
- State that optional LG ground 2S uses the ordered SmartSolar 150/35 if used for the trailer battery.
- State that the Anker PS400 feeds the C1000 only and must not be mixed with LG strings.
- Allow an optional fused/manual 24 V bus top-up branch into the C1000 XT-60 input, capped by the C1000 11-32 V / 10 A band; do not make it automatic until bus capacity is tested.
- Keep MultiPlus-II 48/3000/35-50 120V as the Phase 2 built-in inverter/charger pick.

## Gates That Remain

- Never connect roof 3S to a 145/150 V-class AIO PV input.
- Physically segregate and label the roof 3S PV path, optional LG ground 2S inlet, and Anker PS400/C1000 path so mis-plugging is not plausible.
- Use DC-rated PV disconnect/OCP above worst-case cold 3S Voc; do not use 150 V gear if the cold string can exceed it.
- Fuse/breaker the SmartSolar battery-side output for controller current and conductor ampacity.
- Keep battery-terminal main OCP explicit and DC interrupt-rated; no 32 V automotive fuse gear on the 48 V side.
- Program Victron LiFePO4 charge settings consistently and disable temperature compensation where appropriate.
- Cap combined trailer charge current at or below the ComFlex 100 A continuous limit.
- Keep C1000 shaded/ventilated and within its temperature limits.
- Do not tie the trailer 48 V bus directly into the C1000 solar input without a purpose-built current-limited DC-DC charger.
- If the C1000 is charged from the 24 V bus, fuse/switch the branch, treat it as a discretionary load, and verify it does not overload the 16 A Orion-Tr or starve the fridge.
- Shakedown-test C1000/PS400 against actual small AC loads before leaving the generator home.
- Keep roof drawing and weigh-in gates: panel feet into roof bows, Velit shadow clearance, awning standoff stations, curb/tongue weight, and shakedown PV verification.

## One-Line Verdict

**REVISE D002:** return the ordered LiTime 5 kW; skip the built-in inverter/charger for Juplaya; run critical loads from roof 3S + SmartSolar + 48/24 V DC distribution; use the Anker SOLIX C1000 + PS400 as the portable 120 VAC island; keep Victron MultiPlus-II 48/3000/35-50 120V as Phase 2.
