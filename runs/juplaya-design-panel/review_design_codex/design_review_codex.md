---
schema_version: striatum.finding.v1
artifact_kind: finding
verdict_intent: accept
author: operator
---

# Design review - Codex cycle 2

## Verdict rationale

The revised synthesis discharges the six cycle-1 findings. The previous blocker was not the existence of unresolved field measurements; it was that the synthesis asserted false roof-width clearance and treated a roof-adapter awning mount as settled. That claim is now explicitly withdrawn, the mount is re-architected around riser brackets that consume zero roof field, and the remaining unknowns are correctly expressed as pass/fail gates before fabrication or implementation.

## Prior findings verification

1. **Solar / awning roof-width math and mount architecture - discharged.**

The revision explicitly accepts that the original coexistence math was false: two LG455 panels consume 82.04" in a portrait pair or 83.07" in landscape on the 84" roof, leaving only about 1-2" total slack, not a 21" curbside strip. That matches the local LG sheet dimensions and the 7 ft trailer-width docs.

Decision 3 no longer depends on flat roof adapters or an imagined curbside roof strip. It moves the F45s to fabricated steel riser brackets at the curbside roof edge, rising from the aluminum top rail / wall top plate into backed structure, with the case at or above the roofline and consuming zero roof width. The required pre-fabrication gates now include door-trim height, curb-edge roofline/rail section and backing, a single measured roof drawing placing both panels/rails/clamps/roof bows/riser brackets/door swing, and an actual deployed-fabric/open-door check. The freestanding Moonshade-class fallback is named if those gates fail. This closes the material cycle-1 defect.

2. **Converter margin language and D006 condition - discharged.**

The revision removes the prior ">60% margin" claim as a general statement. It now states the Victron Orion-Tr 48/24-16A is sized for current July loads, gives the more honest ~12-15 A simultaneous range, and carries the D006 condition that a future 24 V diesel heater glow load reopens converter sizing through a second Orion, upsize, or load shedding. That is the needed distinction between "feasible now" and "not future-proof by assertion."

3. **48 V protection schedule - discharged for synthesis.**

The revision preserves the correct rule that the Blue Sea 5026 belongs only on regulated 24 V and that no 32 V automotive fuse gear belongs on the 48 V side. It also makes the protection schedule required implementation content: feed conductor gauge/ampacity, converter output overcurrent, breaker DC interrupt-rating sanity against pack fault behavior, and a correctly rated dedicated Velit 48 V branch fuse/breaker. That is enough for a design synthesis; the actual values belong in implementation drawings or D006 details.

4. **Fridge thermal gate - discharged.**

The CFX3 95DZ integration now names the thermal gate directly: the curbside floor bay aft of the door must be ventilated and shaded, away from the AIO nose-cabinet heat plume, with the 110 F ambient ceiling and above-86 F dual-zone behavior carried forward. The lid-hinge orientation check is also included. The fridge placement is no longer just an E-track strap detail.

5. **Awning door clearance and load-path rigor - discharged.**

The revision keeps the roofline-height door-swing logic but stops treating the small clearance as casual margin. It requires actual-pitch deployment verification before drilling. It also moves beyond static case weight by requiring bracket count/spacing along the 138" case, fastener size, wall-side backing plates spanning studs/top plate, and design against deployed wind plus tie-down loads. The Fiamma Tie Down S anchoring and de-rig discipline are carried forward as operating constraints.

6. **Doc split binding to full maps - discharged.**

The doc-divorce decision now explicitly binds implementation to the full section-by-section maps in `runs/juplaya-design-panel/design_codex/codex_design.md` and `runs/juplaya-design-panel/design_gemini/gemini_design.md`, not the shortened synthesis paragraph. It specifically names the areas the short summary omitted in cycle 1: target-date framing, recommendations provenance, use-case split, E-track footage note, accessories detail, and measurement splits. It also requires verbatim-move-first and re-deriving anchors against the current context doc. That resolves the content-loss risk at the synthesis level.

## Residual implementation gates

The remaining risks are now correctly scoped as implementation gates rather than synthesis defects: awning measurement/fabrication pass, electrical protection schedule values, fridge bay ventilation check, and D006/D007/D008 decision-log capture. None of those require another synthesis revision before implementation can proceed.

VERDICT: accept
