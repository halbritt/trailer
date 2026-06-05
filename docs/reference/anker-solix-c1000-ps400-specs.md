# Anker SOLIX C1000 + PS400 400 W Panel — Key Specs

Juplaya portable 120 VAC island. Sources: Anker SOLIX C1000 support/product specs (https://service.ankersolix.com/article-description/Introduction-to-Anker-SOLIX-C1000), C1000 user guide mirror with input-voltage detail (https://device.report/manual/10423329), and Anker SOLIX PS400 product page (https://www.ankersolix.com/products/400w-portable-solar-panel).

## C1000 portable power station

| Spec | Value |
|---|---|
| Capacity | 1056 Wh |
| Battery | LiFePO4, 3000 cycles to 80% capacity |
| AC output | 1800 W pure sine continuous; 2400 W surge; 6 outlets |
| Solar / car input | XT-60; 11-32 V at 10 A max, or 32-60 V at 12.5 A max; 600 W max |
| AC input | 1300 W max |
| 12 V output | 120 W, 12 V / 10 A |
| UPS switch | <20 ms |
| USB | USB-C 100 W + 30 W; 2x USB-A 12 W |
| Temperature | discharge -4 to 104 F; charge 32 to 104 F |
| Size / weight | 14.8 x 8.07 x 10.5 in; 28.44 lb |

## PS400 portable panel

| Spec | Value |
|---|---|
| Maximum output | 400 W |
| Open-circuit voltage | 57.6 V |
| Operating voltage / current | 48 V / 8.33 A |
| Output | MC4, with MC4-to-XT-60 cable included |
| Protection | IP67 panel; keep ports protected as instructed |
| Size folded | 39 x 26.6 x 2 in |
| Size unfolded | 100 x 39 x 1.2 in |
| Weight | 35.3 lb |

## Build-relevant notes

- **Generator/MultiPlus deferral:** this combination covers small 120 VAC loads for Juplaya without installing a trailer inverter/charger. It is not a substitute for the 48 V trailer battery.
- **Use as an island:** keep C1000/PS400 electrically separate from trailer AC wiring. Do not backfeed trailer AC wiring.
- **Optional 24 V bus charging:** a fused/manual 24 V feed into the C1000 XT-60 input is electrically plausible because the C1000 accepts 11-32 V at 10 A max. Treat this as a ~240 W maximum auxiliary charge path, not primary charging. It competes with fridge/lights/USB on the same 16 A Orion-Tr 48/24 converter, so only enable it when the 24 V bus has spare capacity.
- **Do not direct-feed from the 48 V bus casually:** the C1000 also accepts 32-60 V at 12.5 A, but the trailer's 48 V battery is a stiff high-current source. If a faster trailer-to-C1000 charge path is needed later, build it as a dedicated fused/current-limited DC-DC charger, not an unfused battery-to-XT60 jumper.
- **Do not series the PS400.** Its 57.6 V Voc is already close to the C1000's 60 V solar input ceiling. Use it as the single Anker-matched input.
- **Thermal discipline:** C1000 charge/discharge is limited to 104 F on the spec sheet. Keep it shaded, off hot floor metal, and ventilated.
- **Load discipline:** fine for laptops, radios, tool batteries, Starlink-class loads, camera gear, and brief small appliance hits. Avoid sustained electric cooking/heating; that reopens the MultiPlus/generator question.
