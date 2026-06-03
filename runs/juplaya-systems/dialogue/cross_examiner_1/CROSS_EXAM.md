---
title: Systems / gear cross-examination (OUT-OF-BAND)
author: cross_examiner
kind: handoff
date: 2026-06-03
run_id: run_5b03c224aa588d85eb949f5bd4dee3cc
status: out-of-band-interrogation
---

# Cross-examination — Systems / gear DRAFT.md

**OUT-OF-BAND NOTICE.** This interrogation was NOT driven through striatum. The
`cross_examiner_1` job (lane `agy`) was `blocked` and unclaimable because the
upstream `author_draft` job could not be `completed` — `work.complete` failed a
whole-working-tree write_scope check that flagged the three SIBLING runs'
DRAFT.md files (climate, interior, power-electrical) as "outside scope" even
though they belong to the other concurrent runs and my own artifact was already
published cleanly. Because striatum blocked the lane, the interrogation was run
directly via `agy --dangerously-skip-permissions --print` against the published
DRAFT.md, per the run's documented contingency. The verdict below is advisory;
it was NOT recorded as a striatum review verdict.

Tool: `agy` 1.0.4 (Antigravity / Gemini). Single-pass simulated 4-turn red-team.

---

## What the interrogation surfaced (load-bearing)

1. **Three-voltage DC spaghetti (strongest hit).** The recommended BD35-class
   fridges (Dometic CFX3, ICECO VL60) are natively **12V/24V auto-sensing**.
   The build already needs a 24V bus for the Yuji lighting. agy argues the
   48→12V converter can be DELETED: run the fridge + USB-C + GPS + dome lights
   off the existing 24V bus, removing a whole DC-DC converter, its idle draw,
   its fuse block, and a failure point. This directly attacks the draft's
   "buy 12V NOT 24V" call and the entire 12V-house-bus premise.

2. **Inverter idle paradox.** A 5kW low-frequency AIO idles ~50–70W (~1.2–1.7
   kWh/day) — 25–33% of the single 5.12 kWh pack — and may not keep MPPT active
   while the inverter sleeps. With zero committed 120VAC loads (AC is 48VDC,
   fridge/lights are DC), the AIO is questioned as overkill. (Note: this is
   really a power-electrical-run issue, but it changes the fridge calculus.)

3. **Nose-cabinet tongue weight + sway.** ~200 lb of electrical (AIO + battery
   + converters) at the extreme nose spikes tongue weight on a single axle;
   compensating by loading cargo rearward lowers polar moment and invites
   high-speed sway. (Cross-domain: interior/power, but the fridge + 12V gear
   add nose mass.)

4. **Juplaya thermal.** Battery BMS cutoff ~113–122°F vs ~105°F ambient in a
   closed nose cabinet; venting depends on running the AC, which drains the
   pack. Thermal-shutdown spiral risk.

## agy verdict (advisory, out-of-band)
- **Q17 Fridge — CONCEDED WEAKNESS.** "Buy 12V not 24V" is wrong if it forces a
  second converter; BD35 fridges are 12/24V auto-sensing. Correction: run the
  fridge on the existing 24V bus and consider deleting the 48→12V converter.
- **Q18 Accessories — PARTIALLY HOLDS.** Security (Proven 2516, Abloy keyed-
  alike, Trimax TCL65) and GPS hardwire HOLD. Electrical distribution should be
  re-pinned to whichever house bus survives (24V vs 12V) — i.e. the bus choice
  is contingent on the converter question, which is itself contingent on the
  power-electrical run.

## Author's likely rebuttal (recorded for the adjudicator, not conceded)
- The 24V-fridge path is genuinely strong IF the BD35 unit's 24V mode is on its
  spec sheet AND the 24V lighting bus has continuous-current headroom for a
  fridge (lighting is a low-amp bus; a fridge adds a sustained ~0.5A@24V plus
  startup surge — verify the 24V source/converter can carry it). If yes, the
  draft should be revised to 24V and the 48→12V converter re-evaluated.
- The 12V vs 24V outlet/accessory market point cuts both ways: many sockets are
  12V-only; auto-sensing 12/24V USB exists but is less common. Net: the bus
  decision is a real open seam that belongs to the power-electrical run.

## Net for adjudication
The fridge DC-vs-Midea call (the draft's stated load-bearing decision) HOLDS —
nobody argued for the Midea-on-inverter path. What does NOT hold is the
secondary "12V not 24V" sub-call: it should flip to 24V (or stay 12V only if
the power run keeps a 48→12V converter for other reasons). Recommend the draft
be revised to (a) make the fridge bus contingent on the power-run converter
decision, and (b) commit to 24V if no independent 12V converter is justified.
