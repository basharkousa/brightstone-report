"""
CSV Reader
list[Order]
generate_report()
ReportSummary

----Markdown
    Human-readable

----JSON
    Machine-readable
"""

import json
from dataclasses import asdict
from pathlib import Path

from report.exceptions import ReportWriteError
from report.models import ReportSummary


def to_json(summary: ReportSummary) -> str:
    """Serialize a report summary to formatted JSON."""
    return json.dumps(asdict(summary), indent=2)


def to_markdown(summary: ReportSummary) -> str:
    """Convert a report summary to Markdown."""
    lines = [
        "# Brightstone Logistics — Daily Order Report",
        "",
        f"**Total orders:** {summary.total_orders}",
        f"**Total revenue:** ${summary.total_revenue:.2f}",
        "",
        "## Top 5 Products",
        "",
        "| Product | Revenue |",
        "|---|---:|",
    ]

    for product, revenue in summary.top_products:
        lines.append(f"| {product} | ${revenue:.2f} |")

    lines.extend(
        [
            "",
            "## Top 5 Customers",
            "",
            "| Customer | Spending |",
            "|---|---:|",
        ]
    )
    for customer, revenue in summary.top_customers:
        lines.append(f"| {customer} | ${revenue:.2f} |")

    lines.extend(
        [
            "",
            "## Revenue by Category",
            "",
            "| Category | Revenue |",
            "|---|---:|",
        ]
    )
    for category, revenue in summary.revenue_by_category:
        lines.append(f"| {category} | ${revenue:.2f} |")

    return "\n".join(lines) + "\n"


def write_report(content: str, output_path: Path) -> None:
    """Write a report to a UTF-8 file."""
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
    except OSError as error:
        raise ReportWriteError(
            f"Cannot write report to {output_path}: {error}"
        ) from error


def format_table(
    heading: str,
    label: str,
    entries: list[tuple[str, float]],
) -> list[str]:
    """Build a Markdown table for ranked revenue data."""
    lines = [
        f"## {heading}",
        "",
        f"| {label} | Revenue |",
        "|---|---:|",
    ]

    for name, amount in entries:
        lines.append(f"| {name} | ${amount:.2f} |")

    return lines
