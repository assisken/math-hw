import itertools

import numpy as np
from sympy import diff, symbols, Matrix, Symbol


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


def easy_iter(F, x, symbol, e):
    r = 0.1
    x_s = symbols(symbol)
    primal = diff(F(x_s), x_s)
    res = primal.subs({symbol: x})
    print(res)
    if abs(e - r * res) >= 1:
        raise Exception(f'{res} не сходится.')
    if res > 0:
        return r
    else:
        return -r


def iter_solve(start, F, e):
    count = 0
    x_old, y_old = start
    x_res, y_res = [x_old], [y_old]

    while True:
        y = float(y_old - easy_iter(F[0], y_old, 'y', e) * F[0](y_old))
        x = float(x_old - easy_iter(F[1], x_old, 'x', e) * F[1](x_old))

        x_res.append(x)
        y_res.append(y)
        if e > np.sqrt((x - x_old) ** 2 + (y - y_old) ** 2):
            break
        x_old, y_old = x, y

    return x_res, y_res, count
