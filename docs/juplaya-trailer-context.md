# Juplaya Trailer Build — Context & Open Questions
*Consolidated for handoff. Target: ready for Juplaya (~July 4, 2026).*

> This doc was reframed from an auto-generated draft that over-stated what was decided. Treat everything under **Open questions** as unresolved — they are the inputs for a striatum workflow. Only **Settled** items are firm. Do not infer decisions that aren't written here.

---

## Settled

### Trailer
- **FasTrac Deluxe FT712S2-D, 7×12, single axle** (ACG-built), **Silverfrost** exterior. Bought at The Trailer Specialist, Acampo CA. **VIN 7V0W11214TU444163**, serial 444163.
- **Interior 6'9" (81") W × 13'1" (157") L × 6'6" tall**; overall ~16'0". Rear **5,000 lb ramp door**; side **32"×72" personnel door, RH** ("RV-style"). **2"×4" tube main rails**; 4× factory 5,000 lb D-rings; 3/4" PlexCore floor.
- Full specs: [fastrac-specs.md](fastrac-specs.md) · factory build sheet: [work order](wells-cargo-ft712s2-d-work-order.md).

### Tow vehicle
- **2021 Ford F-150 EcoBoost, Max Tow package.** Has **Pro Trailer Backup Assist** (relevant to maneuvering/parking). Ordered: **integrated trailer backup camera + TPMS** (both integrate with the truck).

### Power system (48V — current/up to date)
- DIY 48V LiTime stack (F3800 is out):
  - **LiTime 48V 5kW split-phase AIO** — inverter + charger + MPPT in one (battery separate).
  - **LiTime 48V 100Ah LiFePO4** — 5.12 kWh, ~100 lb; mount low and centered.
  - **LiTime 500A Bluetooth shunt**; **ANL 250A fuses**.
- The **AIO lives in the nose, in a cabinet**; anything that needs plugging in plugs in there.

### Envelope & cooling
- **Closed-cell spray foam** insulation — given.
- **Elastomeric roof coating** — given.
- **Velit Mini 2000R AC — ordered (48 VDC unit).** (No longer deferred.)

### Use case & on-hand
- Hauls two bikes — **WR250R + CRF450RL, ~590 lb** combined — convertible "bikes-out → sleeping deck."
- **~(6) 10 ft black powder-coated E-track sections** — believed ordered (confirm).

---

## Open questions (striatum workflow inputs)

Each is unresolved. **Do not solve here** — these are for the workflow to resolve.

### Power / electrical
1. **Solar count & string** — 2–4 × **LG455N2W-E6** (455 W), permanent roof mount; maybe **3 if a 3s string** fits the AIO's MPPT window. Decide count + series/parallel.
2. **Solar mounting** — roof is **flat aluminum**; preference to mount **off the side of the aluminum top rail**. **UNDECIDED — needs a mount design.**
3. **48V→12V converter** — needed at all? If so, size it to the 12V loads.
4. **12V load list** — define what actually runs on 12V. Known intent: door switch, maybe awning/misc. (Strip lights are 24V; AC is 48V.) Other than strip lights, a door switch, and the AC, no other wiring is currently foreseen — validate that.
5. **Lighting** — 24V LED strips (**Yuji**) in **Klus** extrusions/diffusers; maybe 12V for the awning + misc.
6. **Wiring diagram** — produce once voltages/loads settle (48V AC + charging, 24V lighting, maybe 12V). **Don't solve yet.** (Conduit/ENT runs are an option to revisit here, not a decided spec.)
7. **Truck charging** — run a **high-current line from the F-150** to charge the 48V pack while towing; spec + wire a **12V→48VDC charger**.

### Climate / envelope
8. **Windows** — up for discussion (whether, how many, type). Prior idea: 2 frameless tinted awning windows — **not decided**.
9. **HRV** — maybe, later (was AccuraSEE MINI).
10. **Diesel heater** — maybe, later. (Pair a CO detector if it happens.)
11. **Awning** — **in scope for Juplaya (July 4)**; must be selected.

### Interior / layout
12. **E-track layout** — convertible bikes-out → sleeping deck; full layout open. Sub-decisions: floor-track orientation (**side-by-side vs single-file** for the two bikes), row spacing (needs front-tire centerlines), mounting method (**flush-recessed vs surface**, bolting **through to the steel crossmembers** vs plywood only), chocks/soft-loops/straps. Source: US Cargo Control.
13. **Horizontal track heights** — two horizontal tracks: reason out **bed height + optimal shelf height in the 6'9" interior**; survey comparable builds. Constraints: sit-up clearance over the bed; bikes-out, so nothing must clear under the bed; wall track must be backed (point loads + tipping moment on a high shelf).
14. **Bed shoring beams** — **aluminum shoring beams** vs **E-track inserts that accept 2×4 lumber**. Decide.
15. **Wall finish + build-up** — leaning **FRP** (Home Depot textured panel); could be talked into luan; **no paint**; maybe a **1/4" XPS sheet** as a thermal break. Need the wall build-up spec + trim options.
16. **Personnel-door stairs** — need stairs for the 32"×72" side door.

### Systems / gear
17. **Fridge** — explore: a **DC-compressor unit** (48 / 24 / 12 VDC) vs a small **Midea** running off the inverter (which adds idle inverter load).
18. **Accessories ordering list** — produce it. Candidates from prior research: GPS **LandAirSea 54** (hardwired 12V), security (**Proven 2516** coupler lock, **Paclock/Abloy** puck locks keyed-alike, **Trimax TCL65** boot), Blue Sea fuse block, 12V sockets / USB-C PD, dome/task lights.

---

## Weight
- **GVWR 3,500 lb** (confirmed). Real payload = 3,500 − actual curb; **will be weighed**, not estimated. Single axle is nose-sensitive — aim ~**10–12% tongue weight** when positioning the bikes.

---

## Standing preferences (for whoever picks this up)
- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
