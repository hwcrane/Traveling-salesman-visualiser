import math
import numba


class Graph:
    def __init__(self) -> None:
        self.nodes = {}
        self.connections = {}

    def add_node(self, name, position):
        self.nodes[name] = position

    def create_connections(self):
        self.connections = {n: {} for n in self.nodes.keys()}
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    pos1 = self.nodes[node1]
                    pos2 = self.nodes[node2]
                    distance = math.sqrt(
                        (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
                    self.connections[node1][node2] = distance
