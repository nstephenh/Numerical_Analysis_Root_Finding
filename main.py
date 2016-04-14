from Newton import newton
from Secant import secant
from Bisection import bisect

def f(x):
    return x**6 -x -1


def fprime(x):
    return (6 * x**5) - 1


newtonapprox = newton(f, fprime, 1.5, .0000000000000001, 100)
secantapprox = secant(f, 1, 2, .0000000000000001, 100)
bisectapprox = bisect(f, 1, 2, .0000000000000001, 1000)
print("Newton", "Secant", "Bisection")
print(newtonapprox, secantapprox, bisectapprox)



#
# from sympy import *
# import numpy
# x = Symbol('x')
# f = x**6 -x -1
# fprime = f.diff(x)
# newton(f, fprime, 1.5, .00000001, 10)
