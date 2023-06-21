import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def print_poly(z):
    terms = []
    for deg, coef in enumerate(z):
        c = f'{coef:.4f}'
        if deg == 0:
            term = c
        elif deg == 1:
            term = f'{c}x'
        else:
            term = f'{c}x^{deg}'
        terms.append(term)
    return "y = " + " + ".join(terms)


for algorithm in ["bellman-ford-list", "bellman-ford-matrix", "dijkstra-list", "dijkstra-matrix"]:
    data = pd.read_csv(f"{algorithm}.txt", sep=';', header=None)
    data.columns = ["Vertices", "Edges", "Time"]
    y = data["Time"]

    x0 = data["Vertices"]
    x1 = data["Edges"]

    fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharex=False, sharey=True)

    axs[0].scatter(x0, y)
    z0 = np.polyfit(x0, y, 2)
    p0 = np.poly1d(z0)
    axs[0].text(0.01, 0.91, print_poly(z0), horizontalalignment='left', transform=axs[0].transAxes)
    axs[0].plot(x0, p0(x0), "r--")
    axs[0].set_xlabel(x0.name)
    axs[0].set_ylabel(f"{y.name} [s]")
    axs[0].grid()

    axs[1].scatter(x1, y)
    z1 = np.polyfit(x1, y, 2)
    p1 = np.poly1d(z1)
    axs[1].text(0.01, 0.91, print_poly(z1), horizontalalignment='left', transform=axs[1].transAxes)
    axs[1].plot(x1, p1(x1), "r--")
    axs[1].set_xlabel(x1.name)
    axs[1].set_ylabel(f"{y.name} [s]")
    axs[1].grid()

    plt.suptitle(algorithm)
    plt.show()