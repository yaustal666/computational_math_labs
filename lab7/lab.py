from math import sin, pi, cos

def myf(x):
    return 1/sin(x) - x**2 - 1

def myfd(x):
    return -cos(x)/(sin(x)*sin(x)) - 2*x - 1

