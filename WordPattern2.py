class Solution:

    def __init__(self):
        self.mappingPattern = {} 
        self.asegurarReglaBiyectiva = {}

    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        #0.pasos de emergencia
        #ambos terminaron al mismo tiempo , exito
        if pattern == "" and s == "":
            return True
        #si uno termino pero el otro todavia tiene letras
        if pattern == "" or s == "":
            return False

        #1.Agarrar la letra actual 
        letra = pattern[0]

        #2.ya conocemos la letra?
        if letra in self.mappingPattern:
            palabra_extraida = self.mappingPattern[letra] #extraigo la palabra
            #el string s , empieza con la palabra que ya conocemos?
            if s.startswith(palabra_extraida):
                #avanzamos cortando el patron y cortando el tamaño de la palabra en s
                if self.wordPatternMatch(pattern[1:],s[len(palabra_extraida):]):
                    return True
            
            return False # si no empezaba con esa letra , o el camino de adelante fallo
        
        #3.Si la letra es nueva 
        for index in range(1,len(s)+1):
            pedazo = s[0:index]
            #asegurar de que ninguna otra letra se halla adueñado de ese pedazo antes
            if pedazo not in self.asegurarReglaBiyectiva:
                #apuesta
                #guardar en los 2 dicc la nueva relacion 
                self.mappingPattern[letra] = pedazo
                #para evitar que otra letra use el mismo pedazo
                self.asegurarReglaBiyectiva[pedazo] = letra

                #backtracking , probar el futuro y limpiar si falla 
                if self.wordPatternMatch(pattern[1:],s[index:]):
                    return True
                
                del self.mappingPattern[letra]
                del self.asegurarReglaBiyectiva[pedazo]

        return False






        


            







            
        
