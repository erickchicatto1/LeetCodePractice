def miniMaxSum(arr):
    # Inicializamos con el primer elemento para tener un punto de partida
    total_sum = 0
    min_val = arr[0]
    max_val = arr[0]
    
    for x in arr:
        # 1. Acumular la suma
        total_sum += x
        
        # 2. Buscar el mínimo manualmente
        if x < min_val:
            min_val = x
            
        # 3. Buscar el máximo manualmente
        if x > max_val:
            max_val = x
            
    # Calculamos los resultados restando los extremos encontrados
    resultado_min = total_sum - max_val
    resultado_max = total_sum - min_val
    
    print(f"{resultado_min} {resultado_max}")

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)