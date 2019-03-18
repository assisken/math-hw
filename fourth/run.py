import numpy as np

from sympy import tan
from sympy import symbols

from fourth.lib import get_yakobi

x, y = symbols('x y')

functions = [
    tan(x*y + 0.1) - x**2,
    0.6 * x**2 + 2 * y**2 - 1
]

W = get_yakobi(functions, 'x y')
print(W)
