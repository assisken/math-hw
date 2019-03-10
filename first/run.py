import numpy as np
import matplotlib.pyplot as plt
from first.lib import ctg, solve

plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylim(-2, 2)
plt.xlim(-4, 4)

F = lambda x: ctg(x) - x / 3
t1 = np.arange(-5, 5, pow(2, -5))

plt.plot(t1, F(t1), color='#478FC1')
plt.savefig('fig1.png', dpi=150.0)

e = 0.001
t = [(-4, -3.5), (-1.5, -1), (1, 1.5), (3.5, 4)]
res = []
counters = []

for interval in t:
    x, count = solve(interval[0], interval[1], F, e)
    res.append(x)
    counters.append(count)

print(f'Количество итераций: {counters}')
print(f'Приблизительный корни: {[round(x, 3) for x in res]}')
print(f'Их значения: {[round(x, 5) for x in map(F, res)]}')

plt.plot(t1, F(t1), color='#478FC1')
for x in res:
    plt.scatter(x, F(x), color='r')
plt.savefig('fig2.png', dpi=150.0)
