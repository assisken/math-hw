from matplotlib import pyplot as plt
import numpy as np
import sympy as sp
from numpy.ma import sqrt

from sixth.lib import square, trapezoidal, simpson, integrate


def gen_plot():
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.ylim(0, 5)
    plt.xlim(-3, 3)


gen_plot()

e = 0.0001
zeroes = len(str(e).split('.')[1])
a, b = -1, 1

F = lambda x: 1 / (sqrt(1 - x**2) * (1 + x**2))
_F = lambda x: 1 / (sp.sqrt(1 - x**2) * (1 + x**2))

# F = lambda x: x + 1
# _F = lambda x: F(x)

x = np.arange(-2, 2, 0.001)
plt.plot(x, F(x), c='#ff0000')
plt.savefig('fig1.png', dpi=150.0)

square_res = round(square(F, a, b, 1), zeroes)
trap_res = trapezoidal(F, a, b, 1)
simps_res = simpson(F, a, b)
res = integrate(_F, a, b)

print(f'Значение интеграла методом средних квадратов:\n\t{square_res}\n')
print(f'Значение интеграла методом трапеции:\n\t{trap_res}\n')
print(f'Значение интеграла методом Симпсона:\n\t{simps_res}\n')
print(f'Действительное значение интеграла:\n\t{res}\n')
