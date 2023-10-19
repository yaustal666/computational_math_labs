from math import cos, pi
from scipy.integrate import quad


def myf(x):
    return x * x - cos(0.5 * pi * x)


def sli(a, b, step):
    i = a
    res = 0
    while i < b + step:
        res += myf(i) * step
        i += step
    return res


def squares_left_integral(a, b, eps):
    i = a
    step = 0.25

    prev = sli(a, b, step)

    step /= 2
    res = sli(a, b, step)

    while abs(prev - res) > eps:
        prev = res
        step /= 2
        res = sli(a, b, step)

    return res


def sri(a, b, step):
    i = a
    res = 0
    while i < b:
        res += myf(i + step) * step
        i += step
    return res


def squares_right_integral(a, b, eps):
    i = a
    step = 0.25

    prev = sri(a, b, step)

    step /= 2
    res = sri(a, b, step)

    while abs(prev - res) > eps:
        prev = res
        step /= 2
        res = sli(a, b, step)

    return res


def tri(a, b, step):
    i = a
    res = 0
    while i < b:
        s1 = myf(i)
        s2 = myf(i + step)

        res += (s1 + s2) / 2 * step
        i += step

    return res


def trapezoid_integral(a, b, eps):
    i = a
    step = 0.25

    prev = tri(a, b, step)

    step /= 2
    res = tri(a, b, step)

    while abs(prev - res) > eps:
        prev = res
        step /= 2
        res = sli(a, b, step)

    return res


def Simpi(a, b, steps):
    step = (b - a) / steps

    k1 = 0
    k2 = 0

    for i in range(1, steps, 2):
        k1 += myf(a + i * step)
        k2 += myf(a + (i + 1) * step)

    return step / 3 * (myf(a) + 4 * k1 + 2 * k2)


def Simpson_integral(a, b, eps):
    i = a
    steps = 2

    prev = Simpi(a, b, steps)

    steps *= 2
    res = Simpi(a, b, steps)

    while abs(prev - res) > eps:
        prev = res
        steps *= 2
        res = Simpi(a, b, steps)

    return res


def Gauss3(a, b):
    t = [0.774597, 0, -0.774597]
    c = [5 / 9, 8 / 9, 5 / 9]

    k = (b - a) / 2

    res = 0
    for i in range(3):
        x = (b + a) / 2 + k * t[i]

        res += c[i] * myf(x)

    res *= k
    return res


def Gauss3_extended(a, b, eps):
    prev = Gauss3(a, b)

    step = (b - a) / 2
    res = 0
    i = 0
    while i < 2:
        res += Gauss3(a + i * step, a + (i + 1) * step)
        i += 1

    i = 2
    while abs(res - prev) > eps:
        print(abs(res - prev))
        prev = res
        res = 0
        step = (b - a) / pow(2, i)
        j = 0

        while j < pow(2, i):
            res += Gauss3(a + i * step, a + (i + 1) * step)
            j += 1

        i += 1

    return res
