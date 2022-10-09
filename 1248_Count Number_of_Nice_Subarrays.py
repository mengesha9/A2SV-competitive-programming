class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count,numberOfOdds,prefix=0,0,collections.defaultdict(int)
        
        for i in range(len(nums)):
            prefix[numberOfOdds]+=1
            if nums[i]%2!=0:
                numberOfOdds+=1
            if numberOfOdds  >= k:
                PossibleSubarray=numberOfOdds-k
                count+=prefix[PossibleSubarray]               
        return count 
