class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        indice_minimo = 0

        while(k>0):
            #1. Find the min value x in nums
            for i in range(len(nums)):
                if nums[i] < nums[indice_minimo]:
                    indice_minimo = i   # for only appears first the min value  
                #2. make the operation with the min value
            nums[indice_minimo] = nums[indice_minimo] * multiplier
            k-=1

        return nums
