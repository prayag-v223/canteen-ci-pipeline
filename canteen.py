
from decimal import Decimal, ROUND_HALF_UP


def calculate_total(subtotal):
    """
    Calculate the canteen order total.

    Apply a 10% discount when the subtotal is above ₹300,
    then apply 5% GST to the discounted subtotal.
    Return the final amount rounded to two decimal places.
    """
    subtotal = Decimal(str(subtotal))

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    discount_rate = Decimal("0.10")
    gst_rate = Decimal("0.05")

    if subtotal > Decimal("300"):
        subtotal *= Decimal("1") - discount_rate

    total = subtotal * (Decimal("1") + gst_rate)

    return total.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
