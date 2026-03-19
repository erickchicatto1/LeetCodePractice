# Función que imprime una lista de elementos con su índice
def imprimir_elementos(*elementos):
    for indice, elemento in enumerate(elementos):
        print(f"{indice}. {elemento}")


# Función que imprime pares clave-valor como una tabla
def imprimir_tabla(**datos):
    for clave, valor in datos.items():
        print(f"{clave} = {valor}")


# Ejemplos de uso
imprimir_elementos('apple', 'banana', 'cabbage')
imprimir_tabla(apple='fruit', cabbage='vegetable')
