class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0 and len(s) == 0:
            return 

        #crear las cajas  , contenedor de cada fila
        cajas = [[] for i in range(numRows)]#error [] * numRows , hacer subcajas vacias [[],[]]

        fila_actual = 0
        yendo_hacia_abajo = False

        #Recorrer el texto original letra por letra
        for letter in s:
            #1. Meter la letra en la caja que le toca
            cajas[fila_actual].append(letter) #append lo envia hasta lo ultimo

            #2.tocamos un extremo?, el techo de la fila 0, el fondo es la fila (numRows-1) , interruptor
            if fila_actual == 0 or fila_actual == (numRows-1):
                yendo_hacia_abajo = not yendo_hacia_abajo #inversor , error al haber puesto True , se necesita invertir
            
            #3. moverlos a la sigt fila segun la direccion , motor
            if yendo_hacia_abajo == True:
                fila_actual = fila_actual + 1
            else:
                fila_actual = fila_actual - 1
            
        #Juntar el contenido de todas las cajas
        resultado_final = ""
        for caja in cajas:
            texto_unido = "".join(caja)
            resultado_final = resultado_final + texto_unido
        
        return resultado_final
