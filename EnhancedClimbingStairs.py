class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return [[]]
        if n == 1: return [[1]]
        
        # En lugar de empezar con prev, curr = 1, 1
        # Empezamos con las combinaciones reales
        prev = [[]]    # Formas para escalón 0
        curr = [[1]]   # Formas para escalón 1
        
        for i in range(2, n + 1):            
            # Calculamos los caminos que vienen de 2 escalones atrás
            caminos_desde_atras = []
            for c in prev:
                caminos_desde_atras.append(c + [2])
            
            # Calculamos los caminos que vienen de 1 escalón atrás
            caminos_desde_actual = []
            for c in curr:
                caminos_desde_actual.append(c + [1])
            
            # --- Tu lógica original de intercambio ---
            temp = curr
            curr = caminos_desde_atras + caminos_desde_actual # Unimos ambas listas
            prev = temp
            
            print(f"Escalón {i}: {curr}")
            
        return len(curr)

solution = Solution()
print(f"\nTotal de formas: {solution.climbStairs(4)}")