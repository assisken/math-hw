import itertools
import numpy as np

from sympy import diff, symbols, Matrix, Symbol, lambdify


def get_yakobi(F: Matrix, _symbols: str) -> Matrix:
    sym = symbols(_symbols)
    if isinstance(sym, (str, Symbol)):
        sym = [sym]
    diffs = []
    functions = list(itertools.chain.from_iterable(F.tolist()))
    for func in functions:
        diffs.append([diff(func, s) for s in sym])
    return Matrix(diffs)


def newton_solve(sym, start, F, e):
    x_s, y_s = symbols(sym)
    count = 0
    W = get_yakobi(F, 'x y').inv()
    x_old, y_old = start
    x_res, y_res = [x_old], [y_old]

    while True:
        count += 1
        X = Matrix([[x_old], [y_old]])
        res: Matrix = X - W.subs({x_s: x_old, y_s: y_old}) * F.subs({x_s: x_old, y_s: y_old})
        x, y = map(lambda x: float(x), itertools.chain.from_iterable(res.tolist()))
        x_res.append(x)
        y_res.append(y)
        if e > np.sqrt((x - x_old) ** 2 + (y - y_old) ** 2):
            break
        x_old, y_old = x, y
    return x_res, y_res, count
