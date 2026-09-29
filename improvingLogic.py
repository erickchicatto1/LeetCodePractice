# Estilo básico o menos eficiente
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_cuadrados_viejo = []
for n in numeros:
    if n % 2 == 0:
        pares_cuadrados_viejo.append(n * n)

# Estilo lógico y optimizado (List Comprehension)
pares_cuadrados_nuevo = [n * n for n in numeros if n % 2 == 0]

print(pares_cuadrados_nuevo)  # [4, 16, 36, 64, 100]
