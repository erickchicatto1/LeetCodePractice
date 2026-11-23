class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)

    # Recorrido In-Order (imprime los datos ordenados de menor a mayor)
    def imprimir_ordenado(self, nodo):
        if nodo is not None:
            self.imprimir_ordenado(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.imprimir_ordenado(nodo.derecha)

# --- Uso del código ---
arbol = ArbolBinarioBusqueda()
numeros = [50, 30, 70, 20, 40, 60, 80]

for num in numeros:
    arbol.insertar(num)

print("Elementos ordenados:")
arbol.imprimir_ordenado(arbol.raiz)  # Salida: 20 30 40 50 60 70 80

print("\n¿Está el 40 en el árbol?:", arbol.buscar(40))  # Salida: True
print("¿Está el 99 en el árbol?:", arbol.buscar(99))  # Salida: False
