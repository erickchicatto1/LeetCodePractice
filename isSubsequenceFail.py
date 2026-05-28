class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        
        for i in s:
            for j in t:
                if i == j:
                    return True
                else:
                    return False
            

        
        
