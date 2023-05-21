import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    axs[0].plot(x0, p0(x0), "r--")
    axs[0].set_xlabel(x0.name)
    axs[0].set_ylabel(f"{y.name} [s]")
    axs[0].grid()

    axs[1].scatter(x1, y)
    z1 = np.polyfit(x1, y, 2)
    p1 = np.poly1d(z1)
    axs[1].plot(x1, p1(x1), "r--")
    axs[1].set_xlabel(x1.name)
    axs[1].set_ylabel(f"{y.name} [s]")
    axs[1].grid()

    plt.suptitle(algorithm)
    plt.show()