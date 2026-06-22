class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        words = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i in words:
                words[i] += 1
            else:
                words[i]= 1
        
        for j in t:
            if j not in words or words[j]==0:
                return False
            else:
                words[j] -= 1
        return True



        
