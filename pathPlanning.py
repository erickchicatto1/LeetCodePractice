"""
Algoritmo A* (A-star) para planificación de rutas en robótica.

Este script simula un mapa en forma de grid (cuadrícula) con obstáculos,
un punto de inicio y un punto objetivo. El algoritmo A* encuentra el
camino más corto evitando los obstáculos, combinando:
    - g(n): costo real desde el inicio hasta el nodo n
    - h(n): heurística (distancia estimada) desde n hasta el objetivo
    - f(n) = g(n) + h(n): costo total estimado

Es uno de los algoritmos más usados en robótica móvil para navegación
autónoma (junto con Dijkstra, RRT, y variantes como Hybrid A*).
"""

import heapq
import matplotlib.pyplot as plt
import numpy as np


class NodoAStar:
    """Representa un nodo del grid dentro del algoritmo A*."""

    def __init__(self, posicion, padre=None):
        self.posicion = posicion  # (fila, columna)
        self.padre = padre
        self.g = 0  # costo desde el inicio
        self.h = 0  # heurística hacia el objetivo
        self.f = 0  # costo total (g + h)

    def __eq__(self, otro):
        return self.posicion == otro.posicion

    def __lt__(self, otro):
        # Necesario para que heapq pueda comparar nodos por su costo f
        return self.f < otro.f

    def __hash__(self):
        return hash(self.posicion)


def heuristica(a, b):
    """Distancia euclidiana entre dos puntos (a y b son tuplas (fila, col))."""
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def obtener_vecinos(posicion, grid):
    """
    Devuelve las posiciones vecinas válidas (8 direcciones: incluye
    diagonales), descartando las que están fuera del grid o son obstáculos.
    """
    filas, columnas = grid.shape
    movimientos = [
        (-1, 0), (1, 0), (0, -1), (0, 1),      # arriba, abajo, izq, der
        (-1, -1), (-1, 1), (1, -1), (1, 1)     # diagonales
    ]

    vecinos = []
    for df, dc in movimientos:
        nueva_pos = (posicion[0] + df, posicion[1] + dc)
        fila, col = nueva_pos

        # Verificar límites del grid
        if 0 <= fila < filas and 0 <= col < columnas:
            # Verificar que no sea un obstáculo (1 = obstáculo, 0 = libre)
            if grid[fila, col] == 0:
                vecinos.append(nueva_pos)

    return vecinos


def costo_movimiento(pos_actual, pos_vecino):
    """Costo de moverse a un vecino: 1.0 en línea recta, ~1.41 en diagonal."""
    if pos_actual[0] != pos_vecino[0] and pos_actual[1] != pos_vecino[1]:
        return np.sqrt(2)  # movimiento diagonal
    return 1.0  # movimiento recto


def a_estrella(grid, inicio, objetivo):
    """
    Ejecuta el algoritmo A* sobre un grid 2D.

    Parámetros:
        grid: matriz numpy 2D donde 0 = celda libre, 1 = obstáculo
        inicio: tupla (fila, columna) del punto de partida
        objetivo: tupla (fila, columna) del punto destino

    Retorna:
        Lista de tuplas (fila, columna) representando el camino encontrado,
        o None si no existe un camino posible.
    """
    nodo_inicio = NodoAStar(inicio)
    nodo_objetivo = NodoAStar(objetivo)

    lista_abierta = []       # nodos por explorar (cola de prioridad)
    lista_cerrada = set()    # nodos ya explorados

    heapq.heappush(lista_abierta, nodo_inicio)
    nodos_por_posicion = {inicio: nodo_inicio}

    while lista_abierta:
        nodo_actual = heapq.heappop(lista_abierta)

        if nodo_actual.posicion in lista_cerrada:
            continue
        lista_cerrada.add(nodo_actual.posicion)

        # ¿Llegamos al objetivo?
        if nodo_actual.posicion == nodo_objetivo.posicion:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual.posicion)
                nodo_actual = nodo_actual.padre
            return camino[::-1]  # invertir para ir de inicio -> objetivo

        # Explorar vecinos
        for vecino_pos in obtener_vecinos(nodo_actual.posicion, grid):
            if vecino_pos in lista_cerrada:
                continue

            g_tentativo = nodo_actual.g + costo_movimiento(nodo_actual.posicion, vecino_pos)

            if vecino_pos not in nodos_por_posicion or g_tentativo < nodos_por_posicion[vecino_pos].g:
                nodo_vecino = NodoAStar(vecino_pos, padre=nodo_actual)
                nodo_vecino.g = g_tentativo
                nodo_vecino.h = heuristica(vecino_pos, objetivo)
                nodo_vecino.f = nodo_vecino.g + nodo_vecino.h

                nodos_por_posicion[vecino_pos] = nodo_vecino
                heapq.heappush(lista_abierta, nodo_vecino)

    return None  # no se encontró camino


def crear_mapa_ejemplo(filas=20, columnas=20):
    """Crea un grid de ejemplo con algunos obstáculos rectangulares."""
    grid = np.zeros((filas, columnas))

    # Obstáculos de ejemplo (puedes modificar estas coordenadas)
    grid[5:15, 8] = 1
    grid[5, 8:15] = 1
    grid[10:18, 15] = 1
    grid[2:8, 3] = 1

    return grid


def visualizar_camino(grid, camino, inicio, objetivo):
    """Dibuja el grid, los obstáculos y el camino encontrado."""
    fig, ax = plt.subplots(figsize=(8, 8))

    # Dibujar el grid: blanco = libre, negro = obstáculo
    ax.imshow(grid, cmap="Greys", origin="upper")

    if camino:
        filas_camino = [p[0] for p in camino]
        columnas_camino = [p[1] for p in camino]
        ax.plot(columnas_camino, filas_camino, color="royalblue", linewidth=2, label="Camino A*")

    ax.scatter(inicio[1], inicio[0], color="green", s=150, marker="o", label="Inicio", zorder=5)
    ax.scatter(objetivo[1], objetivo[0], color="red", s=150, marker="*", label="Objetivo", zorder=5)

    ax.set_title("Planificación de rutas con A*")
    ax.legend(loc="upper right")
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    plt.savefig("ruta_astar.png", dpi=150)
    print("Imagen guardada como 'ruta_astar.png'")
    plt.show()


if __name__ == "__main__":
    # 1. Crear el mapa (grid) con obstáculos
    grid = crear_mapa_ejemplo(filas=20, columnas=20)

    # 2. Definir posiciones de inicio y objetivo (fila, columna)
    inicio = (0, 0)
    objetivo = (19, 19)

    # 3. Ejecutar A*
    camino = a_estrella(grid, inicio, objetivo)

    # 4. Mostrar resultado
    if camino:
        print(f"Camino encontrado con {len(camino)} pasos:")
        print(camino)
    else:
        print("No se encontró un camino posible entre el inicio y el objetivo.")

    # 5. Visualizar
    visualizar_camino(grid, camino, inicio, objetivo)
