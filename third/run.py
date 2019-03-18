import numpy as np

from third.lib import iter_solve, extract_result, seidel_solve

e = 0.0001

# A = np.matrix([[2, -5, -1],
#                [-1.5, 0.1, 2],
#                [1.25, 0.3, -0.5]])
# B = np.matrix([[200],
#                [600],
#                [500]])

A = np.matrix([[10, 2, -1],
               [-2, -6, -1],
               [1, -3, 12]])
B = np.matrix([[5],
               [24.42],
               [36]])

x = seidel_solve(A, B, e=e)
x1, x2, x3, *_ = extract_result(x)
print([round(x1, 4), round(x2, 4), round(x3, 4)])

x = iter_solve(A, B, e=e)
x4, x5, x6, *_ = extract_result(x)
print([round(x4, 4), round(x5, 4), round(x6, 4)])
