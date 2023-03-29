class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        self.grid = grid
        arr = []
        for i in range(len(grid)-2):
            newarr = []
            for j in range(len(grid)-2):
                newarr.append(self.find(i,j))
            arr.append(newarr)    

        return arr        
    def find(self, r, c):
        total = 0
        for i in range(r,r+3):
            for j in range(c , c+3):
                total = max(total, self.grid[i][j])
        return total        





