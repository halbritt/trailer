---
kind: handoff
title: "Climate / envelope — cross-examination of author draft"
run_id: run_c1b091b11f35c09b89d195e2f0fd9469
workflow_id: juplaya-climate
domain: climate-envelope
author: operator [self-declared: climate-xexam-2]
status: cross-examination-complete
interrogator: agy (Antigravity / Gemini) — independent family, run out-of-band via `agy --dangerously-skip-permissions`
target_artifact: runs/juplaya-climate/dialogue/author/DRAFT.md (art_ddfff47c55269de704eda12d32c5789a)
---

# Cross-examination — Climate / envelope draft

**Procedural note (read first):** the questions below were produced by **agy
(Gemini), the independent cross-examiner family** declared for this lane. They
were generated **out-of-band** via `agy --dangerously-skip-permissions --print`
rather than through striatum's own agy supervisor. Reason: at the time the
interrogation was run, the striatum `cross_examiner_1` job was still blocked
behind the author_draft job, so striatum could not dispatch the agy lane (a
Claude operator session also cannot *be* the agy family). The interrogation
content is genuinely agy's; this CROSS_EXAM artifact is the operator's faithful
capture of that thread, published back through the striatum claim loop so the
adjudicator has the real challenge/rebuttal trajectory. The author's rebuttals
were authored by the Claude author session staying live for interrogation.

Two threads were pressed to settlement: **(A) windows geometry** and
**(B) the diesel-heater "install now" call** (the author's self-flagged weakest
recommendation). Both landed material weaknesses.

---

## Thread A — Q8 Windows: geometric falsification (SETTLED, author conceded twice)

**agy Q1 (falsifying):** "How do you propose to fit a window with a nominal 22"
(or even 18") rough opening between vertical tube posts spaced **16" o.c.**
(work order) without cutting a load-bearing tube post, given that the maximum
clear bay width between these posts is at most ~15 inches?"

**Author A1 (CONCEDED):** Correct — the draft's "fits in one bay" assumption is
falsified. 16" o.c. posts leave only ~14–15" clear; no 18–22" window fits between
two posts. Corrected position: the opening **will** span and cut one intermediate
post, requiring a mandatory welded/bolted sub-frame (header + sill + jack-studs)
to transfer the cut post's load around the opening. To halve structural risk/cost,
drop from two windows to **one** framed curbside window (~30" W × 18" H spanning
two bays), with a **no-glass + powered roof-vent-fan fallback** if the operator
rejects cutting a post.

**agy Q2 (follow-up, falsifying):** "If you span two 16" o.c. bays (32"
center-to-center between the remaining uncut posts) and install jack-studs each
side, how do you fit a **30" RO** window when the clear width between jack-studs
is at most ~29" (1" tube) or ~27.5" (standard 1.5" tube)?"

**Author A2 (CONCEDED again):** Right — even 30" doesn't clear after jack-studs.
**Final corrected window position:** spec the window to the **achievable measured
clear opening** (target ≤ ~26" RO width to leave margin to ~27.5" clear with 1.5"
tube jack-studs); **the exact clear dimension is a mandatory physical measurement
that picks the window, not the reverse.** Recommendation collapses to **ONE framed
curbside awning window sized to measured clear opening (≤~26" RO width)**, with the
no-glass + roof-fan option as fallback.

**Outcome of Thread A:** Material weakness landed and was rebutted by *correcting*
the recommendation. The draft's two-window, 22"-fits-a-bay claim is **dead**;
the surviving recommendation is one measurement-driven framed window (or none).

## Thread B — Q10 Diesel heater "install now for July" (SETTLED, author concedes the trip-scope)

**agy Q (falsifying, bundled):** "How does the marginal utility of active diesel
heating during **mild 50–60°F July desert nights** justify introducing a
**catastrophic fire risk from hot under-floor exhaust over dry vegetation**,
adding **48V-to-12V conversion overhead** (stack has no 12V system yet), and
placing a **heavy fuel tank forward on an already nose-sensitive tongue**, when a
sleeping bag or a 48V heated blanket achieves the same comfort with zero added
risk?"

agy's stated survival bar for the author: must prove (1) sleep-comfort utility
under localized temp anomalies outweighs towing-instability + scrub-ignition risk;
(2) lightweight alternatives (passive insulation, 48V electric blanket) are
insufficient; (3) long-term sub-freezing-trip utility offsets the persistent
weight/complexity penalty imposed on *this specific July voyage*.

**Author rebuttal (PARTIAL CONCESSION — trip scope yields):** The author cannot
clear bar (1)/(2) for July: July Black Rock nights are mild enough that a quilt +
the closed-cell-foam envelope handle sleep comfort, so the *active install for
July* is not justified against the fire/tongue-weight/12V-overhead cost. The
author **withdraws "install now for July"** and converts the diesel heater to the
**same "penetrate-while-open, defer-the-device" treatment as the HRV (Q9):** cut
and seal the through-floor exhaust + fuel-line penetrations and pull the
CO-detector + 12V power string NOW (cheap while the envelope is open, miserable
after foam + FRP), but **defer the heater unit and external tank** to the
cold-weather mission profiles (mission doc #2/#4) where bar (3) is actually met.
The **CO detector remains a commit** if/when the heater is ever fired.
Through-floor exhaust over dry vegetation is accepted as a real operating hazard
to be managed at deploy time (don't park the running heater over scrub), not a
reason to wall-route exhaust.

**Outcome of Thread B:** Material weakness landed. The aggressive "install diesel
heat for July" recommendation **does not survive**; it is downgraded to a
rough-in-now / defer-unit decision, aligning Q10 with the Q9 (HRV) posture.

---

## Conceded weaknesses (for the adjudicator's ledger)

1. **Q8 windows — falsified and corrected.** Two-window / 22"-in-a-bay claim is
   geometrically impossible against 16" o.c. posts. Survives only as ONE
   measurement-driven framed window (≤~26" RO width, spanning two bays / cutting
   one post with a load-transfer sub-frame) OR no glass + roof fan. Exact clear
   opening is a hard pre-purchase measurement.
2. **Q10 diesel heater — downgraded.** "Install now for July" withdrawn; becomes
   "rough-in penetrations + CO-detector wiring now, defer the unit to cold-weather
   profiles." CO detector stays a commitment conditional on the heater ever running.

## Recommendations that held up (not materially challenged)

- **Q9 HRV — defer + rough-in now.** Consistent with the corrected Q10 posture and
  not contested.
- **Q11 Awning — 12 ft manual lateral-arm, curbside, through-bolted to the top
  rail.** Not contested; remains the committed deliverable for July (coordinate
  top-rail real estate with solar-mount run).

## Net effect on the draft
The cross-examination tightened the envelope plan toward **measurement-gated,
defer-where-July-doesn't-need-it** decisions: one framed window or none; HRV and
diesel both rough-in-now/defer-unit; awning stands. No settled item (foam,
elastomeric roof, 48VDC Velit AC) was relitigated.
