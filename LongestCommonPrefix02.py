class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==0:
            return ""
        prefijo = strs[0]

        #por que desde la segunda palabra? , para no compararse consigo misma
        for i in range(1,len(strs)):
            while not strs[i].startswith(prefijo): # mientras la palabra actual no empiece con mi prefijo
            #achicamos el prefijo
                prefijo = prefijo[:-1] #quitamos lo ultimo del prefijo

                if prefijo=="":
                    break
        return prefijo
