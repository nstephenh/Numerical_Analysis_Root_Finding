def bisect(f, a, b, minerror, maxiter):
    i = 0
    c = (a+b)/2
    error = (b-a)/(2^i)
    print("a", "%10s" % "b", "%10s" % "c", "%10s" % "b-c", "%10s" % "f(c)")
    while (minerror < abs(error)) and (i < maxiter):
        print(a, "%10s" % b, "%10s" % c, "%10s" % (b-c), "%10s" % f(c))
        error = (b-a)/(2**i)
        a, b, c = iteration(a, b, f)

        i += 1
    return c
def iteration(a, b, f):
    c = (a+b)/2
    if (sign(f(b))*sign(f(c))) <= 0:
        a = c
    else:
        b = c
    return (a, b, c)
def sign(x):
    return abs(x)/x
