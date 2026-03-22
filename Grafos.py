class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=None, directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        if not directed:
            self.graph[vertex2][vertex1] = weight

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"Vértice {vertex} tiene como conexiones a:")
            for neighbor, weight in edges.items():
                if weight:
                    print(f"  - {neighbor} (peso: {weight})")
                else:
                    print(f"  - {neighbor}")
