# We use dictionaries to represent the Graph
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
    def __init__(self, graph: dict = {}):
        self.graph = graph  # adjacency list
        
        print(" Grafo cargado:")
        for node, neighbors in graph.items():
            print(node, "->", neighbors)

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}

        # agregar conexión (dirigida)
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):

        # 1. Inicializar distancias
        distances = {}
        previous = {}
        
        for node in self.graph:
            distances[node] = float("inf")

        distances[source] = 0

        for node in self.graph:
            previous[node] = None
        
        visited = set() #mhace conjuntos , como los conjuntos matematicos

        # 2. Loop principal
        while len(visited) < len(self.graph):

            print("\n==============================")
            print(" NUEVA ITERACIÓN")
            print("Visitados:", visited)
            print("Distancias:", distances)

            # 3. Encontrar nodo más cercano no visitado
            current_node = None
            current_distance = float("inf")

            for node in self.graph:
                if node not in visited and distances[node] < current_distance:
                    current_node = node
                    current_distance = distances[node]

            # Si no hay nodo alcanzable
            if current_node is None:
                break

            print(f"Nodo actual: {current_node} (distancia {current_distance})")

            # 4. Marcar como visitado
            visited.add(current_node)

            # 5. Revisar vecinos
            for neighbor, weight in self.graph[current_node].items():

                new_distance = current_distance + weight

                print(f"    Vecino: {neighbor}")
                print(f"     Peso: {weight}")
                print(f"     Nueva distancia: {new_distance}")

                if new_distance < distances[neighbor]:
                    print(f"      Actualizando {neighbor}: {distances[neighbor]} → {new_distance}")
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node
                else:
                    print(f"      No mejora")

        return distances,previous
    
    def get_path(self,previous,target):
        path = []
        current = target
        
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return "->".join(path)
        
# =============================
# PRUEBA
# =============================

G = Graph(graph=graph)

# Puedes modificar aristas si quieres probar
G.add_edge("B", "A", 7)

print("Ejecutando Dijkstra desde A...\n")
result = G.shortest_distances("A")

print("Ejecutando Dijkstra desde G...\n")
result = G.shortest_distances("G")

distances, previous = G.shortest_distances("G")

print(distances)
# {'A': 9.0, 'B': 9.8, 'C': 6.0, 'D': 10, 'E': 7, 'F': 2.5, 'G': 0}

print(G.get_path(previous, "A"))
# G → F → C → A

print(G.get_path(previous, "B"))
# G → E → B


print("\n==============================")
print("RESULTADO FINAL:")
print(result)
