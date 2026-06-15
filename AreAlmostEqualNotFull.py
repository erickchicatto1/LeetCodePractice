class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        #Ideas
        #1.check if all the elements inside are the same
        for index1 in s1:
            for index2 in s2:
                #2.Iterate over the s1 to check if exist a similar character
                if index1==index2:
                    return True
                #3.Check only for one character        
                else:
                    return False
            


                

