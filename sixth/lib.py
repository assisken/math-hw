from numpy.ma import arange
from sympy import symbols

import sympy as sp


def square(fn, a, b, n) -> int:
    res = 0.0
    for i in arange(a, b, n):
        x_i = i
        x_i2 = i + 1

        res += fn((x_i + x_i2) / 2) * (x_i2 - x_i)
    return res


def trapezoidal(fn, a, b, n):
    res = 0.0
    for i in arange(a, b, n):
        x_i = i
        x_i2 = i + 1

        res += ((fn(x_i) + fn(x_i2)) / 2) * (x_i2 - x_i)
    return res


def simpson(fn, a, b):
    return ((b - a) / 6) * (fn(a) + 4 * fn((a + b) / 2) + fn(b))


def integrate(fn, _a, _b):
    x, a, b = symbols('x a b')
    F = sp.integrate(fn(x), (x, a, b)).subs({a: _a, b: _b})
    return F.evalf()
