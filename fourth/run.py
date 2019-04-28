import numpy as np
from matplotlib import pyplot as plt
from numpy.ma import arctan
from sympy import symbols, Matrix, atan, sqrt, tan

from fourth.lib import newton_solve, iter_solve

plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylim(-1.5, 1.5)
plt.xlim(-1.5, 1.5)

_f1 = lambda x, y: tan(x * y + 0.1) - x ** 2
f1 = lambda x: (arctan(x ** 2) - 0.1) / x
_f2 = lambda x, y: 0.6 * x ** 2 + 2 * y ** 2 - 1
f2 = lambda y: np.sqrt(5 / 3 - 10 / 3 * y ** 2)

x = np.linspace(-1.5, 1.5, 101)
y = np.linspace(-1.5, 1.5, 101)
X, Y = np.meshgrid(x, y)
F = _f2(X, Y)
plt.contour(X, Y, F, [0])
plt.plot(x, f1(x))
plt.savefig('fig1.png', dpi=150)

x_s, y_s = symbols('x y')
F = Matrix([
    [_f1(x_s, y_s)],
    [_f2(x_s, y_s)]
])

e = 0.0001
starts = [
    (1.0, 0.5),
    # (0.5, -1),
    # (-1.0, -0.5),
    # (-0.5, 1),
]

# print('Метод Ньютона:')
# for start in starts:
#     x_res, y_res, count = newton_solve('x y', start, F, e)
#     print(f'\tДля точки {start}:')
#     print(f'\tКоличество итераций: {count}')
#     print(f'\t\tx = {round(x_res[-1], 4)}; y = {round(y_res[-1], 4)}')
#
#     plt.plot(x_res, y_res, 'ro-', color='#ff0000')
# plt.savefig('fig2.png', dpi=150)
#


def test1():
    for start in starts:
        x_res, y_res, count = newton_solve('x y', start, F, e)


def test():
    for start in starts:
        x_res, y_res, count = iter_solve('x y', start, F, e)


for start in starts:
    x_res, y_res, count = iter_solve('x y', start, F, e)
    # print(f'\tДля точки {start}:')
    # print(f'\tКоличество итераций: {count}')
    # print(f'\t\tx = {round(x_res[-1], 4)}; y = {round(y_res[-1], 4)}')

    # plt.plot(x_res, y_res, 'ro-', color='#ff0000')
plt.savefig('fig3.png', dpi=150)
# plt.show()

if __name__ == '__main__':
    import timeit
    print('Метод простых итераций:')
    res1 = timeit.timeit("test()", setup="from __main__ import test", number=1)
    print(f'{res1} sec')
    print('Метод Ньютона:')
    res2 = timeit.timeit("test1()", setup="from __main__ import test1", number=1)
    print(f'{res2} sec')
