# Solar Mounting Order Sheet

Date: 2026-06-10. Itemized breakout of the [order-sheet.md](order-sheet.md) line **"Roof solar NXT rails, spacers, backing, and through-fasteners" ($500 allowance, BUY AFTER GATE)**. Spec source: [solar_mounting.md](solar_mounting.md). Prices are June 2026 web price signals, pre-tax/pre-shipping unless noted.

**Finish decision: mill.** Mill rail is $26.20 vs $41.93 dark and the rail sits under the panels on a coated roof; nothing here is a visual part. All SKUs below are the mill/cheapest-equivalent variants.

## Gate status

| Slice | Gate | State |
|---|---|---|
| Rails, clamps, lugs, clips, caps, adhesive, sealant | None — quantities fixed by the spec | **Orderable now** |
| Through-fasteners, backing, spacers, isolation | **G02** roof bows (stations, tube width, wall thickness, access) | Blocked |
| PV roof gland | **G03** Velit station / final gland position | Blocked |

Buying the clamps now is deliberate: the 40 mm LG frame sits at the top of the CCLAMP 30–40 mm range, and the clamp-bite test on a real frame is itself an open measurement. Test one clamp on a panel the day the box arrives — before any roof drilling.

## A. Order now

| Qty | Item | SKU | Unit | Ext | Vendor / price signal | Notes |
|---:|---|---|---:|---:|---|---|
| 2 | NXT UMOUNT rail, 168 in, mill | `168RLM1` | $26.20 | $52.40 | [US Solar Supplier](https://ussolarsupplier.com/products/unirac-nxt-horizon-168rlm1-168-14-mill-rail) | In stock (677). Cut to 126–129 in after roof dry-fit per [solar_mounting.md](solar_mounting.md). **Freight-only** — see shipping note below. |
| 10 | NXT combo clamp, 30–40 mm, mill | `CCLAMPM1` | $5.99 | $59.90 | [US Solar Supplier](https://ussolarsupplier.com/products/unirac-nxt-horizon-cclampm1-mill-mid-end-combo-clamp-30-40mm) | 8 installed + 2 spares. Sold loose. Test fit on the 40 mm LG frame on arrival. |
| 2 | NXT grounding / MLPE lug clamp | `NULGMLP1` | $3.72 | $7.44 | [RES Supply](https://ressupply.com/racking-and-mounting/unirac-nulgmlp1-nxt-umount-mlpe-and-ground-lug-clamp) | One per rail; do not assume trailer steel is the PV bond path. |
| 20 | NXT wire-management clip, in-rail | `WRMCLPD1` | $0.50 | $10.00 | [Capital Electric](https://www.capitalelectricsupply.com/product/detail/1760980/unirac-inc-wrmclpd1) | Snap-in. Skip the $4.97 `WRMCNSD1` between-rail clamp unless the wire run demands it. |
| 4 | Rail + clamp end cap kit | `ENDCAPD1` | $1.85 | $7.40 | [SolarFlexion](https://www.solarflexion.com/product-p/endcapd1.htm) | One kit per rail end (kit = 1 rail cap + 1 clamp cap). `NUENDCAPKIT` has no retail listing; `ENDCAPD1` is the current equivalent. Cosmetic — cut rail ends get capped. |
| 2 | Sikaflex-252, 300 ml cartridge | Sika `90915` white / `90916` black | $15.42 | $30.84 | [EMI Supply](https://www.emisupply.com/catalog/sikaflex-white-elastic-polyurethane-adhesive-103oz-cartridge-p-15768.html) | Secondary bond/bedding only, interrupted pads. Patch-test on roof skin + rail offcut first. |
| 1 | Sika surface prep (Aktivator-205 wipe) | — | $25.00 | $25.00 | Allowance | 252 on metal wants cleaner/activator prep; price with the Sika order. |
| 2 | Henry 884 Tropi-Cool, 10.1 oz | `HE884004` | $20.03 | $40.06 | [McCoy's](https://www.mccoys.com/shop/p/8781155-052303-27/henry-884-tropi-cool-he884004-silicone-roof-sealant-white-48-hr-curing-35-deg-f-101-fl-oz-cartridge) | Exposed caps/edges under the Henry 887 system only. Home Depot stocks it in-store and typically undercuts — check shelf price. |
| | **Subtotal A** | | | **$233.04** | | |

**Fulfillment decided 2026-06-10: local branch will-call.** Owner is picking the Unirac order up locally — no LTL freight (168 in rails can't ship UPS Ground; LTL starts ~$199, [SolarFlexion's stated policy](https://www.solarflexion.com/product-p/168rld1.htm)). Branch pricing is quote-only; the unit prices above are the online comparison baseline for the quote.

Contingency: a possible third rail is in the allowance lot. Decide at the roof drawing/dry-fit — adds $26.20 and nothing else if it's in the same pickup, so decide **before** placing the branch order.

## B. Order after G02 (bow stations, tube width, wall thickness, access)

Fastener diameter (1/4-20 vs 5/16-18), length, backing style (through-bolt vs plusnut/rivnut), and pad footprint all depend on G02 measurements. Allowances below assume ~12 stations + spares.

| Qty | Item | Sizing trigger | Ext (signal) | Vendor / price signal | Notes |
|---:|---|---|---:|---|---|
| 16 | SS hex bolts, 1/4-20 or 5/16-18, ~1.5–2 in + nylocks + fender washers | Bolt dia + stack height from G02 | $40.00 | [Home Depot Everbilt packs](https://www.homedepot.com/p/Everbilt-1-4-in-20-x-2-in-Stainless-Steel-Hex-Bolt-5-Pack-812240/302007776) / McMaster | ~$35–45 in retail packs; cheaper per-piece at fastener houses. Anti-seize on all stainless. |
| 1 pk | Bonded sealing washers, 18-8 SS/EPDM, 100-pk | Bolt dia | $11.55 | [BCP Fasteners](https://bcpfasteners.com/products/100-qty-1-4-stainless-steel-epdm-bonded-sealing-neoprene-rubber-washers-14-bcp640) (McMaster `94709A317` equiv.) | Under exposed heads, then cap with Henry 884. |
| 1 | 6061 aluminum bar, 1/4 in × 2 in × 48 in | Pad footprint + roof crown from G02 | $33.00 | [Metals4U](https://www.metals4uonline.com/aluminum-flat-bar-6061-1_4thx2in/) (McMaster ~+20%) | One 48 in bar cuts 12–16 short spacer pads. |
| 1 | EPDM strip, 1/16 in × 1 in × 10 ft, 60A | Pad footprint | $14.66 | [Fix Industrial Supply](https://www.fixsupply.com/bulk-rs-e60-60-epdm-rubber-strip-60a-1-16-thick-x-1-wide-x-10-ft-long) (McMaster `8610N` equiv.) | Isolation/bedding layer only — not the structural spacer. |
| 1 lot | Backing plates / crush sleeves / plusnuts | Bow access from G02 decides which | $30.00 | McMaster / allowance | Do not collapse the bow or oil-can the skin. |
| 1 | Anti-seize, small tube | — | $10.00 | Local | Stainless galling control. |
| 1 | PV roof cable gland | **G03** — final gland station | $40.00 | Allowance (Scanstrut-class entry plate) | In the allowance lot but not yet spec'd; pick with the Velit/roof drawing. |
| | **Subtotal B** | | **$179.21** | | |

## Budget vs the $500 allowance

| Bucket | Total |
|---|---:|
| A — order now | $233.04 |
| B — after G02/G03 | $179.21 |
| **Parts total** | **$412.25** |

Local will-call (decided) removes the $150–250 LTL freight exposure; the lot sits **inside the $500 allowance** with ~$88 of headroom for branch-quote drift or the third-rail contingency.

## Do-not-buy reminders

Per [solar_mounting.md](solar_mounting.md): no 96 in rails, no splices unless forced, no SOLARMOUNT clamps on NXT rail, no hidden end clamps as default, no HD rail unless the dry-fit shows a long unsupported span, no adhesive-only mounting, no full-length adhesive dam. "NXT Horizon" and "NXT UMOUNT" listings are the same SKUs (line renamed) — discontinued-flagged Horizon listings can be clearance buys of identical parts.
