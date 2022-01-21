import math
from typing import Dict, Any, List
from lab7.lab7 import Graph, Vertex, EdgeType, Edge


class GraphPath:
    graph: Graph
    start: Vertex
    end: Vertex

    def __init__(self, graph: Graph, start: Vertex, end: Vertex):
        self.graph = graph
        self.start = start
        self.end = end

    def dijkstra(self) -> List[Vertex]:
        path: List[Vertex] = [self.end]
        cost_tab: Dict[Vertex, int] = {self.end: 999999999}
        parents: Dict[Vertex, Vertex] = {}
        visited: List[Vertex] = [self.start]
        v: Vertex = None
        min_weight = math.inf
        for i in self.graph.adjacencies[self.start]:
            cost_tab[i.destination] = int(i.weight)
            parents[i.destination] = self.start
        for i in cost_tab.keys():
            if cost_tab[i] < min_weight and i not in visited:
                min_weight = cost_tab[i]
                v = i
        while v is not None:
            c: int = cost_tab[v]
            for n in self.graph.adjacencies[v]:
                nc: int = int(c + n.weight)
                if n.destination in cost_tab.keys() and cost_tab[n.destination] > nc:
                    cost_tab[n.destination] = nc
                    parents[n.destination] = v
                elif n.destination not in cost_tab.keys():
                    cost_tab[n.destination] = nc
                    parents[n.destination] = v
            visited.append(v)
            min_weight = math.inf
            temp: Vertex = None
            for i in cost_tab.keys():
                if cost_tab[i] < min_weight and i not in visited:
                    min_weight = cost_tab[i]
                    temp = i
            v = temp
        v = self.end
        while v in parents.keys():
            path.insert(0, parents[v])
            v = parents[v]
        return path


def all_weighted_shortest_paths(g: Graph, start: Any) -> Dict[Any, List[Edge]]:
    path_vertex: Dict[Vertex: List[Vertex]] = {}
    path_edges: Dict[Vertex: List[Edge]] = {}
    for i in g.adjacencies.keys():
        if i != start:
            path: GraphPath = GraphPath(g, start, i)
            path_vertex[i] = path.dijkstra()
            path_edges[i] = []
    for e in path_vertex.keys():
        for i in range(len(path_vertex[e]) - 1):
            temp: Edge = None
            for j in g.adjacencies[path_vertex[e][i]]:
                condition: bool = j.source == path_vertex[e][i] and j.destination == path_vertex[e][i + 1]
                if condition and temp is None or condition and j.weight < temp.weight:
                    temp = j
            path_edges[e].append(temp)
    return path_edges


d: EdgeType = EdgeType(1)
# graf 1
g1: Graph = Graph()
g2: Graph = Graph()
g3: Graph = Graph()
v1: Vertex = g1.create_vertex(1)
v2: Vertex = g1.create_vertex(2)
v3: Vertex = g1.create_vertex(3)
v4: Vertex = g1.create_vertex(4)
v5: Vertex = g1.create_vertex(5)
g1.add(d, v1, v2, 4)
g1.add(d, v1, v3, 11)
g1.add(d, v3, v5, 7)
g1.add(d, v2, v4, 4)
g1.add(d, v4, v5, 3)
g1.add(d, v2, v3, 3)
g1.add(d, v3, v4, 2)
g1.add(d, v1, v4, 1)
g1.add(d, v4, v2, 2)
g1.show("graf1")
paths1: Dict = all_weighted_shortest_paths(g1, v1)
print("Graf 1")
for i in paths1.keys():
    print(f"Sciezka do {i.data}: {v1.data}", end=" ")
    for j in paths1[i]:
        print(f"-> {j.destination.data}", end=" ")
    print()
print("\nGraf 2")
# graf 2
g2: Graph = Graph()
v12: Vertex = g2.create_vertex(1)
v22: Vertex = g2.create_vertex(2)
v32: Vertex = g2.create_vertex(3)
v42: Vertex = g2.create_vertex(4)
g2.add(d, v12, v22, 8)
g2.add(d, v22, v32, 4)
g2.add(d, v32, v42, 10)
g2.add(d, v32, v22, 3)
g2.add(d, v12, v32, 3)
g2.add(d, v22, v42, 1)
g2.show("graf2", "neato")
paths2: Dict = all_weighted_shortest_paths(g2, v12)
for i in paths2.keys():
    print(f"Sciezka do {i.data}: {v12.data}", end=" ")
    for j in paths2[i]:
        print(f"-> {j.destination.data}", end=" ")
    print()
# graf 3
g3: Graph
v33: Vertex = g3.create_vertex(3)
v23: Vertex = g3.create_vertex(2)
v13: Vertex = g3.create_vertex(1)
v43: Vertex = g3.create_vertex(4)
v53: Vertex = g3.create_vertex(5)
v63: Vertex = g3.create_vertex(6)
v73: Vertex = g3.create_vertex(7)
v83: Vertex = g3.create_vertex(8)
g3.add(d, v33, v83, 9)
g3.add(d, v33, v23, 1)
g3.add(d, v23, v43, 2)
g3.add(d, v43, v83, 5)
g3.add(d, v23, v13, 4)
g3.add(d, v13, v53, 6)
g3.add(d, v13, v73, 7)
g3.add(d, v43, v73, 1)
g3.add(d, v73, v63, 3)
g3.add(d, v53, v63, 5)
g3.show("graf3", "circo")
paths3: Dict = all_weighted_shortest_paths(g3, v33)
print("\nGraf 3")
for i in paths3.keys():
    print(f"Sciezka do {i.data}: {v33.data}", end=" ")
    for j in paths3[i]:
        print(f"-> {j.destination.data}", end=" ")
    print()
