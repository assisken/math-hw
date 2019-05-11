from matplotlib import pyplot as plt
import numpy as np
from numpy import log
import pandas as pd

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
end = 101
step = 0.01

gen_plot()
plt.plot(x, _F(x, c), c='#ff0000')
plt.scatter(x0, y0, c='#478FC1')
plt.savefig('fig1.png', dpi=150.0)
plt.clf()

gen_plot()
plt.plot(x, _F(x, c), c='#ff0000')

points1 = gen(F, x0, y0, step, end, euler)
plt.scatter(x0, y0, c='#ff0000')
plt.plot([i[0] for i in points1], [i[1] for i in points1], c='#478FC1')
plt.savefig('fig2.png', dpi=150.0)
plt.clf()

gen_plot()
plt.plot(x, _F(x, c), c='#ff0000')

points2 = gen(F, x0, y0, step, end, runge_kutta)
plt.scatter(x0, y0, c='#ff0000')
plt.plot([i[0] for i in points2], [i[1] for i in points2], c='#478FC1')
plt.savefig('fig3.png', dpi=150.0)
plt.clf()

check = [-2.5, -2, -1, 0, 1, 2, 5, 10, 20, 30, 50, 100]
true = [_F(x, c) for x in check]
predicate = lambda point: round(point[0], 11) in check
euler = [point[1] for point in filter(predicate, points1)]
rk = [point[1] for point in filter(predicate, points2)]
data = {
    'True': list(map(lambda x: round(x, 2), true)),
    'Euler': list(map(lambda x, y: round(x - y, 6), true, euler)),
    'Runge-Kutta': list(map(lambda x, y: round(x - y, 5), true, rk))
}
frame = pd.DataFrame(data, check)
print(frame)
