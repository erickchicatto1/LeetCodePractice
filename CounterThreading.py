import threading

contador = 0
lock = threading.Lock()

def incrementar_contador():
    global contador
    for idx in range(10):
        with lock:
            contador += 1
            print("Recurso bloqueado")


if __name__ == "__main__":
    hilos = []
    
    for idx in range(5):
        t = threading.Thread(target=incrementar_contador)
        hilos.append(t)
        t.start()
    
    for t in hilos:
        t.join()
    
    print(f"Valor final: {contador}")
