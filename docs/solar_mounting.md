# Solar Mounting Build Sheet - NXT Horizon / NXT UMOUNT

Date: 2026-06-06

## Verdict

Use **Unirac NXT Horizon / NXT UMOUNT rail** as the panel rail family, but treat the trailer attachment as a **custom cargo-trailer structural mount**, not a normal house-roof install.

The selected load path is:

```text
panel frame -> NXT combo clamp -> NXT rail -> through-rail machine fastener -> steel roof bow -> trailer frame
```

The wrong load path is:

```text
panel frame -> bracket / rail -> thin roof skin
```

The rails should run **fore-aft**, spanning the three roof panels as one row. The brackets do not need to align with the roof bows; the **through-rail fasteners do**. The rail will be bonded/bedded down as secondary retention and sealing, but the adhesive is not the primary highway load path.

Low-profile target: keep the rail as close to the roof as practical, but use **1/4 in aluminum spacer pads at each roof bow** if needed to prevent the rail from becoming a water dam. That adds only 1/4 in under the rail while preserving cross-drainage and giving the adhesive/bedding a controlled thickness. Rubber is useful as an isolation/bedding layer, but generic soft rubber should not be the only crush-control spacer.

## Geometry

Current roof-panel layout:

- Panels: 3 x LG455N2W-E6 on the roof.
- Panel size: 83.07 in x 41.02 in x 1.57 in / 40 mm frame.
- Roof array field, landscape: about 83.07 in across the trailer x about 123.06 in fore-aft before gaps.
- Roof measured width: 84-7/8 in rail-edge to rail-edge, so side-clamp hardware outside the panel edges is a bad fit.

NXT layout math for the fore-aft rail length:

| Item | Math | Length |
|---|---:|---:|
| Three panel short sides | 3 x 41.02 in | 123.06 in |
| Two inter-panel gaps | 2 x 0.5 in | 1.00 in |
| Minimum NXT combo-clamp rail end margin | 2 x 1.0 in | 2.00 in |
| **NXT stated minimum** | 123.06 + 1.00 + 2.00 | **126.06 in** |
| Owner target extra margin | panel field + about 6 in | **~129 in cut length** |

Order **two 168 in NXT rails** and cut each rail to roughly **129 in** after the roof dry-fit. Do not order 96 in rails; they are too short. Do not use a splice unless rail availability forces it.

## Primary Buy List

| Qty | Part / family | Candidate part numbers | Notes |
|---:|---|---|---|
| 2 | NXT UMOUNT rail, 168 in, mill or dark | `168RLM1` mill / `168RLD1` dark; domestic `-US` variants if useful | Cut to ~129 in. 185 in also works but wastes more rail. |
| 8 minimum | NXT UMOUNT combo clamp, 30-40 mm | `CCLAMPM1` mill / `CCLAMPD1` dark; domestic dark `NUCCLAMPD2-US` | One clamp at each rail/panel end or seam: 4 clamp positions per rail x 2 rails. Buy 10 if sold loose; a 20-pack is fine. LG frame is 40 mm, right at the upper limit, so verify clamp bite on the actual frame before drilling roof holes. |
| 2 recommended | NXT grounding / lug assembly | `NULGMLP1` / `NULGMLP1-US` | Use one per rail unless a listed rail-to-rail bond path is deliberately installed and verified. Do not assume trailer steel contact is the PV bond path. |
| 1 set | NXT wire-management clips | `WRMCLPD1`; add `WRMCNSD1` only if useful | Clip PV conductors to rails/module frames. No loose MC4 leads on the roof. |
| 1 set optional | Rail / combo clamp cap kit | `NUENDCAPKIT` or current equivalent | Nice-to-have to close rail ends after cutting. Not structural. |
| 12-16 | Through-rail fastener set | likely 1/4 in or 5/16 in stainless machine screws/bolts after bow check | Drill through the NXT rail at bow crossings only. Use locking hardware and anti-seize. |
| 12-16 | Low-profile spacer pads | 1/4 in aluminum flat-bar/plate, cut into short pads | Preferred spacer if drainage or roof crown needs it. Mechanically captured by the through-bolt; bonded/bedded for sealing and anti-rattle. |
| 1-2 tubes | Secondary rail bond / bedding adhesive | Sikaflex-252 preferred candidate; 3M 5200 acceptable but more permanent; patch-test first | Use interrupted pads/beads, not a full-length dam. This is secondary retention and bedding, not the design load path. |
| 12-16 | Isolation / bedding layer | thin EPDM/neoprene, primer/paint, or controlled adhesive layer | Isolate aluminum/stainless/steel interfaces and keep the rail/spacer stack from oil-canning the roof skin. Use EPDM/neoprene, not mystery rubber. |
| 12-16 optional | Rubber spacer pads | high-durometer EPDM/neoprene only | Acceptable only with crush sleeves or hard stops. Good for isolation; worse than aluminum for dimensional control. |
| 12-16 | Stainless machine fasteners + locking hardware | likely 1/4 in or 5/16 in after bow/tube check | Final size waits on bow width, wall thickness, and access. Use anti-seize on stainless. |
| 12-16 | Backing / crush-control pieces | backing plates, sleeves, plusnuts/rivnuts, or through-bolt washers | Do not collapse the roof bow or oil-can the skin. |
| 1 tube+ | Henry 884 silicone roof sealant | `HE884` family | Use for exposed penetration caps and rail-edge/fastener detailing under the Henry 887 roof system. Do not count it as the structural adhesive. |

## Do Not Buy / Do Not Lead With

| Part family | Reason |
|---|---|
| Unirac shingle flashings / residential roof kits | Wrong roof. This trailer does not have shingles, rafters, or roof sheathing behaving like a house. |
| Stronghold butyl attachment kit as the whole answer | Useful reference hardware, but the included roof fasteners are not the trailer load path. The steel bows are. |
| Adhesive-only / VHB-only mounts | Not acceptable as primary retention for large rigid glass panels at highway speed. |
| Hidden end clamps as the default | `NUHECLMP1` is cleaner looking, but it adds flange-geometry dependency. Combo clamps are simpler, visible, and inspectable. |
| NXT HD rail | Not needed unless the dry-fit creates a long unsupported span. Standard NXT rail is the first choice. |
| SOLARMOUNT clamps on NXT rail | Do not mix legacy SOLARMOUNT clamps with NXT UMOUNT/Horizon rail. Stay inside one rail/clamp family. |
| Full-length adhesive dam under rail | Even if bonded, a continuous rail bead can block drainage and trap playa grit. Use interrupted bonded zones with drainage breaks. |

## Attachment Detail

Selected detail: **direct through-rail fastening at bow crossings**, with secondary adhesive/bedding and optional 1/4 in aluminum spacer pads under the rail.

The rail should not be bonded continuously to the roof edge-to-edge. Continuous contact traps water, dust, alkali playa grit, and corrosion under the rail and can create a drainage dam. Use interrupted adhesive/bedding zones at and near bow crossings, with drainage breaks between them. If the rail wants to sit too tight to the skin, use short **1/4 in aluminum pads** at each bow crossing; that is the low-profile drainage spacer.

Rubber option: use EPDM or neoprene as a thin isolation/bedding layer under aluminum pads, or as a high-durometer spacer only if the bolt stack includes crush sleeves/hard stops. Do not use soft rubber that can creep, loosen torque, or let the rail pump under highway vibration.

Build each rail-to-bow station as:

```text
NXT rail
  -> drilled through-rail machine fastener
  -> optional 1/4 in aluminum spacer pad at bow crossing
  -> optional thin EPDM/neoprene isolation layer
  -> secondary adhesive/bedding pad or controlled bead
  -> trailer roof skin, sealed as weather layer only
  -> steel roof bow, mechanically fastened
  -> backing washer / plate / crush-control detail
```

This is a custom non-listed trailer detail:

- Drill the NXT rail at bow crossings and through-bolt it to the bow with controlled adhesive/bedding, sealed penetrations, backing, and locking hardware.
- Use 1/4 in aluminum spacer pads if the rail would otherwise sit as a continuous dam on the roof skin. Keep pads short, only at bow stations. Add thin EPDM/neoprene for isolation if needed.
- If substituting rubber spacer pads for aluminum, use high-durometer EPDM/neoprene and crush sleeves/hard stops so bolt torque cannot relax as the rubber creeps.
- Confirm bolt heads/nuts do not interfere with combo clamps, wire clips, panel service, or the NXT rail channel.
- Deburr every drilled rail hole and treat exposed aluminum/steel edges before final assembly.
- Do not place through-rail bolts where combo clamps need to slide or clamp.

Adhesive candidate:

- **Sikaflex-252** is the first candidate for the secondary bond because it is an elastic polyurethane vehicle-assembly adhesive intended for dynamic loads and bonds aluminum/steel/painted metal when prepped correctly.
- **3M 5200** is acceptable as a permanent marine adhesive/sealant candidate, but it is more removal-hostile.
- **Henry 884** remains the exposed roof-system sealant for caps and edges; do not treat it as the structural rail adhesive.

For this trailer, the practical target is **about 12 through-rail attachment stations**: 2 rails x about 6 bow crossings. Add a few extra fasteners/backing pieces for mistakes or one more bow station if the final layout allows it.

## Panel Hold-Down Pattern

Use the NXT combo clamps as both end and mid clamps.

Per rail:

```text
front end clamp
panel 1
mid clamp
panel 2
mid clamp
panel 3
rear end clamp
```

Counts:

- 4 clamp positions per rail.
- 2 rails.
- **8 combo clamps installed.**
- Buy at least 10 loose, or buy the normal pack quantity and keep spares.

Before roof drilling, test one `CCLAMPM1` / `CCLAMPD1` clamp on an LG frame. The LG frame is 40 mm, and NXT combo clamps are listed for 30-40 mm frames. That is compatible on paper but right at the upper edge.

## Install Sequence

1. Mark roof bow stations from inside the trailer and transfer them to the roof.
2. Draw the Velit curb, PV gland, awning standoff line, roof seams, and panel rectangle.
3. Dry-fit the three panels or a full-size template.
4. Cut the two NXT rails only after the dry-fit; target ~129 in, not shorter than the clamp/gap minimum.
5. Place rail centerlines so all rail-to-roof attachment points land on bow crossings.
6. Verify NXT combo clamp locations on every panel edge/seam.
7. Mark combo-clamp travel zones on the rails so through-rail bolts do not block panel installation.
8. Drill pilot holes through the rails and roof at bow attachment points only.
9. Deburr every hole and prime/paint exposed steel or aluminum edges.
10. Dry-assemble one rail with bolts, backing, and clamps to confirm no interference.
11. Mask the roof and rail so adhesive squeeze-out does not fill clamp slots or drainage paths.
12. Place short 1/4 in aluminum spacer pads at bow zones if needed for drainage/crown control.
13. Apply interrupted Sikaflex-252 or selected adhesive/bedding pads at bow zones.
14. Set the rail, install through-fasteners, and torque only enough to compress bedding without crushing the roof skin or starving the adhesive joint.
15. Install backing/crush-control hardware from inside.
16. Cap fastener heads and rail-edge leak paths with Henry 884 after the adhesive cure window allows it.
17. Hose-test all penetrations before panels go on.
18. Apply Henry 887 roof coating after penetrations pass, lapping onto cured compatible sealant without burying NXT clamp slots or grounding lugs.
19. Install panels, combo clamps, grounding lugs, and wire clips after coating cure.
20. Re-torque / inspect after the first tow and after the first rough-road trip.

## Open Measurements Before Ordering

- Exact roof bow stations in the roof rectangle.
- Roof bow tube width and wall thickness.
- Whether through-bolting or backing installation is accessible before foam.
- Roof crown at the rail lines; spacer/pad thickness may need to vary slightly.
- Whether 1/4 in aluminum spacer pads are needed at all bow stations or only where crown/drainage demands it.
- Whether rubber is only an isolation layer or a spacer; if spacer, define durometer and crush sleeve/hard-stop detail.
- Final Velit curb and PV gland positions.
- Actual NXT combo clamp fit on the 40 mm LG module frame.
- Final rail spacing from the LG module clamp-zone guidance.
- LG short-side clamp-zone permission for the final fore-aft rail orientation.
- Adhesive patch test on actual roof skin and rail offcut, including cure time and peel/removal behavior.

## McMaster Sourcing Shortlist

Do not lock exact SKUs until the bolt diameter, bow wall thickness, and pad footprint are known. McMaster has the commodity pieces:

| Need | McMaster category | Selection note |
|---|---|---|
| Hard low-profile spacer pads | 6061 aluminum bar, 1/4 in thick | Cut short pads from 1-2 in wide 6061 bar. |
| Isolation / gasket layer | EPDM rubber strips or sheet, plain back | Prefer solid EPDM/neoprene around 60A-70A. Avoid soft foam as the structural spacer. |
| Rubber spacer option | hard EPDM/neoprene or polyurethane strip | Use only with crush sleeves/hard stops. Polyurethane is tougher; EPDM is better as weather gasket material. |
| Fastener leak control | bonded sealing washers, preferably stainless + EPDM | Use under exposed screw/bolt heads where geometry allows, then cap with Henry 884. |
| Crush control | aluminum or stainless unthreaded spacers / sleeves | Use where the rail/spacer/roof/bow stack could be over-compressed. |
| Backing | stainless fender washers or backing plates | Final shape depends on bow access and whether the fastener is through-bolted, rivnut/plusnut, or tapped. |

## Panel Review Notes

The panel review agreed on the core decision:

- NXT rail is a good part family for the panel-to-rail side.
- The drilled through-rail trailer roof attachment is the custom part of the build.
- Do not let the roof skin become the structure.
- Do not trap water under a continuous adhesive-bonded rail.
- Do not use adhesive as primary retention.
- Serviceability matters: panels should come off without destroying roof sealant.

## Sources

- Unirac NXT UMOUNT product page: https://unirac.com/products/pitched-roof/nxt-umount/
- Unirac NXT UMOUNT installation manual: https://unirac.com/document/nxt-umount-install-guide/
- Unirac NXT UMOUNT cut sheet: https://unirac.com/document/nxt-umount-cut-sheet/
- Unirac Stronghold Butyl attachment page: https://unirac.com/products/attachments/stronghold-butyl/
- Sikaflex-252 vehicle assembly adhesive: https://usa.sika.com/en/industry/transportation/cargo-trailer/cargo-trailer-adhesives-sealants/exterior-sidewallpanelbondingframetometal/sikaflex-252.html
- 3M Marine Adhesive Sealant 5200: https://www.3m.com/3M/en_US/p/dc/v100693085/
- Henry 884 Tropi-Cool silicone roof sealant: https://www.henry.com/residential/products/residential-roof-coatings/roof-repair-sealants/884-tropi-cool-silicone-roof-sealant/
- McMaster 6061 aluminum bars: https://www.mcmaster.com/products/made-to-order-6061-aluminum-bars/
- McMaster EPDM rubber strips: https://www.mcmaster.com/products/epdm-rubber-strips/
- McMaster bonded sealing washers: https://www.mcmaster.com/products/bonded-sealing-washers/
- McMaster aluminum unthreaded spacers: https://www.mcmaster.com/products/aluminum-unthreaded-spacers/
- Local dimensions: [dimensions.md](dimensions.md)
- Solar mounting strategy research: [solar-panel-mounting-backing-2026-06-06.md](research/solar-panel-mounting-backing-2026-06-06.md)
