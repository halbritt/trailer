---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
---

# Exterior-Lighting Fixture Verdict

Panel scope: find vehicle-area / porch / scene lights similar to the Super Bright LEDs `VAL2-WW9` target for a 24 V house-bus cargo/camping trailer. The hard constraints were wide-input DC, exterior rating, hardwired surface mount, low profile, about 1000-2000 lm per flood position, sane current for seven perimeter floods, and light quality that will not make camp unpleasant.

This was an out-of-band product panel using three reviewers:

- Super Bright LEDs family/sibling review.
- Commercial trailer/marine/work-light review.
- Budget/retail availability review.

## Final recommendation

Use **7 x Super Bright LEDs `VAL2-NW9`** for the flood/scene positions. **Order status: ordered by owner on 2026-06-05.**

- 2 curbside floods
- 2 roadside floods
- 2 V-nose floods, one on each nose face
- 1 rear flood

Use a separate warm 24 V dimmable awning strip, such as **Super Bright LEDs `RA-IP68-80CRI-5m`, 3000 K**, under the awning/case/rail area.

`VAL2-WW9` remains the warm-white alternate if the owner wants all exterior floods at 3000 K. The panel prefers `VAL2-NW9` for the flood positions because 4000 K is more useful for work, loading, roadside repair, and security while keeping the same 18 W draw and same low-profile fixture class.

## Why this beats the first-pass fixture

The owner-linked `VAL2-WW9` was a good catch because the critical spec is **12-28 VDC**, not "12 V only." That means it runs on the trailer's 24 V house bus and does not require a distributed 12 V lighting branch.

The slight adjustment is color temperature:

- **Flood/scene lights:** 4000 K neutral white (`VAL2-NW9`) gives better task clarity for loading bikes, checking straps, rear-ramp work, and roadside work.
- **Awning/camp light:** 3000 K warm strip is better as a dimmed living/camp light and avoids turning the awning into a glare bar.

## Load math

| Load | Count | Per fixture | Total | Approx current @ 24 V |
|---|---:|---:|---:|---:|
| `VAL2-NW9` floods | 7 | 18 W | 126 W | 5.25 A |
| `RA-IP68-80CRI-5m` awning strip | 1 full 5 m strip | 64 W | 64 W | 2.7 A |
| Floods + full strip | - | - | 190 W | 7.9 A |

This fits the 16 A 24 V Orion as a short-duration lighting load, but it is not free. Do not run all floods, full awning strip, full USB-C load, optional C1000 top-up, and winter heater glow simultaneously.

Hard voltage gate: the flood fixtures are **12-28 VDC**. Set and verify the Orion 48/24 output remains below 28 V under all charge/load states. This is a converter-fed 24 V bus, not a 24 V battery charging profile.

## Candidate field

| Candidate | Source | Fit | Panel ruling |
|---|---|---|---|
| Super Bright LEDs `VAL2-NW9` | https://www.superbrightleds.com/vehicle-lights/interior-and-utility-led-vehicle-lights/vehicle-area-lights/9-rv-trailer-led-light-porch-and-utility-light-1450-lumen-12v | 9", black, 1450 lm, 18 W, 4000 K, 90 deg, IP67, 12-28 VDC, pigtail, surface mount, about $29.99 | **Winner for the seven flood positions.** Same load/cost as the warm target, better task-light CCT. |
| Super Bright LEDs `VAL2-WW9` | https://www.superbrightleds.com/vehicle-lights/interior-and-utility-led-vehicle-lights/vehicle-area-lights/9-rv-trailer-led-light-porch-and-utility-light-1450-lumen-12v | Same fixture class, 3000 K warm white | Acceptable warm alternate. Better ambience, less crisp for work/security floods. |
| Super Bright LEDs `RA-IP68-80CRI-5m`, warm 3000 K | https://www.superbrightleds.com/5m-white-led-strip-light-radiant-series-led-tape-light-24v-ip68-waterproof | 24 V, IP68, 3000 K, dimmable, 351 lm/ft, 3.9 W/ft, 64 W per 5 m | **Winner for awning/camp lighting.** Warm, diffuse, dimmable, and native 24 V. |
| Super Bright LEDs 13" `VAL-x13-x` | https://www.superbrightleds.com/vehicle-lights/interior-and-utility-led-vehicle-lights/vehicle-area-lights/13-rv-trailer-led-light-porch-and-utility-2000-lumen-12v | 2000 lm, 28 W, 4000 K or 5700 K, IP67, 12-28 VDC | More output, but seven fixtures would be 196 W. Use only if a specific position needs extra throw. |
| Super Bright LEDs 9" `VAL-x9-x` older class | https://www.superbrightleds.com/vehicle-lights/interior-and-utility-led-vehicle-lights/vehicle-area-lights/9-rv-trailer-led-light-porch-and-utility-light-1300-lumen-12v | 1300 lm, 18 W, 4000 K or 5700 K, IP67, 12-28 VDC | Same draw/price class as `VAL2`, fewer lumens. No reason to choose it. |
| Super Bright LEDs `VAL-CW17` / `VAL-CW22` | https://www.superbrightleds.com/vehicle-lights/interior-and-utility-led-vehicle-lights/vehicle-area-lights/17-rv-led-flood-light-black-2800-lumens-36w-5700k-12v-cool-white and https://www.superbrightleds.com/vehicle-lights/interior-and-utility-led-vehicle-lights/vehicle-area-lights/22-rv-led-flood-light-black-4000-lumens-50w-5700k-12v-cool-white | 2800-4000 lm, 36-50 W, 5700 K, IP67, 12-28 VDC | Too power-hungry and harsh for seven camp-perimeter positions. |
| Optronics `UCL41CB` | https://optronicsinc.com/PRODUCTS/Brands/OptronicsLED/Products.aspx?SeriesID=810 and https://www.etrailer.com/RV-Exterior-Lights/Optronics/UCL41CB.html | 12/24 V, IP67, hardwired surface flange, about 1200 effective lm, trailer-native form | Best trailer-native fallback, but far more expensive and CCT is not as camp-friendly. |
| TecNiq `P06` SteelHead flood | https://www.tecniqinc.com/product/P0x and https://needatrailerpart.com/products/tecniq-steelhead-6x3x2-mountable-work-light-6-led-flood-pattern-lens-heavy-duty | 9-30 V, IP68, pigtail, about 1900 lm, rugged work-light body | Best rugged/premium fallback. Better abuse rating, worse low-profile/camp-fit/cost. |
| Buyers Products `1492135` | https://www.etrailer.com/Work-Lights/Buyers-Products/3371492135.html | 12/24 V, IP67, 1620 lm, 6000 K, blunt leads | Strong budget output, but too cool and work-light-looking for primary camp lighting. |
| Abrams Cobalt XS 5" scene light | https://abramsmfg.com/products/5-cobolt-xs-series-15w-1500lm-led-down-scene-area-light-rv-exterior-porch-flood-light | 9-32 VDC, IP68, black, 1500 raw / 1200 real lm, flood | Budget contender if CCT is acceptable or verified. Good price/spec, less known for this build. |
| Handxen 9" 20 W 2000 lm | https://www.handxen.com/products/led-flood-porch-light-20w-2000lm-curved-wide-angle | 12/24 VDC, IP67, 2000 lm, 90 deg, 6000 K | Cheap and bright, but 6000 K is harsh and direct-brand confidence is lower. |
| NAPA/STEDI Mini LED Flood | https://www.napaonline.com/en/p/BK_MINIOSRM10W | 12/24 V, IP67, black powder-coated aluminum, about 1000 lm, compact bracket light | Decent local-style fallback, but narrower/bracketed and less porch-like. |
| Hella SM2000 | https://www.autozone.com/p/hella-vehicle-mounted-work-light-357098011/1479990 | 10-30 VDC, IP68/IP6K9K, 2000 lm, 6000 K | Technically excellent, but far too expensive and too cool for seven fixtures. |
| Grote Trilliant / ECCO EW2411 / Scandvik E-500 / Primelux PX0415 | https://shop.grote.com/item-detail?itemId=19662&organizationId=27 and https://www.northerntool.com/products/ecco-led-rectangular-work-light-12-24v-1000-lumens-6-leds-model-ew2411-100880 and https://www.scandvik.com/index.cfm?method=products_detail&productID=972 and https://www.primelux.com/products/5-inch-900lm-mini-rv-porch-light-flood-beam-model-px0415-1-pack | Generally 12/24 V work/utility lights, often cool white, bracketed, lower output, higher cost, or less available | Viable emergency substitutes only. None beats `VAL2` on this trailer's mix of cost, form, current, and light quality. |
| Home Depot low-voltage deck lights | https://www.homedepot.com/b/Lighting-Outdoor-Lighting-Deck-Lighting/Waterproof/12v/N-5yc1vZ1z18gecZ1z0u5o5Z1z18uce | Mostly landscape/deck accent fixtures, not RV hardwired area lights | Skip for flood/scene lighting. Could be useful only for step/courtesy accents. |

## One-line verdict

**Seven `VAL2-NW9` floods are ordered; add one warm 24 V dimmable awning strip.** Keep `VAL2-WW9` as the warm-flood alternate, Optronics `UCL41CB` as the trailer-native fallback, and TecNiq `P06` as the rugged premium fallback. No 12 V exterior lighting bus is needed for this selection.
