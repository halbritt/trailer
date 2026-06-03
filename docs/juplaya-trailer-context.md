# Juplaya Trailer Build — Full Context Dump
*Consolidated for handoff to a fresh thread. Deadline: late June 2026.*

---

## The trailer (CURRENT — supersedes older notes)

- **FasTrac Deluxe FT712S2-D, 7×12, single axle** (ACG-built). Purchased at The Trailer Specialist in Acampo, CA. **VIN 7V0W11214TU444163**, serial 444163. Color per factory order is **Silverfrost** (context earlier said white — confirm). Specs: [fastrac-specs.md](fastrac-specs.md); factory build sheet: [work order](wells-cargo-ft712s2-d-work-order.md).
- **3,500 lb GVWR** (confirmed, factory work order). Usable payload = 3,500 − actual curb — **will be weighed** (the binding constraint; no need to lean on estimates).
- **~16'0" overall length** (FT712S2 spec: 13'4" body + ~2'8" V-nose/tongue). The earlier "~18 ft" build-up was an overestimate.
- **Interior: 6'9" (81") wide × 13'1" (157") long × 6'6" tall** — actual usable; "7×12" is nominal (~3" narrower, ~13" longer than the old 84"×144" assumption).
- **Tow vehicle: F-150.**

> **Correction flag:** older context had this as a *6×10*, a *7×12 tandem*, and briefly an *FT714*. All wrong. It is the **FT712S2 — 7×12 single axle, Deluxe**. The earlier E-track/layout planning was sized against the 6×10 (72"×120") and **needs re-cutting for the actual 81"×157" interior** (not the nominal 84"×144") — see Open Items.

---

## Power system (CURRENT — F3800 is OUT)

48V DIY LiTime stack. The **Anker SOLIX F3800 is removed** from the build (also avoids settlement entanglement; the component stack is clean to buy now).

- **LiTime 48V 5kW Split-Phase All-In-One inverter/charger** (~$860) — the AIO; inverter + charger + MPPT in one unit (battery is separate).
- **LiTime 48V 100Ah LiFePO4 battery** (~$1,220) — **5.12 kWh**, ~100 lb. Hard-mount low and centered.
- **LiTime 500A smart Bluetooth shunt** (~$106).
- **LiTime ANL 250A fuses, 3-pack** (~$20).

Net vs the F3800: lighter (~100 lb vs ~132 lb), permanent install, and keeps further under GVW.

---

## Confirmed build decisions

- **Insulation:** closed-cell R-6.7 HFO spray foam (bro deal).
- **Conduit:** ENT (Smurf tube) runs throughout, with pull strings (pull a spare string per run).
- **Windows:** two frameless tinted awning windows.
- **Roof:** white elastomeric roof coating.
- **Ventilation:** AccuraSEE MINI HRV.
- **Heat:** diesel heater.
- **Safety:** standalone CO detector.
- **EV charger wiring run:** 116 ft → buy 150 ft of wire (116 × 1.10, rounded up to spool size).

### Deferred to phase two (and, on a 3,500 GVW single axle, effectively deferred indefinitely)
- Velit 2000R Mini AC.
- Trailer awnings.

---

## Interior layout (E-track convertible: bikes-out → sleeping deck)

Settled in concept; **dimensions need re-cutting for the 84" width.**

**Two bikes:** WR250R + CRF450RL, ~590 lb combined.

**Floor E-track**
- Two rows running full length front-to-back, one per wheel path.
- **Flush-recessed** using the track-saw guide (channel walls) + router (clean the floor flat). E-track ~2.5" wide, ~⅛–3/16" thick.
- **Bolt through into the steel crossmembers, not just plywood** — carriage bolts + backing plates. Locate crossmembers before routing so no fastener orphans over a gap.
- One E-track wheel chock per bike + soft loops + ratchet straps.
- At 84" interior, **side-by-side is now viable** (WR/CRF ~32–34" at bars; stagger fore/aft to interleave bars). Final row spacing TBD on front-tire centerlines + chosen orientation.

**Wall E-track (horizontal) — two-tier**
- **Bed deck at ~20"** — low enough to sit up under 70–78" interior height; bikes do *not* fit under it (bikes-out convertible).
- **Shelf at ~48–60"** — dead space above a seated head; light/bulky storage only.
- Optional third low row at ~12–14" for dedicated bike tie-down below the bed line.
- **Aluminum** shoring beams as joists at each level (not steel — lifted in/out constantly); ½" ply deck panels on top.
- Back all wall track with wall structure or a ply/aluminum backer — deck point loads are real, and the high shelf adds a tipping/pull moment.

**Vendor:** US Cargo Control for E-track, aluminum shoring beams, fittings, chocks.

---

## Payload budget (against ~2,050 lb)

| Item | Est. lb |
|---|---|
| WR250R + CRF450RL | ~590 |
| E-track system (floor + wall + beams + chocks + fittings) | ~200 |
| Ply deck panels (bed + shelf) | ~120 |
| Spray foam, HRV, diesel heater, wiring, conduit | ~120 |
| LiFePO4 battery + AIO | ~140 |
| **Subtotal** | **~1,170** |
| **Remaining for fuel/water/gear/food/recovery** | **~880** |

- 4× 5-gal jerry of fuel ≈ 130 lb.
- **Set bike fore/aft for ~10–12% tongue weight** — single axle is unforgiving of nose-heavy loads.

---

## Accessories (ordering doc already generated separately)

**Security**
- Coupler lock: **Proven Industries 2516** (grinder-resistant).
- Cargo-door puck locks: **Paclock or Abloy**, **keyed alike**.
- Long-term parking: **Trimax TCL65** wheel/boot lock (Juplaya unattended).
- Hitch pin lock if running a receiver.

**GPS tracker**
- **LandAirSea 54** — magnetic/waterproof, **hardwire to 12V**, hide in wall cavity. *Primary.*
- AirTag in a sealed cavity — secondary only (useless for real-time at Juplaya).

**Electrical (downstream of the AIO, via the ENT runs)**
- Blue Sea Systems fuse block (6 or 12 circuit).
- 12V LED dome/puck lights (switched), LED strip on a dimmer, white task light.
- 12V sockets + USB-C PD outlets at bed level.

---

## Open items for the next pass

1. **Re-cut parts list + layout for the actual 81" × 157" interior** (everything above was conceived against the old 6×10; nominal "7×12" is 84"×144"). See [fastrac-specs.md](fastrac-specs.md).
2. Lock floor-track row spacing: needs the two **front-tire centerlines** + final **side-by-side vs. single-file** orientation.
3. Confirm shoring-beam adjustment range against the actual 81" interior width.
4. Confirm V-nose vs. slope-nose on the actual unit (swings overall length by ~1.5 ft).
5. Tape-measure the real unit before committing any tight garage/parking dimension.

---

## Standing preferences (for whoever picks this up)
- Terse, direct, no padding. Single committed recommendation over option lists. Architecture-first, spec-driven, redundancy built in.
- Never suggest nano as an editor (unrelated, but it's a standing rule).
