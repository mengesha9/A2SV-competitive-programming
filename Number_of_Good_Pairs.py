class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count=0
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                count+=dic[nums[i]]
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1 
                
        return count 
