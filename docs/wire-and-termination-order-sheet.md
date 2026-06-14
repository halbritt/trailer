# Wire And Termination Order Sheet

Date: 2026-06-14. First-pass buy sheet for Juplaya DC wire, lugs, terminals, ferrules, and cable consumables. This is the detailed breakout behind the wiring allowance in [ancillary-order-sheet.md](ancillary-order-sheet.md) and the generated [order-sheet.md](order-sheet.md).

## Scope And Assumptions

- These are ordering lengths, not final cut lengths. Cut only after the nose bench component board, roof gland, Velit station, fridge bay, and wall chases are dry-fit.
- Use tinned copper marine primary cable or better for all DC branch wiring; use PV-rated 10 AWG solar cable for roof/ground PV wiring.
- Use adhesive-lined heat shrink on crimped lugs and heat-shrink terminals on branch wiring. Label both ends before the wall closes.
- The 48 V side must use DC-rated protection and switching. Do not use 32 V automotive fuse gear upstream of the 48/24 or 48/12 converters.
- AWG selections are deliberately conservative against the generated power diagram: 2 AWG ~= 35 mm2, 6 AWG ~= 16 mm2, 8 AWG ~= 10 mm2, 10 AWG ~= 6 mm2, 12 AWG ~= 4 mm2, 14 AWG ~= 2.5 mm2.

Known terminal facts:

- LiTime 48 V 100 Ah Smart ComFlex battery terminals: M8 bolts.
- Victron SmartShunt 500A shunt bolts: M10.
- Victron SmartSolar 250/60-Tr PV and battery terminals accept up to 35 mm2 / AWG2.
- Victron SmartSolar 150/35 terminals accept up to 16 mm2 / AWG6.
- Victron Orion-Tr isolated 48/12-20A and 48/24-16A use screw terminals with 16 mm2 / AWG6 maximum cable cross-section.
- Blue Sea 5026 has #10-32 positive/negative bus studs and #8-32 captive branch screws.
- Blue Sea 7443 breaker has #10-32 terminal screws.
- Blue Sea 1011 dash sockets use 0.250 in female quick-connects and are 15 A maximum.
- Scanstrut SC-USB-F3 is 10-32 V input, 6 A maximum input current, with a 10 A recommended fuse.

Sources checked: local reference notes for the LiTime battery, SmartShunt, SmartSolars, Cerbo, and MultiPlus; [Victron Orion-Tr isolated datasheet](https://www.victronenergy.com/upload/documents/Datasheet-Orion-Tr-DC-DC-converters-isolated-100-250-400W-EN.pdf); [Blue Sea 5026](https://www.bluesea.com/products/5026/ST_Blade_Fuse_Block_-_12_Circuits_with_Negative_Bus_and_Cover); [Blue Sea 7443](https://www.bluesea.com/products/7443/UL-489_Circuit_Breaker_-_20A_Flat_Rocker); [Blue Sea 1011 FAQ](https://www.bluesea.com/products/1011/Dash_Socket_12V_DC_with_Watertight_Cap/FAQ); and [Scanstrut SC-USB-F3](https://www.scanstrut.com/marine/power/usb/flip-pro/sc-usb-f3).

Still verify at dry-fit:

- Class-T holder stud size.
- Final positive/negative busbar stud size.
- Velit delivered harness, fuse, and termination style.
- Blue Sea 8282 switch tab size; plan for 0.250 in female quick-connects but verify on the delivered switches.
- Chassis bond bolt size and exact cleaned-frame bond location.

## Wire To Order

| Qty | Wire | Length to buy | Primary use | Terminal plan |
|---:|---|---:|---|---|
| 1 | 2 AWG red tinned battery cable | 10 ft | 48 V battery positive spine: battery -> Class-T -> positive bus | M8 battery lug; Class-T and busbar studs TBD |
| 1 | 2 AWG black tinned battery cable | 10 ft | 48 V negative spine: battery -> SmartShunt -> negative bus | M8 battery lug; M10 SmartShunt lug; busbar stud TBD |
| 1 | 4 AWG red tinned battery cable | 35 ft | Future truck-charge tongue pre-wire positive | Coil until charger plan; Anderson SB175-style 4 AWG contact or fuse lug later |
| 1 | 4 AWG black tinned battery cable | 35 ft | Future truck-charge tongue pre-wire negative | Coil until charger plan; Anderson SB175-style 4 AWG contact or fuse lug later |
| 1 | 6 AWG red tinned primary cable | 20 ft | SmartSolar 250/60 battery-side positive and other 48 V high-current short runs | Ferrule at Victron screw terminal; ring at OCP/bus |
| 1 | 6 AWG black tinned primary cable | 20 ft | SmartSolar 250/60 battery-side negative and high-current returns | Ferrule at Victron screw terminal; ring at bus |
| 1 | 6 AWG green or black tinned cable | 10 ft | DC negative-to-chassis bond | Ring at busbar and chassis bond bolt |
| 1 | 10 AWG red tinned primary cable | 50 ft | Velit branch positive, Orion outputs, 12 V receptacle trunk, winter/top-up rough-ins | #10/#8 rings, ferrules, or quick-connects by endpoint |
| 1 | 10 AWG black tinned primary cable | 50 ft | Matching returns for Velit, Orion outputs, 12 V trunk | #10/#8 rings, ferrules, or quick-connects by endpoint |
| 1 | 12 AWG red tinned primary cable | 50 ft | Orion inputs, heater/C1000 rough-in branch positives, general protected 15 A circuits | #10/#8 rings or ferrules |
| 1 | 12 AWG black tinned primary cable | 50 ft | Matching returns for 12 AWG protected circuits | #10/#8 rings or ferrules |
| 1 | 14 AWG red tinned primary cable | 50 ft | Fridge, USB-C, fan, Cerbo/small fused loads where local run is short | #8 rings/forks at 5026; butt/ferrule/quick-connect by device |
| 1 | 14 AWG black tinned primary cable | 50 ft | Matching returns for fridge, USB-C, fan, Cerbo/small loads | #8 rings/forks at 5026; butt/ferrule/quick-connect by device |
| 1 | 16/2 tinned marine duplex cable | 250 ft | Exterior/interior lighting zone branches | #8 rings/forks at 5026 or switch/dimmer; heat-shrink butt splices at fixtures |
| 1 | 18/2 tinned marine duplex cable | 100 ft | Remote on/off, thermostat, fan control, door/future entry switch signal, small always-on loads | Small ferrules, butt splices, or #8 terminals |
| 1 | 10 AWG red PV wire | 50 ft | Roof 3S and ground 2S PV positive wiring | MC4 contacts, PV disconnect, or ferrule into SmartSolar Tr input |
| 1 | 10 AWG black PV wire | 50 ft | Roof 3S and ground 2S PV negative wiring | MC4 contacts, PV disconnect, or ferrule into SmartSolar Tr input |
| 2 | 10 AWG MC4 extension pair | 25 ft each | Optional deployable LG ground-panel leads | MC4; keep labeled "LG ground 2S only" |

## Circuit Cut List

| Circuit | Est. one-way installed length | AWG | Protection / endpoint notes | Terminations |
|---|---:|---:|---|---|
| Battery positive to Class-T holder | 24 in | 2 AWG red | Main OCP at battery end | M8 battery lug; holder stud TBD |
| Class-T holder to positive bus | 36 in | 2 AWG red | Keep short and protected | Holder stud TBD; busbar stud TBD |
| Battery negative to SmartShunt battery side | 24 in | 2 AWG black | All load/charge current through SmartShunt | M8 battery lug; M10 SmartShunt lug |
| SmartShunt load side to negative bus | 36 in | 2 AWG black | No alternate negative bypasses | M10 SmartShunt lug; busbar stud TBD |
| Negative bus to chassis bond | 36 in | 6 AWG green/black | Bond to cleaned steel with anti-oxidation compound and strain relief | Busbar lug TBD; likely 5/16 in frame lug after dry-fit |
| SmartSolar 250/60 battery positive to OCP/bus | 4 ft | 6 AWG red | Size OCP to conductor and 60 A controller limit | Ferrule at MPPT; ring at OCP/bus |
| SmartSolar 250/60 battery negative to bus | 4 ft | 6 AWG black | Route with positive pair | Ferrule at MPPT; ring at bus |
| SmartSolar 150/35 battery positive/negative to bus | 4 ft pair | 6 AWG red/black | Optional ground solar controller; 35 A limit | Ferrules at MPPT; rings at bus/OCP |
| Roof PV gland/disconnect to SmartSolar 250/60-Tr | 25 ft pair | 10 AWG PV | Roof 3S only; 250 V-class disconnect/OCP | MC4/PV disconnect; ferrules at Tr input if needed |
| Ground PV inlet/disconnect to SmartSolar 150/35 | 10 ft internal + 25 ft external pair | 10 AWG PV | LG ground 2S only; never combine with roof 3S | MC4 at inlet/extensions; ferrules at Tr input if needed |
| 48 V bus to Velit branch OCP to roof unit | 25 ft pair | 10 AWG red/black | Velit branch OCP final value waits on delivered manual/harness; current plan is 48 V, roughly 5-18 A class | Ring at bus/OCP; Velit end per delivered harness |
| 48 V bus to Orion-Tr 48/24 input breaker | 3 ft pair | 10 AWG red/black | Blue Sea 7443 is the 20 A / 80 V DC input breaker | #10 rings at breaker; ferrules at Orion |
| Orion-Tr 48/24 output to Blue Sea 5026 input | 4 ft pair | 10 AWG red/black | 16 A max 24 V house converter output | Ferrules at Orion; #10 rings at 5026 bus studs |
| 48 V bus to Orion-Tr 48/12 input OCP | 3 ft pair | 12 AWG red/black | 48 V input current is small; use DC-rated OCP | Ring at OCP/bus; ferrules at Orion |
| Orion-Tr 48/12 output to 12 V receptacle fuse/sockets | 4 ft trunk + 2 ft/socket | 10 AWG trunk, 12 AWG branch | 20 A converter max; fuse each 12 V socket below socket rating | Ferrules/rings at fuse point; 0.250 in female quick-connects at Blue Sea 1011 sockets |
| Blue Sea 5026 to Dometic CFX3 95DZ fridge | 18 ft pair | 14 AWG red/black | 10 A fuse; verify less than 3 percent voltage drop after route is real | #8 ring/fork at 5026 branch screws; fridge-end pigtail/plug per Dometic harness |
| Blue Sea 5026 to Scanstrut SC-USB-F3 | 10 ft pair | 14 AWG red/black | 10 A fuse per Scanstrut; 24 V input for full PD output | #8 ring/fork at 5026; waterproof butt or device pigtail termination |
| Blue Sea 5026 to LandAirSea GPS hardwire | 8 ft pair | 18 AWG | 3 A fuse; always-on tracker branch | #8 ring/fork at 5026; heat-shrink butt to hardwire lead |
| Blue Sea 5026 to Cerbo GX Mk2 supply | 8 ft pair | 18 AWG | 3 A fuse; dry bench routing | #8 ring/fork at 5026; ferrule/device plug per Cerbo harness |
| Blue Sea 5026 to cabinet fan/thermostat | 8 ft pair | 14-18 AWG | 1 A fuse; thermostat controls fan | #8 ring/fork at 5026; quick-connect/butt at fan and thermostat |
| Interior main/task lighting | 25 ft | 16/2 duplex | 5 A fuse; switch plus dimmer | #8 at 5026; 0.250 quick-connect at switch; butt/ferrule at dimmer/strip |
| Awning strip | 25 ft | 16/2 duplex | 5 A fuse; switch plus dimmer | #8 at 5026; quick-connect/butt/ferrule as panel demands |
| Curbside floods | 35 ft | 16/2 duplex | 5 A fuse; two VAL2-NW9 fixtures on dimmed branch | #8 at 5026; heat-shrink butt to fixture leads |
| Roadside floods | 45 ft | 16/2 duplex | 5 A fuse; two VAL2-NW9 fixtures on dimmed branch | #8 at 5026; heat-shrink butt to fixture leads |
| Nose floods | 18 ft | 16/2 duplex | 5 A fuse; one fixture on each V-nose face | #8 at 5026; heat-shrink butt to fixture leads |
| Rear flood | 45 ft | 16/2 duplex | 5 A fuse; rear loading/work light | #8 at 5026; heat-shrink butt to fixture leads |
| Optional step/courtesy or spare exterior pair | 20 ft | 18/2 or 16/2 duplex | 3-5 A fuse or shared awning branch | #8 at 5026; sealed butt at fixture |
| Side-door future control spare | 25 ft | 18/2 duplex | Signal only; leave labeled pull/spare | Coiled and labeled both ends |
| Future truck-charge pre-wire to tongue | 30 ft pair | 4 AWG red/black | Pull while walls are open; active charger/fuses deferred | Coil at bench; Anderson SB175-style 4 AWG contacts or fuse lugs when charger is selected |

## Terminals And Consumables To Order

| Qty | Item | Use |
|---:|---|---|
| 2 | 2 AWG x M8 tinned copper lugs | Battery positive and negative posts |
| 2 | 2 AWG x M10 tinned copper lugs | SmartShunt 500A shunt bolts |
| 6 | 2 AWG x 5/16 in tinned copper lugs | Likely Class-T/busbar studs; verify before final crimp |
| 4 | 2 AWG x 3/8 in or M10 tinned copper lugs | Spare heavy-lug coverage if holder/busbar wants larger studs |
| 4 | 4 AWG x 5/16 in tinned copper lugs | Future truck-charge fuse/bus terminations |
| 1 set | Anderson SB175-style housing + 4 AWG contacts | Future truck-charge tongue connector, if buying connector now |
| 8 | 6 AWG x 5/16 in tinned copper lugs | SmartSolar/bus/chassis bond large-ring endpoints |
| 6 | 6 AWG x #10 tinned copper lugs | If a selected breaker or terminal block uses #10 screws |
| 20 | 6 AWG ferrules | Victron MPPT/Orion screw-clamp entries |
| 25 | 10 AWG x #10 heat-shrink ring terminals | Blue Sea 7443 and 5026 input studs |
| 25 | 10 AWG x #8 heat-shrink ring or fork terminals | Blue Sea 5026 branch screws where 10 AWG is used |
| 20 | 10 AWG ferrules | Orion and terminal-block entries |
| 20 | 10-12 AWG 0.250 in heat-shrink female quick-connects | Blue Sea 1011 sockets and any high-current switch/device tabs |
| 40 | 12-10 AWG heat-shrink butt connectors | Branch splices and pigtails |
| 50 | 16-14 AWG x #8 heat-shrink ring or fork terminals | Blue Sea 5026 lighting/fridge/USB branch screws |
| 50 | 16-14 AWG 0.250 in heat-shrink female quick-connects | Blue Sea 8282 switches and similar panel controls |
| 50 | 16-14 AWG heat-shrink butt connectors | Lighting fixtures, dimmers, fan, USB/GPS pigtails |
| 50 | 22-18 AWG heat-shrink butt connectors | Signal, remote, thermostat, GPS, Cerbo small wiring |
| 25 | 22-18 AWG x #8 heat-shrink ring or fork terminals | Low-current 5026 branches and signal terminals |
| 1 kit | Assorted insulated ferrules, 18-10 AWG | Screw terminal cleanliness and serviceability |
| 1 kit | 10 AWG MC4 crimp contacts/connectors | PV field repairs and roof/ground lead build-up |
| 1 lot | Adhesive-lined heat shrink, 3:1, 1/4 in, 3/8 in, 1/2 in, 3/4 in | Lug strain relief and environmental sealing |
| 1 lot | Split loom, rubber-lined P-clamps, cable glands, grommets, edge guard | Route protection through bench, wall chases, and penetrations |
| 1 lot | Heat-shrink wire labels plus branch/circuit labels | Label both ends before wall closure |

## Do Not Buy Yet

- Final Class-T holder lug holes and fuse rating until the holder is selected and the main battery OCP decision is closed.
- Final busbar studs if conventional busbars are used, or any Lynx-specific hardware if the build switches to a Victron Lynx distribution block.
- Final Velit extension cable terminals until the delivered 48 V harness and manual are in hand.
- Final panel dimmer terminations until the dimmer SKU is selected after the VAL2-NW9 bench test.
