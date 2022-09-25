class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
        """
        
        for i in range(len(nums)):
            cur_min=i
            for j in range(i,len(nums)):
                if nums[j]<nums[cur_min]:
                    cur_min=j
            nums[cur_min] ,nums[i]=nums[i],nums[cur_min]
        return nums    







