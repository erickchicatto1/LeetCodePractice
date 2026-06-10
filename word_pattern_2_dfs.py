class Solution:

    def wordPatternMatch(self,pattern,text,mape=None,viewed=None):
        if mape is None:
            mape = {}
        if viewed is None:
            viewed = set()

        if len(pattern)==0 and len(text)== 0:
            return True
        
        if not pattern or not text :
            return False

        actual_letter = pattern[0]
        #Option A , letter is already in the dict
        if actual_letter in mape:
            #extract the word
            extraction_of_letter = mape[actual_letter]
            if text.startswith(extraction_of_letter):
                return self.wordPatternMatch(pattern[1:],text[len(extraction_of_letter):],mape,viewed)     
            else:
                return False  

        #Option B , letter in new , backtracking
        #1
        for i in range(1,len(text)+1):
            #2
            selected_word = text[:i]
            #3 biyection
            if selected_word in viewed:
                continue
            #4 register
            else:
                mape[actual_letter] = selected_word
                viewed.add(selected_word)
                #5 backtracking
                if self.wordPatternMatch(pattern[1:],text[i:],mape,viewed):
                    return True #path correct
                else:
                    #6 
                    del mape[actual_letter]
                    viewed.remove(selected_word)
        return False
