import queue
import threading
import urllib.request  # Reemplazo de urllib2

# Función que ejecutarán los hilos
def get_url(q, url):
    try:
        # Abrimos la URL y leemos el contenido
        with urllib.request.urlopen(url) as response:
            data = response.read()
            q.put((url, data[:100])) # Guardamos la URL y una muestra de los datos
    except Exception as e:
        q.put((url, f"Error: {e}"))

theurls = ["https://www.google.com", "https://www.yahoo.com", "https://www.wikipedia.org"]

q = queue.Queue()
threads = []

# 1. Crear e iniciar hilos
for u in theurls:
    t = threading.Thread(target=get_url, args=(q, u))
    t.daemon = True
    t.start()
    threads.append(t)

# 2. Recolectar TODOS los resultados
# En lugar de un solo get(), iteramos según el número de URLs
for _ in range(len(theurls)):
    url, result = q.get()
    print(f"Resultado de {url}: {result}...")
    
print("\nProceso finalizado.")
