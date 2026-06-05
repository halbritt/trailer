# AIO Inverter/Charger Adversarial Review

You are reviewing D002, the current power-source decision:

> AIO = LiTime 48 V 3500 W; the mistakenly ordered 5 kW LiTime unit is returned. Solar = roof 2 x LG455 in 2S plus deployable ground 2S pair into 2S2P when camped. No external MPPT. Commissioning caps total charge <=100 A.

The owner is about to buy the replacement and asks whether something else should be considered, especially if three LG455 panels can fit on the roof with the Velit 2000R AC and a 3S-capable inverter/charger would be useful.

Read:

- `docs/juplaya-trailer-context.md`
- `docs/DECISION_LOG.md`
- `docs/dimensions.md`
- `docs/research/build-decision-validation.md`
- `docs/research/aio-inverter-evidence-2026-06-05.md`
- `docs/reference/litime-48v-3500w-aio-specs.md`
- `docs/reference/litime-48v-5kw-aio-specs.md`
- `docs/reference/litime-48v-100ah-battery-specs.md`
- `docs/reference/lg455n2w-e6-datasheet.md`

Your assigned posture is in the job objective. Argue from that posture and try to break the current D002 recommendation.

Explicitly evaluate:

- LiTime 48 V 3500 W AIO
- keeping/repurchasing LiTime 48 V 5 kW AIO
- EG4 3000EHV-48 or similar 120 V-min high-voltage AIO
- Victron MultiPlus-II + SmartSolar 250-class MPPT
- LiTime 3500 W plus separate 250 V-class MPPT if three roof panels prove real

Score each viable candidate on:

- roof-only solar harvest if three panels fit
- PV voltage safety and hot-roof MPPT floor margin
- single 48 V 100 Ah battery compatibility
- idle draw / ECO discipline
- AC output fit for actual loads
- wiring/protection complexity and deadline risk
- weight/nose-cabinet fit/heat
- vendor/support/return risk
- total cost and order timing

Output:

1. Recommended architecture and exact next purchase.
2. Whether the mistaken 5 kW LiTime should still be returned.
3. Whether 3 roof panels should change the inverter decision.
4. Strongest counterargument to your recommendation.
5. Required gates or install notes.
6. One-line verdict for D002: keep, revise, or reopen.
