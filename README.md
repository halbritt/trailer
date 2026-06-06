# Trailer

Build repo for a **Wells Cargo / ACG FasTrac Deluxe FT712S2-D** (7×12 single-axle, VIN 7V0W11214TU444163) being fitted out as a reconfigurable off-grid platform — moto basecamp first. **Target: ready for Juplaya, ~July 4 2026.**

> The E-track grid is the operating system; the interior is software. — [trailer-mission.md](docs/trailer-mission.md)

## Start here

| Doc | What it is |
|---|---|
| **[Build sheet](docs/juplaya-trailer-context.md)** | **Source of truth** — settled facts, every decision, every binding gate, order lists |
| [Order sheet](docs/order-sheet.md) | Purchase status, remaining buys, price signals, and fit-out budget math |
| [Dimension sheet](docs/dimensions.md) | All known dimensions + the mm measurement-pass fill-in table |
| [Decision log](docs/DECISION_LOG.md) | D001–D010 with context/consequences/revisit conditions |
| [Validation report](docs/research/build-decision-validation.md) | Web fact-check of the original 7 falsifiable decisions plus D010 flooring addendum |
| [Mission](docs/trailer-mission.md) | North star: mission profiles + what stays constant |

## Layout

```
docs/
├── juplaya-trailer-context.md   # the build sheet (source of truth)
├── dimensions.md                # dimension sheet + measurement pass
├── DECISION_LOG.md              # D001–D010
├── trailer-mission.md           # north star
├── reference/                   # distilled spec sheets + factory/purchase records
│   ├── fastrac-specs.md             # manufacturer line specs + derived FT712S2 column
│   ├── wells-cargo-…-work-order.md  # factory build sheet (VIN, options)
│   ├── litime-48v-3500w-aio-specs.md / …5kw…  # inverter/charger key specs
│   ├── litime-48v-100ah-battery-specs.md
│   ├── dometic-cfx3-95dz-specs.md
│   ├── lg455n2w-e6-datasheet.md
│   └── albritton-buyers-order-600485.pdf
├── research/                    # web-validation of the decisions (cited fact-check)
├── manuals/                     # manufacturer literature (PDFs + full conversions)
├── operator/workflows/          # striatum workflow definitions (decision runs)
runs/                            # frozen artifacts from the decision runs
```

## How decisions get made

Open questions are run through **striatum** multi-model workflows (claude / codex / gemini panels with cross-examination and revision cycles); accepted outcomes land as `DECISION_LOG` rows (`proposed` until the owner ratifies) plus **binding gates** in the build sheet. Raw drafts, reviews, and verdicts are preserved under `runs/`.

**Current state:** power architecture, solar, 24 V bus, fridge, awning, windows, wall substrate, roof coating, and flooring are decided or proposed (D001–D010 + window SKUs), now **web-validated** (2026-06-05 — see the [validation report](docs/research/build-decision-validation.md); 4/7 original decisions carried cautions folded into the gates, plus D010 flooring addendum). What "done" means for the design is now explicit — the **design-freeze checklist** in the [build sheet](docs/juplaya-trailer-context.md#design-freeze--definition-of-done) (10 items: ratifications, track heights, window stations, roof drawing, standoff design, floor plan, flooring, FRP trim, frozen order list), fed by the **[measurement pass](docs/dimensions.md#-measurement-pass--fill-in-mm-preferred-these-supersede-spec)**.
