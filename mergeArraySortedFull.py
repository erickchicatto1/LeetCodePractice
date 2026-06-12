class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        Pointernums1 = m-1
        Pointernums2 = n-1 
        Pointertowrite = m+n -1

        while (Pointernums1 >=0 and Pointernums2 >= 0):

            if nums1[Pointernums1] < nums2[Pointernums2]:
                nums1[Pointertowrite] = nums2[Pointernums2]
                Pointernums2-=1
            else:
                nums1[Pointertowrite] = nums1[Pointernums1]
                Pointernums1-=1

            Pointertowrite-=1

        while(Pointernums2 >= 0):
            nums1[Pointertowrite] = nums2[Pointernums2]
            Pointertowrite-=1
            Pointernums2 -= 1
