import networkx as nx
import random

import numpy as np
import matplotlib.pyplot as plt


def get_graph(n_nodes, n_edges, weights_range, adjacency=None):
    n_retires = 0
    G = None
    while n_retires < 10:
        G = generate_random_graph(n_nodes, n_edges, weights=weights_range)
        if G is not None:
            break
        else:
            print("retrying...")
            n_retires += 1

    if G is None:
        print(f"failed after {n_retires} retries")
        exit(-1)
    if adjacency == 'list':
        return convert_to_list(G)
    if adjacency == 'matrix':
        return convert_to_matrix(G)
    if adjacency == 'both':
        return convert_to_list(G), convert_to_matrix(G)


def convert_to_matrix(G):
    adjacency_matrix = np.zeros((len(G.nodes), len(G.nodes)))
    for node, nbrs in G.adjacency():
        for n, w in nbrs.items():
            adjacency_matrix[node, n] = w['weight']
    return adjacency_matrix


def convert_to_list(G: nx.DiGraph):
    adjacency_list = {}
    for node, nbrs in G.adjacency():
        adjacency_list[node] = [(n, w['weight']) for n, w in nbrs.items()]
    return adjacency_list


def add_random_edge(G, weights):
    u = random.choice(list(G.nodes))
    v = random.choice(list(G.nodes))
    if u == v or G.has_edge(u, v):
        return False
    G.add_edge(u, v, weight=random.choice(weights))
    return True


def generate_random_graph(n, m, weights=None):
    G = nx.DiGraph()
    G.add_nodes_from(list(range(n)))
    connected = False
    while not connected:
        if len(G.edges) > m:
            print(f"Failed to create random directed graph with {m} edges")
            return
        success = add_random_edge(G, weights)
        if success:
            connected = nx.is_strongly_connected(G)
    while len(G.edges()) < m:
        add_random_edge(G, weights)
    # nx.draw_networkx(G, pos=nx.spring_layout(G))
    # plt.show()
    return G
