from pathlib import Path

import pytest

from report.exceptions import CSVValidationError
from report.reader import read_orders

# AAA : Arrange - Act - Assert


def test_read_valid_csv(tmp_path: Path) -> None:
    """Read valid CSV rows into Order objects."""
    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,quantity,price\n"
        "ORD-001,2026-10-18,John,Laptop,Electronics,2,800\n"
        "ORD-002,2026-10-18,Emma,Mouse,Accessories,3,20\n",
        encoding="utf-8",
    )

    orders = read_orders(csv_file)

    assert len(orders) == 2
    assert orders[0].product == "Laptop"
    assert orders[0].quantity == 2
    assert orders[0].revenue == 1600.0
    assert orders[1].customer == "Emma"


def test_missing_column(tmp_path: Path) -> None:
    """Reject CSV files with missing required columns."""
    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,quantity,price\n"
        "ORD-001,2026-10-18,John,Laptop,2,800\n"
        "ORD-002,2026-10-18,Emma,Mouse,3,20\n",
        encoding="utf-8",
    )
    with pytest.raises(CSVValidationError):
        read_orders(csv_file)


def test_invalid_quantity(tmp_path: Path) -> None:
    """Reject CSV rows containing invalid quantities."""
    csv_file = tmp_path / "orders.csv"

    csv_file.write_text(
        "order_id,date,customer,product,category,quantity,price\n"
        "ORD-001,2026-10-18,John,Laptop,Electronics,abc,800\n"
        "ORD-002,2026-10-18,Emma,Mouse,Accessories,3,20\n",
        encoding="utf-8",
    )
    with pytest.raises(CSVValidationError, match="row 2"):
        read_orders(csv_file)


def test_missing_file(tmp_path: Path) -> None:
    """Raise FileNotFoundError for a missing input file."""
    missing_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_orders(missing_file)
