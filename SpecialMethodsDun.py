class Activo:
    def __init__(self, nombre, inversion, valor_actual):
        self.nombre = nombre
        self.inversion = inversion
        self.valor_actual = valor_actual

    def rendimiento(self):
        return (self.valor_actual - self.inversion) / self.inversion

    def __str__(self):
        return f"{self.nombre}: rendimiento {self.rendimiento():.2%}"

    def __lt__(self, other):
        return self.rendimiento() < other.rendimiento()
