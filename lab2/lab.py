from math import cos, pi


def myf(x):
    return x**2 - cos(0.5 * pi * x)


def finite_diff(yn):
    res = []

    tmp = []
    for i in range(1, len(yn)):
        tmp.append(yn[i] - yn[i - 1])
    res.append(tmp)

    for i in range(len(yn) - 2):
        tmp = []
        for j in range(1, len(yn) - 1 - i):
            tmp.append(res[i][j] - res[i][j - 1])
        res.append(tmp)

    return res


def fact(n):
    res = 1
    i = 0

    while i < n:
        res *= n - i
        i += 1

    return res


def forward_Newton(xn, yn):
    step = round(xn[1] - xn[0], 3)

    diff = finite_diff(yn)

    def inner(x):
        res = yn[0]
        t = round((x - xn[0]) / step, 2)
        print(t)
        w = 1

        for i in range(1, len(yn)):
            w *= (t - i + 1) / i
            res += w * diff[i - 1][0]
        return res

    return inner


def backward_Newton(xn, yn):
    step = xn[1] - xn[0]
    diff = finite_diff(yn)

    def inner(x):
        res = yn[-1]
        t = (x - xn[-1]) / step
        print(t)
        w = 1

        for i in range(1, len(yn)):
            w *= (t + i - 1) / i
            res += w * diff[i - 1][-1]
        return res

    return inner


# not done

# def forward_Gauss(xn, yn):
#     step = xn[1] - xn[0]
#     diff = finite_diff(yn)

#     def inner(x):
#         res = yn[len(yn) // 2]
#         t = ((x) - xn[len(xn) // 2]) / step
#         print(t)

#         w = 1

#         tmp = 1
#         for i in range(1, len(yn) // 2):
#             if tmp > 0:
#                 w *= ()


x1 = 0.42
x2 = 0.87
x3 = 0.63

a = 0.4
b = 0.9

xn = [i / 10 for i in range(4, 9)]
yn = [myf(i) for i in xn]
frd = forward_Newton(xn, yn)

print(myf(x1))
print(frd(x1))
print(frd(x2))
print()


bkd = backward_Newton(xn, yn)
print(myf(x2))
print(bkd(x2))
