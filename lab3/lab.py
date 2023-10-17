from math import pi, cos, sin, factorial
from sympy import *

def fn(n):
    x = symbols('x')
    a = diff((x*x - cos(pi*x*0.5)), x, n)

    dx = lambdify(x, a)

    return dx

f = fn(0)
f2 = fn(2)

def Lagr4Drvn(xn:list, h, n):
    x = symbols('x')
    a = diff((
        f(xn[0])*((x-xn[1])*(x-xn[2])*(x-xn[3])*(x-xn[4])) / (24*h) + \
        f(xn[1])*((x-xn[0])*(x-xn[2])*(x-xn[3])*(x-xn[4])) / ((-6)*h) + \
        f(xn[2])*((x-xn[0])*(x-xn[1])*(x-xn[3])*(x-xn[4])) / (4*h) + \
        f(xn[3])*((x-xn[0])*(x-xn[1])*(x-xn[2])*(x-xn[4])) / ((-6)*h) + \
        f(xn[4])*((x-xn[0])*(x-xn[1])*(x-xn[2])*(x-xn[3])) / (24*h) ), x, n)

    dx = lambdify(x, a)

    return dx

xn = [20, 21, 22, 23, 24]
h = 1

l = Lagr4Drvn(xn, h, 0)
l2 = Lagr4Drvn(xn, h, 2)

def R4Drv(xn:list, n):

    x, y = symbols('x y')
    a = diff((pi**5 * sin(pi*y/2) / 32)/120 * (x - xn[0])*(x - xn[1])*(x - xn[2])*(x-xn[3])*(x-xn[4]), x, n)

    dx = lambdify([x, y], a)
    return dx

r2 = R4Drv(xn, 2)

test = 22.3

r2real = l2(test) - f2(test)


xmin = 22
xmax = 20

r2min = r2(xmin, xmin)
r2max = r2(xmax, xmax)

with open("lafrange_poly_compare.txt", "w", encoding="utf-8") as file:
    i = 0.4
    while i <= 0.9 :
        file.write(str(i))
        file.write(" : ")
        file.write("f'': ")
        file.write(str(f2(i)))
        file.write("\n")
        file.write("----- L'': ")
        file.write(str(l2(i)))
        file.write("\n---------------------------------------------\n")
        i = round(i + 0.05, 2)
    file.write("Rmin: ")
    file.write(str(r2min))
    file.write("\n")
    file.write("R: ")
    file.write(str(r2real))
    file.write("\n")
    file.write("Rmax: ")
    file.write(str(r2max))
