import matplotlib.pyplot as plt
import numpy as np

from second.lib import gen_x_i, easy_iter, newton

plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylim(-2, 2)
plt.xlim(-2, 2)

F = lambda x: 7**x - 6*x - 2
t1 = np.arange(-5, 5, 0.02)

plt.plot(t1, F(t1), color='#478FC1')
plt.savefig('fig1.png', dpi=150.0)

e = 0.001
x1 = -0.5
x2 = 1
res1 = [x1, *gen_x_i(x1, F, e, 'x', newton)]
res2 = [x2, *gen_x_i(x2, F, e, 'x', newton)]

plt.plot(t1, F(t1), color='#478FC1')

for i in range(0, len(res1)):
    y = [F(x) for x in res1[i:i + 2]]
    plt.plot(res1[i:i + 2], y, 'ro-')

for i in range(0, len(res2)):
    y = [F(x) for x in res2[i:i + 2]]
    plt.plot(res2[i:i + 2], y, 'ro-')

plt.savefig('fig2.png', dpi=150.0)

print(f'Для окрестности x1 = {x1}')
print(f'Число итераций: {len(res1)}')
print(f'Полученные точки: {[round(x, 5) for x in res1]}')
print(f'Полученные значения: {[round(x, 5) for x in map(F, res1)]}')
print()
print(f'Для окрестности x2 = {x2}')
print(f'Число итераций: {len(res2)}')
print(f'Полученные точки: {[round(x, 5) for x in res2]}')
print(f'Полученные значения: {[round(x, 5) for x in map(F, res2)]}')
