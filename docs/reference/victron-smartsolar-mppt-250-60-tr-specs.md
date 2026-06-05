# Victron SmartSolar MPPT 250/60-Tr — Key Specs

Roof-solar controller for the revised D002 3-panel architecture. Source: Victron SmartSolar MPPT 150/60 through 250/70 technical specifications: https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-60_up_to_250-70/en/technical-specifications.html

| Spec | Value |
|---|---|
| Model | SmartSolar MPPT 250/60-Tr |
| Battery voltage | 12/24/48 V auto-select; 36 V manual select |
| Maximum battery current | 60 A |
| Nominal PV power at 48 V | 3440 W |
| Max PV short-circuit current | 60 A |
| Maximum PV open-circuit voltage | 250 V absolute maximum in coldest conditions; 245 V start-up/operating maximum |
| PV start / operating threshold | PV must exceed battery voltage + 5 V to start; thereafter battery voltage + 1 V |
| Peak efficiency | 99% |
| Self-consumption | 48 V: <20 mA |
| Default absorption / float at 48 V | 57.6 V / 55.2 V |
| Temperature range | -30 to +60 C; full rated output up to 40 C |
| Communications | VE.Direct; Bluetooth via VictronConnect |
| Terminals | Tr model: 35 mm2 / AWG2 PV and battery terminals |
| Size / weight | 185 x 250 x 95 mm; 3 kg |

## Build-relevant notes

- **Roof 3S fit:** three LG455 panels are 149.7 V Voc at STC before cold correction and about 163-171 V cold signal, so they need this 250 V-class PV input. They must never be plugged into the LiTime AIO's 145 V PV input.
- **Hot-roof margin:** LG455 3S hot Vmpp can fall near ~105-115 V; this remains well above a 48 V battery + 5 V SmartSolar start threshold, unlike 120 V-min AIOs.
- **Overpaneling:** 3 x 455 W = 1365 W, far below the 3440 W nominal PV power rating at 48 V.
- **Charge coordination:** the 60 A controller can exceed the current needed for a 1365 W string. Program a conservative current limit so the SmartSolar plus LiTime AIO/AC charging stays at or below the ComFlex battery's 100 A continuous charge limit.
- **Protection:** use a DC-rated roof PV disconnect/breaker above worst-case cold 3S Voc, and fuse/breaker the battery-side output for controller current and conductor ampacity.
