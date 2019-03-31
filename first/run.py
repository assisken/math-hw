import numpy as np
import matplotlib.pyplot as plt
from first.lib import ctg, solve

plt.grid(True)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.ylim(-2, 2)
plt.xlim(-4, 4)

F = lambda x: ctg(x) - x / 3
t1 = np.arange(-5, 5, 2**(-5))

plt.plot(t1, F(t1), color='#478FC1')
plt.savefig('fig1.png', dpi=150.0)

e = 0.001
t = [(-4, -3.5), (-2, -1), (1, 2), (3.5, 4)]
res = []
counters = []
results: list

plt.plot(t1, F(t1), color='#478FC1')

for interval in t:
    count, results = solve(interval[0], interval[1], F, e)
    res.append(results[-1])
    counters.append(count)
    for i in range(0, len(results)):
        y = [F(x) for x in results[i:i+2]]
        plt.plot(results[i:i+2], y, 'ro-')

print(f'Количество итераций: {counters}')
print(f'Приблизительный корни: {[round(x, 3) for x in res]}')
print(f'Их значения: {[round(x, 5) for x in map(F, res)]}')

plt.savefig('fig2.png', dpi=150.0)
