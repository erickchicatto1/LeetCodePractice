# -------------------------------------------------------------------------
# 1. ESTRUCTURA DE DATOS: LISTA ENLAZADA SIMPLE (LINKED LIST)
# -------------------------------------------------------------------------

class Nodo:
    """Representa un elemento individual en la lista."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Apuntador al próximo nodo

class ListaEnlazada:
    """Controla los nodos y las operaciones de la lista."""
    def __init__(self):
        self.cabeza = None  # El primer nodo de la lista

    def insertar_al_final(self, dato):
        """Añade un nuevo elemento al final de la lista. Tiempo: O(n)"""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        """Imprime la lista en un formato visual. Tiempo: O(n)"""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")


# -------------------------------------------------------------------------
# 2. ALGORITMO: BÚSQUEDA BINARIA (BINARY SEARCH)
# -------------------------------------------------------------------------

def busqueda_binaria(lista_ordenada, objetivo):
    """
    Busca un elemento en una lista YA ORDENADA.
    Tiempo: O(log n) | Espacio: O(1)
    """
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        # Caso ideal: encontramos el elemento
        if lista_ordenada[medio] == objetivo:
            return medio
        
        # Si el objetivo es mayor, ignoramos la mitad izquierda
        elif lista_ordenada[medio] < objetivo:
            izquierda = medio + 1
            
        # Si el objetivo es menor, ignoramos la mitad derecha
        else:
            derecha = medio - 1
            
    return -1  # El elemento no existe en la lista


# -------------------------------------------------------------------------
# 3. PRUEBA DE LAS IMPLEMENTACIONES
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- 🧪 Probando Estructura de Datos: Lista Enlazada ---")
    mi_lista = ListaEnlazada()
    mi_lista.insertar_al_final(10)
    mi_lista.insertar_al_final(20)
    mi_lista.insertar_al_final(30)
    print("Contenido de la lista:")
    mi_lista.mostrar_lista()
    print()

    print("--- 🧪 Probando Algoritmo: Búsqueda Binaria ---")
    datos_ordenados = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    objetivo_a_buscar = 23
    
    print(f"Lista de datos: {datos_ordenados}")
    print(f"Buscando el número: {objetivo_a_buscar}...")
    
    resultado = busqueda_binaria(datos_ordenados, objetivo_a_buscar)
    
    if resultado != -1:
        print(f"¡Éxito! El número {objetivo_a_buscar} está en el índice {resultado}.")
    else:
        print("El número no se encuentra en la lista.")
