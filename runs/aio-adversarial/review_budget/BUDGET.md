---
author: operator
---

# Budget & Schedule Review: AIO Inverter (D002)

## 1. Recommended Architecture and Next Purchase
**Architecture:** Stick to the D002 baseline: **LiTime 48V 3500W AIO** ($629.99). 
**Next Purchase:** Immediately order the LiTime 48V 3500W unit from the vendor to hit the Juplaya shipping window.

## 2. The 5 kW LiTime Return
**Verdict:** **Return it immediately.** 
Keeping it is a $230 sunk-cost fallacy. The 5 kW unit is an antipattern for this trailer: 
- **Fiscal Waste:** It costs 36% more ($859.99) for capacity the single 100Ah battery cannot safely sustain (104A draw > 100A pack limit).
- **Schedule Friction:** It weighs ~8 lbs more and has a higher idle draw (≤80W vs <50W), requiring more aggressive ECO discipline and cabinet venting management.
- **Technical Trap:** Its 120V MPPT floor makes 3S LG455 panels a "thermal dropout" risk in Juplaya heat.

## 3. The 3-Panel Roof Temptation
**Verdict:** **Reject the 3rd roof panel.**
Adding a third panel to the roof is a budget and schedule killer.
- **Electrical Complexity:** 3S is impossible on the 3500W AIO (149.7V Voc > 145V limit). On high-voltage AIOs (5kW/EG4), the 120V floor means you lose solar harvest precisely when you need it most (noon-day heat).
- **Hardware Cost:** Supporting 3S reliably requires switching to a modular Victron stack (MultiPlus + SmartSolar 250/60), which easily doubles the power-electronics budget (~$1,200+ vs $630) and adds $300+ in extra OCP, wiring, and mounting hardware.
- **Deadline Risk:** Multiple boxes (Victron) or a hybrid MPPT approach adds 2-3 days of wiring/integration labor that the July 4th deadline cannot absorb. 2S roof + 2S ground (1820W total) provides massive charge margin (35% of total battery capacity per hour) for a fraction of the cost.

## 4. Strongest Counterargument
"The Victron modular architecture is more service-friendly and future-proof if the owner eventually expands to a second battery pack or wants 3S roof-only redundancy." 
**Rebuttal:** Future-proofing is a luxury for August. For Juplaya, "One Box, One Vendor, One Week" is the only path that guarantees a cold fridge.

## 5. Required Gates or Install Notes
- **Commissioning:** You MUST cap the AIO's total charge current to 100A in the settings to protect the single LiTime ComFlex battery.
- **Thermal:** The AIO must be in the conditioned nose cabinet; it's rated to -10°C, and winter operation depends on this.
- **Solar:** Use a standard MC4 Y-branch for the 2S2P camped configuration. No external MPPT is required or desired.

## 6. One-Line Verdict for D002
**KEEP:** D002 is the only fiscally sane and schedule-defensible choice; "upgrading" is just paying for complexity and heat dropouts.
