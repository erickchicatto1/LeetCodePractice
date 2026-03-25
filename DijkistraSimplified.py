# ============================================================
# ALGORITMO DE DIJKSTRA - Versión legible
# ============================================================
# Encuentra el camino más corto desde un nodo origen
# hacia todos los demás nodos del grafo.
# ============================================================

INFINITO = float("inf")

# El grafo se representa como diccionario de diccionarios:
# { nodo: { vecino: peso_de_la_arista } }
grafo_ejemplo = {
    "A": {"B": 3,   "C": 3  },
    "B": {"A": 3,   "D": 3.5, "E": 2.8},
    "C": {"A": 3,   "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10 },
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7,   "D": 10 },
}


class Grafo:

    def __init__(self, grafo: dict):
        # Guardamos el grafo como lista de adyacencia
        self.grafo = grafo

    def agregar_arista(self, origen, destino, peso):
        """Agrega una conexión dirigida entre dos nodos."""
        if origen not in self.grafo:
            self.grafo[origen] = {}
        self.grafo[origen][destino] = peso

    # ----------------------------------------------------------
    # DIJKSTRA
    # ----------------------------------------------------------

    def _inicializar_distancias(self, origen):
        """
        Crea el diccionario de distancias.
        Todos los nodos empiezan en infinito, excepto el origen que vale 0.
        """
        distancias = {}
        for nodo in self.grafo:
            distancias[nodo] = INFINITO
        distancias[origen] = 0
        return distancias

    def _inicializar_anteriores(self):
        """
        Crea el diccionario de nodos anteriores.
        Sirve para reconstruir el camino al final.
        Todos empiezan en None porque aún no conocemos ningún camino.
        """
        anteriores = {}
        for nodo in self.grafo:
            anteriores[nodo] = None
        return anteriores

    def _nodo_mas_cercano_no_visitado(self, distancias, visitados):
        """
        De todos los nodos que aún no visitamos,
        devuelve el que tenga la distancia más pequeña conocida.
        Devuelve None si todos los nodos restantes son inalcanzables.
        """
        nodo_elegido = None
        distancia_minima = INFINITO

        for nodo in self.grafo:
            es_no_visitado = nodo not in visitados
            tiene_distancia_menor = distancias[nodo] < distancia_minima

            if es_no_visitado and tiene_distancia_menor:
                nodo_elegido = nodo
                distancia_minima = distancias[nodo]

        return nodo_elegido

    def _relajar_vecinos(self, nodo_actual, distancias, anteriores):
        """
        Revisa todos los vecinos del nodo actual.
        Si pasar por nodo_actual ofrece un camino más corto hacia un vecino,
        actualiza su distancia y anota que el camino viene desde nodo_actual.
        Este proceso se llama 'relajación de aristas'.
        """
        distancia_actual = distancias[nodo_actual]

        for vecino, peso in self.grafo[nodo_actual].items():
            distancia_por_este_camino = distancia_actual + peso
            es_camino_mas_corto = distancia_por_este_camino < distancias[vecino]

            if es_camino_mas_corto:
                distancias[vecino] = distancia_por_este_camino
                anteriores[vecino] = nodo_actual  # venimos desde nodo_actual

    def calcular_distancias(self, origen: str):
        """
        Ejecuta el algoritmo de Dijkstra desde el nodo origen.
        Devuelve dos diccionarios:
          - distancias:  distancia mínima desde origen hasta cada nodo
          - anteriores:  nodo previo en el camino más corto hacia cada nodo
        """
        distancias = self._inicializar_distancias(origen)
        anteriores = self._inicializar_anteriores()
        visitados  = set()

        todos_los_nodos = len(self.grafo)

        while len(visitados) < todos_los_nodos:

            # Elegir el nodo no visitado más cercano al origen
            nodo_actual = self._nodo_mas_cercano_no_visitado(distancias, visitados)

            # Si no hay nodo alcanzable, detenemos el algoritmo
            if nodo_actual is None:
                break

            # Marcar el nodo como visitado (su distancia ya no cambiará)
            visitados.add(nodo_actual)

            # Intentar mejorar las distancias de sus vecinos
            self._relajar_vecinos(nodo_actual, distancias, anteriores)

        return distancias, anteriores

    # ----------------------------------------------------------
    # RECONSTRUIR CAMINO
    # ----------------------------------------------------------

    def obtener_camino(self, anteriores: dict, destino: str):
        """
        Reconstruye el camino más corto desde el origen hasta el destino.
        Usa el diccionario 'anteriores' para ir hacia atrás nodo por nodo.
        Devuelve el camino como string: "G -> F -> C -> A"
        """
        camino = []
        nodo_actual = destino

        # Recorremos hacia atrás hasta llegar al origen (que tiene anterior = None)
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_actual = anteriores[nodo_actual]

        camino.reverse()  # Lo damos vuelta para que vaya de origen a destino
        return " -> ".join(camino)


# ============================================================
# PRUEBA
# ============================================================

g = Grafo(grafo=grafo_ejemplo)

ORIGEN = "G"
distancias, anteriores = g.calcular_distancias(ORIGEN)

print(f"Distancias mínimas desde '{ORIGEN}':")
for nodo, distancia in distancias.items():
    camino = g.obtener_camino(anteriores, nodo)
    print(f"  {ORIGEN} -> {nodo}: {distancia}   ({camino})")
