# AIO Inverter/Charger 3-Panel Rerun Evidence Brief — 2026-06-05

Purpose: corrected source pack for rerunning the D002 inverter/charger adversarial review. The previous run incorrectly let roof geometry kill the 3-panel case. Corrected premise: **the Velit 2000R can fit in the trailer nose section, and three LG455 roof panels will fit on the roof.** Reviewers must not reject 3S on physical-fit grounds.

**Supersession note:** the corrected verdict now favors **Victron MultiPlus-II 48/3000/35-50 120V + SmartSolar MPPT 250/60-Tr**. This brief remains as evidence for the rerun inputs and options considered.

## Corrected Premise

- The roof can carry **3 x LG455N2W-E6** panels in landscape orientation.
- The Velit 2000R rooftop AC can live in the nose section, clear of the three panel rows.
- The remaining question is not "does 3S fit on the roof?" It is: **does a 3S-capable power architecture beat the LiTime 48 V 3500 W AIO replacement once MPPT voltage margin, battery fit, idle draw, cost, schedule, protection, and install risk are counted?**
- The owner explicitly asked for 3S support. The rerun must steelman a 3S-positive architecture before rejecting it.

## Trailer Constraints

- Trailer: 7x12 single-axle FT712S2-D, 3,500 lb GVWR, nose-sensitive.
- Battery: LiTime 48 V 100 Ah Smart ComFlex, 5.12 kWh, 100 A continuous charge/discharge per repo reference.
- Major loads:
  - Velit 2000R Mini rooftop AC is 48 V native, about 5-14 A at 48 V, rated about 670 W, exterior unit about 26.4" x 26" x 6.5", about 61 lb.
  - Fridge is DC compressor and runs 12/24 V native.
  - AC inverter is for tools, induction, microwave-style loads, and occasional 120 VAC use. The rooftop AC is **not** an inverter load.
- Current house architecture: 48 V battery and inverter/charger in the nose cabinet; 24 V house bus via Victron Orion-Tr 48/24-16A; no standing 12 V bus.
- Existing D002 before this rerun: LiTime 48 V 3500 W AIO, roof 2 x LG455 in 2S (910 W), deployable ground 2S pair joining as 2S2P (1820 W) when camped.

## Panel Math

LG455N2W-E6 load-bearing figures:

- Size: 83.07" x 41.02" x 1.57"; 48.5 lb each.
- Vmpp: 42.1 V STC; NMOT Vmpp: 39.60 V.
- Voc: 49.9 V +/-5%; Voc temp coefficient: -0.26 %/C.
- Impp: 10.83 A; Isc: 11.39 A; max series fuse 20 A.

Derived strings:

| String | STC Vmpp | NMOT Vmpp | Hot-roof Vmpp signal | STC Voc | Cold Voc signal | Practical meaning |
|---|---:|---:|---:|---:|---:|---|
| 1S | 42.1 V | 39.6 V | ~36-38 V | 49.9 V | ~54 V at -10 C | Cannot charge a 48 V LiFePO4 battery through normal buck MPPT. |
| 2S | 84.2 V | 79.2 V | ~71-76 V | 99.8 V | ~109 V at -10 C | Correct for the LiTime 3500 W AIO's 60-145 V window and 60-115 V recommended range. |
| 3S | 126.3 V | 118.8 V | ~108-115 V | 149.7 V | ~163 V at -10 C, ~169 V at -25 C | Invalid on LiTime 3500 W (145 V max). Cold-safe on 500 V-class AIOs, but near/below their 120 V MPPT floor in NMOT/hot conditions. Good on a 250 V-class MPPT with a battery+5 V style start threshold. |
| 2S2P | 84.2 V | 79.2 V | ~71-76 V | 99.8 V | ~109 V at -10 C | Four-panel camped configuration for LiTime 3500 W; current about 21.7 A Impp / 22.8 A Isc. |

Critical correction: for 120 V-min AIOs, do **not** assume "below floor" means mathematically zero harvest without analysis. 3S NMOT Vmpp of 118.8 V is close to 120 V; a hot roof may push the MPP farther down. Reviewers should decide whether the result is acceptable clipping, intermittent tracking, or a hard reliability problem for Juplaya.

## Candidate Architectures

| Option | PV input | AC output / idle | What it buys | Main risk |
|---|---|---|---|---|
| LiTime 48 V 3500 W AIO only | 60-145 V operating, 60-115 V recommended, 4400 W, 50 A | 3500 W, 6000 W surge 5 s; normal idle <50 W, ECO <30 W; ~23.15 lb | Cheapest simple one-box fit for 2S roof + 2S ground pair; same vendor as battery; 3.5 kW output fits a single 100 A battery better than 5 kW. | Cannot use all 3 roof panels in one string; third roof panel is stranded unless a separate MPPT is added. |
| LiTime 48 V 3500 W AIO + separate Victron SmartSolar 250-class MPPT | AIO internal MPPT can take deployable ground 2S; external MPPT handles roof 3S | Same 3500 W inverter; added MPPT self-consumption is small | Best 3-panel hybrid: roof 3S becomes real, ground 2S remains usable, inverter/battery sizing stays sane. | More boxes, PV disconnect/OCP design, charge-current coordination, cost, and install time. |
| Keep/repurchase LiTime 48 V 5 kW AIO | 120-500 V operating, 120-450 V recommended, 5500 W | 5000 W; normal idle <=80 W, ECO <=55 W; ~30.86 lb | One-box 3S roof support by voltage ceiling; no separate roof MPPT. The mistakenly ordered unit may already exist in the return flow. | 3S MPP is near/below the 120 V floor in heat; bigger idle tax; sustained 5 kW output can exceed the single-pack comfort zone; deployable 2S ground pair is not usable on the same MPPT. |
| EG4 3000EHV-48 AIO | 120-450 V MPPT range, 500 V max, 5000 W PV, 80 A charge class | 3000 W / 120 VAC; idle <70 W; ~18-21.6 lb depending source | 3S roof support by voltage ceiling, better known solar-DIY support ecosystem than LiTime. | Same 120 V MPPT-floor question; lower inverter output than LiTime 3500; not same battery-vendor integration; deployable 2S ground pair needs a second controller or is unused. |
| Victron MultiPlus-II 48/3000 + SmartSolar MPPT 250/60 or 250/70 | SmartSolar 250-class: 250 V max, starts above battery voltage + about 5 V, 3S friendly | MultiPlus-II 48/3000 120 V: 2400 W continuous at 25 C, 2200 W at 40 C, peak 5500 W, zero-load 11 W | Best engineering ecosystem; real 3S compatibility; low idle; modular serviceability. | Not an AIO; lower continuous inverter output; more wiring/protection parts; higher cost and integration time. |
| Victron EasySolar-II GX 48/3000 MPPT 250/70 | Integrated MultiPlus-II + SmartSolar 250/70 | 230 VAC output per Victron datasheet | True integrated Victron 250 V MPPT package. | Wrong AC output for a US 120 V trailer unless the AC distribution concept changes; likely reject. |
| Renogy/Eco-Worthy/LiTime-like 3500 W 145/150 V AIOs | Usually 145-150 V max PV class | Similar 3500 W class | Similar one-box shape to LiTime 3500. | 3S LG455 is at or above 145-150 V before cold correction and panel tolerance; not a real 3S answer. |

## Claims To Stress-Test

1. **3S-positive steelman:** Now that three roof panels fit, does the simplest acceptable answer become a 120 V-min high-voltage AIO?
2. **Hot-roof MPPT floor:** Is 3S LG455 on a 120 V-min MPPT actually unacceptable in July, or only a manageable clipping risk?
3. **Hybrid route:** Does LiTime 3500 W + separate Victron 250-class MPPT now beat the "no external MPPT" D002 baseline because it harvests all 3 roof panels while preserving battery fit?
4. **5 kW return:** Is returning the mistaken 5 kW still correct, or should it be kept because roof 3S now physically fits?
5. **Ground panels:** If roof becomes 3S, what happens to the deployable 2S ground pair? Does the candidate still support it without another MPPT?
6. **Single battery:** Do any candidates overrun the 100 A continuous battery constraint by inverter draw, charge current, or combined charge sources?
7. **Juplaya schedule:** Which option is the best buy-now answer if the owner wants three roof panels but still needs a July-ready system?

## Source Links

- LiTime 48 V 3500 W AIO product page: https://www.litime.com/products/48v-3500w-solar-converter-charger
- LiTime 48 V 5 kW AIO product page: https://www.litime.com/products/48v-5kw-solar-inverter-charger
- EG4 3000EHV-48 product page: https://eg4electronics.com/categories/inverters/eg4-3000ehv-48-all-in-one-off-grid-inverter
- EG4 3000EHV-48 Signature Solar retail/spec page: https://signaturesolar.com/eg4-3kw-off-grid-inverter-3000ehv-48-3000w
- Victron MultiPlus-II 120 V datasheet: https://www.victronenergy.com/upload/documents/Datasheet-MultiPlus-II-120V-EN.pdf
- Victron SmartSolar MPPT 250-class specs: https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-60_up_to_250-70/en/technical-specifications.html
- Victron EasySolar-II GX datasheet: https://www.victronenergy.com/upload/documents/Datasheet-EasySolar-II-24V-48V-3kVA-48V-5kVA-MPPT-250-70-100-GX-EN.pdf
- Renogy 48 V 3500 W AIO product page: https://www.renogy.com/products/48v-3500w-solar-inverter-charger
- Velit 2000R Mini dimensions/specs: https://www.tecvan.com/products/velit-2000r-mini-rooftop-air-conditioner-12-48v
- LG455N2W-E6 repo reference: docs/reference/lg455n2w-e6-datasheet.md
- LiTime 48 V 100 Ah ComFlex repo reference: docs/reference/litime-48v-100ah-battery-specs.md
