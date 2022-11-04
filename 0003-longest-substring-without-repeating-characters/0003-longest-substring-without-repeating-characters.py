class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength= -1
        test=''
        
        if len(s) == 0:
            return 0
        if len(s)==1:
            return 1
        
        for c in list(s):
            if c in test:
                test=test[test.index(c)+1:]
            test=test + ''.join(c)
            maxLength = max(len(test),maxLength)
        return maxLength    
        
        

                
                
            
        
        
        
        
        
        
        