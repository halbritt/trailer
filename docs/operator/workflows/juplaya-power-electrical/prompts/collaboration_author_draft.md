# Author draft — Power / electrical

Draft the recommendations and **stay live for cross-examination** — publication is gated by the adjudicator's collaboration ledger.

Resolve each open question with **one committed recommendation** (not an option list), a one-line rationale, and the spec/constraint it depends on. Flag anything needing a physical measurement or a purchase.

1. **Solar count & string** — 2-4x LG455N2W-E6 (455 W) on the flat roof; whether 3 in series (3s) fits the LiTime 48V AIO's MPPT window. Recommend count + series/parallel.
2. **Solar mounting** — flat aluminum roof; owner wants to mount off the side of the aluminum top rail. Recommend a mounting approach.
3. **48V->12V converter** — needed? sizing?
4. **12V load list** — enumerate the real 12V loads (strip lights are 24V; AC is 48V).
5. **Lighting** — 24V LED strips (Yuji) in Klus extrusions/diffusers; confirm bus design + any 12V (awning).
6. **Wiring diagram** — bus/wiring plan across 48V (AC+charging), 24V (lighting), any 12V.
7. **Truck charging** — high-current line from the 2021 F-150 (EcoBoost, Max Tow) to charge the 48V pack while towing; spec the 12V->48VDC charger, wire gauge, protection.

**Sources:** `docs/juplaya-trailer-context.md` (context + open questions), `docs/fastrac-specs.md` and `docs/wells-cargo-ft712s2-d-work-order.md` (confirmed specs), and `docs/trailer-mission.md` (the north star — design for reconfigurability / E-track-as-OS across the mission profiles where it's cheap to, even though the current target is the Juplaya moto basecamp).

**Constraints:** 48V LiTime stack (AIO in the nose cabinet, 5.12 kWh); single axle, payload will be weighed (don't optimize against a guessed budget); interior 81" W x 157" L x 6'6"; ready for Juplaya ~July 4 2026.
