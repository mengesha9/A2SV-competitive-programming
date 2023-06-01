class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        hashmap = defaultdict(int)
        n = len(triangle)

        def dp(r,c):
            if r == n-1:
                return triangle[r][c]

            if (r,c) not in hashmap:
                hashmap[(r,c)] = triangle[r][c] +  min(dp(r+1,c),dp(r+1,c+1))

            return hashmap[(r,c)]

        return dp(0,0)