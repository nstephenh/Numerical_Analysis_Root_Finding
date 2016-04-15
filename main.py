from Newton import newton
from Secant import secant
from Bisection import bisect
import math

def f(x):
    return x**6 -x -1


def fprime(x):
    return (6 * x**5) - 1


newtonapprox = newton(f, fprime, 1.5, .0000000000000001, 100)
secantapprox = secant(f, 1, 2, .0000000000000001, 100)
bisectapprox = bisect(f, 1, 2, .0000000000000001, 1000)
print("Newton", "Secant", "Bisection")
print(newtonapprox, secantapprox, bisectapprox)


def troughDerivative(h, L, r):
    return L * (h**2/math.sqrt(r**2-h**2)-r/math.sqrt(1-h**2/r**2)-math.sqrt(r**2-h**2))


def troughFunction(h, L, r, V):
    return L * ((0.5 * math.pi * r**2) - (r**2 * math.asin(h/r)) - (h * math.sqrt(r**2-h**2)))-V


def troughGiven(h):
    return troughFunction(h, 15, 2, 75)


def troughDerivativeGiven(h):
    return troughDerivative(h, 15, 2)

newtonapprox = newton(troughGiven, troughDerivativeGiven, 1, .0001, 100)
secantapprox = secant(troughGiven, 0, 2, .0001, 100)
bisectapprox = bisect(troughGiven, 0, 2, .0001, 1000)
print("Newton", "Secant", "Bisection")
print(newtonapprox, secantapprox, bisectapprox)

