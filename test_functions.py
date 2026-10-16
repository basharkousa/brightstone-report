from report.models import Order
from report.report import (
    calculate_total_revenue,
    calculate_product_revenue,
    calculate_customer_spending,
    calculate_category_revenue,
    top_five,
)

orders = [
    Order("1", "2026-10-12", "John", "Laptop", "Electronics", 2, 800.0),
    Order("2", "2026-10-12", "Emma", "Mouse", "Accessories", 5, 20.0),
    Order("3", "2026-10-13", "John", "Laptop", "Electronics", 1, 900.0),
]

print(calculate_total_revenue(orders))
print(calculate_product_revenue(orders))
print(calculate_customer_spending(orders))
print(calculate_category_revenue(orders))
print(top_five(calculate_product_revenue(orders)))