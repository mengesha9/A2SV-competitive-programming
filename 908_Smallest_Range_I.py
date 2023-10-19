class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        range = max(nums)-min(nums)
        if 2*k >= range:
            return 0
        else:
            return range - 2*k    

        
