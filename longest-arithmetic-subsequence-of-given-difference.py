class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = defaultdict(int)

        for i in arr:
            if i -difference in dp:
                dp[i] = 1 + dp[i-difference]
            else:
                dp[i] = 1
        count = 1

        for k,v in dp.items():
            count = max(v,count )

        return count