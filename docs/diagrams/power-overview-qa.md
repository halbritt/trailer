# Power Overview TikZ QA

Date: 2026-06-07

Artifacts:

- `docs/diagrams/power-overview.tex`
- `docs/diagrams/power-overview.pdf`
- `docs/diagrams/power-overview.png`
- `docs/diagrams/power-overview-visual-qa.json`
- `docs/diagrams/power-lead-calculations.tex`
- `docs/diagrams/power-lead-calculations.pdf`
- `docs/diagrams/power-lead-calculations-1.png`
- `docs/diagrams/power-lead-calculations-2.png`
- `docs/diagrams/power-lead-calculations-3.png`

Sources checked:

- `docs/power.md`
- `docs/diagrams/power-overview.svg`
- `docs/diagrams/power-solar-strings.svg`
- `docs/DECISION_LOG.md` D002 and D006
- `docs/juplaya-trailer-context.md`

Checks:

- Static TikZ safety: pass.
- Overview compile/render: pass with `xelatex` through the `tikz-diagrams` `compile_render.py` helper.
- Rendered visual QA: pass in research mode.
- Calculation sheet compile: pass with `latexmk -xelatex`.
- Calculation sheet page renders: pass with `pdftoppm`; pages inspected manually.
- Manual PNG inspection: no severe text overlap, clipping, blank output, route crossing through labels, table clipping, or slide-fit failure found after the final render.

Design critique outcome: keep.

Math/diagram logic review: schematic for topology; exact arithmetic within stated assumptions for the lead-current and voltage-drop worksheet.

Model or equations: no plotted equations or scale geometry. Numeric labels are sourced planning estimates from `docs/power.md` and local reference notes. Voltage-drop rows use \(V_{drop}=2LI R_T/1000\) with copper resistance corrected to 75 C.

Checked invariants:

- Roof 3S LG array lands only on SmartSolar 250/60-Tr.
- Optional LG ground 2S lands only on SmartSolar 150/35.
- PS400 feeds only the Anker SOLIX C1000 island.
- LiTime ComFlex remains the 48 V battery/bus anchor.
- Velit 2000R stays on a 48 V DC branch.
- Orion-Tr 48/24 feeds the 24 V house loads.
- Orion-Tr IP43 48/12 feeds only auxiliary 12 V cabinet receptacles.
- C1000 top-up is represented as optional/discretionary from the 24 V side and capped at 240 W.
- Lead-current labels distinguish PV string current from MPPT battery-side output current.
- The 24 V bus is represented as converter-limited at 16 A; optional C1000 top-up, full-flood mode, full USB-C load, and heater glow are not treated as simultaneous steady loads.

Schematic limits:

- This is a topology and energy-context diagram, not a wiring schematic.
- The calculation sheet proposes planning conductor sizes from assumed run lengths; it does not finalize wire gauges, disconnects, fuse part numbers, breaker SKUs, insulation class, terminal temperature limits, bundling derates, or connector variants.
- kWh/day labels are Black Rock July clean-sun planning estimates; dust, shade, heat, and runtime change actual yield and draw.
- SmartScan remains TBD/measure; no undocumented draw was invented.
- Exact cable run lengths remain placeholders until the measured roof/cabinet/interior routing is fixed.
