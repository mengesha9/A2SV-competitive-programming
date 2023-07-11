class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        hashmap = defaultdict(int)

        def dp(r,c):

            if min(r,c) < 0 or max(r,c) >= n:
                return float('inf')
            if r == n-1:
                return matrix[r][c]     


            if (r,c) not in hashmap:
                hashmap[(r,c)] =  matrix[r][c] + min(dp(r+1,c),dp(r+1,c+1),dp(r+1,c-1))

            return hashmap[(r,c)]

        ans = float('inf')

        for i in range(len(matrix)):
            ans = min(ans,dp(0,i))

        return ans