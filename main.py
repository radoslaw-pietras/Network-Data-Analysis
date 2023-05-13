import random

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


def main():
    weights = np.arange(1, 11)
    src = 0
    repeats = 5
    Ns = [10, 100, 500, 1000, 2000]
    algs = [Dijkstra, BellmanFord]
    for _ in range(repeats):
        for n in Ns:
            target = n - 1
            adj_list, adj_matrix = get_graph(n, n, weights, adjacency='both')
            adjs = [adj_list, adj_matrix]
            for adj in adjs:
                for alg in algs:
                    dist, path = alg(src, adj)
                    print_path(path, target)
                    print(f'length: {dist[target]}')
                    print()


if __name__ == '__main__':
    main()
