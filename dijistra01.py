import heapq

def dijkstra(graph, start):
    # Distancia mínima a cada nodo
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Cola de prioridad
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Si ya encontramos un camino más corto, ignorar
        if current_distance > distances[current_node]:
            continue

        # Revisar vecinos
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Si encontramos un camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Grafo de ejemplo
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
}

start_node = 'A'

result = dijkstra(graph, start_node)

print("Distancias mínimas desde", start_node)
for node, dist in result.items():
    print(f"{node}: {dist}")
