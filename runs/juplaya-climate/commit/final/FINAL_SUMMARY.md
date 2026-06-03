---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
inputs:
  - author_draft
  - cross_examiner_1
  - collaboration_ledger_cycle_2
  - commit_proposal
---

# Climate / envelope — final summary

**Run:** run_c1b091b11f35c09b89d195e2f0fd9469 (workflow juplaya-climate,
cross_examination shape). **Collaboration gate: CLEARED** — adjudicator verdict
**accept_with_findings** (clearing). Downstream proposal published.

## Gate result
The dialogue phase ran author → cross-examiner → adjudicator. Two material
challenges landed and were directly rebutted by the author *correcting* the
recommendations (not hand-waving), so the verdict is `accept_with_findings`. No
revision cycle was needed; no settled item (closed-cell foam, elastomeric roof,
48 VDC Velit AC) was relitigated.

## Final committed climate/envelope decisions (post-cross-exam)
- **Q8 Windows — CORRECTED:** ONE framed curbside awning window sized to the
  measured clear opening (≤ ~26" RO width), spanning two 16"-o.c. bays and cutting
  one post with a mandatory load-transfer sub-frame; fallback = no glass + a
  powered roof-vent fan. (Original two-window claim was geometrically falsified.)
- **Q9 HRV — HELD:** defer the core; rough-in the paired 4" wall penetrations +
  power string now.
- **Q10 Diesel heater — DOWNGRADED:** no heater for July; rough-in the through-
  floor exhaust + fuel penetrations and CO-detector + 12V string now, defer the
  unit + tank to cold-weather profiles. Hardwired 12V CO detector is committed,
  conditional on the heater ever running.
- **Q11 Awning — HELD:** ~12 ft manual lateral-arm RV awning, curbside,
  through-bolted to the aluminum top rail (never the skin), with desert tie-downs.
  The required July deliverable.

## Provenance chain
- Author DRAFT → `art_ddfff47c55269de704eda12d32c5789a`
  (runs/juplaya-climate/dialogue/author/DRAFT.md)
- Cross-examination → `art_bd1c28a0e1a67893663aec8c09ffd9a2`
  (runs/juplaya-climate/dialogue/cross_examiner_1/CROSS_EXAM.md) — produced by the
  independent agy/Gemini family, run **out-of-band** (striatum could not dispatch
  the agy lane while the job was blocked behind author_draft), captured back into
  the claim loop.
- Collaboration ledger → `art_9bb4069fd61b9d0dd2abc3ebad026ebf`
  (runs/juplaya-climate/dialogue/adjudicator/COLLABORATION_LEDGER_cycle_2.md),
  verdict accept_with_findings (`verdict_e00460ca1beb18e06cb4e596b58e425d`).
- Commit proposal → `art_5e94fc2832509efe577efdc046427987`
  (runs/juplaya-climate/commit/proposal/PROPOSAL.md).

## Open follow-ups for the operator (cross-run + measurements)
- Pre-purchase measurements gate the window, the diesel-exhaust floor bay, the
  awning rail/door-head clearance, and the rolled awning box vs. 8'6" legal width.
- Hand to systems run: eventual diesel 12V load + CO-detector 12V string (Q3/Q4
  converter + load list); curbside top-rail sharing between awning rail and solar
  side-rail mounts (Q2).
- Hand to interior run: keep all penetrations clear of E-track rows + crossmembers.
