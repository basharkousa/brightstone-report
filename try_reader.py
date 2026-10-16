from pathlib import Path

from src.report.reader import read_orders

orders = read_orders(Path("src/data/orders.csv"))

for order in orders:
    print(
        f"{order.order_id} | "
        f"{order.product} | "
        f"Revenue: ${order.revenue:.2f}"
    )