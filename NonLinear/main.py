#!/usr/bin/env python3
import math


# Ֆունկցիա
def f(x):
    return x * math.exp(2 * x) - 2

# Derivative
# Ֆունկցիայի ածանցյալ


def df(x):
    return (2 * x + 1) * math.exp(2 * x)


# Determiantion of Cn and Dn
# Cn և Dn փոփոխականների որոշում
def getCD(oldCD):
    oldC = oldCD[0]
    oldD = oldCD[1]
    newC = oldC - f(oldC) * (oldD - oldC) / (f(oldD) - f(oldC))
    newD = oldD - f(oldD) / df(oldD)
    return (newC, newD)


# Determination of equation root
# Հավասարման արմատի որոշում
def findRoot(baseCD, eps):
    currCD = baseCD
    counter = 1
    delta = eps + 1
    while (delta >= eps):
        currCD = getCD(currCD)
        delta = math.fabs(currCD[0] - currCD[1])
        Cn = currCD[0]
        Dn = currCD[1]
        output = "N={}, Cn={}, Dn={}, g(Cn)={}, g(Dn)={}, Delta={}.".format(
            counter, Cn, Dn, f(Cn), f(Dn), delta)
        print(output)
        counter += 1
    return (Cn + Dn) / 2


# Start
# Ծրագրի սկիզբ
def main():
    eps = 1e-4
    baseCD = (0, 1)
    root = findRoot(baseCD, eps)
    print("Root = {}".format(root))


if __name__ == "__main__":
    main()
