class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
      

        result = []


        def backtrack(index, comb, comb_sum):
            
                if comb_sum == target:
                    result.append(comb.copy()) 
                    return 
                if index == len(nums) or (target-comb_sum ) < nums[index]:
                    return  
                
                for i in range(index, len(nums)):
                    comb.append(nums[i]) 
                    backtrack(i  , comb, comb_sum + nums[i])
                    comb.pop()
                     

        
        backtrack(0, [], 0)
        return result              
        


    
    




