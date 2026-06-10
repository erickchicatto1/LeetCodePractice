from heapq import heappush, heappop
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # 1. Ordenamos los queries por su punto de inicio
        queries.sort(key=lambda x: x[0])
        
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        queries_used = 0
        j = 0
        
        for i, num in enumerate(nums):
            # Aplicamos los queries que ya expiraron en este índice
            operations += deltaArray[i]
            
            # Absorber todos los queries que empiezan en 'i'
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
                
            # Decisión Greedy: Mientras la fuerza actual sea menor a la necesaria...
            while operations < num and heap:
                max_r = -heappop(heap)
                
                # IMPORTANTE: Si el query que sacamos ni siquiera llega a 'i', 
                # no nos sirve para este índice ni para el futuro. Lo descartamos.
                if max_r < i:
                    continue
                
                # Si sí llega, lo activamos
                operations += 1
                queries_used += 1
                
                # Programamos su vencimiento (dejará de aportar en max_r + 1)
                if max_r + 1 < len(deltaArray):
                    deltaArray[max_r + 1] -= 1
            
            # Validación de imposibilidad: Si después de usar los mejores queries
            # disponibles seguimos sin alcanzar el valor de num[i]
            if operations < num:
                return -1
        
        # Total de queries menos los que obligatoriamente tuvimos que gastar
        return len(queries) - queries_used
