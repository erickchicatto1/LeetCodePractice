class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #ideas
        array_left_right = []
        producto_acumulado = 1
        producto_derecha = 1

        #recorrido hacia la izq
        for i in range(len(nums)): #i es el que se pone en la posicion
            array_left_right.append(producto_acumulado)
            producto_acumulado *= nums[i]
        
        #recorrido hacia la derecha
        #empieza en el ultimo indice , detente antes de llegar al -1 , ve restando 1 en 1
        for i in range(len(nums)-1,-1,-1):
            array_left_right[i]*=producto_derecha
            producto_derecha*=nums[i]

        return array_left_right
