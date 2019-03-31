from functools import reduce
from operator import mul
from typing import List, Tuple

from sympy import symbols, linsolve, expand


def avg(l: List[float]) -> float:
    return sum(l) / len(l)


def prod(iterable):
    return reduce(mul, iterable, 1)



def linear(points: List[Tuple[float, float]]) -> Tuple[float, float]:
    x_sum = lambda i: sum([p[0] ** i for p in points])
    yx_sum = lambda i: sum([p[1] * p[0] ** i for p in points])

    k_s, b_s = symbols('k b')
    system = [
        b_s * x_sum(0) + k_s * x_sum(1) - yx_sum(0),
        b_s * x_sum(1) + k_s * x_sum(2) - yx_sum(1)
    ]
    res = linsolve(system, [k_s, b_s])
    k, b = next(iter(res))

    return k, b


def square(points: List[Tuple[float, float]]) -> Tuple[float, float, float]:
    x_sum = lambda i: sum([p[0]**i for p in points])
    yx_sum = lambda i: sum([p[1] * p[0]**i for p in points])

    a2_s, a1_s, a0_s = symbols('a2 a1 a0')
    system = [
        a0_s * x_sum(0) + a1_s * x_sum(1) + a2_s * x_sum(2) - yx_sum(0),
        a0_s * x_sum(1) + a1_s * x_sum(2) + a2_s * x_sum(3) - yx_sum(1),
        a0_s * x_sum(2) + a1_s * x_sum(3) + a2_s * x_sum(4) - yx_sum(2)
    ]
    res = linsolve(system, [a2_s, a1_s, a0_s])
    a2, a1, a0 = next(iter(res))

    return a2, a1, a0


def polynom_lagrange(points: List[Tuple[float, float]]):
    x = symbols('x')

    Q = lambda i: prod(
        [(x - points[j][0]) / (points[i][0] - points[j][0]) if i != j else 1 for j in range(len(points))]
    )
    L = sum([points[i][1] * Q(i) for i in range(len(points))])
    return expand(L), x
