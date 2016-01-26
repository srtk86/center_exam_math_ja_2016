# -*- coding: utf-8 -*-

from numpy import sqrt

def choose_comp_operator(p, q):
    res = []

    try:
        if p in q:
            res.append('0')
    except TypeError:
        print('TypeError is ignored')

    try:
        if q in p:
            res.append('1')
    except TypeError:
        print('TypeError is ignored')

    try:
        if p <= q:
            res.append('2')
    except TypeError:
        print('TypeError is ignored')

    try:
        if p >= q:
            res.append('3')
    except TypeError:
        print('TypeError is ignored')

    return res

def choose_set_operator(p, q, r):
    res = []
    if p == (q.union(r)):
        res.append('4')
    if p == (q.intersection(r)):
        res.append('5')
    return res

set_a = set(range(100))
set_b = set(range(1, 100) * sqrt(7))
set_0 = set([0])
set_empty = set()

print(choose_comp_operator(set_a, set_0))
print(choose_comp_operator(sqrt(28), set_b))
print(choose_set_operator(set_a, set_0, set_a))
print(choose_set_operator(set_empty, set_a, set_b))
