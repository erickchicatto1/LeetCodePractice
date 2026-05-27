class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        countingElements = {}
        
        #Check the frecuency
        for num in nums:
            if num in countingElements:
                countingElements[num] += 1
            else:
                countingElements[num] = 1

        #select the most frecuent value or return the max?
        RepetVal = max(countingElements)

        return RepetVal
