class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        count = 0
        while i < len(nums):
        
            pos = nums[i] - 1
            if pos < 0 or pos > len(nums)-1 or ( 0<= pos <= len(nums)-1 and   nums[pos] == nums[i]):
        
                i += 1  
            else:
                nums[i],nums[pos] = nums[pos], nums[i] 
            

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1  
        return nums[-1] + 1        





