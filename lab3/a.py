from math import pi, cos
from sympy import *

def fn(n):
    x = symbols('x')
    a = diff((x*x - cos(pi*x*0.5)), x, n)

    dx = lambdify(x, a)

    return dx 

f = fn(0)

def Lagr4Drvn(xn:list, h, n):

    a = diff((
        f(xn[0])*((x-xn[1])*(x-xn[2])*(x-xn[3])*(x-xn[4])) 
    ), x, n)

# def polyLagrange4Drv2(xn:list, h):
#     f0, f1, f2, f3, f4 = f(xn[0]),f(xn[1]), f(xn[2]), f(xn[3]), f(xn[4])
#     pass

xn = [20, 21, 22, 23, 24]
h = 1

# pol = polyLagrange4Drv2(xn, h)

# for i in range(20, 25):
#     print(fDrv2(i+0.5), " ----- ", pol(i+0.5))
#     print(fDrv2(i-0.5), " ----- ", pol(i-0.5))

