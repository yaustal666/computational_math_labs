from math import cos, pi
from scipy.integrate import quad

def myf(x):
    return x*x - cos(0.5*pi*x)

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
        res += myf(i+step) * step
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
        k1 += myf(a + i*step)
        k2 += myf(a + (i+1)*step)

    return step/3 * (myf(a) + 4*k1 + 2*k2)

print('\nleft squares result:')
print(squares_left_integral(0, 5, 0.01))
print(squares_left_integral(0, 5, 0.001))
print(squares_left_integral(0, 5, 0.0001))
print(squares_left_integral(0, 5, 0.00001))

print('\nright squares result: ')
print(squares_right_integral(0, 5, 0.01))
print(squares_right_integral(0, 5, 0.001))
print(squares_right_integral(0, 5, 0.0001))
print(squares_right_integral(0, 5, 0.00001))

print('\ntrapezoid result: ')
print(trapezoid_integral(0, 5, 0.01))
print(trapezoid_integral(0, 5, 0.001))
print(trapezoid_integral(0, 5, 0.0001))
print(trapezoid_integral(0, 5, 0.00001))

print('\nSimpson result: ')
print(Simpson_integral(0, 5, 2))
print(Simpson_integral(0, 5, 4))
print(Simpson_integral(0, 5, 8))
print(Simpson_integral(0, 5, 20))
print(Simpson_integral(0, 5, 40))
print(Simpson_integral(0, 5, 100))
print(Simpson_integral(0, 5, 1000))
print(Simpson_integral(0, 5, 10000))

print('\ntrue result: ', quad(myf, 0, 5))