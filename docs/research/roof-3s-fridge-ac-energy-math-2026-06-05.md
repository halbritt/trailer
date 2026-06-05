# Roof-Only 3S Fridge + AC Energy Math

Purpose: estimate whether the permanent roof array alone can carry the Dometic fridge and Velit rooftop AC during Juplaya, without deploying the optional LG ground pair.

This is not a weather forecast or a statistical probability model. It is a daily energy balance using the current build-doc load assumptions and derated solar cases.

## Inputs

Local source docs:

- [Power budget](../power.md)
- [LG455N2W-E6 panel data](../reference/lg455n2w-e6-datasheet.md)
- [Dometic CFX3 95DZ specs](../reference/dometic-cfx3-95dz-specs.md)
- [AIO/Velit evidence brief](aio-inverter-evidence-2026-06-05.md)

Roof solar:

```text
Roof array = 3 x 455 W = 1365 W
Expected clear-day harvest = 1365 W x ~4.4 effective sun-hours
                           = ~6.0 kWh/day before playa dust/shade
```

Expected loads:

| Load | Planning value | Notes |
|---|---:|---|
| Dometic CFX3 95DZ | ~1.2 kWh/day | 1.0-1.3 kWh/day desert-duty band; 4.6 A at 24 V while compressing |
| Velit 2000R | ~2.4 kWh/day | realistic July duty from current power budget |
| 24 V bus / controls overhead | ~0.2 kWh/day | midpoint of the 0.1-0.3 kWh/day budget |
| **Expected total** | **~3.8 kWh/day** | fridge + AC + small DC overhead |

Velit translation:

```text
2.4 kWh/day at ~670 W high draw = ~3.6 full-power hours
Spread over 6 hours  = ~60% average duty
Spread over 8 hours  = ~45% average duty
Spread over 10 hours = ~36% average duty
```

## Expected Case

```text
Roof harvest, clean/good sun  ~6.0 kWh/day
Expected loads                ~3.8 kWh/day
------------------------------------------
Expected daily margin         ~2.2 kWh/day
```

Under expected fridge and AC use, roof-only 3S should be energy-positive on a normal clear day.

## Derated Solar Cases

| Solar condition | Roof harvest | Expected load | Daily margin |
|---|---:|---:|---:|
| Clean / good sun | 6.0 kWh | 3.8 kWh | +2.2 kWh |
| 15% dust/heat loss | 5.1 kWh | 3.8 kWh | +1.3 kWh |
| 25% dust/heat loss | 4.5 kWh | 3.8 kWh | +0.7 kWh |
| 33% ugly dust/shade loss | 4.0 kWh | 3.8 kWh | +0.2 kWh |

The expected case remains positive through a roughly one-third solar derate. At that point there is very little margin, but the fridge + realistic AC day still balances.

## Maximum AC Budget Before Daily Deficit

Using expected non-AC loads:

```text
Fridge + overhead = 1.2 + 0.2 = 1.4 kWh/day
Max AC energy before deficit = roof harvest - 1.4 kWh/day
```

| Solar condition | Max Velit energy before deficit | Approx full-power AC hours at 670 W |
|---|---:|---:|
| Clean / good sun | ~4.6 kWh/day | ~6.9 h |
| 15% dust/heat loss | ~3.7 kWh/day | ~5.5 h |
| 25% dust/heat loss | ~3.1 kWh/day | ~4.6 h |
| 33% ugly dust/shade loss | ~2.6 kWh/day | ~3.9 h |

Current expected Velit use is ~2.4 kWh/day, so the roof-only system clears the clean, moderate, and 25% derate cases with useful margin. In the ugly 33% derate case it is close to break-even.

## Conservative High-Load Check

Use high fridge and overhead numbers:

```text
Fridge high case  = 1.3 kWh/day
Overhead high     = 0.3 kWh/day
Base non-AC load  = 1.6 kWh/day
Realistic AC load = 2.4 kWh/day
Total             = 4.0 kWh/day
```

| Solar condition | Harvest | High-base + realistic AC | Net |
|---|---:|---:|---:|
| Clean / good sun | 6.0 kWh | 4.0 kWh | +2.0 kWh |
| 15% dust/heat loss | 5.1 kWh | 4.0 kWh | +1.1 kWh |
| 25% dust/heat loss | 4.5 kWh | 4.0 kWh | +0.5 kWh |
| 33% ugly dust/shade loss | 4.0 kWh | 4.0 kWh | break-even |

## Conclusion

Roof-only 3S is a credible primary plan for fridge + realistic Velit use.

Operating rule:

- Run roof 3S as the default.
- Treat the LG ground pair as recovery margin for heavy all-day AC, dust/shade, Velit shadow, or a deficit day.
- Watch state of charge after the first real hot day; if the Velit regularly exceeds about 3.5-4.0 kWh/day, the ground pair stops being optional.
