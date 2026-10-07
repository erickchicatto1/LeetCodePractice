import time
import tracemalloc

def analizar_algoritmo(funcion, *args, **kwargs):
    """
    Analiza el tiempo de ejecución y el uso de memoria de una función.
    """
    # 1. Iniciar la medición de memoria
    tracemalloc.start()
    
    # 2. Iniciar la medición de tiempo
    inicio_tiempo = time.perf_counter()
    
    # Executar el algoritmo
    resultado = funcion(*args, **kwargs)
    
    # 3. Finalizar las mediciones
    fin_tiempo = time.perf_counter()
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Calcular métricas
    tiempo_total = fin_tiempo - inicio_tiempo
    memoria_pico_mb = memoria_pico / (1024 * 1024) # Convertir bytes a MB
    
    # Mostrar resultados
    print(f"📊 --- ANÁLISIS DE: {funcion.__name__} ---")
    print(f"⏱️  Tiempo de ejecución: {tiempo_total:.6f} segundos")
    print(f"💾 Pico de memoria usado: {memoria_pico_mb:.6f} MB")
    print("-" * 35)
    
    return resultado

# ==========================================
# EJEMPLO DE USO:
# ==========================================

# Definimos un algoritmo de prueba (ej. Crear una lista de números al cuadrado)
def mi_algoritmo(n):
    lista_cuadrados = [i ** 2 for i in range(n)]
    return len(lista_cuadrados)

# Ejecutamos el análisis con un tamaño de datos grande (1 millón de elementos)
print("Iniciando análisis...")
resultado_final = analizar_algoritmo(mi_algoritmo, 1_000_000)
