import numpy as np
from numpy.linalg import norm

e = 0.0001

A = np.matrix([[2, -5, -1],
               [-1.5, 0.1, 2],
               [1.25, 0.3, -0.5]])
B = np.matrix([[200],
               [600],
               [500]])

beta = np.matrix([[B.item(i, 0) / A.item(i, i)] for i in range(len(A))])
alpha = np.matrix([[-A.item(i, j) / A.item(i, i) if i != j else 0 for j in range(len(A))] for i in range(len(A))])

if norm(alpha, np.inf) > 1:
    print('Система не сходится, решения нет.')
    exit(0)

X = np.matrix([[0], [0], [0]])
x1 = X.item(0, 0)
x2 = X.item(1, 0)
x3 = X.item(2, 0)

count = 0

while count < 100:
    x1_old = x1
    x2_old = x2
    x3_old = x3

    X = beta + alpha * X

    x1 = X.item(0, 0)
    x2 = X.item(1, 0)
    x3 = X.item(2, 0)

    e1 = abs(x1 - x1_old)
    e2 = abs(x2 - x2_old)
    e3 = abs(x3 - x3_old)

    if e1 <= e and e2 <= e and e3 <= e:
        break

    count += 1

print(f'alpha:\n{alpha}')
print(f'count: {count}')
print(f'x1 = {round(x1, 4)}')
print(f'x2 = {round(x2, 4)}')
print(f'x3 = {round(x3, 4)}')
