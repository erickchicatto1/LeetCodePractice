class Solution:

    def longestPalindrome(self, s: str) -> str:
        pointerDer = 0
        pointerIzq = 0 
        resultado = ""
        
        #.1 recorrer el string
        for i in range(len(s)):
            #2. busqueda impar , entonces iniciar los punteros en el centro
            pointerDer = i #punto de partida de la expansion
            pointerIzq = i

            #3.motor que hace que los punteros se expandan hacia los lados
            while((pointerIzq >= 0) and (pointerDer < len(s)) and (s[pointerIzq]== s[pointerDer])):
                #expansion
                pointerIzq -= 1
                pointerDer += 1

            if len(s[pointerIzq+1:pointerDer]) > len(resultado): # por que pointerIza +1?
                #registrar el resultado
                resultado = s[pointerIzq+1:pointerDer]

            #Para la busqueda par
            pointerDer= i+1 # por que + 1? , para que se mueva uno adelande del otro?
            pointerIzq = i

            while((pointerIzq>=0) and (pointerDer < len(s)) and (s[pointerIzq]==s[pointerDer])):
                pointerIzq -= 1
                pointerDer += 1

            if len(s[pointerIzq+1:pointerDer]) > len(resultado): # por que pointerIza +1?
                resultado = s[pointerIzq+1:pointerDer]

            
        #devolver el resultado registrado
        return resultado








            







        
