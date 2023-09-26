class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        visited = set()
        def dfs(ind,sum):
            if ind >= len(stones):
                return 0
            take = stones[ind] + sum
            nottake = sum

            visited.add(take)    
            visited.add(nottake)

            dfs(ind+1,take)
            dfs(ind+1,nottake)
            
            return 

        for k in visited:
            print(k,end="")   

        dfs(0,0)
        total = sum(stones)
        num = (total//2)+1
        ans = float("Inf")
        while num >=0 :
            if total - num in visited:
                ans = min(ans,abs(total-2*num))

            num-=1

        return ans