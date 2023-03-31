class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        i = 1
        anser = 1
        while i <= a:
            if a % i == 0 and b % i == 0:
                anser = max(anser, i)
            i += 1
        return anser        


