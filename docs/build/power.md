# Power / Electrical — Juplaya Trailer Build

Split from `../juplaya-trailer-context.md` (doc divorce, design-panel run). Settled facts first; decisions cite `../DECISION_LOG.md`.

## Settled — the 48 V stack
- DIY 48V LiTime stack (F3800 is out):
  - **AIO: LiTime 48V 3500W (5 kW returned) — sheet verified** ([specs](../litime-48v-3500w-aio-specs.md) · [manual](../litime-48v-3500w-inverter-charger-manual.md)): PV **60–145 V op / 60–115 V rec / 4400 W / 50 A**; **no-load <50 W (<30 W ECO)**; AC 3500 W, surge 6000 W/5 s; ~75 A max battery draw (headroom under the pack's 100 A); 23 lb, 426×336×124 mm. **Commissioning: cap total charge ≤100 A** (unit does 120 A PV+AC; battery accepts 100 A). ECO/off when idle; ventilate the nose cabinet (131 °F ceiling). 5 kW docs kept for reference.
  - **LiTime 48V 100Ah Smart ComFlex** (LiFePO4) — 5.12 kWh, ~100 lb; mount low and centered ([specs](../litime-48v-100ah-battery-specs.md)).
  - **LiTime 500A Bluetooth shunt**; **ANL 250A fuses**.
- The **AIO lives in the nose, in a cabinet**; anything that needs plugging in plugs in there.

## Solar — RESOLVED (2S roof / 2S2P camped)
1. **2 × LG455N2W-E6 in 2S (910 W).** The 3500W AIO's PV window is **60–145 V** and 2S sits mid-window in every condition: Vmpp 84.2 V STC / 79.2 V NMOT / ~71 V desert-hot (≫ the 60 V floor); Voc 99.8 V STC, ≤ ~117 V even at −40 °C (< 145 V). The 5 kW unit's 120 V floor was unmeetable by any roof-fitting string (datasheet NMOT row: 3S = 118.8 V at 20 °C ambient). **Never wire 3S into this unit** — cold-morning Voc ≈ 157–163 V (Voc ±5%, cold) overshoots the 145 V PV max, and 3P (~42 V) is under the 60 V floor; a 3rd roof panel runs on **its own small MPPT** to the battery. No external MPPT otherwise. ([datasheet](../lg455n2w-e6-datasheet.md))
   - *Expansion: a **ground-mounted 2S pair paralleled in → 2S2P, 1820 W** when camped. Voltage unchanged; current ~21.7 A Impp / ~22.8 A Isc — in-spec against the 50 A / 4400 W PV input (a third pair would fit electrically). Hardware: MC4 Y-branch or mini-combiner, per-string inline protection (≤20 A), PV disconnect, weatherproof inlet, 10 AWG extension. Juplaya wind: guy/anchor the ground pair. Transport: panels are 83" vs the 81" interior width → lengthwise, padded E-track wall slot (see [interior](interior.md)).*
2. **Mounting** — aluminum rails on tilt/Z-brackets **bolted through into the 24"-OC steel roof bows**, butyl + Dicor sealed. Side-of-top-rail cantilever rejected (peel/tip at tow speed).
   - **⚠ ROOF-FIT GATE (panel review, D007):** the 84" body width includes **radius corners**; the usable *flat* roof field may be substantially narrower (~72–78" — measure). Two panels are 82.0–83.1" across in any orientation, plus rail-foot landing area. The **measured roof drawing** (panels + rails/clamps + bows + awning risers + door swing in one drawing) is a **pass/fail gate before ordering racking**; panel-frame overhang of the radii is permissible only within the LG frame's rated overhang.

## DC house bus — DECIDED: single 24 V bus (D006)
- **One Victron Orion-Tr 48/24-16A (380 W) isolated converter**, nose cabinet, **remote on/off to a cabin toggle**. **Delete the 48→12 V converter and any 12 V house fuse block.**
- **Margin condition (binding):** 16 A is sized for the *current* loads (realistic simultaneous worst case ~12–15 A: fridge 4.6 A + lighting to its 5 A branch + USB-C PD at full profile). **A future 24 V diesel heater (~8–10 A glow) reopens converter sizing** (second paralleled Orion-Tr, upsize, or glow-window load-shedding).
- **Thermal (binding):** the converter runs near load in the same nose cabinet as the AIO — **cabinet venting must account for power-electronics waste heat**, with converter derating margin at desert ambient (panel review).
- **48 V-side protection:** Blue Sea **7443 20 A UL-489 (80 V-class)** breaker ahead of the converter. **No 32 V automotive fuse gear anywhere on the 48 V side.** Implementation protection schedule (required): feed-conductor gauge/ampacity, converter output overcurrent, breaker DC interrupt rating vs pack fault current, dedicated correctly-rated fuse/breaker on the **Velit 48 V branch**.
- **24 V distribution:** Blue Sea **5026** (32 V rating valid only on the regulated 24 V side). Rail map: fridge 10 A/14 AWG · Yuji strip zones 5 A (Klus extrusions, dimmed) · Scanstrut SC-USB-F3 USB-C PD 7.5 A (24 V in unlocks 60 W profiles) · LandAirSea GPS 3 A (6–24 V in) · door switch dry-contact. Rare 12 V-only fixtures: point-of-load 24→12 bucks, never a bus.
- **Tow-vehicle 12 V is not a house rail:** running/marker/brake lights live on the F-150 7-way, fully isolated from house DC.
- Wiring: single-point ground at the shunt; per-converter fusing on the 48 V bus; ENT + pull strings optional; gauges from measured runs.

### Superseded (history)
- ~~#3 48V→12V converter (~25 A/300 W) + 12 V house rail (#4)~~ — **superseded by D006** (24 V single bus; tow lights aren't house loads).
- ~~#5 lighting on a dedicated 48→24 DC-DC~~ — lighting now rides the single 24 V house bus.

## Truck charging
- **Defer the charger for Juplaya** (solar covers recharge) but **pre-wire 4 AWG + an Anderson tongue connector now**. Charger when added: ~480–600 W 12→48 V DC-DC, ignition-gated.

## Energy budget (July, camped)
- Fridge ~1.0–1.3 kWh/day + AIO ECO idle ~0.72 + Velit duty ~2.4 ≈ **4.1–4.45 kWh/day** vs roof-only ~4.0 kWh/day → **the 2S ground pair is required margin on AC-heavy days**, not optional. ECO/off discipline stands.
