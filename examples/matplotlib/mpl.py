"""
Copyright (C) 2014-2015, Zoomer Analytics LLC.
All rights reserved.

License: BSD 3-clause (see LICENSE.txt for details)
"""
import numpy as np
import matplotlib.pyplot as plt
import xlwings as xw
try:
    import seaborn
except ImportError:
    pass


def get_figure(const):
    # Based on: http://matplotlib.org/users/screenshots.html#streamplot
    Y, X = np.mgrid[-3:3:100j, -3:3:100j]
    U = -1 + const * X**2 + Y
    V = 1 - const * X - Y**2

    fig, ax = plt.subplots(figsize=(6, 4))
    strm = ax.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
    fig.colorbar(strm.lines)
    return fig


def main():
    # Create a reference to the calling Excel Workbook
    wb = xw.Workbook.caller()

    # Get the constant from Excel
    const = xw.Range('B1').value

    # Get the figure and show it in Excel
    fig = get_figure(const)
    plot = xw.Plot(fig)
    plot.show('MyStreamplot', sheet=1)
