# Ancillary Electrical Order Sheet

Date: 2026-06-14. Itemized breakout for the non-Victron electrical and control hardware in [order-sheet.md](order-sheet.md). Spec sources: [power.md](power.md) and [juplaya-trailer-context.md](juplaya-trailer-context.md).

Scope: USB-C PD, Blue Sea distribution/switching, 12 V accessory sockets, lighting controls, protection, bench wiring, labels, and ventilation. All active Juplaya Victron gear is treated as **already ordered**: SmartSolar 250/60-Tr, SmartSolar 150/35, Orion-Tr 48/24-16A, Orion-Tr IP43 48/12-20A, SmartShunt 500A, and Cerbo GX Mk2. MultiPlus-II remains Phase 2/deferred.

Prices are June 2026 web price signals or allowances, pre-tax/pre-shipping unless noted. Replace with receipt values in [order-sheet-overrides.csv](order-sheet-overrides.csv) as orders land.

## Order Now

| Qty | Item | Unit | Ext | Source | Notes |
|---:|---|---:|---:|---|---|
| 1 | Scanstrut SC-USB-F3 Flip Pro Max dual USB-C | $50.99 | $50.99 | [Defender price signal](https://defender.com/en_us/scanstrut-flip-pro-max-dual-usb-c-charge-socket-sc-usb-f3); [Scanstrut spec](https://www.scanstrut.com/rv/power/usb/flip-pro/flip-pro-max) | 12/24 V input; use on the 24 V bus for full USB-C PD output. |
| 1 | Blue Sea 5026 12-circuit ST Blade fuse block with negative bus | $55.00 | $55.00 | [Blue Sea 5026](https://www.bluesea.com/products/5026/ST_Blade_Fuse_Block_-_12_Circuits_with_Negative_Bus_and_Cover) | Downstream of the 24 V Orion only; 32 V max is fine there. |
| 1 | Blue Sea 7443 UL-489 20 A / 80 V DC flat-rocker breaker | $51.26 | $51.26 | [Blue Sea 7443](https://www.bluesea.com/products/7443/UL-489_Circuit_Breaker_-_20A_Flat_Rocker) | Correct 20 A / 80 V DC breaker. Do not buy 7463 for this DC branch; it is a 2-pole 240 V AC breaker. |
| 1 | Battery-terminal Class-T main OCP fuse + holder | $175.00 | $175.00 | Allowance | Final fuse rating follows cable/OCP selection. No 32 V automotive fuse gear on the 48 V side. |
| 1 lot | DC-rated protection for MPPTs, Velit branch, Orion inputs/outputs | $275.00 | $275.00 | Allowance | Fuse/breaker values wait on measured wire runs; budget held as a lot. |
| 1 lot | Roof 250 V PV disconnect + ground 150 V PV disconnect/OCP | $180.00 | $180.00 | Allowance | Roof 3S needs 250 V-class hardware. Ground 2S can use lower voltage hardware but stays separate. |
| 1 lot | Power wiring, lugs, adhesive heat shrink, busbars, labels, loom, clamps | $450.00 | $450.00 | Allowance | Bench wiring and branch terminations; buy after the component board mockup so lug stud sizes and cable lengths are known. |
| 1 set | Cabinet ventilation: 24 V fan, thermostat, transfer grilles/filter | $125.00 | $125.00 | Allowance | Cabin-side low intake + high fan-assisted exhaust; no through-wall vent unless shakedown fails. |
| 1 set | Fused 12 V cabinet receptacles | $40.00 | $40.00 | [Blue Sea 1011 target](https://www.bluesea.com/products/1011/Dash_Socket_12V_DC_with_Watertight_Cap) | Default target is 2 sockets downstream of the 48/12 Orion, with local fuse/labels. Auxiliary only. |
| 1 | Blue Sea 8260 6-position Contura mounting panel | $17.68 | $17.68 | [Fisheries price signal](https://www.fisheriessupply.com/blue-sea-systems-contura-switch-mounting-panels/8260); [Blue Sea 8260](https://www.bluesea.com/products/8260/Contura_Switch_Mounting_Panel_-_6_Position) | Mount in thin inset plate or rabbet thick bench face; official panel thickness limit tops out at 0.38 in. |
| 6 | Blue Sea 8282 SPST OFF-ON Contura switches | $14.00 | $84.00 | [Vanlife price signal](https://www.vanlifeoutfitters.com/products/blue-sea-8282-contura-switch-spst-off-on-black); [Blue Sea 8282](https://www.bluesea.com/products/8282/Contura_Switch_SPST_Black_-_OFF-ON) | Labels: INTERIOR, CURB FLOOD, ROAD FLOOD, NOSE FLOOD, REAR FLOOD, AWNING. |
| 1 set | Custom switch labels / label stock | $25.00 | $25.00 | Allowance | Blue Sea generic labels probably do not cover the exact flood-zone names. |
| 1 | Super Bright LEDs RA-IP68-80CRI-5m 3000 K 24 V awning strip | $109.99 | $109.99 | [Super Bright LEDs](https://www.superbrightleds.com/led-strips-and-bars/waterproof-led-strips/5m-white-led-strip-light-radiant-series-led-tape-light-24v-ip68-waterproof) | Warm camp/awning light; separate from the ordered exterior floods. |
| 1 lot | Interior task/main lighting strips and channels | $250.00 | $250.00 | Allowance | 24 V preferred; exact strip/channel SKU still open. |
| 1 lot | Lighting branch wire, glands, sealant, heat shrink | $140.00 | $140.00 | Allowance | Exterior branch wiring and penetrations for floods/awning/interior lighting. |
| 1 lot | 4 AWG tongue pre-wire + Anderson connector for future truck charging | $200.00 | $200.00 | Allowance | Pull while walls are open; active truck charging hardware stays deferred. |
| | **Order-now subtotal** | | **$2,228.92** | | |

## Buy After Gate / Bench Test

| Qty | Item | Ext | Trigger | Notes |
|---:|---|---:|---|---|
| 6 | Panel-mount 24 V lighting dimmers | $270.00 | Bench-test one ordered `VAL2-NW9` flood with the selected dimmer and finish the bench-panel mockup. | Blue Sea 7509 DeckHand is the robust marine reference; cheap PWM knob dimmers such as `LDK-8A` remain prototype/bench-test parts. |
| 1 lot | Roof solar NXT rails, spacers, backing, and through-fasteners | $500.00 | See [solar-mounting-order-sheet.md](solar-mounting-order-sheet.md). | Separate sub-sheet owns this lot. |
| | **Gated subtotal** | **$770.00** | | |

## Cart Rules

- Keep Blue Sea 5026 on the 24 V side only; it is a 32 V fuse block downstream of the 48/24 Orion.
- Use Blue Sea 7443 for the 20 A / 80 V DC UL-489 breaker. Do not substitute Blue Sea 7463 for the DC branch; 7463 is a 2-pole 240 V AC breaker.
- Do not buy a Blue Sea USB-A/old dual-USB charger for the main USB-C position. The Scanstrut SC-USB-F3 is the PD part.
- Do not build a distributed 12 V house rail. The 12 V sockets are local auxiliary outlets downstream of the ordered 48/12 Orion.
- Put receipt prices back into the generated ledger by editing [order-sheet-overrides.csv](order-sheet-overrides.csv), then run `python3 scripts/sync_order_sheet.py`.
