# Victron MultiPlus-II 48/3000/35-50 120V — Key Specs

House inverter/charger for the revised D002 Victron path. Source: Victron MultiPlus-II 120V technical specifications: https://www.victronenergy.com/media/pg/MultiPlus-II_120V/en/technical-specifications-mp-ii-120v.html

| Spec | Value |
|---|---|
| Model | MultiPlus-II 48/3000/35-50 120V |
| DC input range | 38-66 V |
| AC output | 120 VAC +/-2%, 60 Hz +/-0.1% |
| Continuous output | 3000 VA / 2400 W at 25 C; 2200 W at 40 C; 1700 W at 65 C |
| Peak power | 5500 W |
| Maximum efficiency | 95% |
| Zero-load power | 11 W; 7 W AES; 2 W Search |
| Transfer switch | 50 A |
| AC input | 90-140 VAC, 45-65 Hz |
| Battery charger | 57.6 V absorption, 55.2 V float, 52.8 V storage; 35 A max charge |
| Communications | VE.Bus plus two general purpose communication ports; remote on/off |
| Temperature range | -40 to +65 C, fan-assisted |
| Enclosure | IP21, steel |
| Battery connection | M8 bolts |
| AC connection | Screw terminals, 13 mm2 / 6 AWG |
| Weight | 29 kg / 64 lb |
| Dimensions | 572 x 277 x 147 mm / 22.5 x 10.9 x 5.8 in |
| Listing | UL1741 |

## Build-relevant notes

- **Verdict trade:** this is the cleaner house charger/inverter than the LiTime AIO when reliability, idle draw, ecosystem, programming, and monitoring matter more than lowest purchase cost.
- **Output trade:** continuous AC output is lower than the LiTime 3500 W AIO. Treat 2400 W at 25 C / 2200 W at 40 C as the real sustained design envelope; the Velit remains a 48 V DC load, not an inverter load.
- **Idle win:** 11 W zero-load is roughly 0.26 kWh/day, substantially below the LiTime 3500 W's <30 W ECO / <50 W normal draw.
- **Solar split:** this is not an AIO and has no PV input. Roof 3S stays on the SmartSolar 250/60-Tr. Optional deployable 2S ground solar needs its own MPPT or can be skipped.
- **Charge coordination:** 35 A AC charging plus SmartSolar roof charging stays below the ComFlex battery's 100 A continuous charge limit, but any future charger still counts toward the combined cap.
