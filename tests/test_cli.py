import sys
from pathlib import Path

import pytest
from pytest import MonkeyPatch

from report.cli import main


def test_cli_markdown_success(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    """Generate a Markdown report through the CLI."""
    input_path = tmp_path / "orders.csv"
    output_path = tmp_path / "report.md"

    input_path.write_text(
        "order_id,date,customer,product,category,quantity,price\n"
        "1,2026-10-18,John,Laptop,Electronics,2,800\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "report",
            "--input",
            str(input_path),
            "--output",
            str(output_path),
            "--format",
            "markdown",
        ],
    )

    exit_code = main()

    assert exit_code == 0
    assert output_path.exists()
    assert "**Total revenue:** $1600.00" in output_path.read_text(encoding="utf-8")


def test_cli_missing_input(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    """Return exit code 1 for a missing CSV file."""
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "report",
            "--input",
            str(tmp_path / "missing.csv"),
            "--output",
            str(tmp_path / "report.md"),
        ],
    )

    assert main() == 1


def test_cli_invalid_format(monkeypatch: MonkeyPatch) -> None:
    """Return exit code 2 for an unsupported output format."""
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "report",
            "--input",
            "orders.csv",
            "--output",
            "report.md",
            "--format",
            "xml",
        ],
    )

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2


def test_cli_json_success(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    """Generate a JSON report successfully through the CLI."""
    # TODO: Create a valid CSV file.
    # TODO: Define the JSON output path.
    # TODO: Set command-line arguments using monkeypatch.
    # TODO: Call main().
    # TODO: Assert exit code 0.
    # TODO: Read the generated JSON using json.loads().
    # TODO: Verify total revenue.
    pass


def test_cli_invalid_csv(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    """Return exit code 1 when the CSV contains invalid data."""
    # TODO: Create a CSV file with quantity="abc".
    # TODO: Define the output path.
    # TODO: Set command-line arguments using monkeypatch.
    # TODO: Call main().
    # TODO: Assert exit code 1.
    pass
