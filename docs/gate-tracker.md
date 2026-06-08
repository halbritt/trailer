# Juplaya Gate Tracker

Updated: 2026-06-08

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
| G01 Interior box and nose | Measured, not recorded | Enter tape values for rows 3/3a: box W x L x H, nose taper-start station, centerline depth, tip width | Interior drawing, nose cabinet envelope, panel transport slot | [dimensions.md](dimensions.md) rows 3/3a |
| G02 Roof nose and bows | Open | Enter row 5a roof nose geometry and row 6 roof-bow/solar tie-in stations | Roof drawing, solar rails, Velit station, PV gland | [dimensions.md](dimensions.md) rows 5a/6 |
| G03 Velit roof station | Open | Enter footprint, roof opening, and chosen station | Roof cut, curb, solar/standoff clearance | [dimensions.md](dimensions.md) row 15 |
| G04 Window bay geometry | Open | Enter side wall-post/window clear bays, wall build-up, and door internal frame | Side window cuts, door window re-frame, opening furring | [dimensions.md](dimensions.md) rows 7/12/14 |
| G05 Awning standoff section | Open | Rail 3D scan, rail bolt size, post tube wall thickness, standoff drawing | Awning standoff fab and pre-FRP fasteners | [dimensions.md](dimensions.md) row 16 |
| G06 Floor steel and bike layout | Open | Enter floor steel/crossmember stations, bike bar widths, front-tire centerline/stagger, chock hardware fit | Floor L-track lateral stationing and fastening | [dimensions.md](dimensions.md) rows 10/11 |
| G07 Fridge bay | Open | Enter door aft-edge to first obstruction and verify lid orientation | Fridge bay partition, straps, forced ventilation | [dimensions.md](dimensions.md) row 17 |
| G08 Wall substrate | Open | Ratify D009 and verify OSB thickness | Birch/FRP buy, window sandwich, wall closure | [DECISION_LOG.md](DECISION_LOG.md) D009; [dimensions.md](dimensions.md) row 19 |
| G09 Decision ratification | Open | Owner ratifies D006-D009 and D012 | Design freeze, order freeze, strip-out | [DECISION_LOG.md](DECISION_LOG.md) D006-D009/D012 |
| G10 FRP trim system | Open | Pick FRP brand, adhesive, corner/seam/edge/reveal profiles, and warranty compatibility over birch | Wall closure and sealed interior finish | [juplaya-trailer-context.md](juplaya-trailer-context.md) design-freeze item 9 |
| G11 Gate buys/order freeze | Open | Place or freeze all unblocked SKUs and all BUY AFTER GATE items released by G01-G10 | Design freeze and build start | [order-sheet.md](order-sheet.md) |

## Closed Or Accepted Inputs

| Gate | Status | Recorded value | Remaining follow-up | Source |
|---|---|---|---|---|
| C01 Roof rectangle width | Closed | 84-7/8 in / 2156 mm rail-edge to rail-edge | Use in roof drawing | [dimensions.md](dimensions.md) row 4 |
| C02 Roof rectangle length | Closed | 145.5 in / 3696 mm back-rail edge to nose-triangle base | Use in roof drawing | [dimensions.md](dimensions.md) row 5 |
| C03 Door top clearance | Closed | 5-1/8 in / 130 mm drip rail to top edge | Wall awning mount remains dead | [dimensions.md](dimensions.md) row 8 |
| C04 Window rough openings | Closed | RecPro 1222 = 11-5/8 x 21-5/8 in; RecPro 2015 = 19-5/8 x 14-5/8 in | Still needs G04 bay/frame/sandwich checks | [dimensions.md](dimensions.md) row 13 |
| C05 Floor coating | Closed | Durabak-18 light grey accepted/ordered | PlexCore adhesion and fuel-drip patch before coating | [DECISION_LOG.md](DECISION_LOG.md) D010 |
| C06 Wall E-track mounting | Accepted | 1/4-20 steel rivnuts into steel tube uprights; birch/FRP trims to track | Offcut/first-row fit check | [DECISION_LOG.md](DECISION_LOG.md) D011 |
| C07 Floor L-track spacing | Accepted | Two lengthwise rows, 26 in on center | Still needs G06 lateral stationing and fastening | [dimensions.md](dimensions.md) |

## Build-Phase Checks

| Gate | Status | Needed to close | Blocks | Source |
|---|---|---|---|---|
| B01 Track-height sit test | Open | Mock 31 in sleeping surface; confirm bed row and shelf/window relationship | Wall E-track drilling | [juplaya-trailer-context.md](juplaya-trailer-context.md) design-freeze item 3 |
| B02 Roof and floor patches | Open | 48-hour Henry adhesion patch; PlexCore adhesion and fuel-drip patch | Roof coating and Durabak floor coating | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| B03 Hose test | Open | Hose-test roof rails, Velit curb, PV gland, and penetrations | Foam and ceiling closure | [solar_mounting.md](solar_mounting.md) |
| B04 Fridge thermal check | Open | 50 mm clearance, forced through-flow, desert-sun bay temperature check | Juplaya fridge use | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| B05 Power commissioning | Open | PV segregation, OCP, charge profiles, charge-current cap, optional C1000 top-up test | Shakedown | [power.md](power.md) |
| B06 Weigh-in | Open | Curb weight and tongue weight | Payload and final load plan | [dimensions.md](dimensions.md) row 18 |

## Deferred

| Gate | Status | Notes | Source |
|---|---|---|---|
| D01 MultiPlus and built-in AC distribution | Deferred | Phase 2, not Juplaya | [power.md](power.md) |
| D02 Winter heater unit | Deferred | Rough-in only for Juplaya | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| D03 HRV unit | Deferred | Rough-in only for Juplaya | [juplaya-trailer-context.md](juplaya-trailer-context.md) |
| D04 Truck charging hardware | Deferred | Pull 4 AWG pre-wire now; active charging later | [order-sheet.md](order-sheet.md) |
