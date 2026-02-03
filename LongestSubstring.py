#https://builtin.com/data-science/sliding-window-algorithm

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        last_seen = {} # Diccionario para guardar {caracter: posicion}

        for right in range(len(s)):
            char = s[right]
            
            # Si ya vimos el caracter y está dentro de nuestra ventana actual
            if char in last_seen and last_seen[char] >= left:
                # Movemos el inicio de la ventana justo después de la repetición
                left = last_seen[char] + 1

            # Actualizamos la posición del caracter
            last_seen[char] = right
            
            # Calculamos el tamaño de la ventana: (fin - inicio + 1)
            current_window_len = right - left + 1
            max_len = max(max_len, current_window_len)
            
        return max_len
            
            
solution = Solution()
print(f"This is the soluction {solution.lengthOfLongestSubstring("abcdeee")}")