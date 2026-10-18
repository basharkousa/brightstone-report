import csv
from pathlib import Path
from report.exceptions import CSVValidationError
from report.models import Order

def read_orders(file_path: Path) -> list[Order]:
    """Read orders from a CSV file and validate their fields."""
    orders: list[Order] = []

    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file,strict= True)
        required_columns = {
            "order_id",
            "date",
            "customer",
            "product",
            "category",
            "quantity",
            "price",
        }

        actual_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - actual_columns

        if missing_columns:
            raise CSVValidationError(
                f"Missing required CSV columns: {', '.join(sorted(missing_columns))}"
            )


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
            except (ValueError, KeyError, TypeError) as error:
                raise CSVValidationError(
                    f"Invalid CSV data at row {row_number}: {error}"
                ) from error

            orders.append(order)

    return orders
