class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        #2,1,3,5,6
        minVal = 0
        operation = 0

        #1. Find the min value x in nums
        for i in nums:
            if i < minVal:
                minVal = i   #1 for only appears first the min value
                break
        
        #2. make the operation with the min value
        operation = minVal * multiplier

        #3. 



        
