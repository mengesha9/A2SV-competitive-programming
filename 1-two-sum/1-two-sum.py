class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash_Map={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in Hash_Map:
                return [Hash_Map[diff],i]
            Hash_Map[n]=i
        return   
            
            
       
        
        
    
       
                
                        
        