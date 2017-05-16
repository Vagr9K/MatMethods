#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
# Data
# Տվյալներ
a, b = 0, 1
h = 0.1
n = (b - a) / h
yzero = 0


# f(x,y)
def dy(x, y):
    return x * math.pow(y, 2) + 1


# Euler's method
# Էյլերի մեթոդ
def euler():
    x = a
    y = yzero
    points = [(x, y)]
    for i in range(1, int(n) + 1):
        x = a + i * h
        y += h * dy(x, y)
        points.append((x, y))
    return points


# Table output
# Աղյուսակի արտատպում
def printtable(pts):
    for i in range(len(pts)):
        print("t={:.0f} X={:.1f} Y={:10.5f}".format(i, pts[i][0], pts[i][1]))

# Graph plotting
# Գրաֆիկի գծում


def plotgraph(pts):
    x = []
    y = []
    for pt in pts:
        x.append(pt[0])
        y.append(pt[1])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Euler")
    plt.plot(x, y, linewidth=1, label='Euler')
    plt.legend()
    plt.show()

# Start
# Սկիզբ


def main():
    pts = euler()
    printtable(pts)
    plotgraph(pts)


if __name__ == "__main__":
    main()
