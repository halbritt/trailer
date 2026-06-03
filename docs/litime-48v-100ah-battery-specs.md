# LiTime 48V (51.2V) 100Ah Smart ComFlex — Battery Specs

The house pack in the power system: the **LiTime 48V 100Ah Smart ComFlex** (corrected — not the Golf Cart variant). Pulled 2026-06-03 from `litime.com/products/litime-48v-100ah-smart-comflex-lithium-battery`. EV-grade LiFePO4 cells + LiTime T5.0 BMS. "ComFlex" is LiTime's modular flexible-busbar expansion system (eases the 16P paralleling); core electrical specs are identical to the Golf Cart variant, and the table below is the ComFlex page's own.

| Spec | Value |
|---|---|
| Chemistry | LiFePO4 (EV-grade cells) |
| Nominal voltage | 51.2 V |
| Rated capacity | 100 Ah |
| Energy | 5120 Wh |
| Cycle life | 4000 @ 100% DOD · 6000 @ 80% DOD · 15,000 @ 60% DOD |
| Max expansion | **16P1S** (with comms) / **4P1S** (non-comms) — **parallel only, no series** |
| BMS | 200 A (LiTime T5.0) |
| Max continuous output power | 5120 W |
| Max continuous charge current | 100 A |
| Max continuous discharge current | 100 A (200 A @ 2 min) |
| Max discharge (1 s surge) | 600 A |
| Internal resistance | ≤ 40 mΩ |
| Charge method | CC/CV |
| Charge voltage | 57.6 ± 0.8 V |
| Recommended charge current | 20 A |
| Charge temperature | 0 °C to 50 °C (32–122 °F) |
| Discharge temperature | −20 °C to 60 °C (−4–140 °F) |
| Storage temperature | −10 °C to 50 °C (14–122 °F) |
| Low-temp protection | Yes — auto charge-off < 0 °C (32 °F), recovery ≥ 5 °C (41 °F) |
| Self-heating | No |
| Bluetooth | Yes (real-time monitoring) |
| Terminals | M8 bolts |
| Weight | 97.44 lbs (~44.2 kg) |
| Size | L 19.88 × W 12.32 × H 9.25 in |
| Housing | SPCC steel plate |
| Protection class | IP65 |
| Certifications | FCC, FCC ID, CE, RoHS, UN38.3 |
| Warranty | 5 years |
| Paired charger | 58.4 V 18 A LiFePO4 charger |

## Build-relevant notes

- **Discharge headroom is tight against the 5 kW AIO.** 100 A continuous × 51.2 V = **5120 W continuous — exactly the AIO's max output**. The pack only does 200 A for 2 min and 600 A for 1 s. So running the Velit AC (48 VDC) plus other loads near full inverter output sits at the pack's continuous limit, with no margin on a single pack. Stagger high-draw loads, or this is the argument for a second pack in parallel. *(Update: the planned swap to the 3500W AIO drops max inverter draw to ~76 A — headroom restored.)*
- **Parallel only (1S).** Capacity scales by paralleling (≤16P with comms, ≤4P without); you cannot series these. Not a problem for the current 48 V design.
- **Charging is comfortable.** 100 A max / 20 A recommended, CC/CV at 57.6 V. Solar (~1365 W ÷ 51.2 V ≈ 27 A) and AIO charging are well inside limits.
- **No self-heating + charge cutoff below 0 °C.** Fine for July Juplaya (hot). But for the mission doc's cold-weather profiles, the pack **won't accept charge below freezing** (recovers ≥ 5 °C) — a real limit if this rig ever winters.
- **Weight 97.44 lbs** confirms the context doc's "~100 lb; mount low and centered" — and it's a meaningful chunk of the single-axle payload + a tongue-weight placement decision.
- **Does NOT resolve the D002 3S-vs-2S solar question** — that hinges on the *AIO inverter's* PV Voc-max (in the image-based inverter manual), not this battery.
