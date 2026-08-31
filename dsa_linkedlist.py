class Nodo:
    def __init__(self, datos):
        self.datos = datos  # Guarda el valor
        self.siguiente = None  # Apunta al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista

    def insertar_al_inicio(self, datos):
        nuevo_nodo = Nodo(datos)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.datos} -> ", end="")
            actual = actual.siguiente
        print("None")

# --- Prueba del algoritmo ---
mi_lista = ListaEnlazada()
mi_lista.insertar_al_inicio(30)
mi_lista.insertar_al_inicio(20)
mi_lista.insertar_al_inicio(10)

print("Estructura de la Lista Enlazada:")
mi_lista.mostrar_lista()  # Resultado: 10 -> 20 -> 30 -> None
