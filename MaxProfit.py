class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #B-S-B-S-B-S 
        Total = 0
        profit = []
        for i in range(1,len(prices)): #empieza desde el cero , arrancamos el dia desde el indice 1
            if prices[i] > prices[i-1]:
                total = prices[i] - prices[i-1]   #precio_de_hoy - precio_de_ayer
                Total += total

        return Total
                

            


