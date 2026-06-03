# Design pass — full pass over the whole problem set

You are one of three models doing a **full pass in turn** (relay order: claude → codex → gemini/agy). If a predecessor draft exists under `runs/juplaya-design-panel/design_*/`, read it first, then do your own complete pass: keep what holds, correct what doesn't, extend what's thin. State explicitly what you changed and why.

**Read first:** `docs/juplaya-trailer-context.md` (Settled / Recommendations / Still open), `docs/DECISION_LOG.md` (D001–D005), `docs/trailer-mission.md`, and the spec sheets: `docs/litime-48v-3500w-aio-specs.md`, `docs/litime-48v-100ah-battery-specs.md`, `docs/lg455n2w-e6-datasheet.md`, `docs/fastrac-specs.md`, `docs/wells-cargo-ft712s2-d-work-order.md`.

**Resolve — one committed recommendation each (no option lists), with rationale + concrete parts:**
1. **DC house bus.** Owner LEANS **24 V** — treat that as the prior to confirm or overturn on merits. Loads: Yuji 24 V LED strips (committed), fridge (BD35-class compressors are 12/24 V auto-sensing), LandAirSea 54 GPS (12 V), door switch, USB-C PD outlets, possible awning accessories. Decide: bus voltage(s), which converter(s) exist (48→24? 48→12? both? neither beyond one), fuse block(s), and exactly which load lands on which rail. Kill the 48→12 question for good.
2. **Fridge.** A specific unit (~50–55 L DC compressor; D005 ruled out Midea-on-inverter) consistent with the bus decision. Model, price class, dimensions, mounting spot consistent with the interior plan.
3. **Awning.** Specific ~12 ft manual lateral-arm unit + top-rail mount + desert tie-down scheme. Curbside; must clear the 32"×72" personnel door; **hard deadline Juplaya ~July 4**; the top rail is uncontested (solar lives on roof-bow rails).

**Also propose the doc divorce:** split `docs/juplaya-trailer-context.md` into per-domain docs (e.g., `docs/build/power.md`, `climate.md`, `interior.md`, `systems.md`), specifying exactly what content moves where and what the remaining slim index keeps (settled trailer facts, links, standing preferences). No content may be lost.

**Constraints:** 48 V LiTime 3500W AIO (PV 60–145 V; idle <30 W ECO; charge cap ≤100 A), ComFlex 100 Ah pack, payload to-be-weighed (don't optimize against guesses), interior 81"×157"×78", owner style: terse, committed recommendations.

Write your full pass to your declared artifact path. Stay live for interrogation if asked.
