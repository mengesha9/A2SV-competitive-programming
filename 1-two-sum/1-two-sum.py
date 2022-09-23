class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            dif =target-nums[i]
            if dif in nums:
                j=nums.index(dif)
                if i !=j:
                    return [i,j]
                                    
                         
        return 
            
       
        
        
    
       
                
                        
        