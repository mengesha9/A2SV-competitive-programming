class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        freq=defaultdict(int)
        presum=[nums[0]]
        for i in range(1,len(nums)):
            presum.append(presum[-1]+nums[i])
        ans=0    
        for i in presum:
           
            diff=i-k
            if diff in freq:
                ans+=freq[diff]
            if i==k:
                ans+=1    
            freq[i]+=1
        print(ans)
        return ans

        
        
      
