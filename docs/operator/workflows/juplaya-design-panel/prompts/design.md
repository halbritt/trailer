# Design pass — full pass over the whole problem set

You are one of three models doing a **full pass in turn** (relay order: claude → codex → gemini/agy). If a predecessor draft exists under `runs/juplaya-design-panel/design_*/`, read it first, then do your own complete pass: keep what holds, correct what doesn't, extend what's thin. State explicitly what you changed and why.

**Read first:** `docs/juplaya-trailer-context.md`, `docs/DECISION_LOG.md`, `docs/trailer-mission.md`, and the spec sheets under `docs/reference/`: `litime-48v-100ah-battery-specs.md`, `lg455n2w-e6-datasheet.md`, `dometic-cfx3-95dz-specs.md`, `fastrac-specs.md`, and `wells-cargo-ft712s2-d-work-order.md`.

**Resolve — one committed recommendation each (no option lists), with rationale + concrete parts:**
1. **DC house bus.** Owner LEANS **24 V** — treat that as the prior to confirm or overturn on merits. Loads: 24 V lighting, purchased Dometic CFX3 95DZ fridge, ordered LandAirSea Overdrive GPS, door switch, USB-C PD outlets, possible awning accessories, and cabinet-only auxiliary 12 V receptacles. Decide bus voltage(s), converter(s), fuse block(s), and exactly which load lands on which rail.
2. **Fridge integration.** Purchased unit is Dometic CFX3 95DZ. Resolve bus assignment, bay placement, lid access, ventilation, and daily energy budget consistent with the interior plan.
3. **Awning.** Specific ~12 ft manual lateral-arm unit + fabricated perimeter-rail standoff mount + desert tie-down scheme. Curbside; must clear the 32"×72" personnel door; **hard deadline Juplaya ~July 4**; roof solar lives on roof-bow rails.

**Also propose the doc split:** keep `docs/juplaya-trailer-context.md` as the source-of-truth index and move detailed domain material into existing peer docs such as `docs/power.md` and `docs/solar_mounting.md`, plus possible new peer docs for climate, interior, and systems. Specify exactly what content moves where and what the remaining slim index keeps (settled trailer facts, links, standing preferences). No content may be lost.

**Constraints:** 48 V LiTime ComFlex 100 Ah pack; roof 3× LG455 in 3S through Victron SmartSolar 250/60-Tr; optional LG ground pair through SmartSolar 150/35; built-in inverter/charger deferred for Juplaya in favor of Anker C1000 + PS400; combined trailer charge cap ≤100 A; payload to-be-weighed (don't optimize against guesses); measured interior 81" W × 156" centerline L × 78" H; owner style: terse, committed recommendations.

Write your full pass to your declared artifact path. Stay live for interrogation if asked.
