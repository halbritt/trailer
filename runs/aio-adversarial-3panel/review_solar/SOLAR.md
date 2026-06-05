---
author: operator
---

# Solar / 3S Review — Corrected 3-Panel Premise (D002 rerun)

Posture: attack D002 from the corrected solar angle. Binding premise: **three LG455 roof panels fit and the Velit 2000R fits in the nose.** Geometry is conceded everywhere below; nothing here rejects 3S on fit.

**Bottom line up front: the corrected premise does not change the inverter/charger purchase — it changes the solar topology.** Keep the LiTime 3500 W buy, return the 5 kW, and revise D002's solar clauses: roof goes 3S (1365 W) into a Victron SmartSolar MPPT 250/60, the "no external MPPT for July" clause is deleted, and the AIO's own 60–145 V PV input becomes the ground-string port.

## Fact basis

Sourced: LG455 STC/NMOT electricals and temp coefficients ([datasheet](../../../docs/reference/lg455n2w-e6-datasheet.md)); LiTime 3500 W PV window 60–145 V op / 60–115 V rec, 4400 W / 50 A ([specs](../../../docs/reference/litime-48v-3500w-aio-specs.md)); LiTime 5 kW PV window 120–500 V op / 120–450 V rec, ≤22 A, idle ≤80/55 W ([specs](../../../docs/reference/litime-48v-5kw-aio-specs.md)); ComFlex 100 A continuous charge/discharge ([specs](../../../docs/reference/litime-48v-100ah-battery-specs.md)); energy budget and owner-reported LiTime PV-OV nuisance faulting ([build sheet](../../../docs/juplaya-trailer-context.md)); candidate windows ([evidence brief](../../../docs/research/aio-inverter-3panel-evidence-2026-06-05.md)). Inference is tagged **[inf]** where it appears: hot-roof cell temperatures, below-floor firmware behavior, soiling derate, panel-market availability.

## The 120 V MPPT floor, decided — not handwaved

LG publishes Voc at −0.26 %/°C and Pmax at −0.33 %/°C; no Vmpp coefficient. Vmpp slides at least as fast as Voc, so bracket Vmpp between the two.

| Condition | 3S Vmpp | 3S Voc |
|---|---:|---:|
| STC (25 °C cell) | 126.3 V | 149.7 V (+5% tol → 157.2 V) |
| NMOT (42±3 °C cell, 20 °C ambient) | 118.8 V | 141.3 V |
| July noon, flat low-air-gap roof mount, 65–75 °C cell **[inf]** | **~105–113 V** | ~130–134 V |
| Cold morning −10 °C | ~138 V | 163.3 V (+5% → 171.4 V) |

3S is **already below the 120 V floor at NMOT** — and NMOT assumes a 20 °C ambient with free airflow. A July Black Rock roof (35–40 °C ambient, panels inches off hot steel) runs 65–75 °C cell **[inf]**, putting the MPP 7–15 V below the floor through the highest-insolation hours of every single day of the deployment.

Ruling between the three characterizations the brief demands:

- **Not acceptable clipping.** Clipping implies a bounded, spec-quantified loss. Below-floor behavior on the LiTime 5 kW / EG4 class is not specified at all — the 120 V number is the bottom of the *operating* range. Whatever happens below it is firmware-defined and unverifiable before purchase **[inf]**.
- **Worse than intermittent tracking.** Hot Voc (~132 V) sits *above* the floor while hot Vmpp sits *below* it, which is the classic hunt geometry: controller wakes at Voc, loads the string down through 120 V, trips its undervoltage, releases, repeats **[inf]**. And LiTime firmware has documented owner-reported nuisance faulting at its *other* voltage rail (PV-OV below rated 145 V on the 3500 W, per web-val) — there is no basis to trust graceful boundary behavior here.
- **It is a hard reliability problem,** with one aggravator: the failure is invisible at commissioning. On a cool shakedown day, 3S Vmpp sits above 120 V and the unit works perfectly; it fails for the first time at solar noon on the playa. That is a trap, not a trade-off.

**Consequence: every 120 V-floor AIO (LiTime 5 kW, EG4 3000EHV) is rejected for 3S LG455 on operating physics — geometry fully conceded.** The 145–150 V-class AIOs (Renogy/Eco-Worthy) are rejected on the other rail: 149.7 V STC Voc is over/at the ceiling before cold correction or tolerance. 3S has exactly one sound home in the candidate list: a 250 V-class MPPT that tracks down to battery+5 V (cold Voc ≤ ~178 V worst-case vs 250 V max; hot Vmpp ~105–113 V vs a ~58 V start threshold — margin on both rails at every temperature this trailer will ever see).

## The 3S-positive steelman — adopted, not just entertained

**Steelman A (one-box 3S): keep the mistaken 5 kW.** Best honest case: it is already in hand, it takes 3S by voltage ceiling, no second box, no MPPT coordination. Killed by: the floor analysis above (its 3S harvest degrades or drops out exactly at peak hours); idle ≤80/55 W vs the 3500's <50/<30 W — roughly doubling the budget's third-largest line; 5 kW sustained output exceeds the single pack's 100 A continuous; ≤22 A PV input takes one string only, so the ground pair is electrically stranded on it; and 2S (the fallback string) is *below* its 120 V floor entirely. Rejected.

**Steelman B (hybrid 3S): LiTime 3500 W + Victron SmartSolar MPPT 250/60 on the roof string.** This one survives everything thrown at it:

- Roof 3S → SmartSolar 250/60: in-window at all temperatures (table above). String charge ~26.7 A at 1365 W STC — a 60 A unit loafs.
- Ground 2S → **the AIO's own PV input**. This answers the ground-panel question decisively: **no second external MPPT is ever needed.** The AIO *is* the second MPPT — 2S at 79 V NMOT sits mid-window in its 60–115 V recommended band. One string per input also deletes D002's MC4 Y-combiner/per-string-fusing hardware.
- Energy: the build sheet's own budget is the attack surface. Roof-only 910 W ≈ 4.0 kWh/day vs a 4.1–4.45 kWh/day July load — D002 is **break-even at best** and explicitly calls the ground pair "required margin." 3S roof = 1365 W ≈ **6.0 kWh/day** (same 4.4 sun-hour scaling), clearing the budget by ~35–45% *with zero deployment labor*, while rolling, parked, or unattended. A 10–15% playa-soiling derate **[inf]** still clears it. D002's weakest line — the energy margin — is exactly what 3S fixes.
- Battery: SmartSolar 26.7 A + AIO capped at 70 A (PV+AC) ≤ ~97 A < the pack's 100 A. Inverter sizing unchanged.

**The panel-count catch (the real cost of 3S, surfaced):** the owner owns four LG455s. Promoting one ground panel to the roof leaves a lone fourth panel that is electrically homeless — 1S (Voc 49.9 V, hot Vmpp ~36–38 V) is below the AIO's 60 V floor and below the SmartSolar's battery+5 V start. So the honest options are: **(a)** 3 roof + fourth panel stays home as a damage spare — net payload *drops* 48.5 lb and the 83"-panel transport slot (panels vs 81" interior width) is freed; or **(b)** buy a fifth ~10.8 A-class panel later and restore a ground 2S into the waiting AIO input (zero new electronics). LG exited panel manufacturing, so a fifth panel is used-market or a current-current-matched equivalent **[inf]**. Recommend (a) now, (b) behind a trigger: if shakedown/July shows sustained Velit duty above ~4 kWh/day (≈6 full-power hours), buy the fifth panel.

Worst-case honesty: a brutal AC day (Velit ~4.8 + fridge 1.3 + idle 0.7 ≈ 6.8 kWh) runs ~0.8 kWh past the 6.0 kWh harvest — absorbed by the 5.12 kWh pack and repaid the next normal day. Under D002 the same day *required* deploying and anchoring ground panels in playa wind; under 3S it requires nothing.

---

## Required outputs

### 1. Recommended architecture and exact next purchase/return action

**Architecture:** LiTime 48 V 3500 W AIO (unchanged) · roof **3 × LG455 in 3S (1365 W) → Victron SmartSolar MPPT 250/60** · AIO 60–145 V PV input reserved as the ground-2S port (empty for July) · fourth panel stays home as spare · Velit stays a fused 48 V DC branch.

**Actions:**
1. Complete/keep the LiTime 3500 W purchase — no change.
2. Return the LiTime 5 kW — no change, reinforced (see 2).
3. **Buy: Victron SmartSolar MPPT 250/60**, a ≥250 V-DC-rated roof-string disconnect/breaker, and rail/feet for the third panel row (same roof-work window as rows 1–2; the roof is still bare — build step 4 has not happened).
4. Move panel #3 from the ground pair to the roof plan; panel #4 to home-spare status.
5. Defer any fifth-panel purchase behind the Velit-duty trigger above.

### 2. Whether the mistaken LiTime 5 kW should still be returned

**Yes — unconditionally, and the corrected premise makes the case stronger, not weaker.** The only argument for keeping it was one-box 3S, and 3S is the precise condition under which its 120 V floor fails worst (MPP 7–15 V below floor at peak hours, hunt-prone, firmware unverifiable). Add the doubled idle tax, the 22 A PV input that strands the ground pair, and sustained output beyond the single pack's continuous limit. Return it.

### 3. Whether confirmed 3 roof panels should change the inverter decision

**The inverter/charger box: no.** No candidate dethrones the 3500 W: the HV AIOs die on the hot floor, the 145–150 V class dies on cold Voc, the MultiPlus-II 48/3000 gives up 1,100–1,300 W of continuous output (2400 W @ 25 °C, 2200 W @ 40 °C vs 3500 W) at higher cost and install scope, and the EasySolar-II GX is 230 VAC — wrong continent.

**The solar topology: yes.** D002's "no external MPPT for July" and "roof 2S" were downstream of roof-geometry doubt — the prior verdict's own escape hatch ("if the roof drawing later proves three panels + Velit + awning stations… consider a separate 250 V-class MPPT") names exactly this premise. The geometry condition has now fired. Leaving the clause in place after its justification dissolved would be inertia, not engineering.

### 4. Strongest counterargument to this recommendation

**"Don't add scope 29 days before Juplaya — D002 passes July as-is, and every new box is schedule risk."** It is the best attack because it needs no technical error on my side; it weighs the same facts and prices schedule over margin. Rebuttal: (i) the roof is unbuilt — panel row 3 rides the *same* install window, penetration pass, and sealant session as rows 1–2; deciding 3S later means a second roof campaign; (ii) the SmartSolar is an in-stock commodity and its wiring is purely additive — nothing in the D002 plan gets rewired; (iii) the revision is **fail-safe**: if the MPPT path slips, string two of the three mounted panels as 2S into the AIO and fly D002 unchanged, third panel parked. The downside is bounded at zero; the upside is the budget's break-even line turning into 35–45% daily margin. Secondary counter — losing the camped 1820 W and ground-tilt option — is answered by the trigger-gated fifth panel and the pack-buffer math above.

### 5. Required gates and install notes

- **Mis-plug guard (new, critical):** roof 3S cold Voc ~163–171 V vs the AIO's 145 V max — and this AIO nuisance-faults *below* 145 V (web-val). Both inputs speak MC4. **Physically separate the systems:** exterior weatherproof MC4 inlet wires *only* to the AIO (ground string); the roof string terminates *only* inside at its own disconnect → SmartSolar; tag both ends "3S — 163 V cold — NEVER into AIO."
- **Never 3S into the LiTime 3500 W** — gate retained verbatim from D002.
- **250 V-class DC protection chain:** roof-string disconnect/breaker rated ≥ ~180 V DC (common 150 V "solar" breakers are out of spec against 171 V worst-case cold Voc); single string → no series fuse needed (one string cannot overcurrent itself; module max series fuse 20 A); battery-side output fuse on the SmartSolar per Victron manual; battery-terminal main OCP stays explicit (existing gate).
- **Charge coordination:** set the AIO total charge cap (PV+AC) to **≤70 A** so AIO + SmartSolar (~27 A) ≤ ~97 A < the ComFlex's 100 A. Both chargers at 57.6 V absorption, LiFePO4 profile, temp-comp off. No comms between them — the BMS arbitrates; its <0 °C charge-off covers the SmartSolar's lack of a low-temp link.
- **Nose cabinet thermal ledger:** add the SmartSolar (derates >40 °C ambient) to the AIO + Orion-Tr ventilation requirement.
- **Weigh-in (row 18) stands:** roof +48.5 lb / net total −48.5 lb with panel #4 at home; single-axle tongue sensitivity unchanged as a gate.
- **Roof drawing (rows 5a/6/15) is still a deliverable** — fit is conceded, but feet-to-bow stations, the Velit opening, and awning standoffs still need the drawing. Add one check: **Velit shadow vs the nearest panel row at low sun** — its 6.5" profile clips the whole 3S string current when it shades a row (half-cut + 3 bypass diodes limit, not eliminate, the loss).
- **Soiling discipline:** with a single roof source, panel wipe-down joins the daily camp routine; budget a 10–15% playa-dust derate **[inf]** — still clears the load.

### 6. One-line D002 verdict

**REVISE** — keep the LiTime 3500 W purchase and the 5 kW return exactly as written, but replace the solar clauses: roof = 3 × LG455 in 3S (1365 W) via a Victron SmartSolar MPPT 250/60 bought now; delete "no external MPPT for July"; the AIO's PV input becomes the (optional, trigger-gated) ground-2S port; never 3S into the AIO.
