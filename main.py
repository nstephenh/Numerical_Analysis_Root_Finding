from Newton import newton
from Secant import secant
from Bisection import bisect
import math

print("<Problem1>")
def f(x):
    return x**6 -x -1


def fprime(x):
    return (6 * x**5) - 1


newtonapprox = newton(f, fprime, 1.5, .0000000000000001, 100)
secantapprox = secant(f, 1, 2, .0000000000000001, 100)
bisectapprox = bisect(f, 1, 2, .0000000000000001, 1000)
problem1 = (newtonapprox, secantapprox, bisectapprox)

print("</Problem1><Problem3>")
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
#print("Newton", "Secant", "Bisection")
problem3 = (newtonapprox, secantapprox, bisectapprox)

print("</Problem3><Problem2>")

def f(x):
    return math.log(x**2-(2*x)-3)-3-math.log(x+1)


def fprime(x):
    return 1/(x-3)


newtonapprox = newton(f, fprime, 20, .00000001, 50)
secantapprox = secant(f, 20, 25, .00000001, 50)
bisectapprox = bisect(f, 20, 25, .00000001, 50)
problem2 = (newtonapprox, secantapprox, bisectapprox)

print("</Problem2><Problem4a>")
def f(x):
    return x**4 - 11.7*x**3 + 50.88*x**2 - 97.280*x + 68.8128


def fprime(x):
    return 4*x**3 - 35.1*x**2 + 101.76*x - 97.28


newtonapprox = newton(f, fprime, 3, .00000001, 50)
secantapprox = secant(f, 2.5, 3.5, .00001, 50) #Catastrophic cancellation with more zeroes
bisectapprox = bisect(f, 2.5, 3.5, .00000001, 50)
problem4a = (newtonapprox, secantapprox, bisectapprox)

print("</Problem4a><Problem4b>")
def f(x):
    return x**2-5.3*x+6.72


def fprime(x):
    return 2*x-5.3


newtonapprox = newton(f, fprime, 3, .00000001, 50)
secantapprox = secant(f, 2.5, 3.5, .00001, 50) #Catastrophic cancellation with more zeroes
bisectapprox = bisect(f, 2.5, 3.5, .00000001, 50)
problem4b = (newtonapprox, secantapprox, bisectapprox)

print("</Problem4b>")
print("Problem \t  Newton \t Secant \t Bisection")
print("1 \t ", problem1)
print("2 \t ", problem2)
print("3 \t ", problem3)
print("4a \t ", problem4a)
print("4b \t ", problem4b)


