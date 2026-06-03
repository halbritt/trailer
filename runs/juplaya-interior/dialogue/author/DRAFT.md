---
kind: handoff
schema_version: striatum.artifact.v1
title: "Interior / layout — author draft (committed recommendations)"
author: operator
run_id: run_57a530fde60486e00cfafc255867e3e7
workflow_id: juplaya-interior
job_id: author_draft
status: draft
summary: >
  One committed recommendation per open interior/layout question for the
  FT712S2-D moto-basecamp build, grounded in the confirmed shell (81" W x 157" L
  x 78" tall interior, 2"x4" steel main rails, crossmembers 16" OC, 4x factory
  5,000 lb D-rings, 3/4" PlexCore floor) and the E-track-as-OS reconfigurability
  north star. Live for cross-examination.
---

# Interior / layout — Author Draft

**Build envelope (confirmed):** interior **81" W x 157" L x 78" (6'6") tall**;
floor is 3/4" PlexCore over **2"x4" steel main rails**, **crossmembers 16" OC**,
vertical wall posts 16" OC; **4x factory 5,000 lb welded D-rings**; rear 5,000 lb
ramp (78"x72" opening); side personnel door 32"x72" RH. On hand: **~6x 10 ft
black powder-coated E-track (≈60 lin ft)**. Payload will be **weighed**, not
estimated — do not design against a guessed budget.

**Use case:** convertible bikes-out -> sleeping deck. **WR250R (~250 lb wet,
~57" wheelbase) + CRF450RL (~290 lb wet, ~58.5" wheelbase), ~590 lb combined.**
Handlebar widths ~32-34" each.

**Design principle (north star):** the E-track grid is the OS; nothing welded-in.
Where it is cheap to do so, lay track on a universal pattern that also serves the
fab / kayak / Moab profiles — but optimize the *fixtures* for Juplaya moto.

---

## Q12. E-track floor layout

**Recommendation: Two continuous floor E-track rows running fore-aft (length-wise),
on ~24" centers straddling the trailer centerline, bikes loaded SIDE-BY-SIDE and
both NOSE-FORWARD. Recess the track flush into the 3/4" PlexCore and bolt THROUGH
to the 2"x4" steel main rails / crossmembers, not into plywood.**

- **Side-by-side, not single-file.** Two bikes single-file need ~2 x 85" (front
  wheel to rear axle) ≈ 170" of run — longer than the 157" interior, forcing one
  bike onto the ramp or a compromised wheelbase. Side-by-side uses width we have:
  two ~33" handlebar envelopes = ~66" of the 81" width, leaving ~7" each side for
  knuckle/lever clearance. **Side-by-side fits; single-file does not.**
- **Two fore-aft rows on ~24" centers** (centerline ±12") let a wheel chock + front
  E-track tie ride on the rows for each bike, and convert directly to bed-platform
  leg landings later. Fore-aft (not lateral) rows because the bikes roll in/out
  fore-aft down the ramp and the chocks must index along the roll axis.
- **Mount flush-recessed + bolt through to steel.** Surface-mount track is a
  toe-stub and a chock-roll ramp once bikes are out and the floor is the sleeping
  deck; recessed track gives a flat floor. **Bolt through the PlexCore into the
  2"x4" main rails and 16"-OC crossmembers** (the work order confirms steel there)
  — plywood-only screws will not hold a moving 290 lb bike's tie-down preload.
- **Reuse the 4x factory D-rings** as redundant primary fork tie-downs; the new
  E-track carries chock + rear tie + secondary.

**Depends on:** 2"x4" main rails + 16" OC crossmembers (work order); 81" width;
bike wheelbases.
**MEASURE:** front-tire contact-patch centerlines for BOTH bikes once chocks are
chosen, to set exact chock row positions (drives where the cross-tie track lands).
**BUY:** flush/recess-mount E-track + backing bolts/nutserts rated for through-steel;
2x wheel chocks (see Q14 note).

---

## Q13. Horizontal (wall) E-track heights

**Recommendation: Two horizontal wall E-track rows per side — a BED row at 34"
above the floor and a SHELF row at 60" above the floor. Back BOTH rows with
continuous backer landing on the 16"-OC vertical posts.**

- **Bed at 34".** Bikes are OUT when the bed deploys, so nothing has to clear
  *under* the bed — height is set by sit-up comfort, not clearance. Interior is
  78" tall; a 34" deck leaves **44" of sit-up headroom** over the mattress (a
  ~3-4" pad puts sitting headroom ~40"), which clears a seated adult. 34" also
  matches common chair-height so the deck doubles as a bench bikes-in.
- **Shelf at 60".** Leaves 18" between the 60" shelf row and the 78" ceiling for
  bins/soft gear, and ~22-26" of open volume between the 34" bed and the 60"
  shelf for sitting/reading. A shelf higher than 60" is hard to load over the bed
  and worsens the tipping moment.
- **Back the wall track.** Wall E-track sees point loads + a tipping moment (a
  loaded shelf cantilevers off the wall). Land the track on a continuous ply/steel
  backer that catches the **16"-OC vertical posts** (work order) so anchor pull
  reacts into structure, not just the 3/8" PlexCore sidewall liner.

**Depends on:** 78" interior height; 16" OC vertical posts; bikes-out (no
under-bed clearance constraint).
**MEASURE:** confirm wall-post centerlines vs. door/window cutouts so the backer
spans posts without fouling the 32"x72" side door.

---

## Q14. Bed shoring beams

**Recommendation: E-track shoring-beam INSERTS that accept 2x4 lumber (E-track
"plank/beam sockets"), NOT fixed aluminum shoring beams.**

- **Reconfigurability wins (north star).** 2x4 sockets let the deck span be cut,
  swapped, and re-laid per mission (bed for moto, gear shelf for kayak, nothing
  for fab) with $3 lumber — aluminum beams are a fixed length and a single use.
- **Cheap, replaceable, no welding.** Lumber is sacrificial and field-replaceable;
  a bent aluminum beam at a trailhead is a dead build.
- **Strength is adequate.** Two bodies (~400 lb) over a deck spanning 81" on
  doubled 2x4 lumber landing in E-track sockets at the bed row is well within
  span tables for the short, supported span; verify final span/spacing once bed
  width is fixed.
- **Tradeoff acknowledged:** aluminum is lighter and stiffer per beam — but weight
  is a *managed* tradeoff here, and the lumber's flex over an 81" span is
  acceptable for a sleeping deck (not a structural floor).

**Depends on:** E-track wall rows (Q13); 81" span.
**BUY:** E-track 2x4 lumber-beam sockets (US Cargo Control) — qty = (beams per
deck) + spares. Lumber sourced locally pre-trip.

---

## Q15. Wall finish + build-up

**Recommendation: Leave the factory 3/8" PlexCore sidewall liner as the substrate;
add a 1/4" XPS thermal-break sheet only behind the BED zone, finish the interior
walls in FRP (Home Depot textured white panel) over the existing liner, with
aluminum (or PVC) division-bar + inside-corner trim. NO paint. Do NOT add XPS
full-height where it would bury the wall E-track backing.**

- **FRP over the existing liner.** Wipeable, light, cheap, no paint (matches the
  no-paint rule), and bonds/screws to the PlexCore liner. Luan is the fallback if
  FRP's stiffness/seams prove fussy, but FRP is the durable, moisture-tolerant pick
  for a unit that hauls dirty bikes and gets hosed out.
- **XPS thermal break only behind the bed.** A full-wall 1/4" XPS layer eats into
  the wall-track backing depth and complicates fastening the E-track to posts. The
  high-value thermal break is **where a sleeper's body contacts/radiates to the
  wall (the bed zone)**; spend the build-up there, keep the rest single-layer FRP.
- **Trim:** FRP division bars at seams + inside-corner trim to seal edges; this is
  also what keeps the panel flat without paint.

**Depends on:** 3/8" PlexCore sidewall liner (work order); wall E-track backing (Q13).
**BUY:** FRP textured panels (qty to wall area), FRP trim set (div bars, inside
corners, sealant), 1x 1/4" XPS sheet for the bed zone.
**OPEN/SEQUENCING:** wall E-track backing (Q13) must go in BEFORE the FRP layer —
finish wraps the backer.

---

## Q16. Personnel-door stairs

**Recommendation: A folding/telescoping aluminum RV step that stows INSIDE on the
floor E-track (or clips to the wall track) — not a fixed welded step and not a
loose standalone ladder.**

- **Platform height is 18"; door sill sits at floor + 18" platform** = a single
  big step up. One **height-adjustable telescoping aluminum step (e.g. GlowStep-
  style or a 2-step folding RV stair)** bridges it safely.
- **Stows on the grid (north star).** A step that tie-downs to the floor/wall
  E-track travels secured and deploys in seconds — consistent with "everything
  rides on the grid, nothing loose." A fixed welded fold-down step violates the
  nothing-welded principle and adds a road-height snag.
- **Free-standing > door-hung** for a 32"-wide RV door on a tall-platform cargo
  trailer; door-mounted scissor steps strain a personnel-door hinge not built for
  step loads.

**Depends on:** 18" platform height; 32"x72" RH side door.
**MEASURE:** ground-to-sill height with the trailer at ride height + on a typical
unlevel Juplaya playa surface (drives step count / adjustable range).
**BUY:** telescoping/folding aluminum RV step rated >= occupant weight + margin.

---

## Cross-cutting notes for the examiner

- **E-track budget:** ~60 lin ft on hand. Floor: 2 rows x 157" ≈ 26 ft. Walls:
  4 rows (2 per side) x ~140" usable ≈ 47 ft. **Total ≈ 73 ft > 60 ft on hand —
  this likely needs MORE track or shorter wall runs. FLAGGED for cross-exam.**
- **Tongue weight:** single axle is nose-sensitive; bikes side-by-side both
  nose-forward put mass forward — position the side-by-side pair to land ~10-12%
  tongue weight after the unit is weighed.
- **Everything above is reversible/boltable; nothing welded-in** per the mission.
