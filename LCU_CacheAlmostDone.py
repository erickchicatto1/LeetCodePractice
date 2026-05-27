class Node:

    def __init__(self,key=None,value = None,freq = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None #brazos que apuntan a otros nodos vecinos
        self.next_ = None #brazos que apuntan a otros nodos vecinos

#Para hacer frecuencias ficticias , nodos?
class DoubleLinkedList:

    def __init__(self): #quien utilizaria este value?
        self.head = Node() #Para enlazar los nodos , sin memoria
        self.tail = Node()
    
        #conectar entre si los nodos
        self.head.next_ = self.tail #son los nodos siguientes
        self.tail.prev = self.head 

        self.size = 0  

    def append(self,nuevo_nodo):
        #1.Etiquetar al vecino que ya existe a la derecha
        next_new = self.head.next_ #Este es el nodo(tail) que ya estaba despues del head
        #2.Etiquetar al vecino de la izquierda (que siempre es head)
        prev_new = self.head

        #Conectar el nuevo nodo utilizando las etiquetas
        nuevo_nodo.next_ = next_new #El nuevo nodo apunta a la derecha
        nuevo_nodo.prev = prev_new #El nuevo nodo apunta a la izquierda

        #Hacer que los nuevos vecinos adopten el nuevo nodo 
        prev_new.next_ = nuevo_nodo #El head ahora apunta al nuevo nodo
        next_new.prev = nuevo_nodo #El de la derecha ahora apunta hacia atrás al nuevo nodo
        
        self.size+=1
    
    
    def remove(self,node):
        node.prev.next_ = node.next_
        node.next_.prev = node.prev

        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.desempate = {} #Diccionario de llaves a nodos
        self.Frecuency = {} #Diccionario de frecuencias a listas enlazadas
        self.minFreq_ = 0 # a quien borrar cuando el cache se llene
        #self.nodo = DoubleLinkedList(), las listas deben de vivir en los diccionarios


    def get(self, key: int) -> int:
        #1. buscar que key exista en desempate
        if key in self.desempate:
            nodo = self.desempate[key] #pero como estoy conectando el nodo con el metodo de put 
            #Mudar de casa al nodo
            #1.
            self.Frecuency[nodo.freq] #buscar en la lista vieja donde vive el nodo
            #2.
            self.Frecuency[nodo.freq].remove(nodo) # sacar al nodo de la lista vieja
            #3.truco de desempate , aumentar la frecuencia , si la lista de la frecuencia del nodo se quedo vacia y esa frecuencia coincide con la minima global
            if self.Frecuency[nodo.freq].size == 0 and self.minFreq_ ==nodo.freq:
                self.minFreq_ += 1
            #4.incrementar la frecuencia
            nodo.freq += 1
            #5.buscar en la lista nueva , si no existe una lista para este nuevo numero de frecuencia
            if nodo.freq not in self.Frecuency:
                #Asignamos a esta posicion del diccionario 
                self.Frecuency[nodo.freq] = DoubleLinkedList()# es valido definir asi un objeto en python?
            self.Frecuency[nodo.freq].append(nodo)
        else:
            return -1
        
        return nodo.value

    #aqui se hacen y se fabrican los nodos , suponer
    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return 

        lista_lfu = []
        #1. Update the value of the key if presents 
        if key in self.desempate:
            nodo.value = value # se crea un nuevo nodo
            self.get(key) #para hacer la mudanza del nodo
        #2. or insert the key if not already present
        elif key not in self.desempate:
            #3. when the cache reaches its capacity , it should invalidate and remove the lfu key
            if (len(self.desempate) == self.capacity):
                #buscar la lista de los menos usados , utilizando una variable guia 
                lista_lfu = self.Frecuency[self.minFreq_]
                #desempatr por LRU , tomar el nodo mas viejo
                nodo_a_borrar =  lista_lfu.tail.prev # como se va a instanciar al objeto , ya va a tener las propiedades del Nodo
                #Eliminacion , sacar el nodo de la lista enlazada
                lista_lfu.remove(nodo_a_borrar)
                del self.desempate[nodo_a_borrar.key]
            #4.creando un nuevo nodo real
            nuevo_nodo = Node(key,value)
            self.desempate[key] = nuevo_nodo  
            #si no existe , asegurar que exista en Frecuency
            if nuevo_nodo not in self.Frecuency:
                self.Frecuency[nodo.freq] = DoubleLinkedList()

            self.Frecuency[nodo.freq].append(nuevo_nodo)    
            self.minFreq_ = 1

# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
