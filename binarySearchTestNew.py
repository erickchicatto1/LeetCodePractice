def busqueda_binaria(lista, elemento_buscado):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        # Encontramos el punto medio
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        # ¿El elemento está en el medio?
        if valor_medio == elemento_buscado:
            return medio  # Devuelve el índice del elemento encontrado
        
        # Si el elemento es menor, descartamos la mitad derecha
        elif elemento_buscado < valor_medio:
            derecha = medio - 1
            
        # Si el elemento es mayor, descartamos la mitad izquierda
        else:
            izquierda = medio + 1

    return -1  # Devuelve -1 si el elemento no está en la lista


# --- Ejemplo de uso ---

# La lista DEBE estar ordenada
mi_lista = [10, 22, 35, 47, 50, 61, 78, 89, 93]
objetivo = 47

resultado = busqueda_binaria(mi_lista, objetivo)

if resultado != -1:
    print(f"¡Elemento encontrado! El número {objetivo} está en el índice {resultado}.")
else:
    print(f"El número {objetivo} no se encuentra en la lista.")
