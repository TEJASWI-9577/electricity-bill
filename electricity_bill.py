import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def calculate_bill(units, rate_per_unit):
    """Return the bill amount, rounded to two decimal places."""
    try:
        units = Decimal(str(units))
        rate_per_unit = Decimal(str(rate_per_unit))
    except (InvalidOperation, ValueError):
        raise ValueError("units and rate must be valid numbers") from None

    if not units.is_finite() or not rate_per_unit.is_finite():
        raise ValueError("units and rate must be finite numbers")
    if units < 0 or rate_per_unit < 0:
        raise ValueError("units and rate cannot be negative")

    return (units * rate_per_unit).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate an electricity bill from units consumed and a unit rate."
    )
    parser.add_argument("units", help="electricity consumed")
    parser.add_argument("rate", help="price per unit in your currency")
    args = parser.parse_args()

    try:
        amount = calculate_bill(args.units, args.rate)
    except ValueError as error:
        parser.error(str(error))

    print("Electricity Bill")
    print(f"Units consumed: {args.units}")
    print(f"Rate per unit: {args.rate}")
    print(f"Amount due: {amount:.2f}")


if __name__ == "__main__":
    main()
