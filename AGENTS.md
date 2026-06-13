# AGENTS.md — orientation for agents working this repo

## Operators: start here

**If you've been named an operator** — i.e. you are driving striatum workflows
against this repository, not just editing its files — do not improvise a cold
start. Run the striatum operator initialization first:

```bash
striatum operator bootstrap --markdown
```

Then follow the returned `next_actions` and bounded `reading_plan` before
opening broad repository docs. Use `--json` instead of `--markdown` when another
tool will consume the packet. This needs the striatum daemon running and this
repository registered as a striatum target.

If you are already inside a supervised lane holding a work packet, that packet
and the installed RFC 0015 skill bundle (`.claude/skills/striatum-*/`,
`.codex/agents/striatum-*.md`, `.agy/skills/striatum-*/`, or
`striatum-STRIATUM_AGENT_GUIDE.md`) are authoritative — prefer their command
shapes over anything here. The long-form companion is
`docs/how-to/how-to-agent.md` in the striatum repo.

Build repo for a **Wells Cargo / ACG FasTrac Deluxe FT712S2-D** (7×12 single-axle cargo trailer, VIN 7V0W11214TU444163) being fitted out as a reconfigurable off-grid platform. **Hard deadline: Juplaya, ~July 4 2026.** This is a docs-first engineering repo — markdown build sheets, decision records, and a few generator scripts. There is no application code.

## Hard rules

1. **Commit and push to `origin/main` after every change. No batching.** The owner is remote and reviews exclusively through GitHub; unpushed work is invisible. Descriptive commit messages — they are the owner's changelog.
2. **Never hand-edit generated files.** `docs/order-sheet.md` and `docs/order-sheet.csv` are produced by `scripts/sync_order_sheet.py` from a Google Sheet plus `docs/order-sheet-overrides.csv` — put corrections in the overrides CSV and re-run the script. `docs/reference/juplaya-power-diagram.json` is produced by `scripts/generate_juplaya_power_diagram_json.py`. Diagrams under `docs/diagrams/` build from their `.tex` sources.
3. **Gates govern ordering and building.** Items marked `BUY AFTER GATE` wait for their gate to close. When a gate changes, update `docs/gate-tracker.md` **first**, then propagate. Don't release a gated buy because it seems ready — the gate row says what closes it.
4. **Decisions are D-numbered and owned.** Substantive design choices go through striatum multi-model panels (see below) and land as `docs/DECISION_LOG.md` rows — `proposed` until the owner ratifies. Never silently reverse a decided item; if evidence contradicts one, say so and flag its revisit condition.
5. **Measured values supersede spec.** New measurements go in the `docs/dimensions.md` measurement-pass table (mm preferred, record both), then propagate to the roof drawing, gates, and affected build docs. Dates are absolute (YYYY-MM-DD).
6. **Treat `runs/` as frozen.** They are the preserved artifacts (drafts, cross-examinations, verdicts) behind decisions — append new runs, don't rewrite old ones.

## Source-of-truth map

| Doc | Role |
|---|---|
| `docs/juplaya-trailer-context.md` | **The build sheet.** Settled facts, all decisions, binding gates, design-freeze checklist. Start here. |
| `docs/gate-tracker.md` | Live gate status (measurement, decision, build-phase, deferred). Update first on any gate change. |
| `docs/dimensions.md` | Every known dimension + the measurement-pass fill-in table. |
| `docs/DECISION_LOG.md` | D001–D012: decision, context, consequences, revisit conditions. |
| `docs/order-sheet.md` / `.csv` | Purchase ledger + budget math. **Generated** — edit `order-sheet-overrides.csv`, run `scripts/sync_order_sheet.py`. |
| `docs/power.md` | 48 V → 24 V/12 V power architecture, protection schedule, lighting/switching. |
| `docs/solar_mounting.md` | Roof solar mounting spec (NXT rails on roof bows). Order sheet: `docs/solar-mounting-order-sheet.md`. |
| `docs/trailer-mission.md` | North star: mission profiles, what stays constant. |
| `docs/reference/` | Distilled spec sheets, factory work order, purchase records. |
| `docs/manuals/` | Manufacturer literature (PDFs + markdown conversions). |
| `docs/research/` | Cited web fact-checks of decisions. |
| `docs/operator/workflows/` + `runs/` | striatum panel definitions and their frozen artifacts. |

## How decisions get made

Open design questions run through **striatum** multi-model panels (claude/codex/gemini authors with cross-examination and revision cycles). Use the `run-trailer` skill to start, drive, or recover a panel run; the striatum daemon is `striatumd` on the workstation. Accepted outcomes land as DECISION_LOG rows plus binding gates in the build sheet; raw artifacts freeze under `runs/<workflow>/`.

## Working conventions

- Owner style: terse, decisive, one committed recommendation — not option menus.
- A typical change flows: measurement or finding → `dimensions.md` / research doc → `gate-tracker.md` → affected build docs → DECISION_LOG if a decision moved → commit + push.
- Budget discipline: `extended_price` on counted `LINE` rows is the budget field; keep high-side estimates until a real receipt replaces them.
- Inches are the build unit in docs; the measurement pass prefers mm. Keep both where ambiguity hurts.
- The LiTime 5 kW AIO is a **return item** — do not design it back in. The built-in inverter/charger is deferred for Juplaya (D002).
