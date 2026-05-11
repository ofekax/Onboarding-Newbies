
def price_is_bigger_then_zero(price: float):
    if price <= 0.0:
        raise ValueError("the price most be bigger than 0")
    return price
