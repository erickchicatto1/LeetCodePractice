"""
Simulación de un Robot Limpiador
---------------------------------
El robot se mueve en una cuadrícula (habitación), limpia las celdas
por donde pasa y evita obstáculos. Se detiene cuando ha limpiado
todo lo posible o se queda sin movimientos.
"""

import random


class RobotLimpiador:
    def __init__(self, filas, columnas, obstaculos=None, pos_inicial=(0, 0)):
        self.filas = filas
        self.columnas = columnas
        self.obstaculos = set(obstaculos) if obstaculos else set()
        self.posicion = pos_inicial
        self.celdas_limpias = set()
        self.pasos_dados = 0

        if self.posicion not in self.obstaculos:
            self.celdas_limpias.add(self.posicion)

    def celda_valida(self, pos):
        x, y = pos
        dentro_rango = 0 <= x < self.filas and 0 <= y < self.columnas
        return dentro_rango and pos not in self.obstaculos

    def moverse(self):
        """Elige un movimiento aleatorio válido y limpia la nueva celda."""
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der
        random.shuffle(movimientos)

        for dx, dy in movimientos:
            nueva_pos = (self.posicion[0] + dx, self.posicion[1] + dy)
            if self.celda_valida(nueva_pos):
                self.posicion = nueva_pos
                self.celdas_limpias.add(nueva_pos)
                self.pasos_dados += 1
                return True
        return False  # No hay movimiento posible

    def total_celdas_limpiables(self):
        return (self.filas * self.columnas) - len(self.obstaculos)

    def limpiar_habitacion(self, max_pasos=200):
        while (
            len(self.celdas_limpias) < self.total_celdas_limpiables()
            and self.pasos_dados < max_pasos
        ):
            self.moverse()

    def mostrar_mapa(self):
        for x in range(self.filas):
            fila_str = ""
            for y in range(self.columnas):
                pos = (x, y)
                if pos == self.posicion:
                    fila_str += " R "
                elif pos in self.obstaculos:
                    fila_str += " # "
                elif pos in self.celdas_limpias:
                    fila_str += " . "
                else:
                    fila_str += " o "
            print(fila_str)
        print()


if __name__ == "__main__":
    # Configuración de la habitación: 5x5 con algunos obstáculos
    obstaculos = [(1, 1), (2, 2), (3, 3)]
    robot = RobotLimpiador(filas=5, columnas=5, obstaculos=obstaculos)

    print("Mapa inicial (R=robot, #=obstáculo, .=limpio, o=sucio):")
    robot.mostrar_mapa()

    robot.limpiar_habitacion(max_pasos=200)

    print("Mapa final:")
    robot.mostrar_mapa()

    porcentaje = len(robot.celdas_limpias) / robot.total_celdas_limpiables() * 100
    print(f"Pasos dados: {robot.pasos_dados}")
    print(f"Celdas limpiadas: {len(robot.celdas_limpias)}/{robot.total_celdas_limpiables()}")
    print(f"Porcentaje limpiado: {porcentaje:.1f}%")
