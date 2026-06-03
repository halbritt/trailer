---
kind: handoff
schema_version: striatum.artifact.v1
title: "Interior / layout — cross-examination (OUT-OF-BAND, agy)"
author: operator
run_id: run_57a530fde60486e00cfafc255867e3e7
workflow_id: juplaya-interior
job_id: cross_examiner_1
status: out_of_band
summary: >
  Falsifying interrogation of the interior/layout author DRAFT.md, produced by
  the agy (Gemini) lane via `agy --dangerously-skip-permissions --print`.
  Captured OUT-OF-BAND: striatum could not dispatch the cross_examiner_1 job
  because the upstream author_draft job cannot reach work.complete in a shared
  working tree shared across four concurrent runs (cross-run write_scope
  collision — see operator friction report). This file is NOT a striatum-
  published artifact; it is a captured transcript for the record.
---

# Cross-Examination (out-of-band, agy / Gemini)

**Provenance:** run via `agy --dangerously-skip-permissions --print` against
`runs/juplaya-interior/dialogue/author/DRAFT.md`. Out-of-band because the
striatum `cross_examiner_1` job stayed `blocked` (gated on an un-completable
`author_draft`; the lane is `agy` but never became claimable).

## Challenges raised

### 1. Handlebar collision math (Q12) — LANDS
Bikes side-by-side, both nose-forward, tracks ~24" apart. Handlebars 32"/34"
wide = 16"/17" half-widths; min centerline clearance is 16+17 = **33"**, so a
24" track spacing implies ~**9" of handlebar interference**. Staggering bikes
fore-aft to clear eats the 157" length and shifts weight rearward, hurting
tongue weight.

### 2. Floor steel location + recess depth (Q12) — LANDS
On a 7'-wide trailer the 2"x4" main longitudinal rails run at the **outer
perimeter** (under the walls), not ±12" off centerline — so centerline-straddling
floor rows would **miss the longitudinal steel** and only cross the 16"-OC
crossmembers. A 1/2" recess into 3/4" PlexCore leaves only ~1/4" of wood; most
bolts between crossmembers would clamp ~1/4" plywood — inadequate for a bouncing
290 lb bike's tie-down preload.

### 3. Bed span flex + socket pull-out (Q14) — PARTIALLY LANDS
An 81" span on 2x4 lumber (even on edge) deflects/bounces under dynamic sleeping
load. Thin-wall studs flex outward under lateral load; loose E-track socket
tolerances plus beam sag risk the lumber ends pulling out of the sockets.

### 4. Wall profile mismatch (Q15) — LANDS
A 1/4" XPS layer behind only the bed zone creates a 1/4" step in the wall plane;
the rigid 34" horizontal E-track can't span the transition flat without bending,
a void behind it, or shimming the rest — nullifying the "bed zone only" economy.

### 5. E-track stud alignment + cut logic (Q13) — LANDS
Wall E-track ends should land on structural studs to resist peel. A 120" (10 ft)
rail is not a 16" multiple (112" or 128" are); without cutting to 112" (waste) or
off-stud splices with heavy backer, rail ends overhang unsupported — violating the
backer requirement.

## Author's standing on these (for the adjudicator, if the gate ever clears)
- #1 and #2 are the strongest and require draft revision: re-derive floor-row
  spacing from a measured ~33"+ handlebar clearance (or accept staggered
  fore-aft with a recomputed tongue-weight position), and re-locate floor rows
  over actual steel (perimeter rails and/or land every bolt on a 16"-OC
  crossmember, or add steel backing plates under the PlexCore).
- #3 argues for sizing the lumber-beam span/section deliberately and adding a
  positive socket retention (the beams should still beat fixed aluminum on
  reconfigurability).
- #4/#5 are detailing fixes (full-height thin shim or skip XPS; cut wall track to
  land ends on posts).
