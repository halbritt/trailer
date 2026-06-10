# Juplaya Gate Tracker

Updated: 2026-06-09

This is the central live tracker for build gates. Update this file first when a gate changes. Raw dimensions still belong in [dimensions.md](dimensions.md); decision receipts still belong in [DECISION_LOG.md](DECISION_LOG.md); purchasing state still belongs in [order-sheet.md](order-sheet.md).

Status legend:

- **Closed**: recorded in the repo and usable for downstream design/build work.
- **Accepted**: owner/design decision is fixed, but downstream fit or installation checks may remain.
- **Measured, not recorded**: owner says the measurement exists, but the value is not in the repo yet.
- **Open**: not recorded or not complete enough to unlock work.
- **Deferred**: not a Juplaya blocker.

## Active Blockers

| Gate | Status | Needed to close | Blocks | Source |
|---|---|---|---|---|
| G02 Roof nose and bows | Open | Enter row 5a roof nose geometry and row 6 roof-bow/solar tie-in stations | Roof drawing, solar rails, Velit station, PV gland | [dimensions.md](dimensions.md) rows 5a/6 |
| G03 Velit roof station | Open | AC aft clearance is recorded; still enter exact footprint/opening, final station, rear rail-overhang clearance, and last bow tie-in | Roof cut, curb, solar/standoff clearance | [dimensions.md](dimensions.md) row 15 |
| G04 Window sandwich and door frame | Open | Wall-post/window fit is closed; still enter wall build-up and door internal frame | Side window furring, door window re-frame | [dimensions.md](dimensions.md) rows 12/14 |
| G05 Awning standoff section | Open | Rail 3D scan, rail bolt size, post tube wall thickness, standoff drawing | Awning standoff fab and pre-FRP fasteners | [dimensions.md](dimensions.md) row 16 |
| G07 Fridge bay | Open | Aft clearance is recorded; still verify lid orientation, 50 mm all-sides clearance, and forced through-flow layout | Fridge bay partition, straps, forced ventilation | [dimensions.md](dimensions.md) row 17; [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| G09 Decision ratification | Open | Owner ratifies D006-D008 and D012 | Design freeze, order freeze, strip-out | [DECISION_LOG.md](DECISION_LOG.md) D006-D008/D012 |
| G10 FRP trim system | Open | Pick FRP brand, adhesive, corner/seam/edge/reveal profiles, and warranty compatibility over PlexCore | Wall closure and sealed interior finish | [juplaya-trailer-context.md](juplaya-trailer-context.md) design-freeze item 9 |
| G11 Gate buys/order freeze | Open | Place or freeze all unblocked SKUs and all BUY AFTER GATE items released by active gates G02-G10 | Design freeze and build start | [order-sheet.md](order-sheet.md) |

## Closed Or Accepted Inputs

| Gate | Status | Recorded value | Remaining follow-up | Source |
|---|---|---|---|---|
| C01 Roof rectangle width | Closed | 84-7/8 in / 2156 mm rail-edge to rail-edge | Use in roof drawing | [dimensions.md](dimensions.md) row 4 |
| C02 Roof rectangle length | Closed | 145.5 in / 3696 mm back-rail edge to nose-triangle base | Use in roof drawing | [dimensions.md](dimensions.md) row 5 |
| C03 Door top clearance | Closed | 5-1/8 in / 130 mm drip rail to top edge | Wall awning mount remains dead | [dimensions.md](dimensions.md) row 8 |
| C04 Window rough openings | Closed | RecPro 1222 = 11-5/8 x 21-5/8 in; RecPro 2015 = 19-5/8 x 14-5/8 in | Still needs G04 sandwich and door-frame checks | [dimensions.md](dimensions.md) row 13 |
| C05 Floor coating | Closed | Durabak-18 light grey accepted/ordered | PlexCore adhesion and fuel-drip patch before coating | [DECISION_LOG.md](DECISION_LOG.md) D010 |
| C06 Wall E-track mounting | Accepted | 1/4-20 steel rivnuts into steel tube uprights; PlexCore/FRP trims to track | Offcut/first-row fit check | [DECISION_LOG.md](DECISION_LOG.md) D011 |
| C07 Floor L-track spacing | Accepted | Two lengthwise rows, 26 in on center | Still needs B07 physical fit check before final drill/coating commitment | [dimensions.md](dimensions.md) |
| C08 Interior floor footprint | Closed | 81 in rear width; 141 in straight side walls; 156 in centerline total length; 43 in V-nose flanks; 30 in side door opening; 98 in rear-to-door-aft-jamb; 13 in forward jamb to V-nose start; 78 in interior height | Still needs G04 sandwich and door-frame checks | [interior-footprint-clean.svg](diagrams/interior-footprint-clean.svg); [dimensions.md](dimensions.md) rows 3/3a/17 |
| C09 Wall-post/window fit | Closed | Wall posts are 16 in on center; selected side-window cutouts fit between posts | Still needs G04 sandwich and door-frame checks | [dimensions.md](dimensions.md) row 7 |
| C10 Floor steel | Closed | Floor steel/crossmembers are 16 in on center; main rails remain perimeter per work order | Use for L-track fastening plan | [dimensions.md](dimensions.md) row 10 |
| C11 Factory wall panel thickness | Closed | Factory wall panels are verified 3/8 in | Use as D009 PlexCore substrate | [dimensions.md](dimensions.md) row 19 |
| C12 Bike tape geometry | Deferred | Bar widths and front-tire centerline tape pass are not a design-freeze gate | Physical bike/L-track fit check remains | [dimensions.md](dimensions.md) row 11 |
| C13 D009 wall substrate | Accepted | Reuse existing 3/8 in PlexCore sidewall liner; no birch re-skin | Still needs G10 FRP adhesive/trim selection and G04 window sandwich check | [DECISION_LOG.md](DECISION_LOG.md) D009; [reference work order](reference/wells-cargo-ft712s2-d-work-order.md) |
| C14 AC aft solar clearance | Closed | 125 in / 3175 mm from the laid-out Velit back/aft edge to the trailer rear/top rail | Three panel bodies are plausible; dry-fit rail-only rear overhang for NXT clamp/end margin, ramp/rear-edge clearance, and last roof-bow tie-in | [dimensions.md](dimensions.md) row 15 |

## Build-Phase Checks

| Gate | Status | Needed to close | Blocks | Source |
|---|---|---|---|---|
| B01 Track-height sit test | Open | Mock 31 in sleeping surface; confirm bed row and shelf/window relationship | Wall E-track drilling | [juplaya-trailer-context.md](juplaya-trailer-context.md) design-freeze item 3 |
| B02 Roof and floor patches | Open | 48-hour Henry adhesion patch; PlexCore adhesion and fuel-drip patch | Roof coating and Durabak floor coating | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| B03 Hose test | Open | Hose-test roof rails, Velit curb, PV gland, and penetrations | Foam and ceiling closure | [solar_mounting.md](solar_mounting.md) |
| B04 Fridge thermal check | Open | 50 mm clearance, forced through-flow, desert-sun bay temperature check | Juplaya fridge use | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| B05 Power commissioning | Open | PV segregation, OCP, charge profiles, charge-current cap, optional C1000 top-up test | Shakedown | [power.md](power.md) |
| B06 Weigh-in | Open | Curb weight and tongue weight | Payload and final load plan | [dimensions.md](dimensions.md) row 18 |
| B07 Bike/L-track physical fit | Open | Put the bikes in the trailer and verify 26 in L-track placement plus handlebar overlap before final drill/coating commitment | Floor L-track final install | [dimensions.md](dimensions.md) row 11 |

## Deferred

| Gate | Status | Notes | Source |
|---|---|---|---|
| D01 MultiPlus and built-in AC distribution | Deferred | Phase 2, not Juplaya | [power.md](power.md) |
| D02 Winter heater unit | Deferred | Rough-in only for Juplaya | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| D03 HRV unit | Deferred | Rough-in only for Juplaya | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| D04 Truck charging hardware | Deferred | Pull 4 AWG pre-wire now; active charging later | [order-sheet.md](order-sheet.md) |
