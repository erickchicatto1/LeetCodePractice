class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indexToSave=[]

        #1.recorrer las cadenas al mismo tiempo , como es que se recorren al mismo tiempo?
        for i in range(len(s1)):
            #2.guardar los errores
            if s1[i] != s2[i]:
                indexToSave.append(i)
        
        #3.revisar cuantos errores se encontraron
        #fueron cero?
        if len(indexToSave)==0:
            return True
        #fueron dos?
        if len(indexToSave)==2:
            primer_error = indexToSave[0]
            segundo_error = indexToSave[1]

            if s1[primer_error] == s2[segundo_error] and s1[segundo_error] == s2[primer_error]:
                return True
            else:
                return False

        #fue otro tipo de error?
        if len(indexToSave) != 0 and len(indexToSave) !=2:
            return False 




                





        
