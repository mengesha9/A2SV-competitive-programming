class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        presum={}
        presum[0]=1
        count=0
        s=0
        for n in nums:
            s+=n
            if s-k in presum:
                count += presum[s-k]
            presum[s] = presum.get(s,0) +1
        return count
