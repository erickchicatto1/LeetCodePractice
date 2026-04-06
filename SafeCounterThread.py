import threading

lock = threading.Lock()
counter = 0

local_counts = []

def Counter():
    global counter
    local_counter = 0
     
    for i in range(5):
        local_counter += 1
        with lock:
            counter += 1
            print("Recurso bloqueado")
    local_counts.append(local_counter)

   
if __name__ == "__main__":
    hilos = []
    #counterHilos = 0
    
    for i in range(5):
        t = threading.Thread(target=Counter,args=(i,)) #tiene que ser una tupla
        #counterHilos += 1
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()
    
    total_local = sum(local_counts)
    print(f"Total global: {counter}")
    print(f"Total local (suma de hilos): {total_local}")
    
    #comparar valores de contadores 
    if counter == total_local:
        print("Son iguales \n")
    else:
        print("Diferentes")
        
    print(f"El valor final : {counter}")
    
        
    
