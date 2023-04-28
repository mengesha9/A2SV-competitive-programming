class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        
        
        q = deque()
        
        visited = set()
        for i in range(n):
            
            for j in range(m):
                if mat[i][j] == 0:
                    
                    q.append([0,i,j])
                    visited.add((i,j))
                    
                

        
        while q:
            dis,r,c= q.popleft()
            mat[r][c] =dis
          
            di = [[-1,0],[1,0],[0,1],[0,-1]]

            for sr,sc in di:
                row = r+sr
                col = c+sc
                if min(row,col)>=0 and row<n and  col<m  and mat[row][col] != 0  and (row,col) not in visited:
                    visited.add((row,col))
                    q.append([dis+1,row,col])


        return mat