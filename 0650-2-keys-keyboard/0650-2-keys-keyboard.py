class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
             
        anser = 1  
        arr = [] 
        d = 2  
        while d <=n :
            while n % d == 0:
                n /= d
                arr.append(d)
            d += 1

        return sum(arr)       


