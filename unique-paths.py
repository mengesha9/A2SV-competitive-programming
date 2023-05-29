class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        hashmap = defaultdict(int)
        def back(r,c):
            if min(r,c) < 0 or r>= m or c >= n:
                return 0
            if r == m-1 and c == n-1:
                return 1

            if (r,c) not in hashmap:
                hashmap[(r,c)]  = back(r+1,c) + back(r,c+1)

            return hashmap[(r,c)]

        return back(0,0)