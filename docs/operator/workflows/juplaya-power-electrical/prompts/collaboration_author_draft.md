# Author draft — Power / electrical

Draft the recommendations and **stay live for cross-examination** — publication is gated by the adjudicator's collaboration ledger.

Resolve each open question with **one committed recommendation** (not an option list), a one-line rationale, and the spec/constraint it depends on. Flag anything needing a physical measurement or a purchase.

1. **Solar count & string** — current direction is roof 3× LG455N2W-E6 (455 W) in 3S to Victron SmartSolar 250/60-Tr, plus optional deployable 2S ground pair to SmartSolar 150/35. Re-check only if new measurements or parts change the premise.
2. **Solar mounting** — flat aluminum roof with discrete roof bows; current direction is fore-aft NXT rails tied into multiple roof bows with backing/crush control. Recommend any needed corrections to that mounting approach.
3. **48V->12V converter** — needed? sizing?
4. **12V load list** — enumerate the real 12V loads (strip lights are 24V; AC is 48V).
5. **Lighting** — 24V LED strips (Yuji) in Klus extrusions/diffusers; confirm bus design + any 12V (awning).
6. **Wiring diagram** — bus/wiring plan across 48V (AC+charging), 24V (lighting), any 12V.
7. **Truck charging** — high-current line from the 2021 F-150 (EcoBoost, Max Tow) to charge the 48V pack while towing; spec the 12V->48VDC charger, wire gauge, protection.

**Sources:** `docs/juplaya-trailer-context.md` (context + open questions), `docs/reference/fastrac-specs.md` and `docs/reference/wells-cargo-ft712s2-d-work-order.md` (confirmed specs), and `docs/trailer-mission.md` (the north star — design for reconfigurability / E-track-as-OS across the mission profiles where it's cheap to, even though the current target is the Juplaya moto basecamp).

**Constraints:** 48 V LiTime ComFlex pack (5.12 kWh), Victron MPPT/DC distribution path, built-in inverter deferred for Juplaya, Anker C1000 + PS400 small-AC island; single axle, payload will be weighed (don't optimize against a guessed budget); measured interior 81" W x 156" centerline L x 6'6"; ready for Juplaya ~July 4 2026.
