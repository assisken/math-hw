import numpy as np
from functools import reduce
from operator import mul
from typing import List, Tuple

from sympy import symbols, linsolve, expand, Symbol, pprint, Sum, lambdify, diff, factorial


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
    P = sum([points[i][1] * Q(i) for i in range(len(points))])
    return expand(P), x


def A(i: int, x: Symbol, x_list: List[float]):
    b = [Symbol(f'b_{i}') for i in range(len(x_list))]
    if i == 0:
        return b[0]
    res = b[i] * prod([x - x_list[j] for j in range(i)])
    return res


def b_gen(x: Symbol, points: List[Tuple[float, float]]):
    x_list = [i[0] for i in points]
    b_list = [symbols(f'b_{i}') for i in range(len(points))]
    system = []
    for i in range(len(points)):
        A_sum = sum([A(j, x, x_list) for j in range(i + 1)]).subs({x: x_list[i]})
        res = - points[i][1] + A_sum
        system.append(res)
    res = linsolve(system, b_list)
    solve = next(iter(res))

    return solve


def polynom_newton(points: List[Tuple[float, float]]):
    x = symbols('x')
    x_list = [i[0] for i in points]
    b_list = b_gen(x, points)
    L = sum([A(i, x, x_list) for i in range(len(points))])
    sub = {f'b_{i}': b_list[i] for i in range(len(points))}
    func = L.subs(sub)

    return func, x


def error_estimate(F, x, points: List[Tuple[float, float]]):
    interval = (points[0][0], points[-1][0])
    n = len(points)
    M = get_M(F, x, interval)
    w = abs(prod([x - i[0] for i in points]))
    print(f'M = {M}, fac = {n + 1}!')
    R = M / factorial(n + 1) * w
    return R


def get_M(F, x: Symbol, interval: Tuple[float, float]):
    a, b = interval
    df_dx = diff(F, x)
    M = max([df_dx.subs({x: i}) for i in np.arange(a, b, 0.01)])
    return M
