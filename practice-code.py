# Ejercicio: Analizador de números
# Completa los espacios marcados con _____ 

numeros = [15, 8, 23, 42, 4, 16, 9, 31, 7, 50]

pares = []
impares = []
mayores_20 = []
suma_total = 0

for num in numeros:
    # 1. Suma este número al total acumulado
    suma_total = _____

    # 2. Si el número es par, agrégalo a la lista "pares"
    if _____:
        pares.append(num)
    else:
        # 3. Si no es par, agrégalo a la lista "impares"
        _____

    # 4. Si el número es mayor a 20, agrégalo a "mayores_20"
    if _____:
        _____

# 5. Calcula el promedio (suma_total dividido por la cantidad de números)
promedio = _____

# 6. Encuentra el número más grande de la lista (sin usar max())
mayor = numeros[0]
for num in numeros:
    if _____:
        mayor = num

print("Números pares:", pares)
print("Números impares:", impares)
print("Números mayores a 20:", mayores_20)
print("Suma total:", suma_total)
print("Promedio:", promedio)
print("El número mayor es:", mayor)
