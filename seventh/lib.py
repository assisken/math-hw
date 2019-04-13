from numpy.ma import arange


def gen(f, x0, y0, step, end, method):
    points = [(x0, y0)]
    for i in arange(x0 + step, end, step):
        xn, yn = points[-1]
        x = i
        y = method(f, xn, yn, step)
        points.append((x, y))
    return points


def euler(f, xn, yn, h):
    return yn + h * f(xn, yn)


def runge_kutta(f, xn, yn, h):
    k1 = f(xn, yn)
    k2 = f(xn + h / 2, yn + h / 2 * k1)
    k3 = f(xn + h / 2, yn + h / 2 * k2)
    k4 = f(xn + h, yn + h * k3)
    return yn + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
