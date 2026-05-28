class Node:
    def __init__(self,key,value)
    self.key = key
    self.value = value
    self.next = None
    self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        #conectar entre si los nodos
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def append(self,nuevo_nodo):
        

        

    def remove(self):
        pass


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
