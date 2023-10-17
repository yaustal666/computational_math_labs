from math import sin, pi, cos


def myf(x):
    return 1 / sin(x) - x**2 - 1


def myfd(x):
    return -cos(x) / (sin(x) * sin(x)) - 2 * x


def mixed_method(a, b, eps):
    i = a
    j = b
    while True:
        j = j - myf(j) / myfd(j)
        i = i - ((myf(i) * (j - i)) / (myf(j) - myf(i)))

        if abs(j - i) < eps:
            break
    return j


ab1 = [0.5, 0.6]
ab2 = [21.9, 21.99]

x1 = mixed_method(ab1[0], ab1[1], 0.00001)
print(x1, myf(x1))

x2 = mixed_method(ab2[0], ab2[1], 0.00001)
print(x2, myf(x2))
