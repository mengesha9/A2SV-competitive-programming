class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array=nums[0]
        sum=0
        for i in nums:
            if sum<0:
                sum=0
            sum+=i
            max_sub_array=max(max_sub_array,sum)
        return max_sub_array
            
        