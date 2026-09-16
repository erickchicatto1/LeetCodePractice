import heapq

def dijkstra(grafo, inicio, fin):
    # Distancias iniciales desde el inicio a todos los nodos como infinitas
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    
    # Predecesores para reconstruir la ruta final
    predecesores = {nodo: None for nodo in grafo}
    
    # Cola de prioridad que guarda tuplas: (distancia_actual, nodo)
    cola = [(0, inicio)]
    
    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
        
        # Si llegamos al destino, detenemos la búsqueda
        if nodo_actual == fin:
            break
            
        if dist_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo[nodo_actual].items():
            distancia = dist_actual + peso
            
            # Si encontramos un camino más corto al vecino
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))
                
    # Reconstruir la ruta desde el fin hasta el inicio
    camino = []
    actual = fin
    while actual is not None:
        camino.insert(0, actual)
        actual = predecesores[actual]
        
    return distancias[fin], camino

# Ejemplo de mapa para el robot (grafo con nodos y costos de movimiento)
mapa_robot = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2, 'E': 3},
    'E': {'D': 3}
}

costo_total, ruta_optima = dijkstra(mapa_robot, 'A', 'E')
print(f"Costo total: {costo_total}")
print(f"Ruta óptima para el robot: {ruta_optima}")
