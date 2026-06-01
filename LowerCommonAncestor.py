# Definition for a binary tree node.
#class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #Freno de fin de camino
        if root == None:
            return None
        
        #Freno de exito
        if root == p or root == q:
            return root 

        #Situacion 1 , buscar hacia abajo , 
        izq = self.lowestCommonAncestor(root.left,p,q) #aqui se guarda el resultado de toda la busqueda hacia abajo
        der = self.lowestCommonAncestor(root.right,p,q)
        
        #buscan debajo
        if (izq != None) and (der != None):
            #root es el punto de encuentro
            return root
        
        # cuando estan del mismo lado , escenario A
        if izq != None:
            return izq
        
        #escenario B
        if der != None:
            return der

        


        


        
        


        

        

        
