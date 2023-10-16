class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime = 4
        even = 5
        mod = 10**9 + 7

        def power(base, n):
            if n == 0:
                return 1
            if base == 0:
                return 0    

            if n % 2 == 0:
                result = power(base,n//2)
                return    result % mod * result % mod
            else:
                result = power(base,n//2)  
                return result % mod * result % mod* base   
 
         
        if n % 2 ==  0:
            total =   power(prime,n//2)%mod*power(even,n//2)%mod
        else:
            total =  power(prime,(n)//2) % mod * power(even,((n)//2)+1) % mod  

        return total % mod                 
              
        
       
