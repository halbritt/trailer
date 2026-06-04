---
schema_version: striatum.synthesis.v1
artifact_kind: synthesis
author: operator
inputs:
  - claude_design
  - codex_design
  - gemini_design
  - design_review_claude
  - design_review_codex
  - design_review_gemini
---

# Design synthesis — bus / fridge / awning / doc divorce (REVISED, cycle 2)

Revision after interrogation round 1. Codex's material finding is upheld: **the original solar/awning roof-coexistence claim was false** — two LG455s consume 82.0–83.1" of the 84" roof width at their rows (portrait pair 2×41.02"=82.04"; landscape 83.07"), leaving ~1–2" total slack, **not** a 21" curbside strip. Decision 3 is re-architected accordingly. Claude's and gemini's accept-with-findings are folded in (converter margin language, thermal gate, lid-hinge check, full doc maps).

## Decisions

### 1. DC house bus — **single 24 V house bus; delete the 48→12 V converter** (unanimous; owner's lean confirmed)
- **Converter: Victron Orion-Tr 48/24-16A (380 W) isolated**, nose cabinet, **remote on/off to a cabin toggle**.
- **Margin honesty (per codex):** 16 A is sized for the **current** July loads. Realistic simultaneous worst case is ~12–15 A (fridge 4.6 A + lighting to its 5 A branch + USB-C PD at full 60–120 W profiles), not the earlier "9.6 A / >60% margin" claim. **D006 must carry the condition:** a future 24 V diesel heater (~8–10 A glow) reopens converter sizing — parallel a second Orion-Tr, upsize, or glow-window load-shedding.
- **48 V-side protection:** Blue Sea 7443 20 A UL-489 (80 V-class) breaker ahead of the converter; **no 32 V automotive fuse gear anywhere on the 48 V side**. **Implementation protection schedule (required, per codex):** feed-conductor gauge/ampacity, converter output overcurrent, breaker DC interrupt rating sanity vs pack fault current, and a correctly rated dedicated fuse/breaker on the Velit 48 V branch.
- **24 V distribution:** Blue Sea 5026 (32 V rating valid only on the regulated 24 V side). Rail map unchanged: fridge 10 A/14 AWG, Yuji zones 5 A, Scanstrut SC-USB-F3 7.5 A, GPS 3 A, door switch dry-contact; rare 12 V-only fixtures on point-of-load 24→12 bucks.
- **Tow-vehicle 12 V (7-way: running/marker/brake) is never a house load** — fully isolated.

### 2. Fridge — **integrate the purchased Dometic CFX3 95DZ on the 24 V bus** (settled by purchase)
- 24 V native (4.6 A ≈ 110 W compressing), 10 A fuse, 14 AWG.
- **Placement: floor, curbside, immediately aft of the personnel door — with a THERMAL GATE (per codex):** the bay must be **ventilated and shaded, away from the AIO nose-cabinet heat plume**; the unit's ceiling is 110 °F ambient and dual-zone setpoints constrain above 86 °F. Not just an E-track strap detail.
- **Lid-hinge orientation check (per claude):** verify which way the split lids hinge before fixing the bay orientation against the wall.
- Energy: ~1.0–1.3 kWh/day in July heat; camp total ≈ 4.1–4.45 kWh/day vs ~4.0 kWh/day roof-only solar — **the deployable 2S ground pair is required margin, not optional**, on AC-heavy days; ECO/off discipline stands.
- Bike coexistence: side-by-side roadside, staggered chocks 12–18"; ~30" center aisle clears the 20.9" fridge depth.

### 3. Awning — **Fiamma F45s 350 (06280B01R), mounted on FABRICATED RISER BRACKETS at the curbside roof edge** (re-architected; roof-adapter mount is dead)
- **Why the change:** the corrected math kills the flat-roof-adapter plan — the panels own the roof width; there is no curbside roof strip. Wall-mount remains dead per gemini's door geometry (case 5.35" vs ~4.5" clear above the door; deployed fabric fouls the swing).
- **The mount:** owner-fabricated **steel riser brackets** (this build has metal-fab capability — see the mission doc) rising from the **aluminum top rail / wall top plate into backed structure**, holding the F45s case **at or above the roofline (case bottom ≥ ~78.5")**. This satisfies the same door-swing math as the roof mount (fabric ≥ ~72.9" at the 32" swing radius at 10° pitch) while consuming **zero roof width**.
- **Load path (required engineering, per codex):** bracket count/spacing along the 138" case, fastener size, wall-side backing plates spanning studs/top plate, and design against **deployed wind + tie-down loads** (not just the 55 lb static case). Tie-downs: Fiamma Tie Down S (98655-133) to 3/8"×12" lag anchors / deadman bags. De-rig discipline: wound in before sleep, departure, or gusts >20 mph.
- **Pass/fail measurement gates BEFORE fabrication (per claude+codex):** (a) exact door-trim height above the 72" cutout; (b) roofline/rail section + backing at the curb edge; (c) a **single measured roof drawing** placing both panels, panel rails/clamps, roof bows, riser brackets, and the door swing; (d) a **deployed-fabric vs open-door check at actual pitch**. If the gates fail → fallback: **freestanding/portable shade (Moonshade-class)** anchored to trailer + ground, zero trailer structure.
- **Top-rail contention re-opens and re-closes correctly:** the rail is the awning's (via risers); the panels own the roof field; nothing shares an edge without the measured drawing.

### 4. Doc divorce — execute per the **FULL section-by-section maps** in the codex and gemini passes
Split into `docs/build/{power,climate,interior,systems}.md` + slim index. **Implement must follow `runs/juplaya-design-panel/design_codex/codex_design.md` §"Decision 4" and `runs/juplaya-design-panel/design_gemini/gemini_design.md` §"Doc Divorce Map" (the complete tables), not this summary** (per codex: the compressed map omits the target-date framing, recommendations provenance, use-case split, E-track footage note, accessories detail, and measurement splits). Verbatim-move-first; re-derive section anchors against the **current** doc at execution time (it gained the fridge-purchase rewrite after the maps were drawn); zero content loss verified in round 2.

## Disagreements ruled (updated)
1. Converter: **Victron Orion-Tr 48/24-16A** (remote off, enclosed) — with the margin condition above. Mean Well RSD-500C the budget alternate.
2. Awning mount: codex wall/top-rail ✗ (door geometry) · gemini roof-adapter ✗ (panel width math) → **raised riser brackets at the rail/roof edge**, measurement-gated, freestanding fallback.
3. Fridge: settled by purchase (CFX3 95DZ); integration above.
4. Cold-Voc shorthand: 2S Voc ≈ 116.7 V @ −40 °C nominal, ~122.6 V with +5% tolerance — under the 145 V max.

## Parts list (order long-lead now)
Victron Orion-Tr 48/24-16A · Blue Sea 7443 (80 V, 20 A) · Blue Sea 5026 (24 V side) · Fiamma F45s 350 06280B01R · Fiamma Tie Down S 98655-133 + lag anchors + deadman bags · riser-bracket steel stock + backing plate stock (owner fab) · Scanstrut SC-USB-F3 · 14 AWG runs + fuse assortment + POL 24→12 bucks. *(Dropped: Fiamma flat-roof adapters 98655-316 — dead with the roof mount.)*

## Hand-offs
- Implement: doc divorce per the full maps; D006 (24 V bus + converter condition), D007 (awning riser-mount, measurement-gated, fallback named), D008 (fridge integration + thermal gate) as `proposed`.
- Measurement pass: the four awning gates + fridge-bay ventilation check + lid-hinge orientation.
- Interior plan: staggered chocks, fridge bay, panel transport slot.
