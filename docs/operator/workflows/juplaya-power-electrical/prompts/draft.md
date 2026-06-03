# Draft — Power / electrical decisions

Resolve each open question:

1. **Solar count & string** — 2-4x LG455N2W-E6 (455 W) on the flat roof; determine whether 3 in series (3s) fits the LiTime 48V AIO's MPPT voltage window. Recommend a panel count + series/parallel config.
2. **Solar mounting** — flat aluminum roof; owner wants to mount off the *side of the aluminum top rail*. Recommend a mounting approach (rail/bracket/standoff, sealing, no roof penetration if avoidable).
3. **48V->12V converter** — is one needed? If so, size it to the 12V loads.
4. **12V load list** — enumerate the real 12V loads (note: strip lights are 24V; AC is 48V).
5. **Lighting** — 24V LED strips (Yuji) in Klus extrusions/diffusers; confirm the bus design and any 12V (awning) needs.
6. **Wiring diagram** — produce a bus/wiring plan across 48V (AC + charging), 24V (lighting), and any 12V.
7. **Truck charging** — high-current line from the 2021 F-150 (EcoBoost, Max Tow) to charge the 48V pack while towing; spec the 12V->48VDC charger, wire gauge, and protection.

**Sources:** read `docs/juplaya-trailer-context.md` (context + open questions) and the confirmed specs in `docs/fastrac-specs.md` + `docs/wells-cargo-ft712s2-d-work-order.md`.

**Output:** write `runs/juplaya-power-electrical/DRAFT.md`. For EACH question give **one committed recommendation** (not an option list — see the owner's standing preferences), a one-line rationale, the spec/constraint it depends on, and flag anything needing a physical measurement or a purchase.

**Global constraints:** 48V LiTime stack (5kW AIO in the nose cabinet, 5.12 kWh battery); single axle, payload will be weighed (do not optimize against a guessed budget); interior 81" W x 157" L x 6'6" tall; ready for Juplaya ~July 4 2026.
