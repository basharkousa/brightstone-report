from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    order_id: str
    date: str
    customer: str
    product: str
    category: str
    quantity: int
    price: float

    @property
    def revenue(self) -> float:
        return self.quantity * self.price

    def __post_init__(self) -> None:
        if self.quantity <= 0:
            raise ValueError("Quantity mustn't be negative!!")
        if self.price <= 0:
            raise ValueError("Price must be grater than zero!!")

@dataclass(frozen= True)
class ReportSummary:
    """Contains the calculated statistics for an order report."""
    total_orders: int
    total_revenue: float
    top_products: list[tuple[str, float]]
    top_customers: list[tuple[str, float]]
    revenue_by_category: list[tuple[str, float]]
