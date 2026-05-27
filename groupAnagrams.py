class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for i in strs:
            llave = "".join(sorted(i))          
            if llave in words:
                #primero accedo a la lista
                words[llave].append(i)
            else:
                words[llave] = [i]

        return list(words.values())
                
