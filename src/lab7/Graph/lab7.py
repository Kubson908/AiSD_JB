from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from lab2.lab2 import Queue

class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int = 1

    def __init__(self, data: Any):
        self.data = data
        self.index += 1


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies: Dict[Vertex, List[Edge]]):
        self.adjacencies = adjacencies

    def create_vertex(self, data: Any) -> Vertex:
        v: Vertex = Vertex(data)
        self.adjacencies[v] = []
        return v

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2:
            self.add_undirected_edge(source, destination, weight)
        else:
            print("Nie ma takiego typu krawedzi\n")

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:

