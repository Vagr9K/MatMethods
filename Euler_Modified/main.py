#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt
# Data
# Տվյալներ
a, b = 0, 1
h = 0.1
h2 = 2 * h
yzero = 0


# f(x,y)
def f(x, y):
    return x * math.pow(y, 2) + 1

# Euler's method
# Էյլերի մեթոդ


def euler(step):
    n = (b - a) / step
    x = a
    y = yzero
    points = [(x, y)]
    for i in range(1, int(n) + 1):
        y += step * f(x, y)
        x = a + i * step
        points.append((x, y))
    return points


# Euler's modified method
# Էյլերի մոդիֆիկացված մեթոդ
def eulermod(step):
    n = (b - a) / step
    x = a
    y = yzero
    points = [(x, y)]
    for i in range(1, int(n) + 1):
        x += step / 2
        y += step / 2 * f(x, y)
        ak = f(x, y)
        x += step
        y += ak * step
        if x > b:
            break
        else:
            points.append((x, y))
    return points


# Table output
# Աղյուսակի արտատպում
def printtable(pts):
    for i in range(len(pts)):
        print("t={:.0f} X={:.1f} Y={:5.5f}".format(i, pts[i][0], pts[i][1]))

# Graph plotting
# Գրաֆիկի գծում


def plotgraph(pts, label, show=False):
    x = []
    y = []
    for pt in pts:
        x.append(pt[0])
        y.append(pt[1])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Euler")
    plt.xlim(0, 1.3)
    plt.ylim(0, 1.3)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(x, y, linewidth=1, label=label)
    plt.legend(loc='upper left')
    if show:
        plt.show()

# Start
# Սկիզբ


def main():
    pts = euler(h)
    print("\nEuler 1")
    printtable(pts)
    plotgraph(pts, "Euler 1")

    pts = euler(h2)
    print("\nEuler 2")
    printtable(pts)
    plotgraph(pts, "Euler 2")

    pts = eulermod(h)
    print("\nEuler Modified 1")
    printtable(pts)
    plotgraph(pts, "Euler Modified 1")

    pts = euler(h2)
    print("\nEuler Modified 2")
    printtable(pts)
    plotgraph(pts, "Euler Modified 2", True)


if __name__ == "__main__":
    main()
