class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        dic = defaultdict(int)
        for i in range(9):
            if i < 3:
                dic[i] = 0
            if 3<= i <6:
                dic[i] = 3
            if i>= 6:
                dic[i] = 6        

        def checkRow(num, r):
            count = 0
            for i in range(9):
                if board[r][i] == num:
                    count += 1

            if count >1:
                return False 

            return True     

        def checkCol(num, c):
            count = 0
            for i in range(9):
                if board[i][c] == num:
                    count += 1

            if count > 1:
                return False 

            return True  

        def checkCell( row, col, num):
            r = dic[row]
            c = dic[col]
            count = 0
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] == num:
                        count += 1

            if count > 1:
                return False

            return True


        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and  not (checkRow(board[i][j], i) and checkCol(board[i][j],j) and  checkCell(i,j, board[i][j])):

                    return False 

        return True             




                       





