from math import cos, sin, pi
import matplotlib.pyplot as pp


def myf(x):
    return x**2 - cos(0.5 * pi * x)


def myf_der_1(x):
    return 2 * x + 0.5 * pi * cos(0.5 * pi * x)


def myf_der_2(x):
    return 2 + 0.25 * pi**2 * cos(0.5 * pi * x)


def solve_system_r(down, mid, up, f):
    k = mid[0]
    alp = [-up[0] / k]

    bet = [f[0] / k]

    res = [0 for i in range(len(f))]

    n = len(f)

    for i in range(1, n - 1):
        k = mid[i] + down[i] * alp[i - 1]
        alp.append(-up[i] / k)

        bet.append((f[i] - down[i] * bet[i - 1]) / k)

    bet.append(
        (f[n - 1] - down[n - 1] * bet[n - 2]) / (down[n - 1] * alp[n - 2] + mid[n - 1])
    )

    res[n - 1] = bet[n - 1]

    for i in range(n - 2, -1, -1):
        res[i] = alp[i] * res[i + 1] + bet[i]

    return res


def Spline():
    a = 0.4
    b = 0.9

    n = 10
    h = 0.05
    mu = 0.5
    lm = 0.5

    x = []
    y = []

    for i in range(n + 1):
        x.append(round(a + h * i, 2))
    print(x)
    print("\n")

    for i in range(n + 1):
        y.append(myf(x[i]))
    print(y)
    print("\n")

    down = [0]
    up = [1]
    mid = [2]
    f = []

    for i in range(n - 1):
        down.append(mu)
        up.append(lm)
        mid.append(2)

    down.append(1)
    up.append(0)
    mid.append(2)

    f.append((3 / 2) * (y[1] - y[0]) - (1 / 4) * myf_der_2(x[0]))

    for i in range(1, n):
        f.append((3 * (y[i + 1] - y[i]) / 4) + (3 * (y[i] - y[i - 1]) / 4))

    f.append(myf_der_2(x[n]) / 4 + (3 / 2) * (y[n] - y[n - 1]))

    print(up)
    print("\n")
    print(mid)
    print("\n")
    print(down)
    print("\n")
    print(f)

    m = solve_system_r(down, mid, up, f)
    alpha = []
    beta = []

    for i in range(len(y) - 1):
        alpha.append(6 / h * ((y[i + 1] - y[i]) / h - (m[i + 1] + 2 * m[i]) / 3))
        beta.append(12 / (pow(h, 2)) * ((m[i + 1] + m[i]) / 2 - (y[i + 1] - y[i]) / h))

    s = []
    splain = []
    for i in range(n):
        splain.append(x[i] + h / 8)

    for i in range(len(alpha)):
        s.append(
            y[i]
            + myf_der_2(x[i]) * (splain[i] - x[i])
            + alpha[i] * (splain[i] - x[i]) ** 2 / 2
            + beta[i] * (splain[i] - x[i]) ** 3 / 6
        )

    pp.plot(x, y, color="black")
    pp.plot(splain, s, color="orange")
    pp.show()


Spline()
