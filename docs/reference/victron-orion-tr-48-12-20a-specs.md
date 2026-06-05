# Victron Orion-Tr IP43 48/12-20A Isolated Converter

Source: Victron Energy product page and the official Orion-Tr isolated DC-DC converter datasheet, checked 2026-06-05.

Product page: <https://www.victronenergy.com/dc-dc-converters/orion-tr-dc-dc-converters-isolated>

Datasheet: <https://www.victronenergy.com/upload/documents/Datasheet-Orion-Tr-DC-DC-converters-isolated-100-250-400W-EN.pdf>

## Relevant Build Facts

- Model: **Orion-Tr 48/12-20A (240 W) isolated DC-DC converter**.
- Use in trailer: auxiliary 12 V converter for fused cigarette-lighter receptacles in the power cabinet; not a distributed 12 V house rail.
- Input voltage range: **32-70 V**.
- Nominal output: **12.2 V**.
- Output adjustment range: **10-15 V**.
- Continuous output current at 40 C: **20 A**.
- Continuous output power at 40 C: **240 W**.
- Efficiency: **87 %**.
- No-load input current: **<80 mA**.
- Disabled current via remote port: **<200 uA**.
- Isolation: **200 VDC** between input, output, and case.
- Temperature range: **-20 to +55 C**, derating 3 % per C above 40 C.
- IP43 protection applies only when installed with screw terminals oriented downward.
- Remote on/off eliminates the need for a high-current switch in the input wiring.

## Install Implications

- Switch the remote off unless 12 V receptacles are needed; left enabled, the no-load draw is small but nonzero.
- Fuse/breaker the 48 V input with DC-rated gear; no 32 V automotive fuse hardware on the 48 V side.
- Fuse each 12 V receptacle branch for the receptacle rating and conductor ampacity.
- Label the receptacles as auxiliary 12 V only. They must not backfeed tow-vehicle wiring, OEM trailer lighting, or the 24 V house bus.
