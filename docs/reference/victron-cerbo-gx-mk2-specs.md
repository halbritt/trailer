# Victron Cerbo GX Mk2 — Key Specs

System monitor/controller for the Victron networked path. Ordered 2026-06-14; expected 2026-06-15.

Sources: Victron Cerbo GX product page and official manual/specs:
- https://www.victronenergy.com/communication-centres/cerbo-gx
- https://www.victronenergy.com/media/pg/Cerbo_GX/en/installation.html
- https://www.victronenergy.com/media/pg/Cerbo_GX/en/technical-specifications.html

| Spec | Value |
|---|---|
| Model | Cerbo GX Mk2 |
| Role | local/remote Victron system monitor and controller |
| Supply voltage | 8-70 VDC |
| VE.Direct | 3 ports; up to 15 VE.Direct devices total using USB adapters/hub |
| VE.Bus | 2 paralleled RJ45 sockets |
| VE.Can | 2 ports on Mk2; VE.Can 1 isolated |
| USB | 3 host ports on Mk2 |
| Network | Ethernet, WiFi, Bluetooth Smart |
| IO | 4 digital inputs, 4 temperature inputs, 4 tank inputs, 2 relays |
| Operating temperature | -20 to +50 C |
| IP rating | IP20 |
| Dimensions | 154 x 78 x 48 mm / 6.06 x 3.07 x 1.89 in |
| Draw | about 2.8 W without GX Touch; about 3.8 W with GX Touch backlight off |

## Build-relevant notes

- Connect SmartSolar 250/60-Tr, SmartSolar 150/35, and SmartShunt 500A by VE.Direct. Use VE.Direct-to-USB adapters/hub only if physical ports run short.
- Reserve VE.Bus for the incoming MultiPlus-II 48/3000/35-50 120V.
- Reserve VE.Can for future Victron-compatible CAN gear. The current LiTime ComFlex battery does not become a Victron managed battery just because a Cerbo is present.
- The existing Orion-Tr converters remain remote-on/off power supplies; they do not provide useful GX telemetry.
- Power the Cerbo through its supplied **3.15 A slow-blow inline fuse**.
- Mount it in the dry shallow high wall cabinet per D015, with service access and protected cable routing.
