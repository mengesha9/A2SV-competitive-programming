class Solution:
    def isPowerOfThree(self, n: int) -> bool:
     
        if n<1:
            return False
        answer=log(n,3)
        
        
        return abs(answer-round(answer)) < 1e-10
