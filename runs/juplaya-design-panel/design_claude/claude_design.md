---
author: operator
---

# Design pass — Claude lane (first full pass)

This is the first pass in the relay (claude → codex → gemini). No predecessor draft
exists; this is a clean derivation from the context doc, decision log, mission, and the
five spec sheets. I commit one recommendation per item, with rationale and concrete parts.

---

## Problem framing

The build is a 48 V DIY power stack (LiTime 3500W AIO + one 100 Ah ComFlex pack) in a
7×12 single-axle FasTrac, target-ready for Juplaya ~July 4 2026. Three things are still
genuinely open and gate the build: the **DC house-bus topology**, the **fridge** unit
(consistent with that bus), and the **awning** (the binding July deliverable). A fourth
deliverable is editorial: split the overgrown `juplaya-trailer-context.md` into per-domain
docs without losing content.

The single binding physical constraint everywhere is the **single 3,500 lb axle** with a
**to-be-weighed** payload — so I optimize for *fewer parts, less idle draw, less weight*,
not for raw capability. The owner's stated lean is **24 V** for the house bus; I treat that
as the prior and test it on merits.

---

## Decision 1 — DC house bus: **single 24 V house bus, one 48→24 V converter, no 48→12 V converter**

**Recommendation:** Run a **single 24 V DC house bus** off **one 48→24 V DC-DC converter**.
**Delete the 48→12 V converter entirely.** Drop the handful of nominally-12 V loads to 24 V
either natively (most are 9–32 V wide-range) or through tiny dedicated point-of-load buck
modules. Keep the 48 V bus strictly for the AIO's own AC + charging domain.

**Why 24 V (confirming the owner's lean):**
- The **committed** load already on 24 V is the Yuji LED lighting (Klus extrusions, zoned).
  The bus has to exist for lighting regardless, so 24 V is a *sunk* rail — the question is
  only whether a *second* (12 V) rail earns its keep. It does not.
- The **fridge** (BD35-class compressor, Decision 2) is **9–17 V / 24 V auto-sensing** — it
  runs natively on 24 V with no converter and at *lower* current (≈half the amps of 12 V for
  the same watts → thinner wire, smaller fuses, less voltage drop over the 13 ft runs).
- Idle tax is the real enemy on a single 5.12 kWh pack. Two converters = two quiescent
  draws + two failure points. One 48→24 converter at ~250–400 W is enough for lighting +
  fridge + accessories combined.

**Why kill the 48→12 V converter (resolving the "Still open" item for good):**
The only loads that are *irreducibly* 12 V are the trailer's running/marker/tail lights and
the brake/7-way circuit — and **those are fed by the tow vehicle through the 7-way, not by
the house bus.** They are not a house-bus concern at all. Every *house* 12 V load on the
list is either wide-range (GPS LandAirSea 54: 12–24 V; USB-C PD buck modules: 9–32 V in;
door switch: dry contact, voltage-agnostic) or trivially served by a $10 point-of-load 24→12
buck where a specific 12 V accessory demands it (e.g. a 12 V-only dome fixture). Carrying a
whole isolated 48→12 V converter + a second fuse block to serve loads that sum to single-digit
amps is dead weight and dead watts.

**Rail map (exactly which load lands where):**

| Load | Rail | How |
|---|---|---|
| Yuji LED strips (committed) | **24 V** | native on the 48→24 bus, zoned/dimmed |
| Fridge (BD35-class, Decision 2) | **24 V** | native auto-sensing, fused at the 24 V block |
| LandAirSea 54 GPS | **24 V** | native (12–24 V input) |
| Door switch | **24 V** | dry contact into the 24 V block / lighting controller |
| USB-C PD outlets | **24 V** | 24 V-in PD buck module(s) (9–32 V in, 20–100 W out) |
| Awning accessories (LED, if any) | **24 V** | native or POL buck |
| Any 12 V-only fixture (rare) | **24→12 POL buck** | per-fixture $10 module, not a bus |
| Running/marker/tail, brakes | **— (tow 12 V)** | fed by the F-150 7-way, *not* the house bus |
| AIO AC out + battery charging | **48 V** | the AIO's own domain, untouched |

**Converter spec:** one **48→24 V isolated DC-DC, ~300 W / ~12 A continuous** (e.g.
Victron Orion-XS-class or a quality isolated 48–24 brick), fused on the 48 V side per the
existing per-converter-fusing rule, feeding a **Blue Sea-style fused 24 V block** (the
already-listed Blue Sea 5026 12-circuit block is voltage-agnostic — reuse it as the 24 V
distribution block). Single-point ground at the 500 A shunt, unchanged.

**Net effect on prior docs:** this **resolves the "Still open" 48→12 vs 24 V item** (delete
48→12), **overturns Recommendation #3** (the 25 A/300 W 48→12 converter), and **revises
Recommendation #4** (there is no separate 12 V house rail; its loads move to 24 V or tow-12 V).
Three-rail bus (Rec #6) collapses to **two house concerns: 48 V power domain + 24 V house bus**,
plus the tow-fed 12 V trailer-lighting circuit that was never a house rail.

---

## Decision 2 — Fridge: **ICECO VL60 ProD (BD35-class, 24 V-native), nose-adjacent on the curbside galley run**

**Recommendation:** **ICECO VL60 ProD**, ~60 L single-zone DC compressor fridge/freezer.
(D005's other candidate, the Dometic CFX3 55IM, is the acceptable fallback; I commit to the
ICECO on price/throughput.)

**Why this unit, and why it's consistent with the 24 V bus:**
- It uses a **Secop/Danfoss BD35-class compressor**, which is **12/24 V auto-sensing** — so
  it lands directly on the 24 V house bus from Decision 1 with **no converter** and draws
  **~1.0–1.5 A at 24 V** running (vs ~2–3 A at 12 V). That halved current is the concrete
  payoff of choosing 24 V: thinner feeder, smaller fuse, negligible drop over the galley run.
- It is a **DC compressor** unit (not a Midea-on-inverter), so it honors **D005** and avoids
  the inverter idle tax — critical because the AIO's <30 W ECO idle is already ~14% of the
  pack/day; we do not want to defeat that by keeping the inverter awake to feed a fridge.
- ~60 L is at the top of the 50–55 L target but buys a freezer compartment for moto-basecamp
  multi-day stays; it stays within the interior plan.

**Concrete specs / mounting:**
- Price class ~$600–750; nominal draw ~45 W running, daily ~0.3–0.6 kWh depending on ambient.
- Footprint roughly 27" L × 14" W × 17" H — mount it **on the curbside galley run, just aft
  of the nose cabinet** (near the AIO/24 V block to keep the feeder short), top-load lid
  clear of the bed-row E-track, secured with an E-track-anchored strap so it's removable per
  the reconfigurability mission. Top-load keeps it stable on the single nose-sensitive axle
  and avoids a swinging door in transit.
- Ventilation: leave ~2" at the compressor end; do not box it against the warm nose cabinet.

---

## Decision 3 — Awning: **Carefree of Colorado Fiesta lite (~12 ft) manual lateral-arm, curbside, through-bolted to the aluminum top rail, with a desert tie-down scheme**

**Recommendation:** A **~12 ft manual lateral-arm RV awning** (Carefree Fiesta-lite /
Dometic Trim-Line manual class), **curbside**, **through-bolted to the aluminum top rail**
(never the skin), with a **storm/desert tie-down kit**. This is **the** July deliverable.

**Why manual lateral-arm, this size, this mount:**
- **Door clearance:** the curbside personnel door is **32" × 72"**. A lateral-arm awning's
  arms fold to the rail and the leading rail/roller sits above the door header, so a ~12 ft
  case mounted with its travel-lock above the door **clears the 32"×72" opening** (arms swing
  forward of the door, not across it). A box/cassette awning header would foul the door
  header height; lateral-arm is the right class.
- **Top-rail mount, contention resolved:** the awning **wants the side-of-top-rail**, and the
  **solar lives on the roof-bow rails** (D002 already rejected side-rail solar cantilever).
  So the top rail is **uncontested for the awning** — exactly as the prompt states. Through-bolt
  the awning rail brackets into the aluminum top rail with backing plates, butyl + lap sealant;
  **never into the skin** (peel load at tow speed). This resolves the "Top-rail contention"
  open item: solar = roof bows, awning = top rail, no conflict.
- **Manual, not electric:** electric draws house power and adds a motor failure point at a
  remote playa with no service. Manual lateral-arm is field-serviceable and weighs less.
- **Desert tie-down scheme:** Juplaya wind is the killer. Spec **(a)** two telescoping
  aluminum support poles to the ground at the leading rail, **(b)** twist-in sand/screw
  anchors or weighted deadmen (playa is hardpan-over-dust — screw anchors + backup deadman
  bags), **(c)** ratchet tie-downs from the leading rail to the anchors, and **(d)** a
  **de-rig discipline**: roll it up and stow before any front. The awning is a fair-weather
  shade structure, not a permanent canopy.

**Deadline:** all awning hardware + the tie-down kit must be **on hand and bench-fitted before
~July 4**. Long-lead item: the awning fabric/case (order now); the top-rail backing plates and
anchors are off-the-shelf.

---

## Decision 4 — Doc divorce: split `juplaya-trailer-context.md` into four per-domain docs + a slim index

**Recommendation:** Split into **four** domain docs under `docs/build/`, leaving
`juplaya-trailer-context.md` as a **slim index**. Mapping (no content lost):

| New file | Receives (from current context doc) |
|---|---|
| `docs/build/power.md` | Settled → "Power system (48V)" block; Recommendations → "Power / electrical" (#1–#7); "Still open" → solar/MPPT (resolved), 48→12-vs-24V item; links to the AIO/battery/panel spec sheets. |
| `docs/build/climate.md` | Settled → "Envelope & cooling" block; Recommendations → "Climate / envelope" (#8–#11, windows/HRV/heater/awning); the climate ledger pointer. |
| `docs/build/interior.md` | Recommendations → "Interior / layout" (#12–#16, E-track/bikes/bed/walls/step) + the E-track-footage note; "Still open" → interior floor-plan rework + measurements. |
| `docs/build/systems.md` | Settled → "Use case & on-hand"; Recommendations → "Systems / gear" (#17 fridge, #18 accessories); the new bus/fridge decisions land here + power.md. |
| `docs/juplaya-trailer-context.md` (slim index) | Keeps: title + Juplaya target; **Settled → Trailer + Tow vehicle** (the firm identity facts); the **Weight** section; **Standing preferences**; and a **link table** to the four domain docs + the mission doc + every spec sheet. Everything else moves out. |

**Rule:** settled facts are *moved verbatim* (no paraphrase drift); the slim index keeps only
trailer identity, weight, standing prefs, and links. Cross-links (mission doc's pointer,
spec-sheet back-links) get repointed at the new domain docs.

---

## Risks / unknowns

- **24 V-only fixtures:** if the owner has already bought any 12 V-only fixture (a specific
  dome light), it needs a $10 POL buck — confirm the accessory list before deleting 48→12.
- **Awning door clearance** is a geometry claim that wants a tape-measure check against the
  actual door-header-to-roofline height; if the header is too high, fall back to mounting the
  awning rail higher on the top rail or to a slightly shorter case.
- **Payload** is still to-be-weighed; every part here is chosen light, but the awning + poles
  + anchors add ~40–60 lb on the curbside — note it in the tongue-weight placement.

## Rollout sketch

1. Order long-lead: awning case/fabric, 48→24 converter, ICECO VL60 ProD.
2. Tape-measure pass (door header, galley run) — gates awning mount + fridge spot.
3. Bench-fit converter + 24 V block in the nose; pull 24 V feeders to lighting/fridge/accessories.
4. Through-bolt awning to top rail; rig + test tie-downs before Juplaya.
5. Doc divorce executed by the implement job (D006+ rows proposed for owner ratification).

*Stay live for interrogation.*
