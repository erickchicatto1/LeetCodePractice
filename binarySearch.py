def busqueda_binaria(lista,objetivo):
    izquierda = 0
    derecha = len(lista)-1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) //2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            return medio
        elif objetivo < valor_medio:
            derecha = medio -1
        else:
            izquierda = medio +1 
            
    return -1

mi_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70

resultado = busqueda_binaria(mi_lista, target)

if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("El elemento no se encuentra en la lista.")
