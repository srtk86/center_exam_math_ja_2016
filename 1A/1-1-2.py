# -*- coding: utf-8 -*-

from itertools import product
from fractions import Fraction
from scipy.optimize import minimize_scalar

numerator = range(1, 10)
denominator = range(1, 10)
product = product(numerator, denominator)

min = Fraction(1, 1)
max = Fraction(0, 1)
fracs = (Fraction(n, d) for n, d in product)
for frac in fracs:
    if frac <= Fraction(1, 3):
        f = 2 * frac + 1 - 2 * (frac + 2) / 3
    else:
        f = -frac + 2 - 2 * (frac + 2) / 3
    if f >= 0:
        min = min if min < frac else frac
        max = max if max > frac else frac

print(min)
print(max)
