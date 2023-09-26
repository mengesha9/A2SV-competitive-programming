class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        dp = {}
        def dfs(ind,prev):
            if ind >= len(satisfaction):
                return 0
            if (ind,prev) not in dp:
                cook = satisfaction[ind]*prev + dfs(ind + 1, prev + 1)
                notcook = dfs(ind + 1, prev)

                dp[(ind,prev)] = max(cook,notcook)

            return dp[(ind,prev)]

        return dfs(0,1)