# Solar Mounting Build Sheet - NXT Horizon / NXT UMOUNT

Date: 2026-06-06

## Verdict

Use **Unirac NXT Horizon / NXT UMOUNT rail** as the panel rail family, but treat the trailer attachment as a **custom cargo-trailer structural mount**, not a normal house-roof install.

The correct load path is:

```text
panel frame -> NXT combo clamp -> NXT rail -> discrete rail foot / bow fastener -> steel roof bow -> trailer frame
```

The wrong load path is:

```text
panel frame -> bracket / rail -> thin roof skin
```

The rails should run **fore-aft**, spanning the three roof panels as one row. The brackets do not need to align with the roof bows; the **rail-to-bow attachments do**.

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
| 12-14 | NXT rail clamps for custom feet | `SHCLMPM2` mill / `SHCLMPD2` dark; consider `NUMTLCLMPM` / `NUMTLCLMPD` only if that packages better | Preferred way to retain NXT rail to low custom feet without drilling the rail itself. Final count equals rail/bow crossings. |
| 12-14 | Custom low feet / saddles | owner-fabricated | Bolt these through the roof into steel bows. The Unirac clamp holds the rail to the foot; the foot holds the trailer. |
| 12-16 | Isolation / bedding pads | EPDM, neoprene, butyl pad, or compatible gasket stock | Use only at discrete attachment feet, not as a continuous trapped strip under the entire rail. |
| 12-16 | Stainless machine fasteners + locking hardware | likely 1/4 in or 5/16 in after bow/tube check | Final size waits on bow width, wall thickness, and access. Use anti-seize on stainless. |
| 12-16 | Backing / crush-control pieces | backing plates, sleeves, plusnuts/rivnuts, or through-bolt washers | Do not collapse the roof bow or oil-can the skin. |
| 1 tube+ | Henry 884 silicone roof sealant | `HE884` family | Use for penetrations and rail-foot perimeters under the Henry 887 roof system. |

## Do Not Buy / Do Not Lead With

| Part family | Reason |
|---|---|
| Unirac shingle flashings / residential roof kits | Wrong roof. This trailer does not have shingles, rafters, or roof sheathing behaving like a house. |
| Stronghold butyl attachment kit as the whole answer | Useful reference hardware, but the included roof fasteners are not the trailer load path. The steel bows are. |
| Adhesive-only / VHB-only mounts | Not acceptable as primary retention for large rigid glass panels at highway speed. |
| Hidden end clamps as the default | `NUHECLMP1` is cleaner looking, but it adds flange-geometry dependency. Combo clamps are simpler, visible, and inspectable. |
| NXT HD rail | Not needed unless the dry-fit creates a long unsupported span. Standard NXT rail is the first choice. |
| SOLARMOUNT clamps on NXT rail | Do not mix legacy SOLARMOUNT clamps with NXT UMOUNT/Horizon rail. Stay inside one rail/clamp family. |

## Attachment Detail

Preferred detail: **discrete low-profile feet at bow crossings**, with the NXT rail retained to those feet without relying on the roof skin.

The rail should not be bedded continuously to the roof. Continuous contact traps water, dust, alkali playa grit, and corrosion under the rail. Use discrete sealed pads/feet at the roof bows, with drainage gaps between them.

Build each rail-to-bow station as:

```text
NXT rail
  -> NXT rail clamp or custom saddle/through-fastener detail
  -> isolation pad / butyl gasket
  -> trailer roof skin, sealed as weather layer only
  -> steel roof bow, mechanically fastened
  -> backing washer / plate / crush-control detail
```

There are two viable attachment variants:

1. **NXT-native clamp to custom foot, preferred.**
   Use `SHCLMPM2` / `SHCLMPD2` as the rail-to-foot interface, then bolt the low-profile custom foot through the roof into the steel bow. The `NUMTLCLMPM` / `NUMTLCLMPD` metal-roof rail clamp is a secondary packaging option if it fits the custom foot better. This preserves the NXT rail and clamp behavior while making the trailer bow the structure.

2. **Direct rail-to-bow through-bolt, acceptable only as a custom non-listed trailer detail.**
   Drill the NXT rail at bow crossings and through-bolt it to the bow with isolation pads, sealed penetrations, backing, and locking hardware. This is mechanically straightforward but should be treated as a custom fabrication decision because drilling the rail is outside the cleanest Unirac installation path. Confirm bolt heads/nuts do not interfere with combo clamps, wire clips, or panel service.

For this trailer, the practical target is **about 12 attachment stations**: 2 rails x about 6 bow crossings. Add a few extra pads/fasteners for mistakes or one more bow station if the final layout allows it.

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
7. Drill pilot holes at the bow attachment points only.
8. Deburr every hole and prime/paint exposed steel or aluminum edges.
9. Install isolation pads and rail feet/fasteners with butyl or gasket compression.
10. Mechanically fasten to the bows with locking hardware and crush control.
11. Cap fastener heads and foot perimeters with Henry 884.
12. Hose-test all penetrations before panels go on.
13. Apply Henry 887 roof coating after penetrations pass, lapping onto cured compatible sealant.
14. Install panels, combo clamps, grounding lug, and wire clips after coating cure.
15. Re-torque / inspect after the first tow and after the first rough-road trip.

## Open Measurements Before Ordering

- Exact roof bow stations in the roof rectangle.
- Roof bow tube width and wall thickness.
- Whether through-bolting is accessible before foam.
- Roof crown at the rail lines; foot/pad thickness may need to vary slightly.
- Final Velit curb and PV gland positions.
- Actual NXT rail clamp fit on the chosen custom foot detail.
- Actual NXT combo clamp fit on the 40 mm LG module frame.
- Final rail spacing from the LG module clamp-zone guidance.
- LG short-side clamp-zone permission for the final fore-aft rail orientation.

## Panel Review Notes

The panel review agreed on the core decision:

- NXT rail is a good part family for the panel-to-rail side.
- The trailer roof attachment is the custom part of the build.
- Do not let the roof skin become the structure.
- Do not trap water under a continuous rail.
- Do not use adhesive as primary retention.
- Serviceability matters: panels should come off without destroying roof sealant.

## Sources

- Unirac NXT UMOUNT product page: https://unirac.com/products/pitched-roof/nxt-umount/
- Unirac NXT UMOUNT installation manual: https://unirac.com/document/nxt-umount-install-guide/
- Unirac NXT UMOUNT cut sheet: https://unirac.com/document/nxt-umount-cut-sheet/
- Unirac Stronghold Butyl attachment page: https://unirac.com/products/attachments/stronghold-butyl/
- Local dimensions: [dimensions.md](dimensions.md)
- Solar mounting strategy research: [solar-panel-mounting-backing-2026-06-06.md](research/solar-panel-mounting-backing-2026-06-06.md)
