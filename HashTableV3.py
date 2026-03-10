class HashTable:
    def __init__(self,size=7):
        self.data_map = [None]*size #crea una lista de len size = 7 , [None, None, None, None, None, None, None]
        
    def __hash(self,key):
        my_hash = 0 
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) #funcion hash , ord , devuelve el valor ascii , convierte en un indice de la lista
        return my_hash
    
    def print_table(self):
        for i ,val in enumerate(self.data_map):
            print(i,": ",val)

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] == None: #Revisar si el espacio esta vacio
            self.data_map[index] =[]
        self.data_map[index].append([key,value])
        #to print the recent table
        self.print_table()
    
    '''
    bucket → lista de pares
    pair → [key,value]
    
    pair[0] → key
    pair[1] → value
    
    '''
    
    def get_item(self,key):
        index = self.__hash(key)
        bucket = self.data_map[index]
        
        if bucket is not None:
            for pair in bucket:
                if pair[0] == key:
                    print(f"This is the value{pair[1]}")
                    return pair[1]
        return None
    
    '''
    data_map → bucket → pair → key
    '''
    def keys(self):
        all_keys = []

        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_keys.append(pair[0])
        return all_keys
                
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.get_item('bolts')
print(my_hash_table.keys())

my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)


print(my_hash_table.keys())



    

    
    
    
        
        
        
    
            
        
        
    
    
