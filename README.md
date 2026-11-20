# electricity-bill

Generate a bill from the number of electricity units consumed and the price per
unit. The rate is supplied by the user because electricity tariffs vary by
provider and location.

```sh
python electricity_bill.py 120 0.25
```

The command prints the units consumed, rate per unit, and amount due. The amount
is calculated as `units × rate` and rounded to two decimal places.

Run the tests with:

```sh
python -m unittest discover -s tests
```
