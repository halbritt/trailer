# Build-Decision Web-Validation — 2026-06-05

**Method.** Each of the original 7 falsifiable build decisions was run through a bounded web-research pass — a researcher draft followed by an *independent adversarial skeptic* that tried to refute the load-bearing claims — then synthesized. The skeptic changed **4 of 7** verdicts. D010 flooring was added later as a flat web-validation addendum.

**Scope & limits.** Sources are public web (manufacturer pages, standards summaries, owner forums). This validates *reasoning* and catches *spec/code conflicts*; it does **not** replace the physical measurement gates (rail 3D scan, clamp-stack mock-up, sit-test, weigh-in). D001 (which trailer) and D005 (which fridge was purchased) are facts, not engineering choices, and were not validated.

**Provenance.** Flat validation workflow, run `wf_13d5d5ba-bac`, 15 agents. (An earlier nested deep-research run wedged on concurrent PDF reads and was abandoned; this flat re-run replaced it.)

**Supersession note, 2026-06-08:** D009 no longer uses the birch re-skin path validated below. Current D009 is accepted as reuse of the factory verified 3/8" PlexCore sidewall liner with FRP over PlexCore. The remaining live concern is still the trapped-moisture/adhesive edge case: close dry, seal FRP edges/window sandwiches, and prove adhesive compatibility with PlexCore.

## Verdict summary

| Decision | Verdict | Skeptic changed it? |
|---|---|---|
| **D002** Solar string sizing | ✅ corroborated | no |
| **D006** 24 V house bus | ✅ mostly-corroborated | no |
| **D007** Awning standoff | 🟡 mostly-corroborated | **yes** |
| **D008** Fridge bay | 🔴 **mixed** | **yes** |
| **D009** Birch substrate | superseded 2026-06-08 by PlexCore reuse | **yes** |
| **D010** Flooring bed-liner coating | 🟡 mostly-corroborated | addendum |
| **Windows** RecPro frameless | 🔴 **mixed** | **yes** |
| **Roof** foam + elastomeric | 🟡 mostly-corroborated | no |

## Actions — what this should change in the build docs

These are the findings that should feed back into the build sheet / decision log before the design freeze:

1. **D008 fridge bay — biggest find (safety/compliance).** The Dometic CFX3 manual requires a **50 mm (~2") gap on all four sides** and states **"do not place the cooling device in closed compartments."** The build sheet's *"enclosed curbside bay"* violates the manual as worded. → Rewrite the bay spec and the thermal gate: **50 mm all-sides clearance + forced through-flow ventilation**, then field-measure in-bay air (<43 °C to run, <30 °C to hold dual-zone). Electrical sizing (24 V @ 4.6 A, 10 A / 14 AWG) is fine.
2. **D007 awning — tighten the wind rule (safety).** "Wound in before gusts >20 mph" is **~2× too permissive** for the as-built wall-only (no legs, no tie-down) case; forum consensus is **~10 mph** for that configuration. Also: the limiting failure is the **awning's own arms/extrusions bending**, not fastener pull-out, and an over-rigid standoff can defeat the arms' intended wind/water release. → Decide deployment mode (legs+tie-down earns ~20–25 mph, wall-only forces ~10 mph) and match the retract spec to it.
3. **Windows — the clamp range is a single value, not a range.** RecPro's trim ring is published only as **"for 1-1/2" wall thickness"** (no min/max). The build wall is ~1"–1.4", so it **won't clamp tight as specified** — fixable by **furring the opening up to 1.5"**, but that step is currently missing from the wall sandwich. Cutout sizes confirmed: **1222 → 11-5/8" × 21-5/8"**, **2015 → 19-5/8" × 14-5/8"**. Door cut needs perimeter re-framing. → Feeds dimension rows 12–14 and design-freeze item 4; add the furring step.
4. **D009 birch is superseded — moisture/adhesive risk still governs.** Current D009 reuses the factory verified 3/8" PlexCore sidewall liner and avoids the birch wall-stock buy. Impermeable FRP inside + <1-perm closed-cell foam outside still leaves little drying path, so close dry, seal FRP seams/edges and the window clamp sandwich, and confirm the chosen FRP brand/adhesive works over PlexCore or prove it with a bond patch.
5. **D006 — make the main OCP explicit + fix a part number.** UL-489 / 80 VDC / 10 kA AIC checks out. But standard LiFePO4 practice puts a **Class-T fuse at the battery terminal** as the main OCP — document whether that exists or the close-mounted breaker *is* the main OCP. **Verify the exact Blue Sea SKU**: docs say "7443," but the validated 20 A / 80 V UL-489 part pages came up as 7463 (and 7465 = 30 A) — reconcile the actual part number.
6. **D002 — later superseded by the corrected Victron house-charger verdict.** This validation still applies to any LiTime 3500 W fallback: 2S Voc has huge margin (~113 V cold vs 145 V), but owners report nuisance PV-overvoltage faults below the advertised 145 V with 49 V-class panels, so **never 3S into that AIO input**. Current D002 instead uses Victron MultiPlus-II for the house charger and roof 3S through a SmartSolar 250/60-Tr. *Minor:* LG's page lists Voc 49.9 V, coeff **−0.26 %/°C**, Vmpp 42.1 V — reconcile against the −0.24 %/°C / 41.7 V figures in the reference sheet.
7. **Roof — spec a cold-rated coating.** Building science *endorses* the foam-inside/coating-outside steel sandwich **provided the steel is dry at closure**. The load-bearing open item: standard **acrylic elastomerics go brittle and "zipper" off in deep cold** — specify a **silicone or cold-rated** coating, verify steel dry/clean at closure, and check whether foaming under the steel roof voids any panel warranty.
8. **D010 flooring — bed-liner direction holds, but tighten the claim.** Flexible polyurethane bed-liner coating is a better fit than loose rubber coin roll. However, "fuel-proof" is too broad: Raptor's TDS says petrol is splash-resistant, not immersion-proof. → Build-sheet wording is **fuel/oil spill-resistant, clean promptly**, with mandatory PlexCore adhesion and fuel-drip patches before full coating.

---

# Off-Grid Cargo-Trailer Build — Consolidated Validation Report

## Bottom line

- **Clean / green-light:** **D006** (24V house bus + Orion-Tr + UL-489 breaker) survived adversarial re-derivation as *mostly-corroborated*. **D002's original 2S/2S2P solar topology was later superseded by the corrected 3-panel house-charger verdict**; the LiTime AIO limits below still apply to its own PV input only.
- **Real safety/fit problem — thermal:** **D008** (Dometic CFX3 95DZ) was **downgraded to mixed**. The "enclosed curbside bay" directly violates Dometic's own manual, which requires a **50 mm (~2 in) gap on all four sides** and says **"Do not place the cooling device in closed compartments."** Electrical sizing is fine; the bay is non-compliant until forced ventilation makes it genuinely ventilated.
- **Real safety problem — operating envelope:** **D007** (Fiamma F45s awning). Mount design is correct, but the **>20 mph retract rule is ~2x too permissive** for the as-built wall-only (no legs, no tie-down) configuration — consensus for that case is **~10 mph**. Also the limiting failure is the awning's own arms/extrusions bending, *not* fastener pull-out, so "more fasteners = safer" only holds up to a point.
- **Carry a real caution — moisture:** **D009** (PlexCore + FRP) and **Roof** (foam + elastomeric) both hinge on a trapped-moisture sandwich with little drying path. Both are sound **only if the cavity starts and stays dry**; prove FRP adhesive compatibility with PlexCore and use a cold-rated roof coating.
- **Needs vendor/measurement check — fit:** **Windows** stays **mixed**. Cutout sizes are correct, but the trim ring targets a single **1.5" wall** and the build wall is ~1"–1.4". This is a *fixable* furring/shim step (build the wall up to the ring), not a dead end — but as literally specified it won't clamp tight, and the steel-door cut needs re-framing.
- **One hardware-specific watch:** the LiTime 3500 W fallback reportedly nuisance-faults on PV overvoltage *below* its advertised 145V max with 49V-class panels like these LGs — 2S at ~113V cold is clear of it, but **never add a 3rd panel in series to that AIO input**.

---

## D002 — Solar string sizing: LiTime 3500 W fallback PV input
**Verdict:** superseded for the active roof/house design by the corrected [3-panel house-charger verdict](../../runs/aio-adversarial-3panel/synth/VERDICT.md). This section remains valid only as a check on the **LiTime 3500 W fallback PV input**: 2S is safe there; 3S is not.

- ✅ Holds: LG's official spec page confirms Voc 49.9V, Vmpp 42.1V, Isc 11.39A, Impp 10.83A, Voc temp coeff −0.26%/°C, max series fuse 20A (https://www.lg.com/us/business/neon-h/lg-lg455n2w-e6).
- ✅ Holds: Re-derived 2S cold Voc is only ~108.9V at −10°C and ~112.8V at −25°C against the 145V ceiling; break-even needs per-panel Voc 72.5V (~−149°C), physically unreachable (https://www.lg.com/us/business/neon-h/lg-lg455n2w-e6).
- ✅ Holds: 3S is non-viable — 3 × 49.9V = 149.7V exceeds 145V at STC before any cold correction, ~169V at −25°C (https://www.lg.com/us/business/neon-h/lg-lg455n2w-e6).
- ✅ Holds: a 2S deployable pair sits far inside LiTime's 4400W / 50A PV limits (60–145V window, single 80A MPPT) (https://www.amazon.com/3500W-Solar-Inverter-Charger-Controller/dp/B0DCNMYVD5). A 2S2P four-panel fallback is also electrically in-window if the roof 3S/SmartSolar path slips.
- ⚠️ Watch: Owners report this LiTime AIO does **not** reliably honor its advertised 145V PV max and faults on solar overvoltage, explicitly citing "bigger panels are often 49V open circuit" — the exact LG class. 2S (~113V cold) has margin, but treat headroom as real, not "unlimited," and **never add a 3rd series panel to the AIO** (https://www.amazon.com/3500W-Solar-Inverter-Charger-Controller/dp/B0DCNMYVD5).
- ⚠️ Watch: 2S is effectively *required*, not optional — a single panel's 42.1V Vmpp is below the AIO's 60V PV floor; 2S Vmpp (~84V STC, ~73V hot) stays in-window (https://www.lg.com/us/business/neon-h/lg-lg455n2w-e6).
- ❓ Open: The AIO's rated operating-temp floor is **−10°C**, not the −25°C used in the string stress test — keep the unit in a conditioned compartment or accept it should not charge below −10°C. This, not PV voltage, is the binding cold limit.
- ❓ Open: If a 2S2P fallback is ever used on the AIO, set the two 2S strings to the **same orientation/tilt** (one MPPT tracks one combined point; mismatch costs ~2%+). With exactly 2 strings, per-string fuses are still a design check against the module max series fuse and controller input hardware; adding any further parallel string makes 20A per-string fusing mandatory.

---

## D006 — Single 24V house bus; Orion-Tr 48/24-16A; UL-489 80V breaker; no 12V rail
**Verdict:** mostly-corroborated — architecture is safe and code-aligned; one OCP convention should be made explicit, not assumed.

- ✅ Holds: Blue Sea 7443 is genuinely **UL-489** (branch-circuit, confirmed by the product-page title), 80V DC max, 10,000A interrupting, 20A, single-pole — resolving the draft's biggest open question in its favor (https://www.bluesea.com/products/7463/UL-489_Circuit_Breaker_-_20A_Flat_Rocker).
- ✅ Holds: 10,000A AIC clears the ABYC requirement of **5,000A per 100Ah** for the single LiTime 48V 100Ah pack with 2x margin (https://shop.pkys.com/An-explanation-of-the-interrupt-rating-for-circuit-breakers-and-fuses_b_30.html).
- ✅ Holds: Victron's own Orion-Tr install doc recommends a **20A fuse with 2.5–6mm² cable** for 48V — independently confirming the 7443's trip is correctly sized and that external upstream OCP is required (the potted remote on/off terminal carries no input current) (https://www.victronenergy.com/media/pg/Orion-Tr_Smart_DC-DC_Charger_-_Non-Isolated/en/installation.html).
- ✅ Holds: Orion-Tr input range is 32–70V, so the ~54.6V max LiFePO4 bus sits inside the window with headroom; 32V automotive blade fuses on a 48V bus are a genuine fire hazard (arc won't quench) and are correctly avoided (https://www.solar-electric.com/victron-energy-orion-tr-48-24-16a-dc-dc-converter.html, https://community.victronenergy.com/questions/160126/mega-fuse-32v-for-48v-system.html).
- ⚠️ Contradicts: Draft corroboration #1 cites the **wrong product** (part 7465 / "30A Flat Rocker"); the correct page is part 7463, the 20A breaker. Spec claim is right, URL was mismatched (https://www.bluesea.com/products/category/14/131/Circuit_Breakers/UL-489).
- ⚠️ Watch: The 7443 protects the converter *branch*, but ABYC E-13 / standard LiFePO4 practice puts a **Class-T fuse (20kA AIC) at the battery terminal** as the main OCP. Defensible here (one ≤20A branch on small cable) but it should be stated, not assumed (https://www.anernstore.com/blogs/diy-solar-guides/fuses-vs-breakers-lifepo4-battery).
- ❓ Open: Confirm whether a battery-terminal Class-T main fuse exists or the close-mounted 7443 is intended as the main OCP; read the LiTime BMS short-circuit cutoff / prospective fault current off its datasheet (likely interrupts well below 10,000A) (https://www.litime.com/products/litime-48v-100ah-smart-comflex-lithium-battery).
- ❓ Open: Each 24→12V point-of-use buck needs its own properly DC-rated input OCP on the ~29V-max rail — confirm those are specified and are not 32V automotive types.

---

## D007 — Fiamma F45s 350 on owner-fabricated standoffs at perimeter rail + steel posts
**Verdict:** mostly-corroborated (changed from draft) — the mount design is correct, but the retract threshold and the assumed failure mode both need correcting.

- ✅ Holds: Reacting the deployed arm's prying moment with **≥2 fasteners into each 16"-OC steel post** (not a single centered rail bolt) is correct and mirrors a documented real-world fix: an owner who suffered a wind failure replaced two small factory L-brackets with **three 16" aluminum L-brackets + 3/4" #12 screws** (https://www.trailmanorowners.com/threads/replacing-the-awning.776148/).
- ✅ Holds: F45s uses two 12cm outer load-bearing brackets (+ optional 8cm center on 250–350), and "the two outer, end brackets … support the bulk of the arm weight and force" — confirming the deployed canopy exerts a prying/pulling load the mount must react (https://www.campervan-hq.com/blogs/van-build-guide/fiamma-f45s-install-by-field-van).
- ✅ Holds: Brackets must be mounted **linearly, shimmed even and level, not on a curved edge** — directly supports the build's need for a planar, non-twisting standoff face (https://www.campervan-hq.com/blogs/van-build-guide/fiamma-f45s-install-by-field-van).
- ⚠️ Contradicts (safety — operating envelope): The owner's **>20 mph** retract rule assumes legs staked **plus** a tie-down. For a free-standing wall-only mount carrying load through fasteners alone, consensus is **~10 mph** ("without support poles and tie downs, a recommended limit is about 10mph … with support poles and tie downs, allowable wind speeds increase to 20-25mph") (https://www.tjsrv.com/how-much-wind-can-an-rv-awning-withstand/, https://www.vistashades.com/post/how-much-wind-can-a-retractable-awning-take-and-how-to-protect-it).
- ⚠️ Contradicts (failure mode): The limiting failure in a gust is the **awning's own aluminum extrusions/arms bending** (arms "gone floppy … lost the tension"), not fastener pull-out. A stiffer mount transmits *more* load into the awning body before it yields, so "more fasteners = safer" holds only until the awning hardware becomes the weak link (https://wildcamping.co.uk/threads/fiamma-f45s-awning-disaster.82646/).
- ⚠️ Watch: Fiamma arms are designed to release/collapse under wind or pooled-water overload; a rigid over-constraining standoff could defeat that intended release and redirect damage into the rail/extrusion (https://www.tjsrv.com/how-much-wind-can-an-rv-awning-withstand/).
- ❓ Open: Decide the deployment mode — legs+tie-down (earns ~20–25 mph) **or** wall-only (forces ~10 mph trigger). The build-sheet retract spec must match; as written ("load through fasteners alone") it implies the ~10 mph case.
- ❓ Open: No source gives a quantified design force; compute peak lateral+uplift (fabric area × dynamic pressure at chosen retract speed, with gust/safety factor). Verify fastener pull-out into the 76.5" posts via steel-fastener tables or a pull test (depends on tube wall thickness, fastener type, edge distance) and whether the standoff defeats arm-collapse — needs a deployment test.

---

## D008 — Dometic CFX3 95DZ: 24V native, 10A fuse/14 AWG, enclosed curbside bay
**Verdict:** mixed (downgraded from mostly-corroborated) — electrical sizing is sound and conservative; the enclosed-bay thermal plan **violates Dometic's own manual** as worded.

- ✅ Holds: Official spec confirms ~**4.6A @24V / 10.4A @12V** continuous from a variable-speed VMSO3 soft-start compressor (no big locked-rotor spike), so a 10A fuse is ~2x the continuous draw (https://www.dometic.com/en/product/dometic-cfx3-95dz-9600025322).
- ✅ Holds: A 10A fuse **massively under-protects 14 AWG** (105°C insulation carries far more than 10A even with hot-bay derating), so the wire is well protected and correctly sized for the load (https://www.bluesea.com/support/reference/529/Allowable_Amperage_in_Conductors_-_Wire_Sizing_Chart).
- ✅ Holds: Climate class N/T confirms the **110°F/43°C** ceiling and the >86°F/30°C dual-zone setpoint limitation (https://www.earthtechproducts.com/dometic-cfx3-95dz-electric-cooler.html).
- ⚠️ Contradicts (safety/fit — the headline finding): The draft claimed Dometic publishes no clearance and only says "keep vents clear." **False, and wrong in the unsafe direction** — the CFX3 manual specifies a **minimum 50 mm (~2 in) gap on all four sides** and states **"Do not place the cooling device in closed compartments or areas with none or minimal air flow."** An "enclosed" bay is non-compliant as written (https://manuals.plus/dometic/cfx3-series-compressor-cooler-manual, https://www.frigolab.eu/gb/blog/insights/questions-and-answers-dometic-cfx3-coolers).
- ⚠️ Watch: Dometic ties **Warning 34** ("compressor speed low") to high ambient + "air vent blocked or insufficient clearance," and forum reports tie **Warning 33** to low incoming voltage / line loss — the hot enclosed bay and any voltage drop are the real risks, not the fuse (https://support.dometic.com/en/cfx3-coolers/WARNING-34-Compressor-speed-low-92f).
- ❓ Open: Convert the bay from "closed compartment" to compliant — provide the **50 mm all-sides clearance plus forced through-flow ventilation**, then field-measure in-bay air under desert sun with the awning out: **<43°C to run at all, ideally <30°C** to preserve simultaneous dual-zone setpoints.
- ❓ Open: Confirm 14 AWG round-trip voltage drop at 4.5A/24V holds the fridge above its low-voltage cutoff (keep <3%, else upsize). Verify the unit's manufacture date against the **Nov 2019–Jun 2020 recall** window and that wiring can't create a 12V+120V backfeed. Clamp-meter the actual 24V startup current to rule out nuisance trips on a fast 10A fuse.

---

## D009 — Superseded 3/8" birch ply over pulled OSB, FRP textured panel over birch

**Current status:** superseded 2026-06-08. The active D009 reuses the factory 3/8" PlexCore sidewall liner and applies FRP over PlexCore; this section remains as historical validation of the now-rejected birch path.
**Verdict:** mostly-corroborated (changed from draft) — the swap is sound and workable, but the moisture sandwich is the real hazard and one "precedent" was misread.

- ✅ Holds: 3/8" over 1/4" is correct — plywood bending stiffness scales with the cube of thickness, so 3/8" is ~**3.4x stiffer** at the same 16"-OC span; thinner finish panels are flagged as too flexible (https://up.codes/s/wall-sheathing).
- ✅ Holds: Marlite C-551 FRP adhesive is explicitly for porous subwalls "such as unfinished/untreated drywall or **plywood**," while any non-porous (painted) surface requires a different Advanced Polymer Adhesive — so bare birch is the *preferred* substrate and **"no paint between birch and FRP" is correct** (https://dsisupply.com/product/MLT127986?categoryCode=other_frp).
- ✅ Holds: Closed-cell spray foam against the steel skin is standard practice (vapor/air barrier keeping the metal above dew point) (https://oneclickdiy.com/blogs/insulation/spray-foam-insulation-vapor-barrier).
- ⚠️ Contradicts (moisture — the genuine hazard): Impermeable FRP inside + sub-1-perm closed-cell foam outside leaves interior-glue birch with **essentially no drying path** in a non-climate-controlled vehicle — "water trapped behind closed-cell spray foam stays there and rots the plywood" (https://oneclickdiy.com/blogs/insulation/spray-foam-insulation-vapor-barrier).
- ⚠️ Contradicts (precedent was misread): The mychemicalfreehouse cargo-trailer build cited *for* birch is actually a **moisture-failure cautionary tale** — "MAJOR condensation formed behind the walls," conversion "failed miserably." It supports the rot risk, not the substrate choice; no clean reference of a *successful* OSB→birch-under-FRP build was found (https://www.mychemicalfreehouse.net/2019/06/cargo-trailer-conversion.html).
- ⚠️ Watch: 3/8" is near a **floor, not a generous margin** — code structural-sheathing minimum at 16" OC is 7/16". Defensible here only because the panel is non-structural (FRP-faced finish over steel posts) and the bonded FRP adds composite stiffness; adequacy depends on the lamination, not 3/8" alone (https://up.codes/s/wall-sheathing).
- ❓ Open: Strongly favor **exterior/marine-glue birch over interior-glue ply** as cheap insurance; seal all FRP seams/edges and the window clamp sandwich so liquid water never enters the cavity. Confirm the actual FRP brand (Crane vs Marlite vs Glasbord) approves Baltic birch and which adhesive grade it warranties — the C-551 sheet's "do not use on other wood-based products" note means the chosen brand's spec governs, not a generic "porous plywood" assumption. Confirm 3/8" birch preserves the window clamp-stack fit vs the 3/8" OSB it replaces (added FRP thickness accounted for).

---

## D010 — Durabak-18 flexible polyurethane bed-liner floor, coved before FRP
**Verdict:** mostly-corroborated — the bed-liner coating direction is stronger than rubber coin roll for this moto trailer, but the fuel claim must be phrased as spill resistance rather than proof against immersion.

- ✅ Holds: Durabak describes the product class as a **flexible, one-part, non-slip polyurethane coating** (https://www.durabakstore.com/pages/product-data).
- ✅ Holds: Durabak's textured outdoor/marine product is described as water-resistant, flexible, UV/chemical resistant, anti-slip, and roll/brush friendly; published coverage is about **60 ft² per gallon** for a standard two-coat textured application (https://www.durabakcompany.com/products/durabak-marine-liner-outdoor-textured).
- ✅ Holds: Durabak's own wood-prep guidance makes the right gate explicit: if wood dust remains after sanding, the coating bonds to dust instead of wood fibers and can release; they call out the importance of a patch test on sanded wood (https://www.durabakstore.com/pages/general-surface-preparation-application).
- ✅ Holds: Raptor validates the broader flexible-polyurethane liner class: the TDS lists wood as a substrate, says stable wood can be coated directly after prep, and supports brush/roller application as well as spray (https://www.raptorliner.com/uploads/6/9/6/5/6965393/u-pol_raptor_liner_black_technical_data.pdf).
- ✅ Holds: The old SBR coin-roll lean is materially weaker for moto use: SBR has poor oil/fuel resistance and is not recommended around petroleum-based oils, fuels, or solvents (https://www.thomasnet.com/articles/plastics-rubber/all-about-sbr-rubber/).
- ⚠️ Corrected claim: Raptor's chemical table says diesel and hydraulic oil have no effect, but **petrol/gasoline is only splash-resistant**. Do not document the floor as "fuel-proof"; document it as spill-resistant and clean gasoline promptly (https://www.raptorliner.com/uploads/6/9/6/5/6965393/u-pol_raptor_liner_black_technical_data.pdf).
- ⚠️ Watch: Any bed-liner-on-wood system lives or dies on prep. The build should sand, vacuum, remove dust exactly per the coating instructions, run a PlexCore adhesion patch, and run a small gasoline/diesel drip patch before coating the full floor.
- ❓ Fallback: If Durabak fails the actual-floor patch, use a Raptor-class flexible polyurethane with proper wood prep. If coating fails entirely, the only acceptable roll fallback is fully glued G-Floor PVC trailer flooring; G-Floor's trailer line is waterproof and marketed as resisting oil, grease, gas, corrosives, chemicals, and contaminants, but loose-lay would reintroduce the dust/water trap (https://bltllc.com/gfloor-universal-flooring/trailer-flooring/).

---

## Roof — Closed-cell foam underside + elastomeric exterior coating on steel roof
**Verdict:** mostly-corroborated — the foam-inside/coating-outside steel sandwich is endorsed by building science **provided the steel is dry at closure**; cold-weather coating selection is the load-bearing open item.

- ✅ Holds: Lstiburek's framework does more than tolerate this geometry — a metal deck trapped between two vapor-impermeable layers is named among the **"most common and successful"** roof assemblies, working "fabulously well … in all the climate zones," the sole condition being it "start out dry" (https://buildingscience.com/documents/insights/bsi-073-macbeth-does-vapor-barriers).
- ✅ Holds: Closed-cell foam is the **correct inside layer** (continuous insulator + vapor/air barrier, "the most effective solution to prevent condensation on metal roofs"); open-cell would be the dangerous choice (https://duratite.co.uk/blog/condensation-on-metal-roof/).
- ✅ Holds: No chemical corrosion from foam-on-steel contact — "no chemicals in the spray foam which would react with the steel or the galvanized or galvalume" layer; corrosion risk is strictly trapped moisture from a leak or open-cell condensation, **not** the closed-cell + coating sandwich (https://www.hansenpolebuildings.com/2018/02/spray-foam-insulation-steel-roofing-corrosion/).
- ✅ Holds: White elastomeric cool-roof coatings deliver ~**87–89% solar reflectance** with a field-measured roof-surface drop of **155°F → 95°F (60°F)** — claim of meaningful deck-temperature reduction is quantitatively supported (https://usmadesupply.com/resources/guides/what-is-an-elastomeric-roof-coating).
- ⚠️ Watch (the real, outcome-determining hazard): Standard water-based **acrylic elastomerics go brittle in deep cold and "zipper" off**; cracks admit water that freezes and pries the coating loose. If the trailer sees sub-freezing exposure, this is the failure mode to design against (https://www.americanweatherstar.com/installing-roof-coatings-in-cold-weather/).
- ⚠️ Watch: Steel-roof manufacturers may **decline warranty** on panels with spray foam adhered underneath (attribution of future damage becomes hard) — not a safety issue, but confirm it's acceptable before foaming (https://www.hansenpolebuildings.com/2018/02/spray-foam-insulation-steel-roofing-corrosion/).
- ❓ Open: Specify a coating **explicitly rated for cold-weather flexibility/cure** (silicone or cold-rated formulation), applied above the manufacturer's minimum temp onto a fully dry skin — not a generic summer-cure acrylic.
- ❓ Open: Verify the steel is clean/dry/rust-free at closure (the sole condition the endorsement rests on); confirm the foam is continuous and **air-sealed at every bow, fastener, and penetration** (interior-air leakage to cold steel is the dominant corrosion path on a sealed trailer); run the 48-hr adhesion test patch on galvanized/aluminized; schedule periodic exterior **blister inspections** since hidden-steel corrosion is otherwise invisible until advanced.

---

## Windows — RecPro RP-FRMWIN frameless windows, wall + door
**Verdict:** mixed (changed from draft) — cutout sizes are correct and orderable; the trim-ring/wall mismatch is a **fixable furring step that's missing from the stated sandwich**, not an inherent fail, but the steel-door cut and seal-against-thin-steel remain real unknowns.

- ✅ Holds: Cutouts verified on RecPro pages — **RP-FRMWIN-1222 = 11-5/8" W × 21-5/8" H** (overall 14×24×2.5) and **RP-FRMWIN-2015 = 19-5/8" W × 14-5/8" H** (overall 22×17×2.5) (https://recpro.com/rv-frameless-window-12-w-x-22-h/, https://recpro.com/rv-frameless-window-20-w-x-15-h/).
- ✅ Holds: The trim ring is published as a **single value, "Trim Ring for 1 1/2" wall thickness," with no min/max range**, confirmed identically across multiple RecPro models — so the wall must be brought to ~1.5" at the opening (https://recpro.com/rv-frameless-window-20-w-x-15-h/).
- ⚠️ Contradicts (the draft over-stated this as near-certain failure): The documented standard fix for a thin/metal cargo wall is to **fur out / shim the opening with wood spacers** so the wall reaches the ring's target depth — clamp rings are routinely mounted over wood fillers and shimmed to suit. The ~1"–1.4" wall is a solvable build detail, not a dead end (https://www.rvwindows.com/rv-window-installation/, https://www.motionwindows.com/rv-window-installation/).
- ⚠️ Watch (but weaker than the draft framed): RV screw/clamp-ring windows are **commonly and successfully installed in steel cargo trailers / metal-skin conversions** with butyl + sealant — metal-wall use is normal, not outside the envelope. Still, as *literally* specified (no furring), the 1.5" ring won't seat tight, which is the documented leak mode (https://darkskiesfilm.com/how-to-cut-windows-in-a-cargo-trailer/).
- ⚠️ Watch: Cutting a 20"×15" hole in a steel personnel door removes a structural panel and **warrants added perimeter metal framing/reinforcement** — standard cargo-trailer practice (https://darkskiesfilm.com/how-to-cut-windows-in-a-cargo-trailer/).
- ❓ Open: Confirm with RecPro the actual clamp/screw depth and that **furring from ~1"–1.4" up to 1.5" is supported** (or whether a thinner-wall ring/spacer exists) — the single published value gives no tolerance.
- ❓ Open: Mock up to verify the **0.02" steel skin + FRP face is flat/rigid enough** to seat the exterior pane's butyl without foam-core compression; isolate **galvanic corrosion** between the aluminum frame/clamp screws and steel skin/door (butyl + stainless or nylon); measure the actual **32×72 door gauge/stiffener layout** to size re-framing around the 20×15 cut. No RecPro-specific long-term leak data was found by name — reliability evidence on metal walls remains generic.
