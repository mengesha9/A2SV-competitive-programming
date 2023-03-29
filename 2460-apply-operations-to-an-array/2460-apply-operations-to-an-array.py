class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:


        for i in range(len(nums)):
            if i < len(nums)- 1 and nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        print(nums) 
        l = r = 0
        while r < len(nums):
            if nums[r] != 0 and nums[l] == 0:
                nums[l] , nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] != 0  :
                l += 1
                r += 1
            elif nums[r] == 0:
                r += 1
        return nums        


            



