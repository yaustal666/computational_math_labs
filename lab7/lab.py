from math import sin, pi, cos


def myf(x):
    return 1 / sin(x) - x**2 - 1


def myfd(x):
    return -cos(x) / (sin(x) * sin(x)) - 2 * x


def chord_method(a, b, eps):
    tmp = a
    while True:
        x = tmp - myf(tmp) / (myf(b) - myf(tmp)) * (b - tmp)
        if eps > abs(myf(x) - myf(tmp)):
            return [x, myf(x)]
        tmp = x


ab1 = [0.5, 0.6]
ab2 = [21.9, 21.99]

x1 = chord_method(ab1[0], ab1[1], 0.0001)
print(x1)

x2 = chord_method(ab2[0], ab2[1], 0.0001)
print(x2)
