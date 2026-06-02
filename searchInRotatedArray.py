class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        pointerDer = len(nums) - 1
        pointerIzq = 0
        
        while pointerIzq  <= pointerDer:

            medium = (pointerDer + pointerIzq) //2

            #caso lo encontre
            if nums[medium] == target:
                return medium # regresa el limite
            
            #paso 1 , averiguar cual mitad esta ordenada
            if(nums[pointerIzq] <= nums[medium]):

                #mitad izq esta ordenada , preguntar si el target esta ordenado
                if target >= nums[pointerIzq] and target <= nums[medium]:
                    pointerDer = medium - 1 # lo muevo hacia la izq
                else: #esta en la otra mitad desordenada
                    pointerIzq = medium + 1 
            else:
                #mitad derecha esta ordenada
                if target >= nums[medium] and target <= nums[pointerDer]:
                    pointerIzq = medium + 1
                else:
                    pointerDer = medium - 1 

            #retornar la posicion del target

        return -1













            


        
