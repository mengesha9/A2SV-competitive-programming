class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n > 1 and n%3 != 0:
            return False
        if n <  1:
            return False   
        if n == 1:
            return True
        return self.isPowerOfThree(n/3) 



        
        
        