class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        hashmap = defaultdict(int)
        n = len(nums)
        def back(ind,curr):
            if ind >= n:
                if curr == target:
                    return 1
                else:
                    return 0 
            if (ind,curr) not in hashmap:
                hashmap[(ind,curr)] = back(ind+1,curr-nums[ind]) + back(ind+1,curr+ nums[ind])  

            return hashmap[(ind,curr)]  

        return back(0,0)