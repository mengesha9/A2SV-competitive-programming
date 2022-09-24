class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        target_idx=[]
        for i in range(1,len(nums)):
            j=i
            while nums[j-1]>nums[j] and j>0:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1      
       

        for i in range(len(nums)):
            if nums[i] == target:
                target_idx.append(i)
        
        return target_idx