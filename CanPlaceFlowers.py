class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # _ x _ x _ flowerbed , flowers cannot be planted in adjacent plots
        plant=1
        noplant=0
        FlagPlant = None

        for i in range(len(flowerbed)):
            #checar las flores adyacentes , filtro de los 3 puntos , en donde utilizar n?
            if (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0) and (flowerbed[i]==0):
                #plantar
                flowerbed[i] = plant
                n-=1
        

        return n <= 0


        
