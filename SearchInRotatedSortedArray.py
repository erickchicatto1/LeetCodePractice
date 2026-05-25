class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #1.iterate over the list
        for i in range(len(nums)):
            #2.Select the target
            if nums[i] == target:
                return i
        
        else:
            return -1







        
