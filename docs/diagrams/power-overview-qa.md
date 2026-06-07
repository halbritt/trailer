# Power Overview TikZ QA

Date: 2026-06-07

Artifacts:

- `docs/diagrams/power-overview.tex`
- `docs/diagrams/power-overview.pdf`
- `docs/diagrams/power-overview.png`
- `docs/diagrams/power-overview-visual-qa.json`

Sources checked:

- `docs/power.md`
- `docs/diagrams/power-overview.svg`
- `docs/diagrams/power-solar-strings.svg`
- `docs/DECISION_LOG.md` D002 and D006
- `docs/juplaya-trailer-context.md`

Checks:

- Static TikZ safety: pass.
- Compile/render: pass with `xelatex` through the `tikz-diagrams` `compile_render.py` helper.
- Rendered visual QA: pass in research mode.
- Manual PNG inspection: no severe text overlap, clipping, blank output, route crossing through labels, or slide-fit failure found after the final render.

Design critique outcome: keep.

Math/diagram logic review: schematic.

Model or equations: no plotted equations or scale geometry. Numeric labels are sourced planning estimates from `docs/power.md`.

Checked invariants:

- Roof 3S LG array lands only on SmartSolar 250/60-Tr.
- Optional LG ground 2S lands only on SmartSolar 150/35.
- PS400 feeds only the Anker SOLIX C1000 island.
- LiTime ComFlex remains the 48 V battery/bus anchor.
- Velit 2000R stays on a 48 V DC branch.
- Orion-Tr 48/24 feeds the 24 V house loads.
- Orion-Tr IP43 48/12 feeds only auxiliary 12 V cabinet receptacles.
- C1000 top-up is represented as optional/discretionary from the 24 V side and capped at 240 W.

Schematic limits:

- This is a topology and energy-context diagram, not a wiring schematic.
- It does not specify final wire gauges, disconnects, fuse part numbers, breaker SKUs, or connector variants.
- kWh/day labels are Black Rock July clean-sun planning estimates; dust, shade, heat, and runtime change actual yield and draw.
- SmartScan remains TBD/measure; no undocumented draw was invented.
