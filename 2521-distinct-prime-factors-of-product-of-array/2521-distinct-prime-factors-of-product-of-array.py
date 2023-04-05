class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        self.visited = set()
        for i in range(len(nums)):
            self.findprime(nums[i])


        return len(self.visited)    
            

    def findprime(self, n):
       
        d = 2
        while d*d <= n:
            while n %d == 0:
                n //=d
                self.visited.add(d)
            d += 1
        if n > 1:
            self.visited.add(n)    
        return         


