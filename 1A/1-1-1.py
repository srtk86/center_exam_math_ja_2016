# -*- coding: utf-8 -*-

from scipy.optimize import minimize_scalar
from sympy import *

def cl_f(a):
    return lambda x: (1 + 2 * a) * (1 - x) + (2 - a) * x

def generate_min(x1, x2):
    var('a:z')
    plots = []
    for a1 in [x1, x2]:
        f = cl_f(a1)
        x_min = minimize_scalar(f, bounds=(0, 1), method='bounded')
        plots.append((a1, x_min.fun))

    return solve([a * plots[0][0] + b - plots[0][1], a * plots[1][0] + b - plots[1][1]], [a, b])

print(generate_min(-1, 0))
print(generate_min(1, 2))
