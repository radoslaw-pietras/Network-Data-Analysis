import numpy as np
import heapq as hq
import time


def timeit(f):
    def timed(*args, **kw):
        print("running")
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r took: %2.4f sec' % (f.__name__, te - ts))
        return result

    return timed


@timeit
def BellmanFord(src, adjacency):
    N = len(adjacency)
    dist = [float("Inf")] * N
    dist[src] = 0
    predecessor = [None] * N
    for _ in range(N - 1):
        for u in range(N):
            for v, w in get_neighbours(adjacency, u):
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    predecessor[v] = u

    for u in range(N):
        for v, w in get_neighbours(adjacency, u):
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
    return dist, predecessor


@timeit
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

    if type(adjacency) == np.array:
        return adjacency[i, j]
