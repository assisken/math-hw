import numpy as np
from matplotlib import pyplot as plt
from numpy.ma import arctan
from sympy import symbols, Matrix
from sympy import tan

from fourth.lib import newton_solve

plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylim(-1.5, 1.5)
plt.xlim(-1.5, 1.5)

_f1 = lambda x, y: tan(x * y + 0.1) - x ** 2
f1 = lambda x: (arctan(x**2) - 0.1) / x
_f2 = lambda x, y: 0.6 * x ** 2 + 2 * y ** 2 - 1

x = np.linspace(-1.5, 1.5, 101)
y = np.linspace(-1.5, 1.5, 101)
X, Y = np.meshgrid(x, y)
F = _f2(X, Y)
plt.contour(X, Y, F, [0])
plt.plot(x, f1(x))

x_s, y_s = symbols('x y')
F = Matrix([
    [_f1(x_s, y_s)],
    [_f2(x_s, y_s)]
])

e = 0.0001
starts = [
    (1.0, 0.5),
    (0.0, -0.5),
    (-1.0, -0.5),
    (-0.0, 0.5),
]
print('Метод Ньютона:')
for start in starts:
    x0, y0 = start
    x_res, y_res, count = newton_solve('x y', (x0, y0), F, e)
    print(f'\tДля точки {start}:')
    print(f'\tКоличество итераций: {count}')
    print(f'\t\tx = {x_res[-1]}; y = {y_res[-1]}')

    plt.plot(x_res, y_res, 'ro-', color='#ff0000')
plt.savefig('fig1.png', dpi=150)
