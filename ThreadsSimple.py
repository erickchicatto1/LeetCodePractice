import threading
import time

def tarea(nombre: str, segundos: int) -> None:
    print(f"[{nombre}] iniciando")
    time.sleep(segundos)      # GIL se libera aquí
    print(f"[{nombre}] listo")

# Crear y lanzar threads
t1 = threading.Thread(target=tarea, args=("A", 2))
t2 = threading.Thread(target=tarea, args=("B", 1))

t1.start()
t2.start()

t1.join()   # espera a que t1 termine
t2.join()

print("ambos terminaron")
