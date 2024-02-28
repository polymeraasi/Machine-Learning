"""
DATA.ML.100 
(EX01) To do: program that asks user to give N points with a mouse
by clicking left to add points then right to stop.
After that the program plots the points ans a fitted linear model.
"""

from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Prints the coordinate window in where you click points.
    To the empty lists we'll append data later.
    """
    fig, ax = plt.subplots()
    ax.grid(False, which='both')
    x = []
    y = []

    sumxy = []
    sumx = []
    sumy = []
    sumx2 = []


    def my_linfit(sum_xy, sum_x, sum_y, sum_x2):
        """
        Returns the derived parameters that are used to plot the fitted line.
        """
        N = len(x)
        # the derived parameters:
        b = (sum_y - (sum_xy * sum_x) / (sum_x2)) / (N - (sum_x * sum_x) / sum_x2 )
        a = (sum_xy - b * sum_x) / sum_x2
        return a, b


    def on_click(event):
        """
        Will add the clicked points to an empty list and finally plot the fitted line in between collected points.
        """
        xi, yi = event.xdata, event.ydata

        if event.button is MouseButton.LEFT:
            x.append(xi)
            y.append(yi)

        if event.button is MouseButton.RIGHT:

            for i in range(0, len(x)):
                mult = x[i] * y[i]
                sumxy.append(mult)

            for i in range(0, len(x)):
                sumx.append(x[i])

            for i in range(0, len(x)):
                sumy.append(y[i])

            for i in range(0, len(x)):
                x_pot = x[i]**2
                sumx2.append(x_pot)

            plt.disconnect(point)

    point = plt.connect('button_press_event', on_click)

    plt.title("left click: add point, right click: stop collecting. Close window when done.")
    plt.show()

    a, b = my_linfit(sum(sumxy), sum(sumx), sum(sumy), sum(sumx2))

    # draws a red line between clicked points.
    plt.plot(x, y, 'kx')
    xp = np.arange(-2, 5, 0.1)
    plt.plot(xp, a * xp + b, 'r-')
    plt.axis([0, 1, 0, 1])

    plt.title(f"Fitting the line: a = {a:.2f} and b = {b:.2f}")
    plt.show()

main()
