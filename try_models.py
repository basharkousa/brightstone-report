from src.report.models import Order

order = Order(
    order_id="1001",
    date="2026-10-12",
    customer="John Smith",
    product="Laptop",
    category="Electronics",
    quantity=2,
    price=800.0,
)

print(order)
print(f"Order revenue: ${order.revenue:.2f}")
