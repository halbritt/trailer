# Ancillary Electrical Order Sheet

Date: 2026-07-10. Itemized breakout for the non-Victron electrical and control hardware in [order-sheet.md](order-sheet.md). Spec sources: [power.md](power.md), [wire-and-termination-order-sheet.md](wire-and-termination-order-sheet.md), and [juplaya-trailer-context.md](juplaya-trailer-context.md).

Scope: USB-C PD, Blue Sea distribution/switching, 12 V accessory sockets, lighting controls, protection, split-enclosure wiring, labels, and ventilation. Active Victron gear and the incoming MultiPlus-II are treated as on hand or already ordered. MultiPlus placement and installation hardware remain gated separately.

Prices are June 2026 web price signals or allowances, pre-tax/pre-shipping unless noted. Replace with receipt values in [order-sheet-overrides.csv](order-sheet-overrides.csv) as orders land.

## Order Now

| Qty | Item | Unit | Ext | Source | Notes |
|---:|---|---:|---:|---|---|
| 1 | Scanstrut SC-USB-F3 Flip Pro Max dual USB-C | $50.99 | $50.99 | [Defender price signal](https://defender.com/en_us/scanstrut-flip-pro-max-dual-usb-c-charge-socket-sc-usb-f3); [Scanstrut spec](https://www.scanstrut.com/rv/power/usb/flip-pro/flip-pro-max) | 12/24 V input; use on the 24 V bus for full USB-C PD output. |
| 1 | Blue Sea 5026 12-circuit ST Blade fuse block with negative bus | $55.00 | $55.00 | [Blue Sea 5026](https://www.bluesea.com/products/5026/ST_Blade_Fuse_Block_-_12_Circuits_with_Negative_Bus_and_Cover) | Downstream of the 24 V Orion only; 32 V max is fine there. |
| 1 | Blue Sea 7443 UL-489 20 A / 80 V DC flat-rocker breaker | $51.26 | $51.26 | [Blue Sea 7443](https://www.bluesea.com/products/7443/UL-489_Circuit_Breaker_-_20A_Flat_Rocker) | Correct 20 A / 80 V DC breaker. Do not buy 7463 for this DC branch; it is a 2-pole 240 V AC breaker. |
| 1 | Battery-terminal Class-T main OCP fuse + holder | $175.00 | $175.00 | Allowance | Final fuse rating follows cable/OCP selection. No 32 V automotive fuse gear on the 48 V side. |
| 1 lot | DC-rated protection for MPPTs, Velit branch, Orion inputs/outputs | $275.00 | $275.00 | Allowance | Include the Victron-specified 70-80 A roof-MPPT battery fuse and 40-45 A ground-MPPT battery fuse. Velit and Orion ratings called TBD in the install diagrams remain gated. |
| 1 lot | Roof 250 V PV disconnect + ground 150 V PV disconnect/OCP | $180.00 | $180.00 | Allowance | Keep the sources separate; both disconnect current ratings remain TBD. |
| 1 lot | Power wiring, lugs, adhesive heat shrink, busbars, labels, loom, clamps | $450.00 | $450.00 | Allowance | D015 invalidated the old cut lengths. Close G12 and dry-fit the low battery bench, protected feeder chase, and shallow high cabinet before final cuts. |
| 1 set | Cabinet ventilation: 24 V fan, thermostat, transfer grilles/filter | $125.00 | $125.00 | Allowance | Shallow high cabinet only: cabin-side low intake + high fan-assisted exhaust; no through-wall electronics vent unless shakedown fails. |
| 1 set | Fused 12 V cabinet receptacles | $40.00 | $40.00 | [Blue Sea 1011 target](https://www.bluesea.com/products/1011/Dash_Socket_12V_DC_with_Watertight_Cap) | Socket count and individual fuse ratings wait on G12. Mount locally in the shallow high cabinet and label auxiliary only. |
| 1 | Blue Sea 8260 6-position Contura mounting panel | $17.68 | $17.68 | [Fisheries price signal](https://www.fisheriessupply.com/blue-sea-systems-contura-switch-mounting-panels/8260); [Blue Sea 8260](https://www.bluesea.com/products/8260/Contura_Switch_Mounting_Panel_-_6_Position) | Mount in a thin inset plate or rabbet the shallow-cabinet face; official panel thickness limit tops out at 0.38 in. |
| 6 | Blue Sea 8282 SPST OFF-ON Contura switches | $14.00 | $84.00 | [Vanlife price signal](https://www.vanlifeoutfitters.com/products/blue-sea-8282-contura-switch-spst-off-on-black); [Blue Sea 8282](https://www.bluesea.com/products/8282/Contura_Switch_SPST_Black_-_OFF-ON) | Labels: INTERIOR, CURB FLOOD, ROAD FLOOD, NOSE FLOOD, REAR FLOOD, AWNING. |
| 1 set | Custom switch labels / label stock | $25.00 | $25.00 | Allowance | Blue Sea generic labels probably do not cover the exact flood-zone names. |
| 1 | Super Bright LEDs RA-IP68-80CRI-5m 3000 K 24 V awning strip | $109.99 | $109.99 | [Super Bright LEDs](https://www.superbrightleds.com/led-strips-and-bars/waterproof-led-strips/5m-white-led-strip-light-radiant-series-led-tape-light-24v-ip68-waterproof) | Warm camp/awning light; separate from the ordered exterior floods. |
| 1 lot | Interior task/main lighting strips and channels | $250.00 | $250.00 | Allowance | 24 V preferred; exact strip/channel SKU still open. |
| 1 lot | Lighting branch wire, glands, sealant, heat shrink | $140.00 | $140.00 | Allowance | Lighting branch lengths and terminations are included in [wire-and-termination-order-sheet.md](wire-and-termination-order-sheet.md). |
| 1 lot | 4 AWG tongue pre-wire + Anderson connector for future truck charging | $200.00 | $200.00 | Allowance | Pull while walls are open; active truck charging hardware stays deferred. |
| | **Order-now subtotal** | | **$2,228.92** | | |

## Buy After Gate / Bench Test

| Qty | Item | Ext | Trigger | Notes |
|---:|---|---:|---|---|
| 6 | Panel-mount 24 V lighting dimmers | $270.00 | Bench-test one ordered `VAL2-NW9` flood with the selected dimmer and finish the shallow-cabinet control-panel mockup. | Blue Sea 7509 DeckHand is the robust marine reference; cheap PWM knob dimmers such as `LDK-8A` remain prototype/bench-test parts. |
| 1 lot | Roof solar NXT rails, spacers, backing, and through-fasteners | $500.00 | See [solar-mounting-order-sheet.md](solar-mounting-order-sheet.md). | Separate sub-sheet owns this lot. |
| | **Gated subtotal** | **$770.00** | | |

## Cart Rules

- Keep Blue Sea 5026 on the 24 V side only; it is a 32 V fuse block downstream of the 48/24 Orion.
- Use Blue Sea 7443 for the 20 A / 80 V DC UL-489 breaker. Do not substitute Blue Sea 7463 for the DC branch; 7463 is a 2-pole 240 V AC breaker.
- Do not buy a Blue Sea USB-A/old dual-USB charger for the main USB-C position. The Scanstrut SC-USB-F3 is the PD part.
- Do not build a distributed 12 V house rail. The 12 V sockets are local auxiliary outlets downstream of the ordered 48/12 Orion.
- Put receipt prices back into the generated ledger by editing [order-sheet-overrides.csv](order-sheet-overrides.csv), then run `python3 scripts/sync_order_sheet.py`.

## Wire Breakout

Use [wire-and-termination-order-sheet.md](wire-and-termination-order-sheet.md) for the actual wire cart: cable lengths by AWG, per-circuit cut allowances, ring terminal stud sizes, ferrules, quick-connects, MC4 parts, labels, loom, and dry-fit holds.
