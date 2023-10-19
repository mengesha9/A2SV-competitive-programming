class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        curr = sum(nums)
        n = len(nums)

        if len(nums)==1 or curr % 2 != 0:
            return False
        memo = set()
        memo.add(0)
        for n in nums:
            tmp = set()
            for v in memo:
                tmp.add(v+n)
            memo |= tmp
            if curr//2 in memo:
                return True
        return False        

        
