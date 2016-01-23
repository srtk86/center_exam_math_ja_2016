# -*- coding: utf-8 -*-

from sympy import *

x, a = symbols('x a')
f = (1 + 2 * a) * (1 - x) + (2 - a) * x
f = collect(expand(f), x)
print(f.coeff(x, 1))
