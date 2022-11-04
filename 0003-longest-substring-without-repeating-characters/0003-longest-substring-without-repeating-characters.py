class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength= 0
      
        
        dic={}
        i=0
        for j in range(len(s)):
            if s[j] in dic:
                i=max(i,dic[s[j]]+1)
                
            dic[s[j]]=j
                

            maxLength = max(j-i+1,maxLength)
        return maxLength    
        
        

                
                
            
        
        
        
        
        
        
        