"""Provides an undirected weighted Graph class.

The Graph class is iterable over its vertices.  For example, to iterate
over all edges in a graph, you may do:

```
graph = Graph()

# Fill in graph

for vertex in graph:
    for neighbor, weight in graph[vertex].items():
        ...  # do something
```
"""
# NOTE: Do not alter this file.
# CSC 349 Assignment 5
from __future__ import annotations


class Graph(dict[int, dict[int, int]]):
    """A graph type using adjacency lists."""

    def add_vertex(self, vertex: int) -> None:
        """Add a vertex to the graph if it doesn't already exist.

        Args:
            vertex: The vertex to add
        """
        self.setdefault(vertex, {})

    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        """Add an undirected weighted edge to the graph.

        Args:
            vertex1: The first vertex
            vertex2: The second vertex
            weight: The weight of the edge
        """
        self.setdefault(vertex1, {})[vertex2] = weight
        self.setdefault(vertex2, {})[vertex1] = weight

    @classmethod
    def from_file(cls, file_name: str) -> Graph:
        """Read and return a graph from a file.

        The file is expected to be as an edge list with weights.

        Args:
            file_name: The name of the file specifying the graph.

        Returns:
            The specified graph.
        """
        graph = cls()

        with open(file_name, encoding="utf8") as graph_file:
            for edge in graph_file:
                v1, v2, weight = (int(value) for value in edge.split())
                graph.add_edge(v1, v2, weight)

        return graph
