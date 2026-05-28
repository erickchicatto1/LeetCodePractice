class Node:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node() # lo mas nuevo
        self.tail = Node() #lo mas viejo

        #conectar entre si los nodos
        self.head.next = self.tail #esta es la propiedad que hace que sea DLL
        self.tail.prev = self.head

        self.size = 0

    def append(self,nuevo_nodo):
        next_new = self.head.next
        prev_new = self.head #guarda elementos justo despues de esta linea 
        
        #estirar los brazos , paso para actualizar
        nuevo_nodo.next = next_new
        nuevo_nodo.prev = prev_new

        #los vecinos lo adoptan
        prev_new.next = nuevo_nodo
        next_new.prev = nuevo_nodo

        self.size += 1

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.KeystoNode = {}
        self.lista = DoubleLinkedList()
    
    def get(self, key: int) -> int:
        #return the value of the key
        #if the key exist if not return -1
        if key in self.KeystoNode:
            nodo = self.KeystoNode[key]
            self.lista.remove(nodo) #lo elimino de su posicion actual
            self.lista.append(nodo) #lo agrego al inicio
        else:
            return -1

        return nodo.value    

    #aqui se hacen y se fabrican los nodos
    def put(self, key: int, value: int) -> None:
        #if a number exceeds the capacity evict the least recently used key

        #update the value of the key if exist
        if key in self.KeystoNode:
            nodo = self.KeystoNode[key]#primero extraigo el nodo completo
            nodo.value = value #actualizo el atributo interno con el valor que me da la funcion , sin romper la memoria
            #nodo = value # error no hacer esto o pierdo el acceso al nodo y a sus metodos y propiedades
            self.lista.remove(nodo) #lo elimino de su posicion actual
            self.lista.append(nodo) #lo agrego al inicio
        #if not add key-value pair to cache
        else:
            #nodo = self.KeystoNode[key] # error este nodo aun no existe 
            nodo_viejo = self.lista.tail.prev
            #controlar la capacidad del cache
            #1. validar el espacio del cache
            if len(self.KeystoNode) == self.capacity:
                #si esta lleno toca hace evict , que es desalojar , eliminar el miembro mas viejo de mi lista
                self.lista.remove(nodo_viejo) 
                del self.KeystoNode[nodo_viejo.key]
            #insertamos un nuevo nodo
            nodoNuevo = Node(key,value)
            #guardar en el diccionario y agregarlo al inicio de la lista
            self.KeystoNode[key] = nodoNuevo
            #agregarlo al inicio de la lista 
            self.lista.append(nodoNuevo)

# Your LRUCache object will be instantiated and called as such:
capacity = 2
key = 2
value = 1
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
