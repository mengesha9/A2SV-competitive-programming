class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count = False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count = True
                break
        return count 
          
        
        