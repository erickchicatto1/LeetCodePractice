class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        frecuency = {}
        restante =0
        totalNumber = 0
        CandidateSum = 0
        MaxValue = float('-inf')

        #Total
        for i in range(len(nums)):
            totalNumber += nums[i]
            
        #count the frecuency
        for num in nums:
            if num in frecuency:
                frecuency[num] += 1   
            else:
                frecuency[num] = 1
        
        #Evaluate candidates
        for num in nums:
            restante = totalNumber - num  #20-10 = 10
           
            #por la ecuacion
            if restante %2 ==0:
                candidateSum = restante//2 #10

                if not candidateSum in frecuency: #5
                    continue

                if candidateSum == num: #5,10
                    #verificar que existe almenos 2 veces 
                    if frecuency[num] > 1:
                        print("valid candidate")
                        MaxValue = max(MaxValue,num)
                elif candidateSum != num:
                    # 5,10
                    # eliminar el 10 , este es el outlier , con que aparezca una vez basta 
                    MaxValue = num
            else:
                print("No es par")

        return MaxValue
            


            


                


        


        
                

        
