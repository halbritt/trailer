# Author draft — Systems / gear

Draft the recommendations and **stay live for cross-examination** — publication is gated by the adjudicator's collaboration ledger.

Resolve each open question with **one committed recommendation** (not an option list), a one-line rationale, and the spec/constraint it depends on. Flag anything needing a physical measurement or a purchase.

1. **Fridge** — DC-compressor unit (48/24/12 VDC) vs small Midea on the inverter (idle-load tradeoff). Account for the 48V system + off-grid Juplaya use.
2. **Accessories ordering list** — concrete order list. Current direction: ordered LandAirSea Overdrive GPS hardwired to the 24 V block, Proven 2178 for the 2" coupler, keyed-alike PACLOCK UCS-7A pucks, Trimax TCL65 boot, Blue Sea 5026, cabinet-only 12 V receptacles, USB-C PD, and 24 V lighting. Specific parts + quantities.

**Sources:** `docs/juplaya-trailer-context.md` (context + open questions), `docs/reference/fastrac-specs.md` and `docs/reference/wells-cargo-ft712s2-d-work-order.md` (confirmed specs), and `docs/trailer-mission.md` (the north star — design for reconfigurability / E-track-as-OS across the mission profiles where it's cheap to, even though the current target is the Juplaya moto basecamp).

**Constraints:** 48 V LiTime ComFlex pack (5.12 kWh), Victron MPPT/DC distribution path, built-in inverter deferred for Juplaya, Anker C1000 + PS400 small-AC island; single axle, payload will be weighed (don't optimize against a guessed budget); measured interior 81" W x 156" centerline L x 6'6"; ready for Juplaya ~July 4 2026.
