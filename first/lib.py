from numpy import sin, cos

ctg = lambda x: cos(x) / sin(x)


def get_new_range(a, b, x, F):
    if F(a) * F(x) < 0:
        return a, x
    else:
        return x, b


def solve(a, b, F, e):
    x = (a + b) / 2
    count = 0
    results = [x]

    while abs(F(x)) >= e:
        count += 1
        a, b = get_new_range(a, b, x, F)
        x = (a + b) / 2
        results.append(x)

    return count, results
