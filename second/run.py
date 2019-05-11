import matplotlib.pyplot as plt
import numpy as np

from second.lib import gen_x_i, easy_iter, newton, convergence

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
gamma = np.euler_gamma

plt.plot(t1, F(t1), color='#478FC1')

con1, rcon1 = convergence(F, -0.5, 'x', 0.1)
con2, rcon2 = convergence(F, 1.0, 'x', 0.1)

# exit(0)

if con1:
    print('Условие сходимости выполнено:')
    print(f'{round(-gamma + 1, 3)} <= {round(rcon1, 3)} <= {round(gamma + 1, 3)}')

    res1 = [x1, *gen_x_i(x1, F, e, 'x', easy_iter)]

    for i in range(0, len(res1)):
        y = [F(x) for x in res1[i:i + 2]]
        plt.plot(res1[i:i + 2], y, 'ro-')

    print(f'Для окрестности x1 = {x1}')
    print(f'Число итераций: {len(res1)}')
    print(f'Полученные точки: {[round(x, 5) for x in res1]}')
    print(f'Полученные значения: {[round(x, 5) for x in map(F, res1)]}')

else:
    print('Условие сходимости не выполнено!')
    print(f'{round(-gamma + 1, 3)} <= {round(rcon1, 3)} <= {round(gamma + 1, 3)}')

print()

if con2:
    print('Условие сходимости выполнено:')
    print(f'{round(-gamma + 1, 3)} <= {round(rcon2, 3)} <= {round(gamma + 1, 3)}')

    res2 = [x2, *gen_x_i(x2, F, e, 'x', easy_iter)]

    for i in range(0, len(res2)):
        y = [F(x) for x in res2[i:i + 2]]
        plt.plot(res2[i:i + 2], y, 'ro-')

    print(f'Для окрестности x2 = {x2}')
    print(f'Число итераций: {len(res2)}')
    print(f'Полученные точки: {[round(x, 5) for x in res2]}')
    print(f'Полученные значения: {[round(x, 5) for x in map(F, res2)]}')

else:
    print('Условие сходимости не выполнено!')
    print(f'{round(-gamma + 1, 3)} <= {round(rcon2, 3)} <= {round(gamma + 1, 3)}')

plt.savefig('fig2.png', dpi=150.0)

