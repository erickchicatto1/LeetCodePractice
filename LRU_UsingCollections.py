import collections
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]
 

    #aqui se hacen y se fabrican los nodos
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        self.dic[key] = value

        if len(self.dic) > self.capacity:
            self.dic.popitem(False)

# Your LRUCache object will be instantiated and called as such:
capacity = 2
key = 2
value = 1
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)
