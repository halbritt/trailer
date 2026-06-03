# Wells Cargo FasTrac — Manufacturer Specs

Dimensional and weight specs by model. The five right-hand columns are as published by the manufacturer.

The trailer for this build is the **FT712S2** (7×12 single axle, Deluxe "-D" trim): operator-confirmed **3,500 lb GVWR**, **Electric Drum** brakes, **RV-style** side door. It is not a row on the published sheet — the sheet's 7-wide models are the FT714T2 / FT716T2 *tandems*. Its column below is **derived from the sheet** (method in Derivation notes); estimates are marked `≈`.

| Spec | **FT712S2** | FT58S2 | FT610S2 | FT612S2 | FT714T2 | FT716T2 |
|---|---|---|---|---|---|---|
| BODY LENGTH | 13'4" | 9'4" | 11'4" | 13'4" | 15'4" | 17'4" |
| BODY WIDTH | 7'0" | 5'0" | 6'0" | 6'0" | 7'0" | 7'0" |
| OVERALL LENGTH | 16'0" | 11'4" | 14'0" | 16'0" | 18'0" | 20'0" |
| OVERALL WIDTH | 8'6" | 6'8" | 7'8" | 7'8" | 8'6" | 8'6" |
| OVERALL HEIGHT | 8'1" | 7'1" | 8'1" | 8'1" | 8'2" | 8'2" |
| INTERIOR LENGTH | 13'1" | 9'1" | 11'1" | 13'1" | 15'1" | 17'1" |
| INTERIOR WIDTH | 6'9" | 4'9" | 5'9" | 5'9" | 6'9" | 6'9" |
| INTERIOR HEIGHT | 6'6" | 5'6" | 6'6" | 6'6" | 6'6" | 6'6" |
| PLATFORM HEIGHT | 18" | 18" | 18" | 18" | 19" | 19" |
| AXLE QUANTITY | Single | Single | Single | Single | Tandem | Tandem |
| TOTAL AXLE CAPACITY | 3,500 lbs. | 3,500 lbs. | 3,500 lbs. | 3,500 lbs. | 7,000 lbs. | 7,000 lbs. |
| BRAKES WITH BREAKAWAY KIT | Electric Drum | N/A | Optional | Optional | Electric Drum | Electric Drum |
| RADIAL TIRE SIZE | 15" | 15" | 15" | 15" | 15" | 15" |
| TIRE LOAD RANGE | C | C | C | C | C | C |
| HITCH BALL SIZE | 2" | 2" | 2" | 2" | 2-5/16" | 2-5/16" |
| HITCH HEIGHT TO TOP OF BALL | 16" | 16" | 16" | 16" | 17" | 17" |
| HITCH WEIGHT (% OF CURB WEIGHT) | 10% to 15% | 10% to 15% | 10% to 15% | 10% to 15% | 10% to 15% | 10% to 15% |
| CURB WEIGHT (APPROXIMATE) | ≈1,450 lbs. | 900 lbs. | 1,220 lbs. | 1,285 lbs. | 2,260 lbs. | 2,420 lbs. |
| GVWR | 3,500 lbs. | 2,990 lbs. | 2,990 lbs. | 2,990 lbs. | 7,000 lbs. | 7,000 lbs. |
| PAYLOAD CAPACITY (APPROXIMATE) | ≈2,050 lbs. | 2,090 lbs. | 1,770 lbs. | 1,705 lbs. | 4,740 lbs. | 4,580 lbs. |
| SIDE DOOR | RV-style door | OPT | 32" Bar Lock | 32" Bar Lock | 32" Bar Lock | 32" Bar Lock |
| REAR DOOR TYPE | Ramp | Single Swing | Ramp | Ramp | Ramp | Ramp |
| REAR DOOR OPENING (W x H) | 78" x 72" | 54" x 60" | 66" x 72" | 66" x 72" | 78" x 72" | 78" x 72" |
| 12v MALE CONNECTION | 7-Way | 4-Way | 4-Way | 4-Way | 7-Way | 7-Way |
| TUBE MAIN RAILS | 2" x 4" | 2" x 3" | 2" x 3" | 2" x 3" | 2" x 4" | 2" x 4" |

## Derivation notes (FT712S2)

**Operator-confirmed:** single axle, GVWR 3,500, Electric Drum brakes, RV-style side door.

**Length-driven (from the 12-ft column, FT612S2):** body 13'4", interior length 13'1", overall length 16'0" (overall = body + 2'8", constant across the line).

**Width-driven (from the 7-wide columns, FT714T2/FT716T2):** body width 7'0", overall width 8'6", interior width 6'9", rear-door opening 78"×72".

**Interior/height:** interior height 6'6" (all 6–7-wide models). Overall height 8'1" = the 18"-platform + 6'6"-interior case (FT610S2/FT612S2); the tandems read 8'2" only because their platform is 19".

**Axle-driven (single-axle column):** platform 18", total axle capacity 3,500, hitch ball 2", hitch height 16". Constant across all models: tire 15" / load range C, tongue weight 10–15%.

**Inferred:**
- **12v = 7-Way** — Electric Drum brakes need a brake-controller pin; a 4-way flat has none. Every electric-brake model on the sheet is 7-Way.
- **Rear door = Ramp** — every model except the 5×8 is a ramp.
- **Tube main rails = 2"×4"** — tracks the 7-wide body (both 7-wide models use 2"×4"; ≤6-wide use 2"×3"). *Lower confidence:* if rail size tracks axle load rather than width, a 3,500 single could be 2"×3".

**Weight estimates (`≈`):** A floor-area regression on the three single-axle points only — (43.1 ft², 900), (63.7 ft², 1,220), (75.2 ft², 1,285) — gives ≈12 lb/ft² + 383 lb base. The FT712S2 interior is 13'1"×6'9" ≈ 88.3 ft² → **curb ≈ 1,450 lbs.**, so **payload ≈ 3,500 − 1,450 = 2,050 lbs.** This corroborates the build doc's "~1,450 empty → ~2,050 payload." Caveat: the Deluxe electric-brake / RV-door / 7-way upgrades add weight the base-single regression doesn't capture, so real curb is plausibly **1,450–1,600** and payload **~1,900–2,050** — and payload is the binding constraint, so confirm against the actual unit/sticker before committing the budget.

> **Reconciliation with the build doc:** model 7×12 single ✓. But actual **interior is 13'1" × 6'9" (≈157" × 81")**, not the nominal 84" × 144" the doc assumes (~13" longer, ~3" narrower) — re-cut E-track to this. And derived **overall length is 16'0"**, not the doc's "~18 ft" estimate.
