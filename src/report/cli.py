import argparse
from pathlib import Path
from report.reader import read_orders
from report.report import generate_report
from report.writer import to_json, to_markdown, write_report

def main() -> int:
    """Run the Brightstone reporting application."""
    parser = argparse.ArgumentParser(
        description="Brightstone Logistics daily order reporting tool"
    )

    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
    )

    args = parser.parse_args()

    orders = read_orders(args.input)

    summary = generate_report(orders)

    if args.format == "json":
        content = to_json(summary)
    else:
        content = to_markdown(summary)

    write_report(content, args.output)

    print(f"Report generated successfully: {args.output}")

    return 0