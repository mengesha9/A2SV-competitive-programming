class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        nums.sort()
        count=0
        for  i in range(1,len(nums)):
            if nums[i] <=nums[i-1] :
                temp=nums[i]
                nums[i]=nums[i-1]+1
                count+=(nums[i]-temp)
            
        print(nums) 
        print(count)    
        return count   
