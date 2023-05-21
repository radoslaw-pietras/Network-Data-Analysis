import time

import numpy as np

from algorithms import BellmanFord, Dijkstra
from graph import get_graph


def print_path(predecessors, target):
    node = target
    path = [target]
    while True:
        p = predecessors[node]
        if p is None:
            break
        path.append(p)
        node = p
    print('->'.join([str(p) for p in reversed(path)]))


def run_test(alg, adj, src, target):
    ts = time.time()
    dist, paths = alg(src, adj)
    te = time.time()
    duration = te - ts
    print_path(paths, target)
    print(f'length: {dist[target]}, time: {duration}')
    print()
    return duration


def main():
    weights = np.arange(1, 11)
    src = 0
    repeats = 5
    # Ns = [50, 100, 150, 200, 500, 1000,]
    Ns = np.arange(50, 1050, 50)

    algs = [Dijkstra, BellmanFord]

    for n in Ns:
        dj_list_times = []
        dj_matrix_times = []
        bf_list_times = []
        bf_matrix_times = []
        edges = []
        for r in range(repeats):
            target = n - 1
            adj_list, adj_matrix, m = get_graph(n, weights, adjacency='both')
            edges.append(m)
            print(f"[{r+1}]: running graph with {n} nodes and {m} directed edges")
            print("Dijkstra - list:")
            dj_list_times.append(run_test(Dijkstra, adj_list, src, target))

            print("Dijkstra - matrix:")
            dj_matrix_times.append(run_test(Dijkstra, adj_matrix, src, target))

            print("BellmanFord - list:")
            bf_list_times.append(run_test(BellmanFord, adj_list, src, target))

            print("BellmanFord - matrix:")
            bf_matrix_times.append(run_test(BellmanFord, adj_matrix, src, target))

        with open(f"bellman-ford-list.txt", 'a') as f:
            f.write(f"{n};{round(np.average(edges))};{np.average(bf_list_times)}\n")
        with open(f"bellman-ford-matrix.txt", 'a') as f:
            f.write(f"{n};{round(np.average(edges))};{np.average(bf_matrix_times)}\n")

        with open(f"dijkstra-list.txt", 'a') as f:
            f.write(f"{n};{round(np.average(edges))};{np.average(dj_list_times)}\n")
        with open(f"dijkstra-matrix.txt", 'a') as f:
            f.write(f"{n};{round(np.average(edges))};{np.average(dj_matrix_times)}\n")


if __name__ == '__main__':
    main()