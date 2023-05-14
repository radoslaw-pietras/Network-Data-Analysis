import numpy as np
import heapq as hq


def BellmanFord(src, adjacency):
    N = len(adjacency)
    dist = [float("Inf")] * N
    dist[src] = 0
    predecessor = [None] * N
    for _ in range(N - 1):
        for u in range(N):
            for v in range(N):
                w = get_weight(adjacency, u, v)
                if w != 0:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        predecessor[v] = u

    for u in range(N):
        for v in range(N):
            w = get_weight(adjacency, u, v)
            if w != 0:
                if dist[u] + w < dist[v]:
                    print("Graph contains negative weight cycle")
                    exit(-1)
    return dist, predecessor


def Dijkstra(src, adjacency):
    N = len(adjacency)
    dist = [float('Inf')] * N
    dist[src] = 0
    predecessor = [None] * N
    visited = [False] * N
    queue = []
    hq.heappush(queue, (0, src))

    while queue:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in get_neighbours(adjacency, u):
            if not visited[v]:
                f = g + w
                if f < dist[v]:
                    dist[v] = f
                    predecessor[v] = u
                    hq.heappush(queue, (f, v))
    return dist, predecessor


def get_neighbours(adjacency, i):
    if type(adjacency) == dict:
        for j, w in adjacency[i]:
            yield j, w
    if type(adjacency) == np.ndarray:
        for j, w in enumerate(adjacency[i]):
            if w != 0:
                yield j, w


def get_weight(adjacency, i, j):
    if type(adjacency) == dict:
        for n, w in adjacency[i]:
            if j == n:
                return w
        return 0

    if type(adjacency) == np.ndarray:
        return adjacency[i, j]
