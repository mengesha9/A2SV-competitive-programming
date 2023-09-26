class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total = sum(stones)
        dp = {}
        
        def dfs(ind,currsum):
            if currsum >= ceil(total/2) or ind >= len(stones):
                return abs(currsum-(total-currsum))
           
            if (ind,currsum) not in dp:
                dp[(ind,currsum)] = min( dfs(ind+1,currsum) , dfs(ind+1,currsum+stones[ind]))
            
            return dp[(ind,currsum)]

          

        return dfs(0,0)