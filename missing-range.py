class Solution:

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        recordRange=[]
        curr = lower #number that we always are expecting to see
        #1.iterate in the array of nums
        for i in nums:
            #2.it means i skkiped some numbers
            if i > curr:
                recordRange.append([curr,i-1])
            curr=i+1
        if curr <= upper:
            recordRange.append([curr,upper])
        
        return recordRange

