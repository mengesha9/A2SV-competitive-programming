class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return a
        for i in range(n):
            a,b=b,a+b
            print(a)
        return a    
            
            
        
        
       