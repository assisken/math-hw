from sympy import Symbol, lambdify


def diff(F):
    x = Symbol('x')
    y = F(x)
    yprime = y.diff(x)
    return lambdify(x, yprime, 'numpy')


def easy_iter(F):
    def wrapped(x):
        if diff(F)(x) > 0:
            return 0.1
        else:
            return -0.1
    return wrapped


def newton(F):
    return lambda x: 1 / diff(F)(x)


def gen_x_i(start, F, e, _lambda):
    x_old = start
    while abs(F(x_old)) >= e:
        x = x_old - _lambda(F)(x_old) * F(x_old)
        yield x
        x_old = x
