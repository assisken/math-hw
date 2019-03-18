from sympy import Symbol, lambdify


def diff(F, symbol):
    x = Symbol(symbol)
    y = F(x)
    yprime = y.diff(x)
    return lambdify(x, yprime, 'numpy')


def easy_iter(F, symbol):
    def wrapped(x):
        if diff(F, symbol)(x) > 0:
            return 0.1
        else:
            return -0.1
    return wrapped


def newton(F, symbol):
    return lambda x: 1 / diff(F, symbol)(x)


def gen_x_i(start, F, e, symbol, _lambda):
    x_old = start
    while abs(F(x_old)) >= e:
        x = x_old - _lambda(F, symbol)(x_old) * F(x_old)
        yield x
        x_old = x
