---
schema_version: striatum.finding.v1
artifact_kind: finding
verdict_intent: needs_revision
author: operator
---

# Design Review: Gemini (Devil's Advocate) — Cycle 2

I have interrogated the revised synthesis. While the move away from the flat-roof awning adapter is a step toward realism, the new architecture introduces three "falsifiable" claims that threaten the physical integrity and thermal viability of the build.

### 1. The "Corrected" Roof-Width Falsification (Geometry vs. Math)
The synthesis claims the solar/awning width conflict is resolved because two LG455s (82.0–83.1") leave "1–2" total slack" on an 84" body. This is mathematically correct but **physically impossible** for a FasTrac trailer:
- **Radius Corners:** An 84" (7 ft) body width includes the top-rail radius corners. On a standard Wells Cargo / FasTrac, these radii typically consume 4–6" per side. The usable **flat** roof field is closer to **72–74"**. 
- **The Overhang:** Mounting 82.04" of portrait panels across a 72" flat field means the panel edges will "float" over the radius corners. 
- **Mounting Footprint:** Standard Z-brackets or rail feet require 2–3" of landing area *outside* the panel frame. A portrait pair (82.04") with mounting hardware requires **~86" of flat width**.
- **Falsification:** The panels do not fit the trailer roof without custom cantilevered racking that extends beyond the body width or compromises the panel frames. The "riser bracket" awning mount does not solve this; it only moves the awning out of the way of a solar array that still cannot be mounted safely.

### 2. Awning Load Path (The Lever Arm Risk)
The "riser bracket" plan moves the Fiamma F45s (55 lbs, 138" long) to the top rail/wall plate to clear the door and the panels.
- **Torsional Force:** By raising the case "at or above the roofline," the brackets act as high-leverage crowbars on the aluminum top rail. 
- **Dynamic Load:** In a 15–20 mph desert gust, a 138" deployed awning generates several hundred pounds of pull at the top bracket fasteners.
- **The Skeleton:** FasTrac wall studs are typically light-gauge hat channel or tube. Even with "backing plates," the torsion on the top rail during deployment or travel vibration (11.5 ft of cantilevered mass) is a high-risk failure point for a DIY steel-on-aluminum interface.
- **Falsification:** The load path isn't just "backed structure"; it's a fundamental mismatch between the trailer's thin-wall skeleton and the mechanical moment created by a riser-mounted 3.5m awning.

### 3. Thermal Gate & Converter Margin (The Heat Compounding)
The synthesis acknowledges the tight converter margin (12–15 A load on a 16 A unit) and the fridge's 110 °F ambient ceiling.
- **Heat Plume Synergy:** The AIO (3500 W), the house battery, and the 16 A converter (operating at ~90% load) are all co-located in a "nose cabinet." 
- **The 90% Derate:** Victron Orion-Tr converters generate significant waste heat at peak load. If the cabinet ambient hits 110 °F (trivial in a July desert trailer), the converter will thermal-throttle exactly when the fridge (also in that heat zone) needs peak current to combat the same ambient rise.
- **Falsification:** The "thermal gate" for the fridge is a soft constraint that fails to account for the **waste heat of the power electronics**. The system is being designed at the extreme edge of its thermal and electrical envelope with no active cooling or derating buffer.

### 4. Aisle Clearance (The Handlebar Conflict)
The "~30" center aisle" claim is upheld.
- **Math:** 81" Interior - 21" Fridge - 30" Aisle = 30" for two bikes. 
- **Reality:** Two dual-sports (WR/CRF) have 32–34" handlebars. Even with an 18" stagger, the aisle-side handlebar will overhang the center by 8–10".
- **Falsification:** The usable walking aisle is **~20"**, not 30". This makes the "side-by-side" layout a "clamber-over" layout, complicating fridge access and emergency egress.

### Final Assessment
The revision correctly identifies the roof-width crisis but proposes a solution (riser brackets + 83" panels) that ignores the trailer's radius geometry and structural limits. The thermal plan relies on spec-sheet maximums that will not survive a closed-trailer desert environment.

VERDICT: needs_revision
