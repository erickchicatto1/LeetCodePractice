"""
PRÁCTICA: Máquina de Estados (State Machine)
=============================================
Ejemplo: Semáforo con botón de peatón

Estados posibles: ROJO, AMARILLO, VERDE, PARPADEO
Tu tarea es completar las partes marcadas con # TODO

Reglas que debes implementar:
- VERDE -> AMARILLO (siempre, tras N ciclos)
- AMARILLO -> ROJO (siempre)
- ROJO -> VERDE (siempre, tras N ciclos)
- Si se presiona el botón de peatón estando en VERDE, pasa a AMARILLO antes
- Estado especial PARPADEO se activa manualmente en modo emergencia
"""

from enum import Enum, auto


class Estado(Enum):
    ROJO = auto()
    AMARILLO = auto()
    VERDE = auto()
    PARPADEO = auto()


class Semaforo:
    def __init__(self):
        self.estado = Estado.ROJO
        self.boton_peaton = False
        self.contador = 0

    def presionar_boton_peaton(self):
        """Marca que un peatón pidió cruzar."""
        self.boton_peaton = True

    def activar_emergencia(self):
        """Fuerza el estado de parpadeo (modo emergencia)."""
        # TODO: cambia self.estado a Estado.PARPADEO
        pass

    def transicionar(self):
        """
        Decide el siguiente estado según self.estado actual.
        Debe modificar self.estado y resetear self.contador cuando cambie.
        """
        if self.estado == Estado.VERDE:
            # TODO: si self.boton_peaton es True, pasar a AMARILLO
            #       y resetear self.boton_peaton a False
            pass

            # TODO: si no hay boton_peaton, pasar a AMARILLO
            #       solo cuando self.contador llegue a cierto límite (ej. 5)
            pass

        elif self.estado == Estado.AMARILLO:
            # TODO: AMARILLO siempre pasa a ROJO
            pass

        elif self.estado == Estado.ROJO:
            # TODO: ROJO pasa a VERDE cuando self.contador llegue a un límite (ej. 3)
            pass

        elif self.estado == Estado.PARPADEO:
            # TODO: define cuándo sale de PARPADEO (ej. nunca, o con un método aparte)
            pass

        self.contador += 1

    def __str__(self):
        return f"Estado actual: {self.estado.name} (contador={self.contador})"


def simular(ciclos: int):
    """Corre la máquina de estados varios ciclos e imprime cada paso."""
    semaforo = Semaforo()
    for i in range(ciclos):
        print(f"Ciclo {i}: {semaforo}")

        # TODO (opcional): simula que un peatón presiona el botón
        # en algún ciclo específico, ej. if i == 4: semaforo.presionar_boton_peaton()

        semaforo.transicionar()


if __name__ == "__main__":
    simular(ciclos=15)
