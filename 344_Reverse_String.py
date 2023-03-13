class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.s = s
        self.helper(0,len(s)-1)
        
    def helper(self, i, j):
            if i> j:
                return 

            self.s[i], self.s[j] =  self.s[j], self.s[i]
            
            return self.helper(i+1, j-1)
        


            
