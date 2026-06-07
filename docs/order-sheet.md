# Juplaya Trailer Order Sheet

Generated: 2026-06-07 from the [public Google Sheet](https://docs.google.com/spreadsheets/d/1zsKxk9gyynfV_CnIDnnsLITYhqe7sRdxiN1UAf_xCsE/edit?usp=sharing) plus [local overrides](order-sheet-overrides.csv).

This is the build ordering and budget ledger. The [build sheet](juplaya-trailer-context.md) remains the engineering source of truth; this file tracks what is ordered, what remains, rough current pricing, and the math. Spreadsheet source: [Google Sheets CSV export](https://docs.google.com/spreadsheets/d/1zsKxk9gyynfV_CnIDnnsLITYhqe7sRdxiN1UAf_xCsE/export?format=csv). Local CSV: [order-sheet.csv](order-sheet.csv). Local correction layer: [order-sheet-overrides.csv](order-sheet-overrides.csv).

Rules for the numbers:

- Prices are pre-tax and usually pre-shipping unless the sheet's `extended_price` includes them.
- `extended_price` is the counted budget field; `unit_price` is informational.
- `Receipt needed` means the item is bought/on-hand/ordered, but the repo may still lack the real receipt amount.
- Base trailer purchase, tow vehicle, and receipt-unknown on-hand items are not counted in the fit-out totals unless `extended_price` is populated on a counted `LINE` row.
- The LiTime 5 kW AIO is a return item and is not part of the active build budget.

## Status Legend

| Status | Meaning |
| --- | --- |
| ON HAND | Already owned or physically present. Receipt may still be missing. |
| PURCHASED | Bought before this sheet; included only when a counted line has `extended_price`. |
| ORDERED | Ordered for this build. Replace planning values with receipt values when known. |
| BUY NOW | Needed for the Juplaya build and not blocked by an open gate. |
| BUY AFTER GATE | Needed, but wait for measurement/design gate closure before ordering. |
| FAB/SOURCE | Owner fabrication, local sourcing, or mixed hardware stock. |
| DEFERRED | Phase 2 or winter item, not a Juplaya blocker. |
| RETURN | Remove from the active build. |

## Budget Math

| Bucket | Counted Total | Notes |
| --- | --- | --- |
| Priced committed / ordered / purchased fit-out | $4,233.28 | Calculated from `LINE` rows where `bucket = Committed`. |
| Remaining Juplaya buy list | $10,892.84 | Calculated from `LINE` rows where `bucket = Remaining`. |
| Current Juplaya fit-out planning total | $15,126.12 | Committed plus remaining; excludes base trailer, tow vehicle, and receipt-unknown on-hand major gear. |
| Deferred Phase 2 / winter list | $3,149.00 | Calculated from `LINE` rows where `bucket = Deferred`; not required for Juplaya. |
| Full visible project list including deferred | $18,275.12 | Current total plus deferred, with the same exclusions. |

Remaining Juplaya buy list by category:

| Category | Remaining Total |
| --- | --- |
| Power / solar / cabinet | $2,653.60 |
| Climate / envelope / awning | $4,194.67 |
| Interior / floor / walls | $2,275.00 |
| Lighting / switches / security | $1,269.57 |
| General consumables contingency | $500.00 |

Important interpretation: the current cash-to-spend number is the `$10,892.84` remaining list, reduced by anything already quietly ordered or already in shop stock. The `$15,126.12` number is the visible Juplaya fit-out value, not the remaining cash need.

## Sunk / On-Hand / Receipt-Needed

These are real build inputs, but they are excluded from the fit-out math unless promoted to a counted `LINE` row.

| Status | System | Qty | Item | Price Signal | Counted | Notes |
| --- | --- | ---: | --- | ---: | ---: | --- |
| PURCHASED | Base trailer | 1 | Wells Cargo / ACG FasTrac Deluxe FT712S2-D VIN 7V0W11214TU444163 | $8,456.05 | Excluded | Base trailer cost lives in the buyer-order record not this fit-out subtotal. |
| ON HAND | Solar | 5 | LG455N2W-E6 panels | $300.00 | Excluded | Three roof panels two optional ground panels. |
| ON HAND | Battery | 1 | LiTime 48 V 100 Ah Smart ComFlex battery | $1,219.99 | Excluded | 5.12 kWh trailer battery. |
| ON HAND | Battery monitor | 1 | LiTime 500 A Bluetooth shunt | $105.99 | Excluded | Single-point ground/instrumentation item. |
| ON HAND | AC island | 1 | Anker SOLIX C1000 + PS400 400 W panel | $0.00 | Excluded | Portable AC island for Juplaya small 120 VAC loads. |
| ON HAND | Track | 50ft | E-track | $239.95 | Excluded | Treat as wall-track stock first not floor stock. |
| ON HAND | Wall stock | 2 sheets | 3/8 in and 1/2 in birch sheet stock | $0.00 | Excluded | Existing stock offsets the wall/fixture allowances below. |
| ORDERED | Truck support | 1 set | Ford integrated trailer backup camera + TPMS sensors | $626.27 | Excluded | Tow-vehicle/trailer-support item outside fit-out math for now. |

## Return Items

| Status | System | Qty | Item | Price Signal | Counted | Notes |
| --- | --- | ---: | --- | ---: | ---: | --- |
| RETURN | Power | 1 | LiTime 48 V 5 kW AIO inverter/charger | $859.99 | $0.00 | Mistaken order. Return; do not replace with a LiTime 3.5 kW AIO for Juplaya. |

## Ordered / Purchased / Priced

| Status | System | Qty | Item | Unit | Ext | Basis / Source | Notes |
| --- | --- | ---: | --- | ---: | ---: | --- | --- |
| PURCHASED | Fridge | 1 | Dometic CFX3 95DZ | $875.00 | $875.00 | eBay order price | eBay score. Actual counted cost is 875. |
| ORDERED | Cooling | 1 | Velit 2000R 48 V rooftop AC | $1,679.00 | $1,679.00 | [Actual ordered price](https://velitcamping.com/products/velit-2000r-rooftop-air-conditioner-12v-24v?variant=43751785201901) | Actual ordered price. |
| ORDERED | Roof solar | 1 | Victron SmartSolar MPPT 250/60-Tr | $400.47 | $400.47 | [Actual ordered price](https://www.wholesalemarine.com/victron-smartsolar-mppt-250-60-tr-solar-charge-controller/) | Actual ordered price. |
| ORDERED | Ground solar | 1 | Victron SmartSolar MPPT 150/35 | $150.00 | $150.00 | User order price | Used unit free shipping; TR/MC4 connector variant pending but either is acceptable. |
| ORDERED | 12 V auxiliary | 1 | Victron Orion-Tr IP43 48/12-20A isolated converter | $113.90 | $113.90 | [NAZ Solar price signal](https://www.solar-electric.com/victron-energy-orion-tr-48-12-20a-dc-dc-converter.html) | Receipt needed; feeds cabinet-only fused 12 V receptacles. |
| ORDERED | Floor coating | 3 | Durabak-18 Outdoor Textured light grey | $155.00 | $465.00 | [Durabak product page and conservative prior evidence](https://www.durabakcompany.com/products/durabak-marine-liner-outdoor-textured) | Ordered for June 12-15 delivery. Current page may be lower; keep high-side until receipt is entered. |
| ORDERED | Exterior lights | 7 | Super Bright LEDs VAL2-NW9 floods | $29.99 | $209.93 | [Super Bright LEDs price signal](https://www.superbrightleds.com/vehicle-lights/off-road-lights/9-rv-trailer-led-light-porch-and-utility-light-1450-lumen-12v) | Seven 4000 K flood/scene fixtures. |
| ORDERED | Floor track | 2 | 8 ft flanged L-track sections | $80.00 | $160.00 | [US Cargo Control price signal](https://www.uscargocontrol.com/products/96-flanged-airline-style-track-aluminum) | Receipt needed; user has two sections on the way. |
| ORDERED | Bike chocks | 2 | Bolt It On 360 L-track wheel chocks | $79.99 | $159.98 | [Bolt It On product page](https://boltiton.com/products/new-360-l-track-dirt-bike-bicycle-floor-mount-wheel-chock) | Basic chock price; studs/quick-release kit may add cost if not ordered with them. |
| ORDERED | Security | 1 | Nu-Set 8-1/4 in high-security trailer-door puck hasp | $20.00 | $20.00 | [Actual ordered price](https://www.nusetlock.com/products/nuset-8-1-4-high-security-trailer-door-hasp-in-stealth-blackl) | User ordered Nu-Set RV high-security hasp for puck lock for 20.00. Source says hardware is not included. |

Committed / purchased subtotal: **$4,233.28**.

## Remaining Juplaya Buys

### Power / solar / cabinet

| Status | Qty | Item | Unit | Ext | Basis / Source | Notes |
| --- | ---: | --- | ---: | ---: | --- | --- |
| BUY NOW | 1 | Victron Orion-Tr 48/24-16A isolated converter | $201.45 | $201.45 | [NAZ Solar price signal](https://www.solar-electric.com/victron-energy-orion-tr-48-24-16a-dc-dc-converter.html) | Required 24 V house bus converter. |
| BUY NOW | 1 | Blue Sea 5026 12-circuit ST Blade fuse block | $55.00 | $55.00 | Allowance | 24 V branch distribution; 32 V max is fine downstream of the converter only. |
| BUY NOW | 1 | Blue Sea 7443 UL-489 20 A / 80 V breaker or verified equivalent | $51.26 | $51.26 | [Blue Sea official page](https://www.bluesea.com/products/7443/) | Docs previously had 7463-vs-7443 uncertainty; verify SKU before ordering. |
| BUY NOW | 1 | Battery-terminal Class-T main OCP fuse + holder | $175.00 | $175.00 | Allowance | Main 48 V fault protection. Do not substitute 32 V automotive gear. |
| BUY NOW | 1 lot | DC-rated protection for MPPTs Velit branch Orion inputs/outputs | $275.00 | $275.00 | Allowance | Fuse/breaker values wait on measured wire runs. |
| BUY NOW | 1 lot | Roof 250 V PV disconnect + ground 150 V PV disconnect/OCP | $180.00 | $180.00 | Allowance | Roof 3S needs 250 V-class hardware. |
| BUY NOW | 1 lot | Power wiring lugs heat shrink busbars labels loom | $450.00 | $450.00 | Allowance | Covers cabinet wiring and branch terminations not final gauge-certification. |
| BUY AFTER GATE | 1 lot | Roof solar NXT rails, spacers, backing, and through-fasteners | $500.00 | $500.00 | Allowance | Two fore-aft NXT rails plus possible third rail, 1/4 in aluminum spacer pads at bow crossings if needed, EPDM/neoprene isolation or high-durometer spacer material, backing plates/crush sleeves, through-fasteners, clips, gland, adhesive/bedding, and sealant consumables. |
| FAB/SOURCE | 1 | Power cabinet structure mounting board service panels | $250.00 | $250.00 | Allowance | Does not include battery/electronics above. |
| BUY NOW | 1 set | Cabinet ventilation: 24 V fan thermostat transfer grilles/filter | $125.00 | $125.00 | Allowance | Cabin-side intake/exhaust plan no through-wall vent for now. |
| BUY NOW | 1 set | Fused cigarette-lighter receptacles for cabinet 12 V | $40.00 | $40.00 | Allowance | Auxiliary only not a distributed 12 V rail. |
| BUY NOW | 1 | Scanstrut SC-USB-F3 Flip Pro Max dual USB-C | $50.99 | $50.99 | [Defender price signal](https://defender.com/en_us/scanstrut-flip-pro-max-dual-usb-c-charge-socket-sc-usb-f3) | 24 V input unlocks full USB-C output. |
| BUY NOW | 1 each | LandAirSea Overdrive GPS + hardwire cable | $99.90 | $99.90 | [Tracker + hardwire price signal](https://landairsea.com/products/landairsea-overdrive) | Preferred for Oakland storage if delivery timing allows: larger 4240 mAh backup battery, commercial/rugged tracker, stronger GNSS/cellular antennas. LandAirSea 54 + USB-C hardwire remains the acceptable immediate fallback at about 54.90. Both require a subscription. |
| BUY NOW | 1 lot | 4 AWG tongue pre-wire + Anderson connector for future truck charging | $200.00 | $200.00 | Allowance | Pull while walls are open; active charging hardware deferred. |

Power / solar / cabinet remaining subtotal: **$2,653.60**.

### Climate / envelope / awning

| Status | Qty | Item | Unit | Ext | Basis / Source | Notes |
| --- | ---: | --- | ---: | ---: | --- | --- |
| BUY NOW | 1 | Henry 887 Tropi-Cool White 100% Silicone Roof Coating 4.75 gal | $369.00 | $369.00 | [Home Depot price signal](https://www.homedepot.com/p/Henry-887-Tropi-Cool-White-100-Silicone-Reflective-Roof-Coating-4-75-gal-HE887HS018/205049553) | One pail unless measured roof drawing proves less. |
| BUY NOW | 6 | Henry 884 Tropi-Cool silicone sealant tubes | $21.97 | $131.82 | [Home Depot price signal](https://www.homedepot.com/p/206030008) | Penetrations curbs fasteners transitions. |
| BUY NOW | 1 lot | Roof coating prep/rollers/cleaner/PPE | $120.00 | $120.00 | Allowance | Includes adhesion patch supplies. |
| BUY AFTER GATE | 1 job | Closed-cell spray foam | $1,000.00 | $1,000.00 | Allowance | Confirm clean/dry/rust-free steel before closure. |
| BUY AFTER GATE | 2 | RecPro RP-FRMWIN-1222-TRM frameless windows | $164.95 | $329.90 | [RecPro price signal](https://recpro.com/rv-frameless-window-12-w-x-22-h/) | Rear cross-flow windows; current page showed out-of-stock so watch availability. |
| BUY AFTER GATE | 1 | RecPro RP-FRMWIN-2015-TRM frameless door window | $184.95 | $184.95 | [RecPro price signal](https://recpro.com/rv-frameless-window-20-w-x-15-h/) | Door RO and perimeter re-frame gate first. |
| BUY AFTER GATE | 1 lot | Window furring butyl isolators stainless/nylon hardware | $150.00 | $150.00 | Allowance | Builds openings to the 1.5 in trim-ring spec. |
| ORDERED | 1 | Fiamma F45s 350 06280B01R | $1,419.00 | $1,419.00 | [Fiamma USA price signal](https://www.fiammausa.com/en/f45s-en.html) | Long-lead shade deliverable. |
| BUY NOW | 1 | Fiamma Tie Down S black kit 98655-133 | $45.00 | $45.00 | Allowance | Source with the awning if possible. |
| FAB/SOURCE | 1 lot | Awning standoff steel backing fasteners sealant | $250.00 | $250.00 | Allowance | Wait for rail scan/post wall thickness before cutting final parts. |
| BUY NOW | 1 lot | 3/8 in x 12 in lags/deadman bag materials | $75.00 | $75.00 | Allowance | Playa anchoring for awning legs/tie-down. |
| BUY AFTER GATE | 2 | HRV 4 in rough-in ports/caps + pull string | $0.00 | $0.00 | Zeroed until parts are selected | Cost intentionally held at zero for now. |
| BUY AFTER GATE | 1 set | Heater 3 in duct rough-in + 24 V feed + CO detector | $120.00 | $120.00 | Allowance | LF Bros N4 itself deferred. |

Climate / envelope / awning remaining subtotal: **$4,194.67**.

### Interior / floor / walls

| Status | Qty | Item | Unit | Ext | Basis / Source | Notes |
| --- | ---: | --- | ---: | ---: | --- | --- |
| BUY NOW | 1 lot | L-track studs/quick-release hardware backing through-bolts | $150.00 | $150.00 | Allowance | Confirm what shipped with the Bolt It On chocks first. |
| BUY NOW | 1 lot | Durabak floor prep/coating supplies | $120.00 | $120.00 | Allowance | Rollers masking solvent/wipes PPE patch-test supplies. |
| BUY AFTER GATE | 1 lot | Additional exterior/marine birch wall stock | $300.00 | $300.00 | Allowance | Offset by on-hand sheets where usable. |
| BUY AFTER GATE | 1 lot | FRP panels trim profiles adhesive | $600.00 | $600.00 | Allowance | Must be warranted over selected birch/adhesive stack. |
| BUY AFTER GATE | 1 lot | Wall E-track backing/hardware + shoring sockets | $300.00 | $300.00 | Allowance | E-track itself is on hand; backing/hardware still costs money. |
| BUY AFTER GATE | 1 lot | Bed platform lumber/hardware | $250.00 | $250.00 | Allowance | 2x4 shoring-beam deck removable. |
| BUY AFTER GATE | 1 lot | Fridge bay partition ventilation pieces straps | $200.00 | $200.00 | Allowance | Must keep Dometic 50 mm clearance and forced through-flow. |
| BUY NOW | 1 | Folding/telescoping RV entry step | $125.00 | $125.00 | Allowance | Stows on track grid. |
| BUY AFTER GATE | 1 lot | Panel transport slot padding/straps/fittings | $75.00 | $75.00 | Allowance | For the two optional LG ground panels. |
| BUY AFTER GATE | 1 | Durabak-18 Outdoor Textured light grey conditional 4th gallon | $155.00 | $155.00 | [Conditional allowance](https://www.durabakcompany.com/products/durabak-marine-liner-outdoor-textured) | Order only if the 3 gal coverage or patch test says ramp cove or wear lanes need it. |

Interior / floor / walls remaining subtotal: **$2,275.00**.

### Lighting / switches / security

| Status | Qty | Item | Unit | Ext | Basis / Source | Notes |
| --- | ---: | --- | ---: | ---: | --- | --- |
| BUY NOW | 1 lot | Interior task/main lighting strips channels local dimmers | $250.00 | $250.00 | Allowance | 24 V preferred; final strip SKU still open. |
| BUY NOW | 1 | Super Bright LEDs RA-IP68-80CRI-5m 3000 K 24 V awning strip | $109.99 | $109.99 | [Super Bright LEDs price signal](https://www.superbrightleds.com/led-strips-and-bars/waterproof-led-strips/5m-white-led-strip-light-radiant-series-led-tape-light-24v-ip68-waterproof) | Separate warm camp light not another flood. |
| BUY NOW | 1 | Blue Sea 8260 6-position Contura mounting panel | $17.68 | $17.68 | [Fisheries Supply price signal](https://www.fisheriessupply.com/blue-sea-systems-contura-switch-mounting-panels/8260) | Mount in thin inset plate or rabbet thick cabinet face. |
| BUY NOW | 6 | Blue Sea 8282 SPST OFF-ON Contura switches | $14.00 | $84.00 | [Vanlife Outfitters price signal](https://www.vanlifeoutfitters.com/products/blue-sea-8282-contura-switch-spst-off-on-black) | INTERIOR CURB FLOOD ROAD FLOOD NOSE FLOOD REAR FLOOD AWNING. |
| BUY NOW | 1 | Super Bright LEDs LDK-8A PWM dimmer | $7.95 | $7.95 | [Super Bright LEDs price signal](https://www.superbrightleds.com/led-strips-and-bars/ldk-8a-12-24-volt-dc-single-color-led-dimmer-single-color-led-dimmer) | After the AWNING switch. |
| BUY NOW | 1 set | Custom switch labels / label stock | $25.00 | $25.00 | Allowance | Blue Sea generic labels may not cover these names. |
| BUY NOW | 1 lot | Lighting branch wire glands sealant heat shrink | $140.00 | $140.00 | Allowance | Exterior branch wiring and penetrations. |
| BUY NOW | 1 set | Security locks: Proven 2178, 2 keyed-alike PACLOCK UCS-7A pucks, Trimax TCL65 | $589.95 | $589.95 | [Proven + Trimax + PACLOCK high-side allowance](https://paclock.com/product/7-series/) | Trailer has a 2 in coupler; Proven 2516 is for 2-5/16 in and is not the correct default. Buy two PACLOCK 7-Series flat-back puck locks in the same UCS keyed-alike/U-PICK code: one rear ramp, one Nu-Set personnel-door hasp. Match the truck's existing PACLOCK U-PICK code only if those truck locks are UCS; PRO/SR/RD families do not automatically share codes. Prefer stainless bodies if the storage spot is exposed to Bay Area wet/salt; aluminum UCS-7A is acceptable if budget wins. Verify the ramp latch is puck-compatible; if not, add a puck hasp or use a PACLOCK keyed-alike UCS padlock as the fallback. |
| BUY NOW | 1 set | Personnel-door hasp backing/install hardware | $45.00 | $45.00 | [Allowance](https://www.nusetlock.com/products/nuset-8-1-4-high-security-trailer-door-hasp-in-stealth-blackl) | Nu-Set hasp needs six 3/8 in carriage bolts/washers/nuts plus backing plates and sealant. Tie into the door frame/jamb, not thin door skin alone. External puck remains unattended/travel/storage only, not an occupied-mode latch. |

Lighting / switches / security remaining subtotal: **$1,269.57**.

### General consumables contingency

| Status | Qty | Item | Unit | Ext | Basis / Source | Notes |
| --- | ---: | --- | ---: | ---: | --- | --- |
| BUY NOW | 1 | General consumables contingency | $500.00 | $500.00 | Allowance | Stainless hardware blades/bits sealants abrasives cable clamps shop supplies. |

General consumables contingency remaining subtotal: **$500.00**.

Remaining Juplaya subtotal: **$10,892.84**.

## Deferred / Not Juplaya

| Status | System | Qty | Item | Unit | Ext | Notes |
| --- | --- | ---: | --- | ---: | ---: | --- |
| DEFERRED | Inverter / shore | 1 | Victron MultiPlus-II 48/3000/35-50 120V | $1,200.00 | $1,200.00 | Phase 2 built-in inverter/charger/transfer. Not a Juplaya blocker. |
| DEFERRED | AC distribution | 1 lot | Shore inlet AC panel outlets transfer wiring conduit | $400.00 | $400.00 | Only needed if MultiPlus is installed. |
| DEFERRED | Winter heat | 1 | LF Bros N4 24 V diesel heater | $300.00 | $300.00 | Unit stays outside when operating; July rough-in only. |
| DEFERRED | Ventilation | 1 | Future HRV unit | $350.00 | $350.00 | Rough-in only for Juplaya. |
| DEFERRED | Power cabinet | 1 | Exterior vent retrofit | $100.00 | $100.00 | Only if cabin-side ventilation fails shakedown. |
| DEFERRED | Truck charging | 1 lot | 12 V truck to 48 V trailer charging hardware | $550.00 | $550.00 | Pre-wire now active charging later. |
| DEFERRED | Comms | 1 | Starlink Mini kit | $249.00 | $249.00 | Optional Oakland-storage and camp comms path; secondary to hidden cellular GPS. Requires open sky, theft-resistant mount if left outside, and a power schedule or live solar. Service plan is recurring and not included in the fit-out subtotal. |

Deferred subtotal: **$3,149.00**.

## Sync Procedure

Edit the public Google Sheet, then run:

```bash
python3 scripts/sync_order_sheet.py
```

The script downloads the sheet, applies [order-sheet-overrides.csv](order-sheet-overrides.csv), rewrites [order-sheet.csv](order-sheet.csv), regenerates this Markdown file, and prints the counted totals.
