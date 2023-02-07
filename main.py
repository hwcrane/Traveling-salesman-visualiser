from math import inf
from threading import Thread
from graph import Graph
from visuliser import Visuliser
import numba
import random
import time

NUM_NODES = 1000


def pairwise_exchange(graph: Graph, vis: Visuliser, path):
    improved = True
    while improved:
        improved = False
        for i in range(len(path) - 1):
            for j in range(i + 1, len(path) - 1):

                if i == j or i + 1 == j or j + 1 == i:
                    continue

                if - graph.connections[path[i]][path[i+1]] - graph.connections[path[j]][path[j + 1]] + graph.connections[path[i]][path[j]] + graph.connections[path[i + 1]][path[j + 1]] < 0:

                    path = path[0:i+1] + path[j:i:-1] + path[j+1:]
                    vis.set_path(path)
                    improved = True


def two_step(graph, vis, start='A'):
    path = nearest_neighbour(graph, vis, start)
    pairwise_exchange(graph, vis, path)
    print('finished')


def len_path(path, graph: Graph):
    return sum(graph.connections[path[i]][path[i + 1]] for i in range(len(path) - 1))


def nearest_neighbour(graph: Graph, vis: Visuliser, start='A'):
    path = [start]
    visited = {n: False for n in graph.nodes}
    visited[start] = True

    current = start
    for _ in range(len(graph.nodes)):
        vis.set_path(path)
        options = [(k, v)
                   for k, v in graph.connections[current].items() if not visited[k]]

        v.set_options(current, options)
        time.sleep(3 / len(graph.nodes))
        if len(options) == 0:
            closest = start
        else:
            closest = closest_node(options)

        path.append(closest)
        visited[closest] = True
        current = closest
    return path


def closest_node(paths) -> str:
    closest_node = ''
    shortest_path = inf

    for path in paths:
        if path[1] < shortest_path:
            closest_node = path[0]
            shortest_path = path[1]

    return closest_node


g = Graph()

for i in range(NUM_NODES):
    g.add_node(chr(ord('A') + i), (random.random() * 20, random.random() * 20))

g.create_connections()

v = Visuliser((800, 800), (20, 20), g.nodes)

Thread(target=two_step, args=[g, v]).start()
v.mainloop()
