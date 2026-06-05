# Victron SmartSolar MPPT 150/35 — Key Specs

Optional deployable LG ground-pair controller for D002. Source: Victron SmartSolar MPPT 150/35 and 150/45 technical specifications: https://www.victronenergy.com/media/pg/Manual_SmartSolar_MPPT_150-35__150-45/en/technical-specifications.html

| Spec | Value |
|---|---|
| Model | SmartSolar MPPT 150/35 |
| Battery voltage | 12/24/48 V auto-select; 36 V manual select |
| Maximum battery current | 35 A |
| Nominal PV power at 48 V | 2000 W |
| Max PV short-circuit current | 35 A |
| Maximum PV open-circuit voltage | 150 V |
| PV start / operating threshold | PV must exceed battery voltage + 5 V to start; thereafter battery voltage + 1 V |
| Peak efficiency | 98% |
| Self-consumption | 48 V: 10 mA |
| Default absorption / float at 48 V | 57.6 V / 55.2 V |
| Temperature range | -30 to +60 C; full rated output up to 40 C |
| Communications | VE.Direct; Bluetooth via VictronConnect |
| Terminals | 16 mm2 / AWG6 |
| Size / weight | 130 x 186 x 70 mm; 1.25 kg |

## Build-relevant notes

- **2S LG ground fit:** two LG455 panels in series are 99.8 V Voc at STC and roughly 109-114 V cold signal, comfortably below the 150 V PV ceiling.
- **Output headroom:** 2 x 455 W = 910 W. At 48 V battery voltage that is roughly 17-19 A before losses, well under the 35 A output limit.
- **Not for roof 3S:** three LG455 panels exceed 150 V in cold conditions. Roof 3S stays on the SmartSolar 250/60-Tr.
- **Connector variant:** Tr and MC4 versions are both electrically acceptable for the portable ground pair. If MC4 arrives, still provide a proper disconnect/fusing plan and strain relief at the trailer inlet.
- **Charge coordination:** program current limits so roof SmartSolar + ground SmartSolar + any future charger stays at or below the ComFlex battery's 100 A continuous charge limit.
