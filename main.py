from Newton import newton
from Secant import secant

def f(x):
    return x**6 -x -1


def fprime(x):
    return (6 * x**5) - 1


newton(f, fprime, 1.5, .00000001, 10)
secant(f, 1, 2, .00000001, 10)


#
# from sympy import *
# import numpy
# x = Symbol('x')
# f = x**6 -x -1
# fprime = f.diff(x)
# newton(f, fprime, 1.5, .00000001, 10)
