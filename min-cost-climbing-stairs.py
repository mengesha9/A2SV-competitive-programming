class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        hashmap = defaultdict(int)
        n = len(cost)
        def dp(n):
            if n < 2:
                return cost[n]
            
            if n not in hashmap:
                hashmap[n] = cost[n] + min(dp(n-1),dp(n-2)) 

             

            return   hashmap[n] 

        return min(dp(n-1),dp(n-2))