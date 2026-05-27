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
            nodo = self.desempate[key] #pero como estoy conectando el nodo ? 

            #Mudar de casa al nodo


        else:
            return -1

    #aqui se hacen y se fabrican los nodos
    def put(self, key: int, value: int) -> None:
        pass

        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
