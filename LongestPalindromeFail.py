class Solution:

    def longestPalindrome(self, s: str) -> str:
        pointerDer = 0
        pointerIzq = 0 
        
        #.1 recorrer el string
        for i in range(len(s)):
            #2. busqueda impar , entonces iniciar los punteros en el centro
            pointerDer = i
            pointerIzq = i 

            while(len(s)):


