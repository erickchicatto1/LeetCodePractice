import time
import random

# 1. Define el algoritmo que quieres analizar
# Como ejemplo, usaremos una búsqueda lineal (O(n))
def buscar_elemento(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

# 2. Función para analizar el rendimiento
def analizar_algoritmo():
    # Probaremos el algoritmo con diferentes tamaños de datos
    tamanos = [1000, 10000, 100000, 1000000]
    
    print(f"{'Tamaño de datos (N)':<20} | {'Tiempo de ejecución (segundos)':<30}")
    print("-" * 55)
    
    for n in tamanos:
        # Generamos una lista de números aleatorios para la prueba
        datos_prueba = [random.randint(1, 1000000) for _ in range(n)]
        objetivo_no_existente = -1  # Forzamos el peor escenario (recorrer toda la lista)
        
        # Tomamos el tiempo de inicio
        inicio = time.perf_counter()
        
        # Ejecutamos el algoritmo
        buscar_elemento(datos_prueba, objetivo_no_existente)
        
        # Tomamos el tiempo de fin
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio
        
        print(f"{n:<20,} | {tiempo_total:<30.6f}")

# Ejecutar el análisis
if __name__ == "__main__":
    analizar_algoritmo()
