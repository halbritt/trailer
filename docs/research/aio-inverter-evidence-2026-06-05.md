# AIO Inverter/Charger Evidence Brief — 2026-06-05

Purpose: source pack for an adversarial review of D002 before buying the replacement inverter/charger. The owner accidentally ordered the LiTime 48 V 5 kW AIO and plans to return it; current D002 says buy the LiTime 48 V 3500 W AIO. The new challenge is whether a different inverter/charger or MPPT architecture is better now that three roof panels may physically fit with the Velit rooftop AC.

## Trailer Constraints

- Trailer: 7x12 single-axle FT712S2-D, 3,500 lb GVWR, nose-sensitive.
- Battery: LiTime 48 V 100 Ah Smart ComFlex, 5.12 kWh. Existing reference says 100 A continuous charge/discharge; the 5 kW AIO can sit at or above that battery limit, while 3.5 kW leaves discharge headroom.
- Major loads:
  - Velit 2000R Mini rooftop AC is 48 V native, about 5-14 A at 48 V, rated ~670 W, exterior unit about 26.4" x 26" x 6.5", ~61 lb.
  - Fridge is DC compressor and runs 12/24 V native.
  - AC inverter is for tools, induction, microwave-style loads, and occasional 120 VAC use, not for the rooftop AC.
- Current house architecture: 48 V battery and AIO in the nose cabinet; 24 V house bus via Victron Orion-Tr 48/24-16A; no standing 12 V bus.
- Roof measured field: width 84-7/8" rail-edge to rail-edge, rectangle length 145.5" plus nose. LG panels fit landscape across the roof width; each landscape row consumes about 41.02" of roof length.
- Existing D002: roof 2 x LG455 in 2S (910 W) plus deployable ground 2S pair, joining as 2S2P (1820 W) when camped.

## Panel Math

LG455N2W-E6 load-bearing figures from the repo reference sheet:

- Size: 83.07" x 41.02" x 1.57"; 48.5 lb each.
- Vmpp: 42.1 V STC; NMOT row Vmpp: 39.60 V.
- Voc: 49.9 V +/-5%; Voc temp coefficient: -0.26 %/C.
- Impp: 10.83 A; Isc: 11.39 A; max series fuse 20 A.

Derived strings:

| String | STC Vmpp | NMOT Vmpp | STC Voc | Cold Voc signal | Practical meaning |
|---|---:|---:|---:|---:|---|
| 1S | 42.1 V | 39.6 V | 49.9 V | ~54 V at -10 C | Cannot charge a 48 V LiFePO4 battery through normal buck MPPT; PV voltage is below battery charge voltage. |
| 2S | 84.2 V | 79.2 V | 99.8 V | ~109 V at -10 C | Correct for the LiTime 3500 W AIO's 60-145 V window and 60-115 V recommended range. |
| 3S | 126.3 V | 118.8 V | 149.7 V | ~163 V at -10 C, ~169 V at -25 C | Invalid on LiTime 3500 W (145 V max). Borderline on 120 V-min high-voltage AIOs because hot/NMOT Vmpp can fall below their MPPT floor. Good on a separate 250 V-class MPPT with a low start threshold. |
| 2S2P | 84.2 V | 79.2 V | 99.8 V | ~109 V at -10 C | Four-panel camped configuration for LiTime 3500 W; current about 21.7 A Impp / 22.8 A Isc. |

Roof implication:

- Two landscape rows = about 82.0" length used, leaving about 63.5" rectangle length plus the nose for AC, standoffs, walk/clearance, and rail feet.
- Three landscape rows = about 123.1" length used, leaving only about 22.4" of the rectangle plus the nose; the Velit exterior unit is about 26" long and needs a 14-1/4" opening plus edge/obstruction clearances. This is plausible only if the roof drawing proves the AC can live in the nose or a non-conflicting station.
- A third roof panel is electrically useful only if there is a 3S-capable MPPT path. With the LiTime 3500 W alone, the third roof panel cannot be roof-only productive unless paired with another panel in series or routed through a separate boost/250 V MPPT solution.

## Candidate Architectures

| Option | Current price signal | PV input | AC output / idle | What it buys | Main risk |
|---|---:|---|---|---|---|
| Keep D002: LiTime 48 V 3500 W AIO | $629.99 from LiTime on 2026-06-05 | 60-145 V operating, 60-115 V recommended, 4400 W, 50 A; MPPT charge 0-80 A | 3500 W, 6000 W surge 5 s; normal idle <50 W, ECO <30 W; ~23.15 lb | Cheapest simple one-box fit for 2S roof + 2S ground pair; same vendor as battery; 3.5 kW output fits a single 100 A battery better than 5 kW. | No 3S; reported PV-overvoltage nuisance-faults make never-3S hard. Roof-only remains 910 W unless a separate MPPT/roof plan changes. |
| Keep/repurchase LiTime 48 V 5 kW AIO | $859.99 from LiTime; visible delivery window on 2026-06-05 | 120-500 V operating, 120-450 V recommended, 5500 W | 5000 W; normal idle <=80 W, ECO <=55 W; ~30.86 lb | High-voltage MPPT and bigger inverter; can accept 3S by voltage max. | 3S Vmpp is below/near the 120 V floor in hot/NMOT conditions; bigger idle tax; sustained 5 kW output exceeds the single-pack comfort zone; already ordered by mistake and slated for return. |
| EG4 3000EHV-48 AIO | $699.99 Signature Solar signal; EG4 page says 120-450 VDC PV, 1 MPPT, 21.6 lb | 120-450 VDC, 5000 W PV, 80 A charge class | 3000 W / 120 VAC | High-voltage AIO with better known solar-DIY ecosystem than LiTime. | Same 120 V MPPT-floor problem for 3S LG455; lower inverter output than LiTime 3500; not same battery-vendor integration. |
| Victron MultiPlus-II 48/3000 + SmartSolar MPPT 250/60 | Higher cost; multiple boxes | SmartSolar 250/60: 250 V max, starts above battery voltage + about 5 V, 3440 W nominal PV at 48 V, 60 A | MultiPlus-II 48/3000: 2400 W continuous at 25 C, 2200 W at 40 C, peak 5500 W, zero-load 11 W | Best engineering ecosystem; real 3S compatibility with LG455 and low idle; modular serviceability. | Not an AIO; lower continuous inverter output; more wiring/protection parts; higher cost and integration time. |
| LiTime 3500 W AIO + separate Victron SmartSolar 250-class MPPT for 3S roof | Higher cost than D002; still simpler than full Victron | AIO internal MPPT remains available for 2S ground pair; external MPPT handles 3S roof | Same 3500 W inverter | Makes three roof panels productive without abandoning the chosen inverter/charger; preserves battery fit and 24 V bus. | More boxes, more PV disconnect/OCP design, charge-current coordination, and roof drawing must prove 3 panels + AC. |
| Growatt/MPP/Sungold-style 5-6 kW high-voltage AIO | varies | Often 120 V-min high-voltage MPPT | 5-6 kW class, often higher idle/weight | Spec-sheet 3S/large-output appeal. | 3S floor problem remains for 120 V-min MPPTs; larger AC output is not needed for a 48 V DC AC load; install/support risk. |

## Claims To Stress-Test

1. **LiTime 3500 default:** Does its 2S/2S2P fit, lower idle, same-vendor battery communication, and single-pack discharge headroom beat every alternative?
2. **3-panel roof temptation:** If three panels physically fit with the Velit, is that enough to change the inverter choice, or is 3S electrically marginal on 120 V-min AIOs?
3. **5 kW return:** Is returning the mistaken 5 kW unit still correct, or should it be kept because it supports high-voltage PV?
4. **EG4/Growatt/MPP class:** Does any high-voltage AIO actually solve the roof problem without creating hotter-roof MPPT dropouts, idle tax, install/support risk, or battery overdraw?
5. **Victron modular alternative:** Is this the right moment to spend more for MultiPlus + SmartSolar, or does lower inverter output / added wiring miss the Juplaya deadline?
6. **Hybrid route:** Should D002 stay LiTime 3500 now but explicitly allow a later separate 250 V MPPT if the measured roof drawing proves three panels plus AC?

## Source Links

- LiTime 48 V 3500 W AIO product page: https://www.litime.com/products/48v-3500w-solar-converter-charger
- LiTime 48 V 5 kW AIO product page: https://www.litime.com/products/48v-5kw-solar-inverter-charger
- EG4 3000EHV-48 product page: https://eg4electronics.com/categories/inverters/eg4-3000ehv-48-all-in-one-off-grid-inverter
- EG4 3000EHV-48 Signature Solar retail/spec page: https://signaturesolar.com/eg4-3kw-off-grid-inverter-3000ehv-48-3000w
- Victron MultiPlus-II 120 V datasheet: https://www.victronenergy.com/upload/documents/Datasheet-MultiPlus-II-120V-EN.pdf
- Victron SmartSolar MPPT 250/60 manual/specs: https://www.victronenergy.com/upload/documents/Manual_SmartSolar_MPPT_150-60_up_to_250-70/29694-MPPT_solar_charger_manual-pdf-en.pdf
- Velit 2000R Mini dimensions/specs: https://www.tecvan.com/products/velit-2000r-mini-rooftop-air-conditioner-12-48v
- LG455N2W-E6 repo reference: docs/reference/lg455n2w-e6-datasheet.md
- LiTime 48 V 100 Ah ComFlex repo reference: docs/reference/litime-48v-100ah-battery-specs.md
