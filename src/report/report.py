from models import Order


def calculate_total_revenue(orders: list[Order]) -> float:
    total = 0.0

    for order in orders:
        total += order.revenue

    return total


def calculate_product_revenue(orders: list[Order]) -> dict[str, float]:
    # Revenue grouped by product
    product_revenue_dict = {}
    for order in orders:
        product_revenue_dict[order.product] = product_revenue_dict.get(order.product, 0.0) + order.revenue

    return product_revenue_dict


def calculate_customer_spending(orders: list[Order]) -> dict[str, float]:
    # total spending grouped by customer.
    customer_total_spending = {}
    for order in orders:
        customer_total_spending[order.customer] = customer_total_spending.get(order.customer, 0.0) + order.revenue
    return customer_total_spending


def calculate_category_revenue(orders: list[Order]) -> dict[str, float]:
    # Calculate total revenue grouped by category.
    total_revenue_by_category = {}
    for order in orders:
        total_revenue_by_category[order.category] = total_revenue_by_category.get(order.category, 0.0) + order.revenue
    return total_revenue_by_category


def top_five(revenues: dict[str, float]) -> list[tuple[str, float]]:
    """Return the five highest revenue entries."""
    sorted_revenues = sorted(revenues.items(), key=lambda item: item[1], reverse=True)
    top_five_revenues = sorted_revenues[:5]
    return top_five_revenues