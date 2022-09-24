class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        
       """     
                
        
        beg=0
        end=0
        size=len(nums)
        while end<size:
            if nums[end]!=0:
                nums[end],nums[beg]=nums[beg],nums[end]
                beg+=1
            end+=1   
        return nums  
        
       
       
                
        
        
        
        