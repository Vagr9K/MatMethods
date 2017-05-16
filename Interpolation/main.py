#!/usr/bin/env python3
import numpy
import matplotlib.pyplot as plt
PointCount = 5
# Data
# Մուտքային տվյալներ
BaseCoords = [(0.2, 0.2013), (0.5, 0.5211),
              (0.7, 0.7586), (0.95, 1.0995), (1, 1.1752)]
# Additional points to interpolate
# Լրացուցիչ 5 կետեր
TestCoords = [0.3, 0.4, 0.6, 0.8, 0.9]


def P(k, X):
    global BaseCoords, PointCount
    numerator, denominator = 1, 1
    for j in range(PointCount):
        if j == k:
            pass
        else:
            numerator *= (X - BaseCoords[j][0])
            denominator *= (BaseCoords[k][0] - BaseCoords[j][0])
    return numerator / denominator

# Lagrange's equation
# Լագրանժի բանաձև


def L(X):
    global BaseCoords, PointCount
    sum = 0
    for k in range(PointCount):
        sum += BaseCoords[k][1] * P(k, X)
    return sum

# Graph plotting
# Գրաֆիկի գծում


def Plot(count=1000):
    global PointCount, BaseCoords
    xcoordlst = numpy.linspace(BaseCoords[0][0], BaseCoords[
        PointCount - 1][0], count)

    XList = xcoordlst.tolist()
    Y = []
    for X in XList:
        newCoordY = L(X)
        Y.append(newCoordY)
    PlotGraph(XList, Y)


def PlotGraph(X, Y):
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Interpolation")
    plt.plot(X, Y, linewidth=1, label='Predicted Graph')
    plt.legend()
    plt.show()

# Start
# Սկիզբ


def main():
    global TestCoords
    for X in TestCoords:
        print("X: {} Y: {}".format(X, L(X)))
    Plot()


if __name__ == "__main__":
    main()
