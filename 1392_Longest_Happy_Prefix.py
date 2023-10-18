class Solution:
    def longestPrefix(self, s: str) -> str:


        pre = suf = ""

        i = 0
        j = len(s)-1
        ans = ""
        while i < len(s)-1 and j >0:
            pre += s[i]
            suf = s[j] + suf
            if suf == pre:
                ans = pre
            i += 1
            j -= 1    

    
        return ans 
        
