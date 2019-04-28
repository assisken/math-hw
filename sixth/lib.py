import numpy as np
import sympy as sp
from sympy import symbols


def frange(x, y, jump):
    while x < y:
        yield x
        x += jump


def square(fn, a, b, n) -> int:
    res = 0.0
    for i in frange(a, b - n, n):
        x_i = i
        x_i2 = i + n

        res += fn((x_i + x_i2) / 2) * (x_i2 - x_i)
    return res


def trapezoidal(fn, a, b, n):
    res = 0.0
    for i in frange(a, b - n, n):
        x_i = i
        x_i2 = i + n

        res += ((fn(x_i) + fn(x_i2)) / 2) * (x_i2 - x_i)

    if res == np.inf:
        res = trapezoidal(fn, a + 0.00001, b - 0.00001, n)
    return res


def simpson(fn, a, b):
    return ((b - a) / 6) * (fn(a) + 4 * fn((a + b) / 2) + fn(b))


def integrate(fn, _a, _b):
    x, a, b = symbols('x a b')
    F = sp.integrate(fn(x), (x, a, b)).subs({a: _a, b: _b})
    return F.evalf()
