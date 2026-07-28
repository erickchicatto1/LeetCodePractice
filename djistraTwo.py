import heapq

def dijkstra(grafo, inicio):
    """
    grafo: diccionario de adyacencia {nodo: [(vecino, peso), ...]}
    inicio: nodo de partida
    Devuelve: diccionario con la distancia mínima a cada nodo
    """
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    cola = [(0, inicio)]  # (distancia, nodo)

    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual]:
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias


# Ejemplo de uso
grafo = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

resultado = dijkstra(grafo, 'A')
print(resultado)
