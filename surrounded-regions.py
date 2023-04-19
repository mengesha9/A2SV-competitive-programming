class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        def dfs(r,c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "0":
                return False
            if board[r][c] == "X":
                return True

            board[r][c] = "0"
            di = [[-1,0],[1,0],[0,-1],[0,1]] 
            for sr,sc in di:
                dfs(r+sr, c+sc)
            return True 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                        dfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "0":
                    board[i][j] = "O"