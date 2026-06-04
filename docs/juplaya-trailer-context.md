# Juplaya Trailer Build — Index
*Target: ready for Juplaya (~July 4, 2026). This is the slim index; the build lives in the domain docs below.*

> **Status framing:** only items marked **settled** are firm. The domain docs carry decisions as DECISION_LOG rows (`proposed` until the owner ratifies) plus **binding gates** — measurement/engineering checks that must pass before drilling, fabricating, or ordering. Provenance: D002–D008 come from the 2026-06-03/04 cross-examined striatum runs (artifacts under `runs/`); do not infer decisions that aren't written in a domain doc or D-row.

**Open gates at a glance:** measured roof drawing (solar racking + awning risers + radius corners) · awning door-trim + deployed-fabric checks · riser load-path engineering outputs · fridge-bay ventilation + lid-hinge · interior floor-plan rework (steel locations + bar width) · window RO · curb-weight weigh-in.

## The trailer (settled)
- **FasTrac Deluxe FT712S2-D, 7×12, single axle** (ACG-built), **Silverfrost** exterior. Bought at The Trailer Specialist, Acampo CA. **VIN 7V0W11214TU444163**, serial 444163.
- **Interior 6'9" (81") W × 13'1" (157") L × 6'6" tall**; overall ~16'0". Rear **5,000 lb ramp door**; side **32"×72" personnel door, RH** ("RV-style"). **2"×4" tube main rails**; 76½" steel tube posts 16" OC; 4× factory 5,000 lb D-rings; 3/4" PlexCore floor.
- Full specs: [fastrac-specs.md](fastrac-specs.md) · factory build sheet: [work order](wells-cargo-ft712s2-d-work-order.md).

## Tow vehicle (settled)
- **2021 Ford F-150 EcoBoost, Max Tow package.** Pro Trailer Backup Assist; ordered: integrated trailer backup camera + TPMS.

## The build — domain docs
| Domain | Doc | Decides |
|---|---|---|
| Power / electrical | [build/power.md](build/power.md) | 48 V stack, solar 2S/2S2P, **24 V house bus (D006)**, protection, truck charging, energy budget |
| Climate / envelope | [build/climate.md](build/climate.md) | foam/roof (settled), windows, HRV/heater rough-ins, **awning F45s riser-mount (D007)** |
| Interior / layout | [build/interior.md](build/interior.md) | bike/E-track layout (rework gated), track heights, shoring, walls, stairs, fridge bay |
| Systems / gear | [build/systems.md](build/systems.md) | **fridge CFX3 95DZ integration (D008)**, accessories + parts orders |

Also: [trailer-mission.md](trailer-mission.md) (north star) · [DECISION_LOG.md](DECISION_LOG.md) (D001–D008) · spec sheets: [AIO 3500W](litime-48v-3500w-aio-specs.md) · [battery](litime-48v-100ah-battery-specs.md) · [panel](lg455n2w-e6-datasheet.md) · [fridge](dometic-cfx3-95dz-specs.md) · run artifacts under `runs/`.

## Weight
- **GVWR 3,500 lb** (confirmed). Real payload = 3,500 − actual curb; **will be weighed**, not estimated. Single axle is nose-sensitive — aim ~**10–12% tongue weight** when positioning the bikes.

## Standing preferences (for whoever picks this up)
- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
