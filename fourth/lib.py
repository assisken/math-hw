import numpy as np
from sympy import diff, symbols


def get_yakobi(functions: list, _symbols: str):
    sym = symbols(_symbols)
    diffs = []
    for func in functions:
        diffs.append([diff(func, s) for s in sym])
    return np.matrix(diffs)
