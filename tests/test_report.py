from dataclasses import asdict

import pytest

from report.models import Order, ReportSummary
from report.report import (
    calculate_total_revenue,
    calculate_product_revenue,
    calculate_customer_spending,
    calculate_category_revenue,
    top_five,
    generate_report,
)


@pytest.fixture
def sample_orders() -> list[Order]:
    """Provide reusable orders for reporting tests."""
    return [
        Order("1", "2026-10-18", "John", "Laptop", "Electronics", 2, 800.0),
        Order("2", "2026-10-18", "Emma", "Mouse", "Accessories", 5, 20.0),
        Order("3", "2026-10-18", "John", "Laptop", "Electronics", 1, 900.0),
    ]


def test_total_revenue(sample_orders: list[Order]) -> None:
    """Calculate the combined revenue of all orders."""
    result = calculate_total_revenue(sample_orders)

    assert result == 2600.0


def test_product_revenue(sample_orders: list[Order]) -> None:
    """Group revenue by product."""
    result = calculate_product_revenue(sample_orders)

    assert result == {
        "Laptop": 2500.0,
        "Mouse": 100.0,
    }


def test_customer_spending(sample_orders: list[Order]) -> None:
    """Group spending by customer."""
    result = calculate_customer_spending(sample_orders)

    assert result == {
        "John": 2500.0,
        "Emma": 100.0,
    }


def test_category_revenue(sample_orders: list[Order]) -> None:
    """Group revenue by category."""
    result = calculate_category_revenue(sample_orders)

    assert result == {
        "Electronics": 2500.0,
        "Accessories": 100.0,
    }


def test_top_five() -> None:
    """Return only the five highest revenue entries."""
    revenues = {
        "A": 100.0,
        "B": 600.0,
        "C": 300.0,
        "D": 500.0,
        "E": 200.0,
        "F": 400.0,
    }

    result = top_five(revenues)

    assert result == [
        ("B", 600.0),
        ("D", 500.0),
        ("F", 400.0),
        ("C", 300.0),
        ("E", 200.0),
    ]


def test_generate_report(sample_orders: list[Order]) -> None:
    """Generate a complete report summary."""
    result = generate_report(sample_orders)

    assert result == ReportSummary(
        total_orders=3,
        total_revenue=2600.0,
        top_products=[
            ("Laptop", 2500.0),
            ("Mouse", 100.0)
        ],
        top_customers=[
            ("John", 2500.0),
            ("Emma", 100.0)
        ],
        revenue_by_category=[
            ("Electronics", 2500.0),
            ("Accessories", 100.0)
        ],
    )
