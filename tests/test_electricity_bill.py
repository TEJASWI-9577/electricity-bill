import unittest
from decimal import Decimal

from electricity_bill import calculate_bill


class CalculateBillTests(unittest.TestCase):
    def test_calculates_units_at_supplied_rate(self):
        self.assertEqual(calculate_bill("120", "0.25"), Decimal("30.00"))

    def test_zero_units_has_no_charge(self):
        self.assertEqual(calculate_bill("0", "0.25"), Decimal("0.00"))

    def test_rounds_half_up_to_cents(self):
        self.assertEqual(calculate_bill("1", "1.235"), Decimal("1.24"))

    def test_rejects_negative_values(self):
        for values in (("-1", "2"), ("1", "-2")):
            with self.subTest(values=values), self.assertRaises(ValueError):
                calculate_bill(*values)

    def test_rejects_non_numeric_and_non_finite_values(self):
        for values in (("abc", "2"), ("NaN", "2"), ("1", "Infinity")):
            with self.subTest(values=values), self.assertRaises(ValueError):
                calculate_bill(*values)


if __name__ == "__main__":
    unittest.main()
