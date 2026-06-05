# LiTime 48V 3500W Solar Inverter Charger (AIO) — Key Specs

**Budget fallback AIO / previous house-charger candidate** (the ordered 5 kW unit would be returned; this 3.5 kW unit is not owned). Distilled from the [manual](../manuals/litime-48v-3500w-inverter-charger-manual.md) (owner-converted). Current D002 favors the Victron MultiPlus-II + SmartSolar path instead. If the LiTime fallback is reopened, its PV input is the optional deployable 2S/fallback input; the roof 3S string still uses a separate Victron SmartSolar 250/60-Tr.

| Spec | Value |
|---|---|
| Rated AC output | 3500 W (run ≤ 95% for sustained loads) · surge 6000 W (5 s) · 29 A @ 120 VAC ±5% · pure sine · 60 Hz |
| Inverter / bypass efficiency | > 91% / > 95% |
| **PV input** | **60–145 V operating, 60–115 V recommended · ≤ 4400 W · ≤ 50 A** |
| MPPT output | ≤ 4200 W · charge 0–80 A · > 94% efficiency |
| Battery | 48 V nominal (40–60 V), M6 terminals; Lithium / Lead Acid / User |
| Max charge (PV + AC combined) | **120 A** ⚠ (battery accepts 100 A — cap in settings) |
| AC input | 90–140 VAC, 40 A max, charges 0–40 A, 60 Hz ±0.3 |
| **No-load draw** | **< 50 W normal · < 30 W ECO** |
| Operating temp | −10 to 55 °C (14–131 °F) · storage −25 to 60 °C |
| Size / weight | 16.77 × 13.23 × 4.88 in (426 × 336 × 124 mm) · ~23.2 lb (10.5 kg) |
| I/O | On/Off switch, ground terminal, AC in/out blocks, USB-B, RS485, dry contacts, cooling fans |

## Build-relevant notes

- **AIO PV gate:** a **2S** LG455 string (Vmpp 84/79/~71 V, Voc ≤ ~109 V cold) sits inside even the **recommended 60–115 V** band; a 2S2P fallback is comfortably inside the **50 A / 4400 W** PV input. **3S is never valid into this AIO** (Voc 149.7 V STC > 145 V hard max before cold correction).
- **⚠ Commissioning if fallback is used: cap combined charge at ≤ 100 A.** The unit can do 120 A (PV 80 A + AC 40 A); the 48V 100Ah ComFlex accepts 100 A max continuous charge, and the roof SmartSolar adds another charge source.
- **Idle tax roughly halved vs the 5 kW:** < 30 W ECO ≈ 0.72 kWh/day (~14% of the pack). Keep the ECO/off-when-idle discipline; the DC-fridge call (D005) stands.
- **Battery headroom if fallback is used:** full 3500 W output draws ~75 A (< the pack's 100 A continuous); the 6000 W/5 s surge ≈ 129 A is inside the pack's 200 A/2 min.
- **Cabinet:** smaller + 8 lb lighter than the 5 kW; same 131 °F operating ceiling and active cooling fans — **ventilate the nose cabinet**.
- AC input is 40 A (vs 63 A on the 5 kW) — fine for shore/generator at 120 V.
