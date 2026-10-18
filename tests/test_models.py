import pytest

from report.models import Order


def test_order_revenue() -> None:
    """Revenue should equal quantity multiplied by price."""
    order = Order(
        order_id="ORD-001",
        date="2026-10-18",
        customer="John Smith",
        product="Laptop",
        category="Electronics",
        quantity=2,
        price=800.0,
    )

    assert order.revenue == 1600.0


def test_order_rejects_zero_quantity() -> None:
    """An order with zero quantity should be rejected."""
    with pytest.raises(ValueError):
        Order(
            order_id="ORD-002",
            date="2026-10-18",
            customer="Emma Brown",
            product="Mouse",
            category="Accessories",
            quantity=0,
            price=20.0,
        )


def test_order_rejects_negative_quantity() -> None:
    with pytest.raises(ValueError):
        Order(
            order_id="ORD-002",
            date="2026-10-18",
            customer="Emma Brown",
            product="Mouse",
            category="Accessories",
            quantity=-3,
            price=20.0,
        )


def test_order_rejects_negative_price() -> None:
    with pytest.raises(ValueError):
        Order(
            order_id="ORD-002",
            date="2026-10-18",
            customer="Emma Brown",
            product="Mouse",
            category="Accessories",
            quantity=3,
            price=-10.0,
        )
