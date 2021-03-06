import inspect

import numpy as np
from matplotlib import pyplot as plt
from sympy import symbols, prod, pprint, Lambda, Array, Point, simplify, expand, lambdify

from fifth.lib import polynom_lagrange, square, linear, polynom_newton, error_estimate


def gen_plot(points: list):
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.ylim(150, 250)
    plt.xlim(0, 11)

    for point in points:
        plt.scatter(point[0], point[1], c='#478FC1')


def print_polinome(L, x):
    _L = lambdify([x], L)
    _x = np.arange(0, 11, 0.02)
    plt.plot(_x, _L(_x), color='#ff0000')


points = [
    (1, 178),
    (2, 182),
    (3, 190),
    (4, 199),
    (5, 200),
    (6, 213),
    (7, 220),
    (8, 231),
    (9, 235),
    (10, 242),
]

gen_plot(points)
plt.savefig('fig1.png', dpi=150.0)

k, b = linear(points)
print('График линейной функции:')
print(f'y = {round(k, 1)}x + {round(b, 1)},')
print(f'где:\tk = {round(k, 1)},')
print(f'\t\tb = {round(b, 1)}\n')
x = np.arange(0, 11, 0.02)
F = lambda x: k * x + b
plt.plot(x, F(x), c='#ff0000')
plt.savefig('fig2.png', dpi=150.0)
plt.clf()

gen_plot(points)
a2, a1, a0 = square(points)
print('График квадратичной функции:')
print(f'y = {round(a2, 1)}x^2 + {round(a1, 1)}x + {round(a0, 1)},')
print(f'где:\ta2 = {round(a2, 5)}')
print(f'\t\ta1 = {round(a1, 5)}')
print(f'\t\ta0 = {round(a0, 5)}')

x = np.arange(0, 11, 0.02)
F = lambda x: a2 * x ** 2 + a1 * x + a0
plt.plot(x, F(x), c='#ff0000')
plt.savefig('fig3.png', dpi=150.0)
plt.clf()

gen_plot(points)
L, x = polynom_lagrange(points)
R = error_estimate(L, x, points)
print('Полином Лагранжа равен:')
pprint(L, wrap_line=False)
print(f'Результат полинома:\t{[L.subs({x: i + 1}) for i in range(len(points))]}')
print(f'Значения точек:\t\t{[point[1] for point in points]}')
print('Погрешность:')
pprint(R, wrap_line=False)
print()
print_polinome(L, x)
plt.savefig('fig4.png', dpi=150.0)
plt.clf()

gen_plot(points)
L, x = polynom_newton(points)
R = error_estimate(L, x, points)
print('Полином Ньютона равен:')
pprint(L, wrap_line=False)
print(f'Результат полинома:\t{[L.subs({x: i + 1}) for i in range(len(points))]}')
print(f'Значения точек:\t\t{[point[1] for point in points]}')
print('Погрешность:')
pprint(R, wrap_line=False)
print()
print_polinome(L, x)
plt.savefig('fig5.png', dpi=150.0)
plt.clf()

it = 5.62563982289509e-6
print(round(it, 5))
