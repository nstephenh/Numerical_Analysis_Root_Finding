

def secant(function, start1, start2, minerror, maxitir):
    i = 0
    xn = start1
    xprev = start2
    error = start1-start2
    print("Xn", "%10s" % "f(xn)", "%10s" % "error")
    print(xn, function(xn), error)
    while (minerror < abs(error)) and (i < maxitir):
        xnext = iteration(function, xn, xprev)
        xprev = xn
        xn = xnext
        error = xn-xprev
        print(xn, function(xn), error)
        i += 1

def iteration(f, xn, xprev):
    return xn - f(xn) * ((xn-xprev) / (f(xn)-f(xprev)))

