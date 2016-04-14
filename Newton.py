import math

def newton(function, derivative, start, minerror, maxitir):
    i = 0
    error = iteration(function, derivative, start)
    xn = start
    xprev = start
    print("Xn", "%10s" % "f(xn)", "%10s" % "error")
    print(xn, function(xn), error)
    while (minerror < abs(error)) and (i < maxitir):
        xprev = xn  #Assign xprev the previous value of xn
        xn = iteration(function, derivative, xn)
        error = xn-xprev
        print(xn, function(xn), error)
        i += 1
def iteration(f, fprime, xn):
    return xn - f(xn)/fprime(xn)

