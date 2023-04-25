class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
     
        visited = set()
        def dfs(r,c):
            if min(r,c) < 0 or r >= len(grid2)  or c >= len(grid2[0]) or grid2[r][c]==0 or (r,c) in visited:
                return True   
            if grid1[r][c]==0 and grid2[r][c]==1:
                return False

            visited.add((r,c))
            di = [[-1,0],[1,0],[0,1],[0,-1]]
            subisland = True
            for sr,sc in di:
                row= r + sr 
                col = c + sc
                if dfs(row, col) == False:
                    subisland = False

            return subisland

        count = 0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and grid1[i][j] == 1 and (i,j) not in visited:
                    if dfs(i,j):
                        count += 1

        return count