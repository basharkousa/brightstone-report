import argparse
from pathlib import Path

import logging

from report.exceptions import CSVValidationError

from report.reader import read_orders
from report.report import generate_report
from report.writer import to_json, to_markdown, write_report

logger = logging.getLogger(__name__)

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

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    args = parser.parse_args()

    try:
        orders = read_orders(args.input)

        summary = generate_report(orders)

        if args.format == "json":
            content = to_json(summary)
        else:
            content = to_markdown(summary)

        write_report(content, args.output)

    except FileNotFoundError:
        logger.error("Input file not found: %s", args.input)
        return 1

    except CSVValidationError as error:
        logger.error("Invalid CSV: %s", error)
        return 1

    logger.info("Report generated successfully: %s", args.output)
    return 0
