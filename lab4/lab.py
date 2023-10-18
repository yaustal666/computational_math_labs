from math import cos, pi
from scipy.integrate import quad


def myf(x):
    return x * x - cos(0.5 * pi * x)


def squares_left_integral(a, b, step):
    i = a
    res = 0
    while i < b + step:
        res += myf(i) * step
        i += step
    return res


def squares_right_integral(a, b, step):
    i = a
    res = 0
    while i < b:
        res += myf(i + step) * step
        i += step
    return res


def trapezoid_integral(a, b, step):
    i = a
    res = 0
    while i < b:
        s1 = myf(i)
        s2 = myf(i + step)

        res += (s1 + s2) / 2 * step
        i += step

    return res


def Simpson_integral(a, b, steps):
    step = (b - a) / steps

    k1 = 0
    k2 = 0

    for i in range(1, steps, 2):
        k1 += myf(a + i * step)
        k2 += myf(a + (i + 1) * step)

    return step / 3 * (myf(a) + 4 * k1 + 2 * k2)


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


def Gauss3_extended(a, b, step):
    i = a
    res = 0
    while i < b - step:
        res += Gauss3(i, i + step)
        i += step
    return res
