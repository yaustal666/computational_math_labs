from math import cos, sin, pi, log10

import sympy as simp

from matplotlib import pyplot as plt


def myfunc(x):
    return x * x - cos(0.5 * pi * x)


def myf_der(n):
    x = simp.symbols("x")
    a = simp.diff(x * x - simp.cos(0.5 * pi * x), x, n)

    dx = simp.lambdify(x, a)

    return dx


def fact(n):
    res = 1
    i = 0

    while i < n:
        res *= n - i
        i += 1

    return res


def LagrangeN(a, b, n):
    h = (b - a) / n

    print(h)

    def inner(x):
        xn = []

        for i in range(n):
            xn.append(round(a + h * i, 2))
        xn.append(b)

        print(xn)

        res = 0
        for i in range(n + 1):
            k = myfunc(xn[i])
            for j in range(n + 1):
                if i != j:
                    k *= (x - xn[j]) / (xn[i] - xn[j])

            res += k

        return res

    return inner


def Rn(a, b, n):
    fder = myf_der(n + 1)
    c = fact(n + 1)
    h = (b - a) / n

    def inner(x):
        w = 1
        i = a
        while i < b + h:
            w *= x - i
            i += h

        return fder(x) * w / c

    return inner


test = [i / 100 for i in range(40, 91)]
real = [myfunc(i) for i in test]

n = 35
a = 0.4
b = 0.9
lag = LagrangeN(0.4, 0.9, n)
rn = Rn(0.4, 0.9, n)

l = []

for i in test:
    l.append(rn(i))

# for i in test:
#     l.append(lag(i))

plt.plot(test, l)
# plt.plot(test, real, color="orange")
plt.semilogx()

plt.savefig(f"r{n}.png", bbox_inches="tight")
# plt.show()
