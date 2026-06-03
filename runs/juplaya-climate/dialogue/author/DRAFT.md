---
kind: handoff
title: "Climate / envelope — committed recommendations (author draft)"
run_id: run_c1b091b11f35c09b89d195e2f0fd9469
workflow_id: juplaya-climate
domain: climate-envelope
author: operator [self-declared: climate-author-halbritt-2]
status: draft-for-cross-examination
---

# Climate / envelope — committed recommendations

Scope: open questions 8–11 (Windows, HRV, Diesel heater, Awning). One committed
recommendation each, with rationale and the spec/constraint it leans on. Settled
and not relitigated: closed-cell spray foam, elastomeric roof coating, Velit Mini
2000R AC (48 VDC, ordered).

Hard frame I am designing against:
- Interior **81" W × 157" L × 78" tall** (6'9" × 13'1" × 6'6"); **76-1/2" tube
  posts, vertical posts 16" o.c., tube roof bows 24" o.c.** (work order).
- **Silverfrost ACP exterior, 1-piece aluminum roof**, semi-screwless.
- **Single 3,500 lb axle**, nose-sensitive, **payload to be weighed** (≈1,900–2,050 lb
  estimated, not budgeted against).
- **48V LiTime stack**, AIO in the nose cabinet, 5.12 kWh; AC is the Velit 48 VDC.
- North star: **E-track-as-OS, reconfigurable, nothing welded-in.** Current target
  is the Juplaya moto basecamp (~July 4 2026); the shell should stay cheap to
  reconfigure for the other mission profiles.
- Factory envelope already present: **sidewall flow-thru vents (1 pr)**, **12V dome
  light**. Sidewall liner is 3/8" PlexCore.

---

## Q8 — Windows

**RECOMMENDATION: Add exactly two (2) RV-style frameless, tinted, dual-pane awning
windows, both on the curbside (door-side) wall, NOT on the roadside or in the
V-nose. Size them to drop cleanly into the 16" o.c. post bays — target a nominal
~22"×18" rough opening that lives between two posts without cutting a vertical
tube. One forward of the personnel door, one aft, both centered at ~eye-height
when seated on the bed deck.**

- Rationale: two windows give cross-flow with the personnel door and standing
  airflow for the AC/passive-vent case, plus daylight so the box isn't a coffin,
  without the asymmetry/structural cost of cutting the roadside or the curved
  V-nose. Awning style opens in rain (Juplaya dust/sun, but shoulder-season rain
  is real). Tint + dual-pane is the thermal-honest choice given closed-cell foam
  everywhere else — a single-pane window would be the envelope's thermal hole.
- Constraint/spec it depends on: **vertical posts 16" o.c.** — a ~22" opening
  spans roughly one bay and I am asserting it fits between posts; **this needs a
  physical measurement of actual clear bay width before ordering** (post wall
  thickness eats into nominal 16"). If a window won't fit a single bay without
  cutting a post, drop to one larger window in a deliberately reinforced opening,
  not two compromised ones.
- Curbside-only keeps all glass on the door/awning/living side and leaves the
  roadside wall as **uninterrupted E-track real estate** (north star: walls are
  the mounting grid; glass fragments that grid).
- FLAG — purchase: 2× frameless tinted dual-pane RV awning windows sized to
  measured bay. FLAG — measurement: actual clear width/height of a curbside post
  bay, and confirm no clearance light / wiring / vent lands in the chosen bays.
- FLAG — weight/structure: a cut opening in a 76-1/2" post wall needs a header;
  framing two openings is a real (small) payload + labor line. Keep openings
  inside a single bay specifically to avoid cutting a load-bearing vertical post.

## Q9 — HRV

**RECOMMENDATION: Do NOT install an HRV for Juplaya. Commit to "later," but
rough-in now: cut and trim-ring two paired 4" wall penetrations (fresh + stale)
on the roadside wall low/high, blanked with insulated plugs, and pull a labeled
24V/12V power string to that location. No core, no ducting bought now.**

- Rationale: the mission doc treats HRV as part of the constant off-grid
  livability stack, but Juplaya is a dry, sips-power moto basecamp where the
  personnel door + two awning windows + factory flow-thru vents already give
  ample ventilation. An HRV's payoff is in sealed cold-weather / engine- or
  gas-adjacent profiles (metal-fab profile #2), which are not the July target.
  Installing the core now spends payload, power, roof/wall penetrations, and
  budget against a use case that isn't this trip.
- Why rough-in anyway: cutting/sealing penetrations and pulling string is cheap
  NOW and miserable LATER once foam + FRP wall finish is in. This is the
  "wired through ENT with pull strings for whatever comes next" principle from
  the mission doc, applied to the envelope. It keeps the HRV a bolt-on, not a
  teardown.
- Constraint/spec it depends on: closed-cell foam + FRP wall build-up (Q15, other
  run) means any later penetration is destructive — so the decision is "penetrate
  while open, defer the device." Coordinate the rough-in location with the wall
  E-track layout so the future core doesn't collide with a track row.
- FLAG — purchase (now, small): 2× 4" insulated wall plugs + trim rings + pull
  string. HRV core itself: deferred, not purchased.

## Q10 — Diesel heater

**RECOMMENDATION: Commit to a 2 kW diesel air heater (Webasto/Espar-class, or a
quality clone if budget-bound), but as a FLOOR-MOUNTED, fully sealed-combustion
unit with its own external tank — and INSTALL IT FOR JULY, paired with a
hardwired CO detector. Mount the heater low against the V-nose-side bulkhead near
the AIO cabinet, exhaust straight down through the floor (not the wall), combustion
air drawn from outside the cabin, fuel from a small external diesel tank on the
tongue or A-frame.**

- Rationale: this contradicts a pure "moto-basecamp sips power, skip heat" read,
  so I am taking the falsifiable position deliberately: Juplaya / high-desert
  early July still drops cold at night, the build is a sleeping deck, and a
  diesel air heater is the off-grid-correct heat source — it does NOT load the
  48V battery the way resistive/heat-pump heat would (the Velit is cooling-biased
  and 48 VDC; running it as a heat pump in cold is marginal and a battery hog).
  Diesel heat decouples "stay warm overnight" from "stay charged." The mission
  doc explicitly lists diesel heat in the constant livability stack, so installing
  now also retires a later teardown.
- Sealed combustion + floor-down exhaust is the safety-correct choice in an
  insulated steel box: no exhaust on the wall where it can wash back along the
  Silverfrost skin or near a window/vent. Combustion air from outside means the
  burner never competes with cabin O2.
- CO detector: **non-negotiable pairing** — hardwire a 12V CO (and ideally CO+LP/
  smoke combo) detector, mounted per the detector's height spec for the sleeping
  area, on its own protected circuit. This is the one item where I will not accept
  "later."
- Constraint/spec it depends on: 3/4" PlexCore floor + 2"×4"/crossmember-16"-o.c.
  steel frame — the through-floor exhaust + tank-line penetrations must land in a
  bay clear of crossmembers and the E-track floor rows (coordinate with the
  interior run's floor-track plan). Fuel: small dedicated diesel tank, NOT plumbed
  from the F-150.
- FLAG — purchase: diesel air heater kit (heater, muffler, external tank, controller,
  ducting), 12V CO/combo detector, fuel/exhaust pass-through fittings.
- FLAG — measurement: floor bay clear of crossmembers for exhaust drop; cabin
  location that doesn't blow hot air directly at the bed sleeper's face.
- FLAG — power: the heater's glow plug/fan is a 12V load (~8–10A startup) — this
  is a real entry on the 12V load list (Q4, systems run): it likely justifies a
  48→12V converter on its own. Hand this dependency to the systems run.

## Q11 — Awning (IN SCOPE for July)

**RECOMMENDATION: Install a manual, side-mounted pull-out box awning rated for the
~13' body — specifically a Carefree/Dometic-class 12-ft manual roll-out lateral-arm
awning — mounted to the curbside top rail (the same side as the personnel door and
the two windows), with the leading edge clearing the 32"×72" door swing. Manual,
not 12V-powered, for the July build. Mount to the aluminum top rail with a
through-bolted aluminum mounting rail / Z-bracket, NOT screwed only into the ACP
skin.**

- Rationale: awning is the required deliverable for Juplaya and the single biggest
  livability multiplier (shade over the door, a dry/shaded outdoor room at a
  desert basecamp). Manual roll-out is the redundancy-first choice: no motor, no
  12V draw, no controller to fail at a remote site, deploys/stows by hand in wind.
  Curbside co-locates shade + door + windows into one "living face" and leaves the
  roadside clean. ~12 ft matches the 13'1" body without overhanging the V-nose.
- Mount: the operator's stated preference (Q2 solar, other run) is to mount off
  the **aluminum top rail** — same logic applies here. The awning's lateral load
  in wind is significant; it must through-bolt to structure (top rail + backing),
  never rely on the 1-piece aluminum roof skin or ACP panel as a fastener
  substrate. Coordinate the awning mounting rail with the solar side-rail mounts
  (other run) so they don't fight for the same top-rail real estate.
- Constraint/spec it depends on: overall body 13'4", curbside wall height to top
  rail, **8'6" overall width / 8'1" overall height** (road-legal envelope — the
  rolled-up awning box must not push width past legal, and the awning rail must
  clear the personnel-door head). Wind: spec the awning with positive lock-down /
  de-flap straps for desert gusts.
- FLAG — purchase: ~12 ft manual lateral-arm RV awning + curbside through-bolt
  mounting rail + backing plates + tie-down kit.
- FLAG — measurement: exact curbside wall height and top-rail profile; door head
  height vs. awning rail; rolled-box added width vs. 8'6" legal.
- FLAG — coordination (other runs): top-rail real estate shared with solar mounts
  (systems run); confirm sequencing so awning rail and solar rail co-exist on the
  curbside top rail.

---

## Cross-run dependencies I am asserting (for the adjudicator)
- Q10 diesel heater adds a **12V load** → hands a requirement to the systems run's
  Q4 (12V load list) and Q3 (48→12V converter sizing). The heater's 12V fan/glow
  draw may by itself justify the converter.
- Q8 windows and Q11 awning both consume **curbside wall / top-rail** real estate;
  Q11 also competes with **solar side-rail mounts** (systems run Q2). Sequencing
  matters.
- All penetrations (windows, HRV rough-in, diesel exhaust) must be coordinated with
  the **interior E-track layout** (interior run, Q12/Q13) so glass/cores/exhaust
  don't land on a track row or crossmember.

## What is FLAGGED as needing a physical measurement before any purchase
1. Actual clear width/height of a curbside post bay (windows).
2. Floor bay clear of crossmembers for the diesel exhaust drop.
3. Curbside wall height, top-rail profile, door-head height (awning + window placement).
4. Rolled awning box added width vs. 8'6" legal envelope.

## Weakest point (offered up for cross-examination)
The **diesel heater "install now for July"** call is the most aggressive and the
most attackable: it spends payload, a floor penetration, a 12V load, and budget on
heat for a July high-desert trip where many would just bring a sleeping bag. If
cross-exam lands that July nights don't justify it, the fallback is HRV-style:
rough-in the floor exhaust + fuel penetrations and CO-detector wiring now, defer
the heater unit — same "penetrate while open, defer the device" logic as Q9.
