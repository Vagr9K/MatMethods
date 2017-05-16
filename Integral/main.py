#!/usr/bin/env python3
import math


# Ֆունկցիա
def f(x):
    return math.sin(math.pow(x, 2))


# Սիմպսոնի բանաձև
def simpson(a, b, n):
    sum = f(a) + f(b)
    h = (b - a) / n
    for i in range(1, n, 2):
        x = a + i * h
        newsum = 4 * f(x)
        sum += newsum
        print("i={} f({})={} 4f(x)={}".format(i, x, f(x), newsum))
        if i + 1 < n:
            x = a + (i + 1) * h
            newsum = 2 * f(x)
            print("i={} f({})={} 2f(x)={}".format(i + 1, x, f(x), newsum))
            sum += newsum
    return sum * h / 3


# Հիմնական ծրագիր
def main():
    a = 0
    b = 2.4
    n = 12
    print("Testing N={}".format(n))
    sum1 = simpson(a, b, n)
    print("Testing N={}".format(int(n / 2)))
    sum2 = simpson(a, b, int(n / 2))
    error = abs(sum2 - sum1) / 12
    print("Results: ")
    print("S{} = {}".format(n, sum1))
    print("S{} = {}".format(int(n / 2), sum2))
    print("Error = {}".format(error))

if __name__ == "__main__":
    main()
