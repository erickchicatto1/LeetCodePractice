class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Prepare the pointers
        pointerLeftN1 = 0
        pointerRightN1 = len(nums1)-1

        pointerLeftN2 = 0
        pointerRightN2 = len(nums2)-1
        
        ArrayMerged = []
        operation = m + n 
        
        #Algorithm
        #1.Evaluate 
        while(len(nums1) and len(nums2)<=operation):
            #Make the merge
            pointerRightN1+=1
            nums1[pointerRightN1]

            
