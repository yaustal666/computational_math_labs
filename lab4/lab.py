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


left = 0.4
right = 0.9
print("\nleft squares result:")
print(squares_left_integral(left, right, 0.1))
print(squares_left_integral(left, right, 0.001))
print(squares_left_integral(left, right, 0.0001))
print(squares_left_integral(left, right, 0.00001))

print("\nright squares result: ")
print(squares_right_integral(left, right, 0.01))
print(squares_right_integral(left, right, 0.001))
print(squares_right_integral(left, right, 0.0001))
print(squares_right_integral(left, right, 0.00001))

print("\ntrapezoid result: ")
print(trapezoid_integral(left, right, 0.01))
print(trapezoid_integral(left, right, 0.001))
print(trapezoid_integral(left, right, 0.0001))
print(trapezoid_integral(left, right, 0.00001))

print("\nSimpson result: ")
print(Simpson_integral(left, right, 2))
print(Simpson_integral(left, right, 4))
print(Simpson_integral(left, right, 8))
print(Simpson_integral(left, right, 20))
print(Simpson_integral(left, right, 40))
print(Simpson_integral(left, right, 100))
print(Simpson_integral(left, right, 1000))
print(Simpson_integral(left, right, 10000))


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


print("\nGauss3 result :")
print(Gauss3(left, right))

print("\nGauss3_extended result :")
print(Gauss3_extended(left, right, 0.1))

print("\ntrue result: ", quad(myf, left, right))

h = [0.1, 0.01, 0.001, 0.0001, 0.00001]
with open("res.txt", "w", encoding="utf=8") as f:
    f.write("Results:\n")
    f.write("Right squares:\n")

    for i in h:
        f.write("h=")
        f.write(str(i))
        f.write("       ")
        f.write(str(squares_right_integral(left, right, i)))
        f.write("\n")

    f.write("\n")
    f.write("Left squares:\n")

    for i in h:
        f.write("h=")
        f.write(str(i))
        f.write("       ")
        f.write(str(squares_left_integral(left, right, i)))
        f.write("\n")

    f.write("\n")
    f.write("Trapezoid:\n")

    for i in h:
        f.write("h=")
        f.write(str(i))
        f.write("       ")
        f.write(str(trapezoid_integral(left, right, i)))
        f.write("\n")

    f.write("\n")
    f.write("Simpson:\n")

    for i in [2, 4, 10, 1000, 10000]:
        f.write("h=")
        f.write(str(i))
        f.write("       ")
        f.write(str(Simpson_integral(left, right, i)))
        f.write("\n")

    f.write("\n")
    f.write("Gauss:\n")

    f.write(str(Gauss3(left, right)))

    f.write("\n\n")
    f.write("Gauss_ext:\n")
    f.write("h = 0.1      ")
    f.write(str(Gauss3_extended(left, right, 0.1)))
