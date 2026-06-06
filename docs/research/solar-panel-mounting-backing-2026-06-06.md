# RV / Cargo Trailer Solar Mounting Strategies - 2026-06-06

## Problem

Cargo trailer roofs are not residential roofs. The roof skin is thin, roof bows are discrete structure, the trailer flexes, and the panels see highway wind and vibration. The immediate issue on this build is that the panel brackets do not land neatly on the 24 in OC roof bows. That is normal: panel geometry, bracket holes, roof bows, AC curbs, and wire glands rarely share the same grid.

The strategy question is therefore: how do we adapt panel hardware to trailer structure without relying on the skin as the structure?

## Strategy Map

| Strategy | Works best when | Pros | Friction / risk | Verdict for this trailer |
|---|---|---|---|---|
| Direct Z-feet / corner feet into roof structure | Small panels, brackets land over real roof framing or plywood deck | Cheap, simple, low height | Lots of penetrations; poor if feet land between bows; panel removal disturbs sealed feet | Not the default. Useful only where a foot lands on a bow/backed point. |
| Direct feet with interior backing plates | Ceiling is open and each bracket location can be backed | Stronger than skin-only screws; cheap materials | Many isolated penetrations; every future panel change depends on hidden backing locations | Viable fallback, but messy for three large panels. |
| Adhesive / VHB / no-drill feet | Small/light panels, known compatible roof surface, low consequence, tested adhesive system | No holes; fast | Depends on roof coating/skin bond, surface prep, heat, peel loads, and long-term inspection; hard to trust for large glass panels at highway speed | Reject as primary retention. Can be secondary bedding/isolation only. |
| Mini-rail under each panel | One or two panels, simple layout, roof has adequate anchor points | Spreads load better than isolated feet; panels removable from rails | Still needs structural anchor points; many short rails can become a layout puzzle | Good concept, but less clean than continuous rails for three rows. |
| Fore-aft rails tied to multiple roof bows | Panel brackets do not align with bows; several panels share one roof field | Brackets can land anywhere on the rails; loads spread into several bows; panels removable without disturbing roof seals | Requires measured bow stations, fabrication, and careful sealing | Recommended. |
| Full roof rack / ladder-rack frame | Need walk deck, gear rack, awning support, or many panels; roof is weak or curved | Strong and serviceable; can avoid many roof-skin penetrations | More height, wind, weight, cost, visual bulk | Strong fallback if simple rails fail the dry-fit. |
| Tilt mounts | Stationary camped trailer, winter/low-sun optimization | Better harvest when deployed | Wind discipline, travel locking, more moving hardware | Not worth the July deadline risk for roof panels. Use ground panels for tilt. |
| Flexible adhesive panels | Curved roof, no height, very small loads | Low profile, no glass-panel rack | Heat, service life, lower output, no match to rigid glass modules | Not relevant to the owned rigid-panel plan. |

## Recommended Strategy For This Build

Use **fore-aft structural rails tied to multiple roof bows**, then mount the existing panel brackets to those rails.

The point is not that the rails are magic solar hardware. The point is that rails turn a bad grid problem into a good one:

- The brackets land where the panel hardware wants them.
- The rails land where the trailer structure is.
- The panels remain removable from above.
- The sealed roof penetrations stay fixed even if panel/bracket details change.

For this trailer, start with two fore-aft rails running under the roof array field. Add a third rail only if dry-fit shows the actual bracket pattern, rail stiffness, or cable routing needs it. The third rail should be a structural or attachment rail, not a pad pushing against a module backsheet.

## Practical Build Pattern

1. **Measure the roof structure.** Mark roof bow stations from a fixed datum. Transfer those stations to the roof drawing with the Velit curb, PV gland, awning standoffs, and panel rows.

2. **Dry-fit the panel field.** Put the brackets on the panels or mock the bracket feet on the roof. The question is where rails need to run so the brackets can bolt to rails without moving the panels into the Velit/awning/gland zones.

3. **Pick rail stock.** Use corrosion-resistant structural rail stock: aluminum T-slot/extrusion, aluminum strut, aluminum square tube with attachment plates, or a purpose-made solar rail. Galvanized steel strut is structurally viable but heavier and needs isolation from aluminum/stainless interfaces.

4. **Tie rails to bows.** Use discrete feet/saddles at bow crossings, not skin-only screws. Preferred while the interior is open: through-bolt or mechanically fasten to the steel roof bow with backing plates/washers and a crush-control detail if the bow tube can deform.

5. **Attach panels to rails.** Use the owned brackets as panel-to-rail hardware if they fit the rail and panel frame cleanly. If they do not, substitute module clamps or mini-rail hardware. Do not make the roof foot pattern drive the panel attachment pattern.

6. **Seal as a roof system.** Bed feet, tighten once, encapsulate fasteners/feet with the chosen roof sealant system, hose-test, then coat the roof. With Henry 887/884 in this build, roof penetrations and fasteners need to be treated as part of the silicone roof system.

7. **Keep it serviceable.** The panel should unbolt from the rail without digging out roof sealant. PV wire should be clipped to rails with service loops and labels; no loose wire should rub on the roof skin.

## Cargo Trailer Specific Notes

- **Do not size from dead weight.** Three 48.5 lb panels are only about 146 lb static. Highway uplift and vibration are the real loads.
- **Do not trust skin-only screws.** The sheet metal can keep water out; it should not be the primary pull-out structure for the array.
- **Do not create a water dam.** Discrete feet are better than a continuously bedded rail lying flat on the roof.
- **Do not close the ceiling first.** Any backing, sleeves, nuts, inspection, or hose-test access is easier before foam and finish.
- **Do not overcommit to tilt.** The optional ground pair is the tilt strategy. Roof panels should be travel-safe and boring.
- **Plan for a failed dry-fit.** If the bow/rail/Velit/awning geometry gets ugly, the fallback is a full perimeter/ladder-rack style frame, not skin screws.
- **Treat mobile use as harsher than the module manual.** Commodity framed modules are usually documented around fixed land-based structures, not cargo-trailer highway service. That does not kill the plan, but it means the mount should be conservative, inspectable, and mechanically retained.

## Minimum Gate Before Drilling

- Roof bow stations measured and marked.
- Rail centerlines drawn.
- Panel bracket-to-rail landing points checked.
- Velit curb/opening placed.
- PV gland location placed.
- Awning standoff stations checked for conflict.
- Rail-foot fastener/backing method selected after confirming roof bow access and tube wall behavior.
- Sealant/coating sequence confirmed.

## Local Conclusion

The build should not try to make panel brackets align with the bows. It should make a small roof rail system that aligns with the bows, then mount the panels to that rail system.

That is the clean cargo-trailer answer: **rails are the adapter between solar hardware and trailer structure.**

## Sources

- Local trailer dimensions and bow spacing: [docs/dimensions.md](../dimensions.md)
- Local panel size/weight and electrical constraints: [docs/reference/lg455n2w-e6-datasheet.md](../reference/lg455n2w-e6-datasheet.md)
- LG product support page for the build panel: https://www.lg.com/us/support/product/lg-LG455N2W-E6.AUA
- LG PV solar module installation manual: https://www.lg.com/content/dam/channel/wcms/es/download/resources/ct32016002/CT32016002_1764.pdf
- Henry 887/884 installation instructions: https://www.buildsite.com/pdf/henry/887-Tropi-Cool-100-Silicone-White-Roof-Coating-Installation-Instructions-2138405.pdf
- Unirac SOLARMOUNT rail-based racking docs: https://unirac.com/products/pitched-roof/solarmount/
- 3M VHB tape resources and design guides: https://www.3m.com/3M/en_US/vhb-tapes-us/resources/
- RV Solar Made Easy DIY/service guide: https://rvsolarconnections.com/wp-content/uploads/2023/03/RV-Solar-Made-Easy-A-Guide-for-DIY-and-Service-Professionals.pdf
- Vroom cargo trailer / RV solar rack examples: https://www.vroom-power.com/rack-products-2
