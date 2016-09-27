#!/usr/bin/env python3
import math


def g(x):
    return math.pow(math.e, 2 * x) - 2


def dg(x):
    return 2 * math.pow(math.e, 2 * x)


def getCD(oldCD):
    oldC = oldCD[0]
    oldD = oldCD[1]
    newC = oldC - g(oldC) * (oldD - oldC) / (g(oldD) - g(oldC))
    newD = oldD - g(oldD) / dg(oldD)
    return (newC, newD)


def findRoot(baseCD, eps):
    currCD = baseCD
    counter = 0
    delta = eps + 1
    while (delta >= eps):
        currCD = getCD(currCD)
        delta = math.fabs(currCD[0] - currCD[1])
        Cn = currCD[0]
        Dn = currCD[1]
        output = "N={}, Cn={}, Dn={}, g(Cn)={}, g(Dn)={}, Delta={}.".format(
            counter, Cn, Dn, g(Cn), g(Dn), delta)
        print(output)
        counter += 1
    return (Cn + Dn) / 2


def main():
    eps = 1e-4
    baseCD = (0, 1)
    root = findRoot(baseCD, eps)
    print("Root = {}".format(root))

if __name__ == "__main__":
    main()
