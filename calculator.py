class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        self.resultado = a + b
        return self.resultado

    def restar(self, a, b):
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a, b):
        self.resultado = a * b
        return self.resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        self.resultado = a / b
        return self.resultado

    def potencia(self, base, exponente):
        self.resultado = base ** exponente
        return self.resultado


# Ejemplo de uso
calc = Calculadora()

print("Suma:", calc.sumar(5, 3))
print("Resta:", calc.restar(5, 3))
print("Multiplicación:", calc.multiplicar(5, 3))
print("División:", calc.dividir(5, 3))
print("Potencia:", calc.potencia(2, 4))
