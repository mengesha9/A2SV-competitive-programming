class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        
        n = len(nums)

        def backtrack(index, comb_arr, comb_sum):
            
            if comb_sum == target:
                result.append(comb_arr.copy())
                return
            
            if index == n  or target - comb_sum < nums[index]:
                return    
            
            visited = set()
            for i in range(index, len(nums)):
                if nums[i] not in visited :
                    comb_arr.append(nums[i])
                    visited.add(nums[i])
                    backtrack(i + 1, comb_arr, comb_sum + nums[i])
                    comb_arr.pop()
            
            
        
        if sum(nums) < target:
            return []
           

        nums.sort()
        backtrack(0, [], 0)

        return result 












