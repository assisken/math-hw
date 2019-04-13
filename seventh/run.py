from matplotlib import pyplot as plt
import numpy as np
from numpy import log

from seventh.lib import euler, runge_kutta, gen


def gen_plot():
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)


x = np.arange(-10, 10, 0.001)
F = lambda x, y: 2 ** (x - y)
_F = lambda x, c: log(2 ** x + c) / log(2)
c = -3 / 32
x0, y0 = -3.0, -5.0
end = 10
step = 0.01

gen_plot()
plt.plot(x, _F(x, c), c='#ff0000')
plt.scatter(x0, y0, c='#478FC1')
plt.savefig('fig1.png', dpi=150.0)
plt.clf()

gen_plot()
plt.plot(x, _F(x, c), c='#ff0000')

points = gen(F, x0, y0, step, end, euler)
plt.scatter(x0, y0, c='#ff0000')
plt.plot([i[0] for i in points], [i[1] for i in points], c='#478FC1')
plt.savefig('fig2.png', dpi=150.0)
plt.clf()

gen_plot()
plt.plot(x, _F(x, c), c='#ff0000')

points = gen(F, x0, y0, step, end, runge_kutta)
plt.scatter(x0, y0, c='#ff0000')
plt.plot([i[0] for i in points], [i[1] for i in points], c='#478FC1')
plt.savefig('fig3.png', dpi=150.0)
plt.clf()
