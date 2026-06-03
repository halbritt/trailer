---
kind: collaboration_ledger
title: "Climate / envelope — collaboration ledger (cycle 1)"
run_id: run_c1b091b11f35c09b89d195e2f0fd9469
workflow_id: juplaya-climate
cycle: 1
verdict: accept_with_findings
author: operator
inputs: "DRAFT.md; cross_examiner_1/CROSS_EXAM.md"
---

# Collaboration ledger — cycle 1 (Climate / envelope)

**VERDICT: accept_with_findings** (a clearing verdict).

I read only the dialogue trajectory: the author DRAFT and the cross_examiner_1
CROSS_EXAM thread. Verdict basis: **material challenges landed and were directly
rebutted in-thread** by correcting the recommendations, not by hand-waving. The
dialogue is substantive and the cross-examination did real work; the surviving
recommendations are tighter than the draft's. Findings below MUST be carried into
the commit proposal.

## Did a material challenge land? Yes — two.

### Finding 1 (Q8 Windows) — geometry was falsified; recommendation corrected.
- Challenge: a 22" (even 18") window cannot fit between 16" o.c. tube posts
  (~15" clear); and a 30" window spanning two bays still won't clear after
  jack-studs (~27.5" clear with 1.5" tube).
- Rebuttal: author conceded both, twice, and corrected to **ONE measurement-gated
  framed curbside awning window, RO width ≤ ~26", spanning two bays / cutting one
  post with a mandatory load-transfer sub-frame (header+sill+jack-studs)** — OR
  **no glass + a powered roof-vent fan** if the operator rejects cutting a post.
  Exact clear opening is a **hard pre-purchase physical measurement**.
- Adjudication: the rebuttal is sound and the corrected recommendation is the one
  the committer must publish. The draft's original two-window claim is dead.

### Finding 2 (Q10 Diesel heater) — "install now for July" did not survive; downgraded.
- Challenge: marginal July thermal need vs. under-floor-exhaust fire risk over dry
  scrub, 48→12V conversion overhead (no 12V system exists yet), and a heavy fuel
  tank forward on a nose-sensitive single axle; lighter alternatives (quilt, 48V
  electric blanket) cover July comfort.
- Rebuttal: author conceded the trip scope and **withdrew "install now for July,"**
  converting Q10 to the same posture as Q9 (HRV): **rough-in the through-floor
  exhaust + fuel-line penetrations and pull CO-detector + 12V power string now
  (cheap while the envelope is open), defer the heater unit + external tank to the
  cold-weather mission profiles.** CO detector remains a commitment conditional on
  the heater ever running.
- Adjudication: the partial concession is the correct outcome; this is a finding,
  not a reason to reject. The committer publishes the downgraded Q10.

## What held up (no material challenge)
- **Q9 HRV** — defer + rough-in now. Uncontested; now mirrored by the corrected Q10.
- **Q11 Awning** — 12 ft manual lateral-arm, curbside, through-bolted to the top
  rail, coordinated with the solar-mount run. Uncontested; remains the committed
  July deliverable.

## Process note (recorded, not disqualifying)
The cross-examiner thread was produced by the declared independent family (agy /
Gemini) but **out-of-band** (`agy --print`) because striatum could not dispatch
the agy lane while the job sat blocked behind author_draft; the operator captured
agy's genuine output into the CROSS_EXAM artifact and published it through the
claim loop. The substance is independent-family cross-examination; I treat the
trajectory as valid. (Flagged to the operator as friction, not held against the
verdict.)

## Disposition
- Clearing verdict (`accept_with_findings`) — phase gate is cleared.
- The commit proposal MUST reflect Finding 1 (one measurement-gated window or
  none) and Finding 2 (diesel = rough-in-now/defer-unit + conditional CO detector),
  and carry Q9/Q11 as-is.
- No revision cycle invoked (challenges were rebutted in-thread).
