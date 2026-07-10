# Victron SmartShunt 500A — Key Specs

Battery monitor for the active Victron monitoring path. Ordered 2026-06-14; expected 2026-06-15.

Sources: Victron SmartShunt product page and official manual/datasheet:
- https://www.victronenergy.com/battery-monitors/smart-battery-shunt
- https://www.victronenergy.com/upload/documents/SmartShunt/9172-Manual_BMV_and_SmartShunt-pdf-en.pdf
- https://www.victronenergy.com/media/pg/SmartShunt/en/installation.html

| Spec | Value |
|---|---|
| Model | SmartShunt 500A / 50mV |
| Role | 48 V battery monitor / system SOC source |
| Supply voltage range | 6.5-70 VDC |
| Current draw | <1 mA |
| Current rating | 500 A |
| Current accuracy | +/-0.4% |
| Voltage accuracy | +/-0.3% |
| Communications | Bluetooth via VictronConnect; VE.Direct to GX device |
| Aux input | second battery voltage, midpoint, or temperature with optional sensor |
| Shunt bolts | M10 |
| Protection | IP21; dry interior mounting |
| Temperature range | -40 to +50 C |
| Dimensions | 120 x 46 x 54 mm / 4.72 x 1.81 x 2.13 in |

## Build-relevant notes

- Replaces the LiTime 500 A Bluetooth shunt as the active trailer battery monitor.
- Install in the battery-negative path: battery negative -> SmartShunt battery-minus side -> load/charger negative bus. Nothing else lands on the battery side.
- Install the supplied fused Vbatt+ cable between battery positive and the SmartShunt Vbatt+ terminal.
- Mount the shunt in the shallow high wall cabinet per D015; route the dedicated battery-negative feeder directly to its battery-side stud.
- Run VE.Direct to the Cerbo GX Mk2 so battery SOC, current, voltage, history, and alarms are visible in VRM.
- Optional temperature sensor can be added later if battery/cabinet temperature telemetry becomes useful; LiFePO4 charge temperature compensation remains off unless the battery manufacturer specifies otherwise.
- Keep the LiTime shunt as spare/test gear, not the design source of truth.
