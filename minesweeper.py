class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:


        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board 
        visited =set((click[0],click[1]))

        n,m = len(board), len(board[0])
        
        di = [[-1, 0],[1, 0],[0, 1],[0, -1],[-1,1],[1,-1],[-1,-1],[1,1]]
        

        def dfs(r,c):
            if board[r][c] != "E":
                return 

            count = 0
            for sr,sc in di:
                row = sr + r 
                col = sc + c
                if min(row,col) >= 0 and row < n and col < m and board[row][col] == "M":
                    count += 1
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = "B"
                for sr,sc in di:
                    row = sr + r 
                    col = sc + c
                    if min(row,col) >= 0 and row < n and col < m and (row,col) not in visited:
                        visited.add((row,col))
                        dfs(row,col)

        dfs(click[0],click[1])
        return board