class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num=[0]*len(nums)
        
        for i in range(len(nums)):
            num[(i+k)%len(nums)]=nums[i]
        for i in range(len(num)): 
            nums[i]=num[i]
        return nums    
   
            
            
        