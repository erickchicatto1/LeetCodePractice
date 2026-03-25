import networkx as nx
import matplotlib.pyplot as plt
import time

# Grafo inicial
graph = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.G_nx = nx.DiGraph()  # usar DiGraph para dirigido, Graph() si no dirigido
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                self.G_nx.add_edge(node, neighbor, weight=weight)
        self.pos = nx.spring_layout(self.G_nx)  # posiciones fijas

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight
        self.G_nx.add_edge(node1, node2, weight=weight)

    def draw_graph(self, visited, current, distances):
        plt.clf()  # limpiar figura
        node_colors = []
        for node in self.G_nx.nodes:
            if node == current:
                node_colors.append('orange')  # nodo actual
            elif node in visited:
                node_colors.append('lightgreen')  # visitado
            else:
                node_colors.append('lightblue')  # no visitado

        nx.draw(self.G_nx, self.pos, with_labels=True, node_color=node_colors, node_size=1500)
        edge_labels = nx.get_edge_attributes(self.G_nx,'weight')
        nx.draw_networkx_edge_labels(self.G_nx, self.pos, edge_labels=edge_labels)
        
        # Mostrar distancias como etiquetas adicionales
        for node, dist in distances.items():
            x, y = self.pos[node]
            plt.text(x, y + 0.08, f"{dist:.1f}", horizontalalignment='center', fontsize=10, fontweight='bold')
        
        plt.pause(0.8)  # pausa para animación

    def shortest_distances(self, source):
        distances = {node: float('inf') for node in self.graph}
        distances[source] = 0
        visited = set()

        plt.figure(figsize=(8,6))
        while len(visited) < len(self.graph):
            # nodo con distancia mínima no visitado
            current_node = None
            current_distance = float('inf')
            for node in self.graph:
                if node not in visited and distances[node] < current_distance:
                    current_node = node
                    current_distance = distances[node]

            if current_node is None:
                break

            visited.add(current_node)

            # Dibujar estado actual
            self.draw_graph(visited, current_node, distances)

            # Relajar vecinos
            for neighbor, weight in self.graph[current_node].items():
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        plt.show()
        return distances

# =============================
# EJEMPLO DE USO
# =============================
G = Graph(graph)
result = G.shortest_distances("A")
print(" Distancias finales:", result)
