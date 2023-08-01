class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
            
        def dp(num):
            rob = [0]*len(num)
            rob[0],rob[1] = num[0],max(num[0],num[1])


            for i in range(2,len(num)):
                rob[i] = max(rob[i-1], rob[i-2] + num[i])

            return rob[-1]
            
        return      max(dp(nums[1:]), dp(nums[:-1]))