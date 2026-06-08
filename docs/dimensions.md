# Dimension Sheet — Juplaya Trailer Build

All known dimensions in one place. **Spec/derived values first; the fill-in table at the bottom is the mm measurement pass** — measured values are the source of truth once entered and supersede everything above. Current pass/fail gate status lives in the [gate tracker](gate-tracker.md). Cross-refs: [build sheet](juplaya-trailer-context.md) · [fastrac-specs](reference/fastrac-specs.md) · [work order](reference/wells-cargo-ft712s2-d-work-order.md).

## Trailer — FT712S2-D (spec / derived)

| Dimension | Value | Source |
|---|---|---|
| Body (box) | 160" L × 84" W (13'4" × 7'0") | FasTrac table |
| Overall | ~192" L (16'0") × 102" W (8'6") × ~97" H (8'1") | derived |
| Interior | **81" W × 156" centerline L × 78" H measured** — 141" straight side walls + V-nose; factory/spec length was ~157" | [interior footprint](diagrams/interior-footprint-clean.svg) + FasTrac table |
| Platform height | 18" | FasTrac table |
| Rear ramp opening | 78" W × 72" H (5,000 lb, 8' H max w/ ext.) | table + work order |
| Side personnel door | **32" W × 72" H**, RH hinge | work order |
| Main rails | 2" × 4" steel tube, **perimeter** | work order (+ agy finding) |
| Crossmembers | **16" OC verified** | work order + owner verification |
| Roof bows (tube) | 24" OC | work order |
| Wall posts | 76½" steel tube, **16" OC verified** → selected side-window cutouts fit between posts | work order + owner verification |
| Coupler / ball | 2" coupler · hitch height 16" | table / work order |
| Tires | ST205/75R15, 5-bolt | work order |
| GVWR / axle | 3,500 lb single, electric drum | work order |

## Components

| Component | Dimensions | Weight |
|---|---|---|
| House inverter/charger — Victron MultiPlus-II 48/3000/35-50 120V | 22.5" × 10.9" × 5.8" (572 × 277 × 147 mm) | 64 lb (29 kg) |
| Battery — ComFlex 48V 100Ah | 19.88" × 12.32" × 9.25" | 97.4 lb |
| Solar panel — LG455N2W-E6 (×3 roof + ×2 optional ground) | **83.07" × 41.02" × 1.57"** (2110 × 1042 × 40 mm) | 48.5 lb ea |
| Fridge — Dometic CFX3 95DZ | **37.9" × 20.9" × 18.6"** (962 × 530 × 472 mm) incl. handles, + lid swing | 66.4 lb |
| Awning — Fiamma F45s 350 | case **138" (11'6")** L × 5.35" H × 3.35" proj · canopy 130" · extension 98" | 55.1 lb |
| Window ×2 — RecPro RP-FRMWIN-1222-TRM | 12" × 22"; **cutout 11-5/8" × 21-5/8"**, overall 14×24×2.5, **ring for 1.5" wall** (RecPro, web-val) | — |
| Window ×1 (door) — RecPro RP-FRMWIN-2015-TRM | 20" × 15"; **cutout 19-5/8" × 14-5/8"**, overall 22×17×2.5, **ring for 1.5" wall** (RecPro, web-val) | — |
| Bikes — WR250R + CRF450RL | ~86" L ea · bars **32–34"** | ~590 lb pair |
| Velit 2000R rooftop AC | footprint + roof opening **TBD — must enter the roof drawing** | TBD |
| Heater (winter) — LF Bros N4 24V | **17" × 13" × 14.8"** (432 × 330 × 376 mm) pedestal, integrated 3.5 L tank — **operates outside; 2 × 3" duct ports** (capped) + exterior 24 V feed | 15.9 lb |

## Derived bands & clearances (from the accepted design)

| Item | Value | Notes |
|---|---|---|
| Wall E-track rows | bed **~27"** (revised from 34" — sit-up headroom; sit-test gate) · shelf **60"** | D011: steel 1/4-20 rivnuts into 1" thin-wall tube posts; birch/FRP trim to track edge |
| **Window band** | sill ~**36"**, top ~58" | above the bed track (~27"), below the shelf track (60"); rear bay station, both walls |
| Effective walking aisle | ~**20"** (nominal 30") | bars overhang at bar height |
| Roof: three panel rows (landscape) | 83.07" across × **123" of length** | **fits: 84-7/8" measured width** (~0.9"/side margin — use under-panel feet/fore-aft rails, not side clamps); leaves ~22" of measured rectangle + nose for Velit/standoff layout |
| Awning case bottom | ≥ **~78.5"** (above roofline) | riser-mounted |
| Deployed fabric @ 32" out, 10° pitch | ~**72.9"** | vs the 72" door — ~0.9" paper margin |
| Fridge bay | starts at the door's aft edge, 37.9" long × 20.9" deep | curbside; band under 18.6" + lid |
| Panel transport | 83" panels vs **81" interior width** → lengthwise only | padded E-track wall slot |
| Floor L-track rows | lengthwise, **26" on center** | spacing accepted; final lateral stationing still depends on bike/chock/steel pass |
| Wall E-track footage | ~**47 ft estimated** after moving the floor to L-track | ~50–60 ft on hand should cover walls; recount after wall-row cut plan |

## 📏 MEASUREMENT PASS — fill in (mm preferred; these supersede spec)

> **Interior footprint diagram: landed 2026-06-08** ([SVG](diagrams/interior-footprint-clean.svg), [PNG](diagrams/interior-footprint-clean.png)). This supersedes the rejected Magicplan sketch for the floor footprint and populates rows 3/3a and 17.
> **Magicplan scan: landed 2026-06-04 and REJECTED as a measurement source** ([sketch](reference/magicplan-interior-sketch.pdf)). Hard fail: its 85¾" interior width exceeds the 84⅞" tape-measured **exterior** rail-to-rail (spec interior 81"); nose flanks asymmetric by 4" (43½" vs 47½"); door 29¼" vs the work order's 32". Do not use it for dimensions.
> **Rail profile (row 16): incoming via a 3D scan** (owner) — capture the section **end-on** where the rail terminates/miters (rear corner / ramp opening); caliper the channel-lip wall thickness once to anchor the mesh. Export → `docs/reference/`. **Stations: the rail's existing bolts mark the uprights, but they sit at the extrusion's center** — a single centered bolt can't react the standoff moment, so **each standoff takes ≥2 fasteners into its upright** (vertical couple, new penetrations, before-FRP). Record bolt size + post tube wall thickness.

| # | Measurement | Expected | Measured | Date |
|---|---|---|---|---|
| 1 | Ball-to-bumper overall length | ~4877 mm (16'0") | | |
| 2 | Overall height (ground → roof peak) | ~2464 mm (8'1") | | |
| 3 | **Interior rectangle (box section): W × L × H** — width between walls (verify no wheel-well intrusion; fenders are external per the work order), length rear wall → nose taper start, height floor → ceiling | ~2057 mm W × ~3660 mm L × 1981 mm H | **81" W × 141" L × 78" H** (2057 × 3581 × 1981 mm) from clean footprint diagram | 2026-06-08 |
| 3a | **Interior nose (trapezoid): taper-start station, centerline depth to the front wall/tip, tip width** — this is the power/nose-cabinet zone; centerline length includes it | ~330+ mm of the 3988 mm total | **taper starts 141" from rear; centerline total 156" → nose depth ~15"; 43" flanks; tip drawn as point/0"** (3581 mm, 3962 mm total, ~381 mm depth, 1092 mm flanks) | 2026-06-08 |
| 4 | **Roof rectangle: usable flat width** | 1830–1980 mm? | **2156 mm (84-7/8")** rail-edge → rail-edge; crown minimal → full width usable | 2026-06-04 |
| 5 | **Roof rectangle: length** | ~3660 mm (144") | **3696 mm (145.5")** back-rail edge → nose-triangle base (usable slightly less) | 2026-06-04 |
| 5a | **Roof nose (trapezoid): taper-start station, centerline nose length, flat tip width** — the V-nose truncates to a flat tip; three numbers make the plan drawable | nose ~460–610 mm long | | |
| 6 | Roof-bow stations (from front wall) + solar through-rail tie-in stations | 610 mm OC; through-rail fasteners land at bow crossings, not arbitrary roof skin | | |
| 7 | Wall-post stations + **clear bay width** at the two window stations (rear, both walls) | ~368 mm (14.5") clear | **16" OC wall posts verified; selected 12×22 side-window cutouts fit between posts** | 2026-06-08 |
| 8 | **Door drip rail → top edge of trailer** (replaces trim-height estimate) | ~114 mm (4.5")? | **130 mm (5-1/8")** — F45s case is 5.35" → wall-mount confirmed dead by 0.225" | 2026-06-04 |
| 9 | Door swing arc vs awning-riser line (deployed-fabric check at pitch) | ≥ door height | | |
| 10 | Floor steel: main-rail inset from walls + crossmember stations | perimeter / 406 mm OC | **floor steel/crossmembers 16" OC verified; main rails remain perimeter per work order** | 2026-06-08 |
| 11 | Bike/L-track physical fit check | 26" L-track rows, bars interleaved | **bike tape geometry deferred/unneeded; owner will verify by putting bikes in the trailer and checking 26" L-track placement + bar overlap** | 2026-06-08 |
| 12 | Wall build-up thickness at window stations — **birch (D009) + FRP** sandwich vs the RecPro frameless clamp ring | ring is **1.5" single spec**; wall ~1–1.4" → **fur opening up to 1.5"** (web-val) | | |
| 13 | Window ROs (from RecPro): 1222-TRM ×2, 2015-TRM ×1 | **1222 = 11-5/8"×21-5/8"; 2015 = 19-5/8"×14-5/8"** | confirmed (RecPro, web-val) | 2026-06-05 |
| 14 | Door internal frame vs 20×15 RO | TBD | | |
| 15 | Velit 2000R footprint + roof-opening size + chosen station | TBD | | |
| 16 | **Perimeter aluminum rail: extrusion section + existing bolt size + post tube wall thickness** (standoff: ≥2 fasteners per upright; tap vs through-bolt) | TBD | | |
| 17 | Fridge bay: door aft-edge → first obstruction | ≥ 963 mm (37.9") | **98" clear from rear/ramp end to side-door aft jamb** (2489 mm) from clean footprint diagram; enough for the 37.9" fridge length | 2026-06-08 |
| 18 | **Curb weight** (scale) + tongue weight | TBD — payload = 3,500 lb − curb | | |
| 19 | **Factory wall panel thickness** (verify before the D009 birch buy — 3/8" assumed) | ~9.5 mm (3/8") | **3/8" factory wall panels verified** | 2026-06-08 |

> **Roof AND interior plans = rectangle (box) + trapezoid (nose).** The track field, bike layout, fridge bay, and panel-transport slot all live in the interior rectangle; the nose trapezoid is the power-cabinet zone. The three panel rows need ~123" of the rectangle; the remaining rectangle plus nose trapezoid is what the drawing assigns to AC clearance, riser stations, and walk space.
> When a row is filled, propagate: the roof drawing (4–6, 15), solar rail/backing detail, window cuts (7, 12–14), riser fabrication (8, 9, 16), floor L-track layout (10, 11), and the payload ledger (18).
