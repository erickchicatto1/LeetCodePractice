def factorial(n):
    # 1. Caso base: detiene la recursión cuando n es 0 o 1
    if n == 0 or n == 1:
        return 1
    
    # 2. Caso recursivo: la función se llama a sí misma con un valor menor
    else:
        return n * factorial(n - 1)

# Probando la función
resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")  # Imprime 120
