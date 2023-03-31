class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        a = n 
        b = n >> 1
        n = n>> 1
        while n:
        
            if (a % 2 == 0 and b % 2 == 0) or ( a % 2 != 0 and b% 2 != 0):
                return False
            a = b 
            b =n = n >> 1
        return True    
            
                  

