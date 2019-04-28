import itertools

import numpy as np
from sympy import diff, symbols, Matrix, Symbol, linsolve, Add, sqrt, pprint


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
    W = get_yakobi(F, sym).inv()
    x_old, y_old = start
    x_res, y_res = [x_old], [y_old]

    while True:
        count += 1
        X = Matrix([[x_old], [y_old]])
        res = X - W.subs({x_s: x_old, y_s: y_old}) * F.subs({x_s: x_old, y_s: y_old})
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
    if abs(e - r * res) >= 1:
        raise Exception(f'{res} не сходится.')
    if res > 0:
        return r
    else:
        return -r


def iter_solve(sym, X0: tuple, F, e):
    x_s, y_s = symbols(sym)
    count = 0
    x_old, y_old = X0
    x_res, y_res = [x_old], [y_old]

    F_list = F.tolist()
    f1: Add
    f2: Add
    f1, f2 = F_list[0][0], F_list[1][0]

    df1_dx1 = diff(f1, x_s)
    df1_dx2 = diff(f1, y_s)
    df2_dx1 = diff(f2, x_s)
    df2_dx2 = diff(f2, y_s)

    df1_dx1_x0 = df1_dx1.subs({x_s: X0[0], y_s: X0[1]})
    df1_dx2_x0 = df1_dx2.subs({x_s: X0[0], y_s: X0[1]})
    df2_dx1_x0 = df2_dx1.subs({x_s: X0[0], y_s: X0[1]})
    df2_dx2_x0 = df2_dx2.subs({x_s: X0[0], y_s: X0[1]})

    la11, la12, la21, la22 = symbols('la11 la12 la21 la22')

    eqns = [
        1 + la11 * df1_dx1_x0 + la12 * df2_dx1_x0,
        la11 * df1_dx2_x0 + la12 * df2_dx2_x0,
        la21 * df1_dx1_x0 + la22 * df2_dx1_x0,
        1 + la11 * df1_dx2_x0 + la22 * df2_dx2_x0,
    ]
    res = linsolve(eqns, [la11, la12, la21, la22])
    la11, la22, la12, la21 = next(iter(res))

    g1 = lambda x, y: x + la11 * f1.subs({x_s: x, y_s: y}) + la12 * f2.subs({x_s: x, y_s: y})
    g2 = lambda x, y: y + la21 * f1.subs({x_s: x, y_s: y}) + la22 * f2.subs({x_s: x, y_s: y})

    while True > e:
        count += 1

        x = float(g1(x_old, y_old))
        y = float(g2(x_old, y_old))

        x_res.append(x)
        y_res.append(y)

        try:
            _e = sqrt(sum([(x - x_old) ** 2, (y - y_old) ** 2]))
        except OverflowError:
            break

        if e >= _e:
            break

        if count > 100:
            break

        x_old = x
        y_old = y

    return x_res, y_res, count
