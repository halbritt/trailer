---
schema_version: striatum.collaboration_ledger.v1
artifact_kind: collaboration_ledger
shape: cross_examination
topic: "Climate / envelope open questions (windows, HRV, diesel heater, awning)"
verdict: accept_with_findings
author: operator
participants:
  - author
  - cross_examiner
  - adjudicator
entries:
  - kind: claim
    by: author
    refs: ["dialogue:1"]
    text: "Q8: add two curbside frameless dual-pane awning windows sized ~22x18 to fit between 16in o.c. posts; Q9 HRV defer+rough-in; Q10 install a diesel air heater now for July (floor-mount, sealed combustion, through-floor exhaust, external tank, CO detector); Q11 12ft manual lateral-arm awning through-bolted to the curbside top rail."
  - kind: challenge
    by: cross_examiner
    refs: ["dialogue:2"]
    text: "Q8 is geometrically impossible: 16in o.c. tube posts leave <=15in clear; a 22in (or 18in) window cannot fit between two posts without cutting a load-bearing post. Even spanning two bays, jack-studs leave only ~27.5in clear, so a 30in window still will not fit."
  - kind: rebuttal
    by: author
    refs: ["dialogue:3"]
    text: "Conceded twice. Corrected to ONE measurement-gated framed curbside awning window, RO width <=~26in, spanning two bays / cutting one post with a mandatory load-transfer sub-frame (header+sill+jack-studs); exact clear opening is a hard pre-purchase measurement; fallback is no glass + a powered roof-vent fan if cutting a post is rejected."
  - kind: challenge
    by: cross_examiner
    refs: ["dialogue:4"]
    text: "Q10 (author's self-flagged weakest): mild ~50-60F July Black Rock nights do not justify a permanent diesel install given under-floor-exhaust fire risk over dry scrub, 48->12V conversion overhead (no 12V system exists yet), and a heavy fuel tank forward on a nose-sensitive single axle; a quilt or 48V electric blanket covers July comfort with zero added risk."
  - kind: rebuttal
    by: author
    refs: ["dialogue:5"]
    text: "Partial concession: withdrew 'install now for July.' Q10 downgraded to the same posture as Q9 HRV: rough-in through-floor exhaust + fuel-line penetrations and CO-detector + 12V power string now (cheap while envelope is open), defer the heater unit + external tank to cold-weather mission profiles; CO detector remains a commitment conditional on the heater ever running."
  - kind: constraint
    by: adjudicator
    refs: ["dialogue:2", "dialogue:4"]
    text: "Binding physical constraints load-bearing on the dialogue: 16in o.c. / 76.5in tube posts (window fit), single 3500lb nose-sensitive axle with payload to be weighed (heater/tank tongue weight), 48V-only stack with no 12V system yet (heater 12V load forces a converter decision), 48VDC Velit AC settled."
rationale: "Two material challenges landed and were directly rebutted in-thread by correcting the recommendations rather than hand-waving, so the dialogue did real work and the surviving recommendations are tighter than the draft. Q8 two-window claim is dead (replaced by one measurement-gated window or none); Q10 'install now' is withdrawn (replaced by rough-in-now/defer-unit). Q9 and Q11 were uncontested and stand. No settled item was relitigated. Clearing verdict accept_with_findings: the committer must carry Finding 1 (one measurement-gated window or none) and Finding 2 (diesel rough-in-now/defer-unit + conditional CO detector) into the proposal."
---

# Collaboration ledger — cycle 1 (Climate / envelope)

**VERDICT: accept_with_findings** (a clearing verdict).

Read only the dialogue trajectory: author DRAFT and cross_examiner_1 CROSS_EXAM.
Two material challenges landed and were directly rebutted by correcting the
recommendations. Findings below MUST be carried into the commit proposal.

## Finding 1 (Q8 Windows) — geometry falsified; recommendation corrected
The two-window / "22in fits a bay" claim is geometrically impossible against
16in o.c. posts and dies. Survives as ONE measurement-gated framed curbside
awning window (RO width <= ~26in, spanning two bays / cutting one post with a
load-transfer sub-frame) OR no glass + a powered roof-vent fan. Exact clear
opening is a hard pre-purchase physical measurement.

## Finding 2 (Q10 Diesel heater) — "install now for July" withdrawn; downgraded
Replaced by the Q9 posture: rough-in the through-floor exhaust + fuel-line
penetrations and pull CO-detector + 12V power string now; defer the heater unit
and external tank to the cold-weather mission profiles. CO detector remains a
commitment conditional on the heater ever running.

## Held up (uncontested)
- **Q9 HRV** — defer + rough-in now.
- **Q11 Awning** — 12 ft manual lateral-arm, curbside, through-bolted to the top
  rail, coordinated with the solar-mount run. Remains the committed July deliverable.

## Process note (recorded, not disqualifying)
The cross-examiner turns were produced by the declared independent family (agy /
Gemini) but **out-of-band** (`agy --print`) because striatum could not dispatch
the agy lane while the job was blocked behind author_draft; the operator captured
agy's genuine output into the CROSS_EXAM artifact and published it through the
claim loop. Substance is independent-family cross-examination; trajectory treated
as valid. Flagged to the operator as friction, not held against the verdict.
