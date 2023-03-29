class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        total = 0
        self.grid = grid
        for i in range(len(grid)-2):
            
            for j in range(len(grid[0])-2):
                temp = self.hourg(i,j)
                total  = max(total, temp)
        return total

    def hourg(self,r,c):
        total = 0
        for i in range(r,r+3):
            for j in range(c,c+3):
                if i == r+1:
                    total += self.grid[i][c+1]
                    break
                total += self.grid[i][j]  
        return total          

                




        