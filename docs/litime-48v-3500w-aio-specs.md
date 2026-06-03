# LiTime 48V 3500W Solar Inverter Charger (AIO) — Key Specs

**The build's AIO** (replaced the returned 5 kW unit). Distilled from the [manual](litime-48v-3500w-inverter-charger-manual.md) (owner-converted). Lives in the nose cabinet.

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

- **All solar gates closed.** Roof **2S** (Vmpp 84/79/~71 V, Voc ≤ ~109 V cold) sits inside even the **recommended 60–115 V** band; the deployable ground pair (**2S2P, 1820 W, ~21.7 A Impp / ~22.8 A Isc**) is comfortably inside the **50 A / 4400 W** PV input. **3S is never valid** (Voc 149.7 V STC > 145 V hard max).
- **⚠ Commissioning: cap total charge at ≤ 100 A.** The unit can do 120 A (PV 80 A + AC 40 A); the 48V 100Ah ComFlex accepts 100 A max continuous charge.
- **Idle tax roughly halved vs the 5 kW:** < 30 W ECO ≈ 0.72 kWh/day (~14% of the pack). Keep the ECO/off-when-idle discipline; the DC-fridge call (D005) stands.
- **Battery headroom restored:** full 3500 W output draws ~75 A (< the pack's 100 A continuous); the 6000 W/5 s surge ≈ 129 A is inside the pack's 200 A/2 min.
- **Cabinet:** smaller + 8 lb lighter than the 5 kW; same 131 °F operating ceiling and active cooling fans — **ventilate the nose cabinet**.
- AC input is 40 A (vs 63 A on the 5 kW) — fine for shore/generator at 120 V.
