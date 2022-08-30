import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy
from sympy import symbols

# import expansion
from mpl_toolkits import mplot3d


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def BaseCases(x, y):
    # Function 1: (a+ib)^4 = a^4 - 6a^2b^2 + b^4 + i(4a^3b - 4ab^3)
    # real
    # return pow(x,4) - 6 * pow(x*y,2) + pow(y^4)
    # imaginary
    # return 4 * (y * pow(x, 3) - x * pow(y, 3))
    if sys.argv[1] == "rf1":
        return pow(x, 4) - 6 * pow(x * y, 2) + pow(y, 4)
    elif sys.argv[1] == "if1":
        return 4 * (y * pow(x, 3) - x * pow(y, 3))
    # Function 2: a^2-b^2 + i(2ab)
    # real
    # return pow(x, 2) - pow(y, 2)
    # imaginary
    # return 2*x*y
    elif sys.argv[1] == "rf2":
        return pow(x, 2) - pow(y, 2)
    elif sys.argv[1] == "if2":
        return 2 * x * y
    # Function 3: a^3 - 3ab^2 + i(3a^2b - b^3)
    # real
    # return pow(x, 3) - (3 * x * pow(y, 2))
    # imaginary
    # return 3 * y * pow(x, 2) - pow(y, 3)
    elif sys.argv[1] == "rf3":
        return pow(x, 3) - (3 * x * pow(y, 2))
    elif sys.argv[1] == "if3":
        return 3 * pow(x, 2) * y - pow(y, 3)
    # Function 4: a + ib
    # real
    # return x
    # imaginary
    # return y
    elif sys.argv[1] == "rf4":
        return x
    elif sys.argv[1] == "if4":
        return y

    elif sys.argv[1] == "trf2":
        return -pow(x, 2) + pow(y, 2)
    elif sys.argv[1] == "tif2":
        return -2 * x * y

    elif sys.argv[1] == "trf3":
        return 3 * pow(x, 2) * y - pow(y, 3)
    elif sys.argv[1] == "tif3":
        return -pow(x, 3) + (3 * x * pow(y, 2))

    elif sys.argv[1] == "trf4":
        return -y
    elif sys.argv[1] == "tif4":
        return x
    else:
        return None


def plotgraph(x_range, y_range, spaces):
    x = np.linspace(x_range[0], x_range[1], spaces)
    y = np.linspace(y_range[0], y_range[1], spaces)
    x, y = np.meshgrid(x, y)
    fig = plt.figure(figsize=[12, 8])
    z = 3 + x - x
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z)
    plt.show()


print(str(sys.argv))
plotgraph(x_range=[-10, 10], y_range=[-10, 10], spaces=200)
