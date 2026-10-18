from src.report.models import ReportSummary
from src.report.models import Order


def calculate_total_revenue(orders: list[Order]) -> float:
    total = 0.0

    for order in orders:
        total += order.revenue
    return total


def calculate_product_revenue(orders: list[Order]) -> dict[str, float]:
    """Revenue grouped by product"""
    product_revenue_dict: dict[str, float] = {}
    for order in orders:
        product_revenue_dict[order.product] = product_revenue_dict.get(order.product, 0.0) + order.revenue

    return product_revenue_dict


def calculate_customer_spending(orders: list[Order]) -> dict[str, float]:
    """total spending grouped by customer."""
    customer_total_spending: dict[str, float] = {}
    for order in orders:
        customer_total_spending[order.customer] = customer_total_spending.get(order.customer, 0.0) + order.revenue
    return customer_total_spending


def calculate_category_revenue(orders: list[Order]) -> dict[str, float]:
    """Calculate total revenue grouped by category."""
    total_revenue_by_category: dict[str, float] = {}
    for order in orders:
        total_revenue_by_category[order.category] = total_revenue_by_category.get(order.category, 0.0) + order.revenue
    return total_revenue_by_category


def top_five(revenues: dict[str, float]) -> list[tuple[str, float]]:
    """Return the five highest revenue entries."""
    sorted_revenues = sorted(revenues.items(), key=lambda item: item[1], reverse=True)
    top_five_revenues = sorted_revenues[:5]
    return top_five_revenues


def generate_report(orders: list[Order]) -> ReportSummary:
    """Generate a complete sales report from validated orders."""

    # Calculate the total number of orders.
    total_orders = len(orders)

    # Calculate total revenue.
    total_revenue = calculate_total_revenue(orders)

    # Find the five highest-revenue products.
    top_products = top_five(calculate_product_revenue(orders))

    # Find the five highest-spending customers.
    top_customers = top_five(calculate_customer_spending(orders))

    # Sort all categories by revenue, highest first.
    revenue_by_category = sorted(calculate_category_revenue(orders).items(), key=lambda item: item[1], reverse=True)

    return ReportSummary(
        total_orders=total_orders,
        total_revenue=total_revenue,
        top_products=top_products,
        top_customers=top_customers,
        revenue_by_category=revenue_by_category,
    )
