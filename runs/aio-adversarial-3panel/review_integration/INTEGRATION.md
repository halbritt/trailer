---
author: operator
---

# Electrical Integration / Reliability Review: D002

Binding premise accepted: three LG455 roof panels fit, and the Velit 2000R fits in the nose. I am not using roof geometry to reject 3S. The integration problem is that D002's inverter choice and D002's "no external MPPT / roof 2S only" solar plan now diverge: the LiTime 3500 W AIO is still the right inverter/charger for one LiTime 48 V 100 Ah battery, but it cannot make a confirmed third roof panel productive.

## Findings

- **Steelman for a 3S-positive one-box AIO:** keep the mistaken LiTime 5 kW or buy an EG4 3000EHV-class unit, wire the roof as 3S, avoid a separate roof controller, keep PV current low, and use the 500 V-class PV ceiling to make cold Voc safe. The LiTime 5 kW also avoids return logistics and has a 100 A combined charge limit that matches the single ComFlex battery's max charge rating.
- **Why that one-box 3S answer fails:** 3S LG455 is at 118.8 V Vmpp at NMOT before July roof heat. Hot-roof Vmpp is in the roughly 104-115 V range, below a 120 V-min MPPT. I classify this as **intermittent tracking that becomes a hard reliability problem**, not acceptable clipping: the controller may wake on Voc, but it cannot be counted on to track the true MPP during the peak-hot hours that also drive AC load. A 120 V-min AIO also strands the deployable 2S ground pair because the ground string's Vmpp is only about 79 V at NMOT.
- **The reliable 3S-positive architecture is split MPPT, not a high-voltage AIO:** roof 3S goes to a Victron SmartSolar 250-class MPPT; the deployable 2S ground pair goes to the LiTime 3500 W AIO's internal MPPT. The Victron 250 V ceiling has cold-Voc margin for LG455 3S, and its low PV start/track threshold is compatible with hot-roof 3S Vmpp instead of fighting a 120 V floor. That preserves the sane inverter/battery fit while making all three roof panels usable.
- **The single battery is still the system limit:** the ComFlex is 51.2 V, 100 Ah, 100 A continuous charge/discharge. The LiTime 3500 W output draws about 75-80 A DC at full AC load before simultaneous 48 V loads; the Velit can add about 5-14 A and the 24 V converter can add another several amps. Full 3.5 kW AC plus Velit turbo plus a loaded 24 V bus can brush the 100 A continuous battery limit, so the 3500 W AIO is acceptable only with load discipline. The 5 kW AIO is not: 5 kW AC output is already above the single-pack continuous limit once inverter losses are counted.
- **Nose-cabinet heat argues against the 5 kW AIO:** the 5 kW idle tax is <=80 W normal / <=55 W ECO, or 1.3-1.9 kWh/day as heat and battery drain. The 3500 W AIO is <50 W normal / <30 W ECO, still material but less bad. Adding a SmartSolar controller adds heat and wiring, but less idle waste than keeping an oversized inverter.
- **Ground-panel compatibility is decisive:** do not parallel a 3S roof string with a 2S deployable string on one tracker. A 3S roof architecture that keeps the D002 ground margin is a five-panel PV plan: three fixed roof panels plus a two-panel deployable pair. If only four LG455s are available, choose either D002's 2-roof/2-ground plan or a 3-roof/no-ground-pair plan; do not pretend the deployable 2S pair still exists.

## Candidate Disposition

| Candidate | Integration / reliability disposition |
|---|---|
| LiTime 48 V 3500 W AIO only | Good inverter/battery fit and good 2S/2S2P MPPT fit, but strands a confirmed third roof panel. Acceptable fallback only if July stays 2-roof/2-ground. |
| LiTime 3500 W + Victron SmartSolar 250/60 | **Recommended revision.** Roof 3S is electrically real; ground 2S remains usable; inverter draw stays sized to one battery. |
| Keep or repurchase LiTime 5 kW | Reject. 120 V MPPT floor is unreliable with hot 3S LG455, 2S ground is unusable, idle heat is worse, and sustained AC output exceeds one battery. |
| EG4 3000EHV / 120 V-min AIO class | Reject for the same MPPT-floor and ground-pair reasons. Better ecosystem does not fix the 120 V floor. |
| Victron MultiPlus-II 48/3000 + SmartSolar 250-class MPPT | Strongest long-term reliability ecosystem and best idle behavior, but lower continuous AC output and a larger rewiring/programming change than needed for July. |
| Victron EasySolar-II GX | Reject for this trailer because the relevant integrated package is a 230 VAC product, not a clean US 120 VAC trailer AIO replacement. |
| Renogy/Eco-Worthy/LiTime-like 145/150 V AIO class | Reject as a real 3S answer. LG455 3S is 149.7 V Voc at STC before tolerance and cold correction, so there is no safe cold-voltage margin. |

## Required Outputs

1. **Recommended architecture and exact next purchase/return action.** Revise D002 to a hybrid architecture if the confirmed third roof panel is to be energized: LiTime 48 V 3500 W AIO remains the inverter, AC charger, and deployable-ground MPPT; add a Victron SmartSolar MPPT 250/60-Tr for the fixed roof 3S LG455 string; keep the Velit on its own fused 48 V branch and the Orion 48/24 bus as already planned. Exact action: return the mistaken LiTime 5 kW, keep/order the LiTime 48 V 3500 W AIO, buy a Victron SmartSolar MPPT 250/60-Tr plus DC-rated PV disconnect/OCP hardware, and buy/allocate a fifth LG455 if the deployable 2S ground pair is still required.

2. **Whether the mistaken LiTime 5 kW should still be returned.** Yes. Return it. Its one-box 3S pitch fails on hot-roof MPPT tracking, makes the 2S ground pair unusable without another controller, imposes a larger idle/heat tax, and invites sustained AC draw above the single battery's 100 A continuous discharge limit.

3. **Whether confirmed 3 roof panels should change the inverter decision.** No for the inverter/charger, yes for the solar architecture. Three roof panels do not justify a 120 V-min high-voltage AIO. They justify either keeping D002's 2-roof/2-ground layout or revising to the split-MPPT architecture; they do not change the conclusion that the LiTime 3500 W is the better inverter fit for one ComFlex battery.

4. **Strongest counterargument to this recommendation.** The cleanest July reliability move is to keep D002 exactly as-is: two roof panels plus the deployable 2S ground pair on one LiTime 3500 W AIO, no second controller, no charge-coordination work, fewer PV penetrations, less nose-cabinet heat, and less schedule risk. That counterargument wins if the owner values minimum install risk over making the third roof panel productive for July.

5. **Required gates or install notes.** Never connect 3S to the LiTime 3500 W PV input. Never combine roof 3S and ground 2S on one MPPT. Put a DC-rated disconnect on each PV source, rated above cold Voc and expected Isc; fuse strings at <=20 A if any strings are paralleled. Fuse or breaker the SmartSolar battery-side output for controller current and conductor ampacity, and keep the Velit, Orion, and AIO on separately protected 48 V branches. Make the battery-terminal main OCP explicit with a high-interrupt DC-rated Class-T or documented equivalent; do not use 32 V automotive/ANL gear on the 48 V battery side. Coordinate charge current so all chargers together stay <=100 A: with an external roof MPPT, set the SmartSolar current limit around 30 A and set the LiTime charge limit so the sum cannot exceed 100 A, including AC charging. Use matching LiFePO4 charge voltages on both chargers. Ventilate the nose cabinet and temperature-test it under desert sun with AIO, SmartSolar, Orion, and Velit wiring installed; charging must keep the battery below its 50 C charge limit and electronics below their 55 C operating limit. Add an operating rule that sustained full-power AC loads are not run simultaneously with Velit turbo and maximum 24 V bus load on a single battery.

6. **One-line verdict for D002.** **REVISE D002:** keep the LiTime 3500 W inverter/charger and return the 5 kW, but replace "no external MPPT / roof 2S only" with a split-MPPT 3S-roof architecture if the confirmed third roof panel is meant to be productive.
