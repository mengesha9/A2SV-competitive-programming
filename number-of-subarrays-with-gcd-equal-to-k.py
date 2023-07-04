class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b 
            return a

        n = len(nums)
        res = 0
        for i in range(n):
            temp = 0
            for j in range(i, n):
                temp = gcd(temp, nums[j])
                if temp == k:
                    res += 1
               
        return res