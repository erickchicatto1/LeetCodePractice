import threading
import time
from concurrent.futures import ThreadPoolExecutor, FIRST_EXCEPTION, wait

def func(raise_exc):
    thread_name = threading.current_thread().name
    print(f"Running in {thread_name}")
    
    if raise_exc:
        time.sleep(1)
        print(f"Error occurring in {thread_name}...")
        raise ValueError("Intentional Exception")

    # Simulamos una tarea larga
    for i in range(3):
        time.sleep(1)
        print(f"{thread_name} working... {i+1}s")
    
    return f"Result from {thread_name}"

# No es estrictamente necesario el Lock para una bandera booleana simple en este flujo
running = True 

with ThreadPoolExecutor(max_workers=2) as executor:
    # Enviamos las tareas
    futures = {
        executor.submit(func, False): "Task_Smooth",
        executor.submit(func, True): "Task_Error"
    }

    # Esperamos hasta que la primera tarea falle o todas terminen
    done, not_done = wait(futures, return_when=FIRST_EXCEPTION)

    for fut in done:
        try:
            res = fut.result()
            print(f"Task finished: {res}")
        except Exception as e:
            print(f"An exception occurred: {e}. Stopping others...")
            # Cancelamos las tareas que aún no han empezado
            for pending_fut in not_done:
                pending_fut.cancel()
            
            # Nota: Los hilos que ya están en time.sleep o ejecutando 
            # no se detendrán instantáneamente en Python, pero
            # el programa principal ya sabe que debe abortar.

print("Bye")
