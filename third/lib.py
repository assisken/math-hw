import itertools
import numpy as np

from numpy.linalg import norm


def extract_result(x: np.matrix):
    return set(itertools.chain.from_iterable(x.tolist()))


def iter_solve(A: np.matrix, B: np.matrix, **kwargs):
    length = len(A)
    beta = np.matrix([[B.item(i, 0) / A.item(i, i)] for i in range(len(A))])
    alpha = np.matrix([[-A.item(i, j) / A.item(i, i) if i != j else 0 for j in range(len(A))] for i in range(len(A))])

    if norm(alpha, np.inf) > 1:
        raise Exception('Система не сходится, решения нет')

    e = kwargs.get('e', 0.0001)
    x = np.matrix([[.0] for _ in range(length)])

    while True:
        x_old = np.copy(x)
        x = beta + alpha * x
        if np.sqrt(sum((x[i] - x_old[i]) ** 2 for i in range(length))) <= e:
            break

    return x


def seidel_solve(A: np.matrix, B: np.matrix, **kwargs):
    e = kwargs.get('e', 0.001)
    n = len(A)
    x = [.0 for _ in range(n)]

    while True:
        x_old = np.copy(x)
        for i in range(n):
            s1 = sum(A.item(i, j) * x[j] for j in range(i))
            s2 = sum(A.item(i, j) * x_old[j] for j in range(i + 1, n))
            x[i] = (B.item(i, 0) - s1 - s2) / A.item(i, i)

        if e >= np.sqrt(sum((x[i] - x_old[i]) ** 2 for i in range(n))):
            break

    return np.matrix([[i] for i in x])
