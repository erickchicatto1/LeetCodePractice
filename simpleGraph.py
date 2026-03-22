class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def agregar_arista(self, v1, v2):
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        self.vertices[v1].append(v2)
        # Para grafo no dirigido, descomenta:
        # self.vertices[v2].append(v1)
    
    def mostrar(self):
        for vertice, vecinos in self.vertices.items():
            print(f"{vertice} -> {vecinos}")

# Uso:
g = Grafo()
g.agregar_arista('A', 'B')
g.agregar_arista('A', 'C')
g.agregar_arista('B', 'D')
g.mostrar()
