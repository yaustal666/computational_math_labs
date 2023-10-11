from math import cos, sin, pi
from numpy import arange

def myfunc(x):
    return x*x - cos(0.5*pi*x)

def myfunc2(x):
    return 2 + 0.5*0.5*pi*pi*cos(0.5*pi*x)

def myfunc3(x):
    return -1*0.5*0.5*0.5*pi*pi*pi*sin(0.5*pi*x)

def Lagrange1(x, x1, x2):
    y1 = myfunc(x1)
    y2 = myfunc(x2)

    k1 = (x - x2) / (x1 - x2)
    k2 = (x - x1) / (x2 - x1)

    return y1*k1 + y2*k2

def Lagrange2(x, x1, x2, x3):
    y1 = myfunc(x1)
    y2 = myfunc(x2)
    y3 = myfunc(x3)

    k1 = ((x - x2) * (x - x3)) / ((x1 - x2) * (x1 - x3))
    k2 = ((x - x1) * (x - x3)) / ((x2 - x1) * (x2 - x3))
    k3 = ((x - x1) * (x - x2)) / ((x3 - x1) * (x3 - x2))

    return y1*k1 + y2*k2 + y3*k3

def R1(test, x, x1, x2):
    f = myfunc2(x)
    w = (test - x1) * (test - x2)
    return f * w / 2

def R2(test, x, x1, x2, x3):
    f = myfunc3(x)
    w = (test - x1) * (test - x2) * (test - x3)

    return f * w / 6

# work
test = 0.64
test_true_result = round(myfunc(test), 6)
x1 = 0.55
x2 = 0.6
x3 = 0.65

l1 = round(Lagrange1(test, x2, x3), 6)
l2 = round(Lagrange2(test, x1, x2, x3), 6)

r1 = round(abs(test_true_result - l1), 6)
r2 = round(abs(test_true_result - l2), 6)

r1min = round(abs(R1(0.64, x3, x2, x3)), 6)
r1max = round(abs(R1(0.64, x2, x2, x3)), 6)

r2min = round(abs(R2(0.64, x1, x1, x2, x3)), 6)
r2max = round(abs(R2(0.64, x3, x1, x2, x3)), 6)

print(test_true_result)
print(l1, r1, r1min, r1max)
print(l2, r2, r2min, r2max)

print("is r1 between r1min and r1max:", r1min < r1 < r1max)
print("is r2 between r2min and r2max:", r2min < r2 < r2max)


# Newton

def f1(x1, x2):
    return (myfunc(x2) - myfunc(x1)) / (x2 - x1)

def f2(x1, x2, x3):
    return (f1(x2, x3) - f1(x1, x2)) / (x3 - x1)

def N1(x, x1, x2):
    return myfunc(x1) + f1(x1, x2)*(x - x1)

def N2(x, x1, x2, x3):
    return N1(x, x1, x2) + f2(x1, x2, x3)*(x - x1)*(x - x2)

n1 = round(N1(test, x2, x3), 6)
n2 = round(N2(test, x1, x2, x3), 6)

print(n1, n2)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write("Result of the first lab\n")
    file.write("------L       R      rmin      rmax\n")
    file.write(str(l1) + " " + str(r1) + " " + str(r1min) + " " + str(r1max))
    file.write("\n\n")
    file.write(str(l2) + " " + str(r2) + " " + str(r2min) + " " + str(r2max))