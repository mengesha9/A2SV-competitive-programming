class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        arr = []
        for i in range(len(scores)):
            arr.append([ages[i],scores[i]])
        arr.sort()
        dp = defaultdict(int)
        def dfs(ind):
            if ind >= len(scores):
                return 0
            if ind not in dp:
                count = arr[ind][1]
                for i in range(ind+1,len(scores)):
                    if arr[i][1] >= arr[ind][1]:
                        count = max(count,dfs(i) + arr[ind][1])

                dp[ind] = count        

            return dp[ind]


        res = 0
        for i in range(len(arr)):
            res = max(res,dfs(i))

        return  res