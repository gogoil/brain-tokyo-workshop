import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def create_graph(a, b):
    G = nx.DiGraph(directed=True)
    for node in range(len(a)):
        G.add_edge(a[node], b[node])
    return G


def draw_graph(G):
    nx.draw_networkx(G, arrows=True)
    plt.draw()
    plt.show()


def is_cycle_exist(G):
    try:
        nx.algorithms.cycles.find_cycle(G)
        return True
    except nx.exception.NetworkXNoCycle:
        return False


if __name__ == '__main__':
    a = np.array([0., 1., 2., 3., 4., 5., 4., 107., 1., 3.,
                  4., 883., 6.]
                 )
    b = np.array([6., 6., 6., 6., 6., 6., 107., 6., 107., 107.
                     , 883., 107., 883.])
    G = create_graph(a, b)
    draw_graph(G)
    try:
        cycle = nx.algorithms.cycles.find_cycle(G)
        for c in cycle:
            print(c)
    except nx.exception.NetworkXNoCycle:
        print('no cycle found')
