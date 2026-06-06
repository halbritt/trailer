#!/usr/bin/env python3
"""Sync the trailer order sheet from a public Google Sheets CSV export."""

from __future__ import annotations

import argparse
import csv
import io
import re
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "docs" / "order-sheet.csv"
MD_PATH = ROOT / "docs" / "order-sheet.md"

SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1zsKxk9gyynfV_CnIDnnsLITYhqe7sRdxiN1UAf_xCsE/export?format=csv"
)
SHEET_EDIT_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1zsKxk9gyynfV_CnIDnnsLITYhqe7sRdxiN1UAf_xCsE/edit?usp=sharing"
)

HEADERS = [
    "type",
    "bucket",
    "category",
    "status",
    "system",
    "qty",
    "item",
    "unit_price",
    "extended_price",
    "basis",
    "source_url",
    "notes",
]

REMAINING_CATEGORY_ORDER = [
    "Power / solar / cabinet",
    "Climate / envelope / awning",
    "Interior / floor / walls",
    "Lighting / switches / security",
    "General consumables contingency",
]


def money_value(value: str) -> Decimal | None:
    value = (value or "").strip()
    if not value or value.upper() == "TBD":
        return None
    negative = value.startswith("(") and value.endswith(")")
    cleaned = re.sub(r"[^0-9.\-]", "", value)
    if not cleaned:
        return None
    try:
        parsed = Decimal(cleaned)
    except InvalidOperation:
        return None
    return -parsed if negative else parsed


def number_value(value: str) -> Decimal | None:
    value = (value or "").strip()
    if not value or not re.fullmatch(r"-?\d+(\.\d+)?", value):
        return None
    return Decimal(value)


def money_cell(value: str) -> str:
    parsed = money_value(value)
    if parsed is None:
        return (value or "").strip()
    return f"{parsed:.2f}"


def money_display(value: Decimal | str | None, *, blank: str = "TBD") -> str:
    if value is None:
        return blank
    if isinstance(value, str):
        parsed = money_value(value)
        if parsed is None:
            return value.strip() or blank
        value = parsed
    return f"${value:,.2f}"


def md_escape(value: object) -> str:
    text = str(value if value is not None else "").strip()
    if not text:
        return ""
    return text.replace("|", "\\|")


def fetch_csv(url: str) -> str:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8-sig")
    except HTTPError as exc:
        body = exc.read(400).decode("utf-8", errors="replace")
        raise SystemExit(f"Google Sheets export failed: HTTP {exc.code}: {body}") from exc
    except URLError as exc:
        raise SystemExit(f"Google Sheets export failed: {exc.reason}") from exc
    if text.lstrip().lower().startswith("<!doctype") or "<html" in text[:200].lower():
        raise SystemExit("Google Sheets export returned HTML, not CSV. Check sharing/export URL.")
    return text


def read_rows(text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text))
    if reader.fieldnames is None:
        raise SystemExit("CSV has no header row.")
    missing = [header for header in HEADERS if header not in reader.fieldnames]
    if missing:
        raise SystemExit(f"CSV is missing expected columns: {', '.join(missing)}")

    rows: list[dict[str, str]] = []
    for raw in reader:
        row = {header: (raw.get(header) or "").strip() for header in HEADERS}
        if not any(row.values()):
            continue
        row["type"] = row["type"].upper()
        row["bucket"] = row["bucket"].strip()
        row["status"] = row["status"].upper()
        row["unit_price"] = money_cell(row["unit_price"])
        row["extended_price"] = money_cell(row["extended_price"])
        rows.append(row)
    return rows


def write_csv(rows: list[dict[str, str]]) -> None:
    with CSV_PATH.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def ext(row: dict[str, str]) -> Decimal:
    return money_value(row["extended_price"]) or Decimal("0")


def bucket_total(rows: list[dict[str, str]], bucket: str) -> Decimal:
    return sum((ext(row) for row in rows if row["type"] == "LINE" and row["bucket"] == bucket), Decimal("0"))


def remaining_category_totals(rows: list[dict[str, str]]) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = defaultdict(lambda: Decimal("0"))
    for row in rows:
        if row["type"] == "LINE" and row["bucket"] == "Remaining":
            totals[row["category"]] += ext(row)
    return dict(totals)


def source_cell(row: dict[str, str]) -> str:
    basis = md_escape(row["basis"])
    url = row["source_url"].strip()
    if basis and url:
        return f"[{basis}]({url})"
    if url:
        return f"[source]({url})"
    return basis


def table(headers: list[str], lines: list[list[str]]) -> list[str]:
    out = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---:" if header in {"Qty", "Unit", "Ext", "Price Signal", "Counted"} else "---" for header in headers) + " |",
    ]
    out.extend("| " + " | ".join(md_escape(cell) for cell in line) + " |" for line in lines)
    return out


def row_lines(rows: list[dict[str, str]], *, bucket: str | None = None, row_type: str | None = None, category: str | None = None) -> list[dict[str, str]]:
    selected = rows
    if row_type is not None:
        selected = [row for row in selected if row["type"] == row_type]
    if bucket is not None:
        selected = [row for row in selected if row["bucket"] == bucket]
    if category is not None:
        selected = [row for row in selected if row["category"] == category]
    return selected


def price_warnings(rows: list[dict[str, str]]) -> list[str]:
    warnings: list[str] = []
    for row in rows:
        if row["type"] != "LINE":
            continue
        qty = number_value(row["qty"])
        unit = money_value(row["unit_price"])
        extended = money_value(row["extended_price"])
        if qty is None or unit is None or extended is None:
            continue
        expected = qty * unit
        if abs(expected - extended) > Decimal("0.01"):
            warnings.append(
                f"{row['item']}: qty x unit = {money_display(expected)}, "
                f"extended_price = {money_display(extended)}"
            )
    return warnings


def render_markdown(rows: list[dict[str, str]], source_url: str) -> str:
    committed = bucket_total(rows, "Committed")
    remaining = bucket_total(rows, "Remaining")
    deferred = bucket_total(rows, "Deferred")
    current_total = committed + remaining
    full_total = current_total + deferred
    categories = remaining_category_totals(rows)
    category_order = REMAINING_CATEGORY_ORDER + sorted(
        category for category in categories if category not in REMAINING_CATEGORY_ORDER
    )

    out: list[str] = [
        "# Juplaya Trailer Order Sheet",
        "",
        f"Generated: {date.today().isoformat()} from the [public Google Sheet]({SHEET_EDIT_URL}).",
        "",
        "This is the build ordering and budget ledger. The [build sheet](juplaya-trailer-context.md) remains the engineering source of truth; this file tracks what is ordered, what remains, rough current pricing, and the math. Spreadsheet source: [Google Sheets CSV export](" + source_url + "). Local CSV: [order-sheet.csv](order-sheet.csv).",
        "",
        "Rules for the numbers:",
        "",
        "- Prices are pre-tax and usually pre-shipping unless the sheet's `extended_price` includes them.",
        "- `extended_price` is the counted budget field; `unit_price` is informational.",
        "- `Receipt needed` means the item is bought/on-hand/ordered, but the repo may still lack the real receipt amount.",
        "- Base trailer purchase, tow vehicle, and receipt-unknown on-hand items are not counted in the fit-out totals unless `extended_price` is populated on a counted `LINE` row.",
        "- The LiTime 5 kW AIO is a return item and is not part of the active build budget.",
        "",
        "## Status Legend",
        "",
    ]

    out.extend(
        table(
            ["Status", "Meaning"],
            [
                ["ON HAND", "Already owned or physically present. Receipt may still be missing."],
                ["PURCHASED", "Bought before this sheet; included only when a counted line has `extended_price`."],
                ["ORDERED", "Ordered for this build. Replace planning values with receipt values when known."],
                ["BUY NOW", "Needed for the Juplaya build and not blocked by an open gate."],
                ["BUY AFTER GATE", "Needed, but wait for measurement/design gate closure before ordering."],
                ["FAB/SOURCE", "Owner fabrication, local sourcing, or mixed hardware stock."],
                ["DEFERRED", "Phase 2 or winter item, not a Juplaya blocker."],
                ["RETURN", "Remove from the active build."],
            ],
        )
    )

    out.extend(
        [
            "",
            "## Budget Math",
            "",
        ]
    )
    out.extend(
        table(
            ["Bucket", "Counted Total", "Notes"],
            [
                ["Priced committed / ordered / purchased fit-out", money_display(committed), "Calculated from `LINE` rows where `bucket = Committed`."],
                ["Remaining Juplaya buy list", money_display(remaining), "Calculated from `LINE` rows where `bucket = Remaining`."],
                ["Current Juplaya fit-out planning total", money_display(current_total), "Committed plus remaining; excludes base trailer, tow vehicle, and receipt-unknown on-hand major gear."],
                ["Deferred Phase 2 / winter list", money_display(deferred), "Calculated from `LINE` rows where `bucket = Deferred`; not required for Juplaya."],
                ["Full visible project list including deferred", money_display(full_total), "Current total plus deferred, with the same exclusions."],
            ],
        )
    )

    out.extend(["", "Remaining Juplaya buy list by category:", ""])
    out.extend(
        table(
            ["Category", "Remaining Total"],
            [[category, money_display(categories[category])] for category in category_order if category in categories],
        )
    )
    out.extend(
        [
            "",
            f"Important interpretation: the current cash-to-spend number is the `{money_display(remaining)}` remaining list, reduced by anything already quietly ordered or already in shop stock. The `{money_display(current_total)}` number is the visible Juplaya fit-out value, not the remaining cash need.",
            "",
            "## Sunk / On-Hand / Receipt-Needed",
            "",
            "These are real build inputs, but they are excluded from the fit-out math unless promoted to a counted `LINE` row.",
            "",
        ]
    )
    sunk_rows = row_lines(rows, row_type="SUNK")
    out.extend(
        table(
            ["Status", "System", "Qty", "Item", "Price Signal", "Counted", "Notes"],
            [
                [
                    row["status"],
                    row["system"],
                    row["qty"],
                    row["item"],
                    money_display(row["unit_price"]) if row["unit_price"] else "TBD",
                    money_display(row["extended_price"], blank="Excluded") if row["extended_price"] else "Excluded",
                    row["notes"],
                ]
                for row in sunk_rows
            ],
        )
    )

    return_rows = row_lines(rows, row_type="RETURN")
    if return_rows:
        out.extend(["", "## Return Items", ""])
        out.extend(
            table(
                ["Status", "System", "Qty", "Item", "Price Signal", "Counted", "Notes"],
                [
                    [
                        row["status"],
                        row["system"],
                        row["qty"],
                        row["item"],
                        money_display(row["unit_price"]) if row["unit_price"] else "TBD",
                        money_display(row["extended_price"], blank="$0.00"),
                        row["notes"],
                    ]
                    for row in return_rows
                ],
            )
        )

    out.extend(["", "## Ordered / Purchased / Priced", ""])
    committed_rows = row_lines(rows, row_type="LINE", bucket="Committed")
    out.extend(
        table(
            ["Status", "System", "Qty", "Item", "Unit", "Ext", "Basis / Source", "Notes"],
            [
                [
                    row["status"],
                    row["system"],
                    row["qty"],
                    row["item"],
                    money_display(row["unit_price"]),
                    money_display(row["extended_price"]),
                    source_cell(row),
                    row["notes"],
                ]
                for row in committed_rows
            ],
        )
    )
    out.extend(["", f"Committed / purchased subtotal: **{money_display(committed)}**.", ""])

    out.extend(["## Remaining Juplaya Buys", ""])
    for category in category_order:
        category_rows = row_lines(rows, row_type="LINE", bucket="Remaining", category=category)
        if not category_rows:
            continue
        out.extend([f"### {category}", ""])
        out.extend(
            table(
                ["Status", "Qty", "Item", "Unit", "Ext", "Basis / Source", "Notes"],
                [
                    [
                        row["status"],
                        row["qty"],
                        row["item"],
                        money_display(row["unit_price"]),
                        money_display(row["extended_price"]),
                        source_cell(row),
                        row["notes"],
                    ]
                    for row in category_rows
                ],
            )
        )
        out.extend(["", f"{category} remaining subtotal: **{money_display(categories[category])}**.", ""])

    out.extend([f"Remaining Juplaya subtotal: **{money_display(remaining)}**.", "", "## Deferred / Not Juplaya", ""])
    deferred_rows = row_lines(rows, row_type="LINE", bucket="Deferred")
    out.extend(
        table(
            ["Status", "System", "Qty", "Item", "Unit", "Ext", "Notes"],
            [
                [
                    row["status"],
                    row["system"],
                    row["qty"],
                    row["item"],
                    money_display(row["unit_price"]),
                    money_display(row["extended_price"]),
                    row["notes"],
                ]
                for row in deferred_rows
            ],
        )
    )
    out.extend(["", f"Deferred subtotal: **{money_display(deferred)}**."])

    warnings = price_warnings(rows)
    if warnings:
        out.extend(
            [
                "",
                "## Sync Warnings",
                "",
                "`extended_price` is still counted for these rows. Fix the Google Sheet only if the difference is not intentional tax/shipping/placeholder handling.",
                "",
            ]
        )
        out.extend(f"- {warning}" for warning in warnings)

    out.extend(
        [
            "",
            "## Sync Procedure",
            "",
            "Edit the public Google Sheet, then run:",
            "",
            "```bash",
            "python3 scripts/sync_order_sheet.py",
            "```",
            "",
            "The script downloads the sheet, rewrites [order-sheet.csv](order-sheet.csv), regenerates this Markdown file, and prints the counted totals.",
        ]
    )

    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=SHEET_URL, help="CSV export URL. Defaults to the trailer Google Sheet.")
    parser.add_argument("--local", action="store_true", help="Regenerate Markdown from the existing local CSV instead of fetching.")
    args = parser.parse_args()

    text = CSV_PATH.read_text() if args.local else fetch_csv(args.url)
    rows = read_rows(text)
    write_csv(rows)
    MD_PATH.write_text(render_markdown(rows, args.url))

    committed = bucket_total(rows, "Committed")
    remaining = bucket_total(rows, "Remaining")
    deferred = bucket_total(rows, "Deferred")
    print(f"Synced {len(rows)} rows")
    print(f"Committed: {money_display(committed)}")
    print(f"Remaining: {money_display(remaining)}")
    print(f"Deferred: {money_display(deferred)}")
    warnings = price_warnings(rows)
    if warnings:
        print(f"Warnings: {len(warnings)} unit/extended mismatches; see docs/order-sheet.md")


if __name__ == "__main__":
    main()
