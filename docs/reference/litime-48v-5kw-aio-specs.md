# LiTime 48V 5kW Solar Inverter Charger (AIO) — Key Specs

> **NOTE:** the **5 kW unit is being returned**; the build uses the **LiTime 48V 3500W AIO (PV 60–145 V)**. This sheet is kept for reference.

Distilled from the [manual](../manuals/litime-48v-5kw-inverter-charger-manual.md) (owner-converted from the scanned PDF). The AIO in the power system — lives in the nose cabinet.

| Spec | Value |
|---|---|
| Rated AC output | 5000 W (run ≤ 95% for sustained loads) · surge 10,000 W · 42 A max @ 120 VAC ±5% · pure sine |
| Inverter / bypass efficiency | > 90% / > 95% |
| **PV input** | **120–500 V operating, 120–450 V recommended · ≤ 5500 W · ≤ 22 A** |
| MPPT charge | 100 A max, > 92% efficiency |
| Battery | 48 V nominal (40–60 V), LF16 default, M6 terminals |
| Max charge (PV + AC combined) | 100 A |
| AC input | 90–140 VAC, 63 A breaker, charges 0–40 A, 50/60 Hz |
| **No-load draw** | **≤ 80 W normal · ≤ 55 W ECO** |
| Operating temp | −10 to 55 °C (14–131 °F) · storage −25 to 60 °C |
| Protection | **IP20** (indoor only) · safety class I |
| Parallel | up to 6 units, split-phase capable |
| Size / weight | 17.60 × 13.78 × 5.24 in (447 × 350 × 133 mm) · ~30.9 lb (14 kg) |

## Build-relevant notes

- **Idle tax is now quantified: ≤ 80 W normal / ≤ 55 W ECO = 1.3–1.9 kWh/day** — 26–37% of the 5.12 kWh pack daily, just idling. Use ECO mode and power the inverter off when nothing needs AC. This hard-confirms the D005 fridge call (12 VDC compressor, not Midea-on-inverter).
- **PV string limits:** 120 V floor confirmed (recommended range starts at 120 V) — the 3-panel/3S hot-Vmp tension stands (see context "Still open"). **Max PV input 22 A**: one series string of LG455 (Imp ~10.9 A) is fine; two parallel strings (~21.8 A) would sit at the limit.
- **Sustained AC ceiling is the battery, not the inverter:** 5000 W out at >90% efficiency draws ~108 A from the pack — above the ComFlex's 100 A continuous. On one battery, sustained AC ≈ **~4.6 kW** (100 A × 51.2 V × 0.9); 2-minute bursts to 200 A cover surges. A second parallel pack lifts this.
- **Cabinet heat:** operating ceiling is **131 °F (55 °C)** and the unit is IP20 (indoor). A closed nose cabinet in desert sun can approach that — **ventilate the AIO cabinet** (the unit has an air-inlet vent that must breathe).
- **Cabinet fit:** 17.6 × 13.8 × 5.2 in + clearance for the 63 A breaker side-vent and terminal panel; ~31 lb on the wall of the nose cabinet (counts toward tongue weight).
- Off-grid only; never parallel two AC sources; PV/AC cabling fused + breakered per manual.
