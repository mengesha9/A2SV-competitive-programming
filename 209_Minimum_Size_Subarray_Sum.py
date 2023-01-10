class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n=len(nums)
        
        presum=0
        for i in range(n):
            presum+=nums[i]
        if presum<target:
            return 0  
        j=0
        count=n
        total=0
        i=0      
        while i<n:
            total+=nums[i]
            while total>=target and j<=i:
                    count=min(count,i-j+1)
                    total-=nums[j]
                    j+=1
            else:
                i+=1
               
        return count  
