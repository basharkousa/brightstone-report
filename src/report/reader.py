import csv
from pathlib import Path

from src.report.models import Order


def read_orders(file_path: Path) -> list[Order]:
    orders: list[Order] = []

    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):
            try:
                order = Order(
                    order_id=row["order_id"],
                    date=row["date"],
                    customer=row["customer"],
                    product=row["product"],
                    category=row["category"],
                    quantity=int(row["quantity"]),
                    price=float(row["price"]),
                )
            except (ValueError, KeyError) as error:
                raise ValueError(
                    f"Invalid CSV data at row {row_number}: {error}"
                ) from error

            orders.append(order)

    return orders
