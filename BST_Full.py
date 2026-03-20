class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None #raiz

    def insert(self,value):
        #temp = self.value
        new_node = Node(value) #el objeto ya se creo y se puede utilizar con las variables creadas abajo
        #evaluamos si la raiz es cero y si es cero asignamos un nodo        
        if self.root is None:
            self.root = new_node # self.root, es un objeto de la clase Node
            return True       
        
        #Se usará para recorrer el árbol y encontrar dónde colocar new_node.
        temp = self.root #para que avance entre el arbol , guarda todo el nodo 

        while True:
            #Primero, se comprueba si el valor que quieres insertar ya existe en el árbol.
            #Si existe, no se permite duplicados, así que se retorna False.
            if new_node.value == temp.value: # si los nodos son iguales entones se retorna falso  , temp.value esta guardando una referencia
                return False
            
            #Si el valor del nuevo nodo es menor que el nodo actual (temp.value):
            #   Se verifica si no hay hijo izquierdo (temp.left is None).
            #       Si no hay, el nuevo nodo se coloca allí y se termina la función.
            #   Si ya hay un hijo izquierdo, temp = temp.left → se mueve a ese nodo y sigue comparando.
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
                
            #Si el valor es mayor o igual que temp.value (en tu caso ya manejaste igualdad arriba):    
            #   Se verifica si no hay hijo derecho (temp.right is None).
            #       Si no hay, el nuevo nodo se coloca allí y se termina la función.
            #   Si ya hay un hijo derecho, temp = temp.right → se mueve a ese nodo y sigue comparando.    
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self,value):
        temp = self.root
        while(temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

         

            
        
            
            
        
                
