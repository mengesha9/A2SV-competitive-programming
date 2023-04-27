class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1]:
            return -1
        visited = set()

        q = deque([[1,0,0]])
        dis = float("inf")
        while q:
            depth,r,c = q.popleft() 
            
            if r == n-1 and c == n - 1:
                return depth 
            di =  [[0,-1],[-1,0],[1,0],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]    
            for sr,sc in di:
                row = sr+r
                col = sc+c
                if  min(row,col) >=  0 and max(row,col)< n and grid[row][col] == 0  and (row,col) not in visited:
                    visited.add((row,col))
                    q.append([depth+1,row,col])

        return -1