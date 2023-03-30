class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_col = set()
        zero_row = set()
        for i in range(len(matrix)):
           for j in range(len(matrix[0])):
               if matrix[i][j] == 0:
                   
                   zero_row.add(i)
                   zero_col.add(j)

        

        
        
        for k in zero_row:
            matrix[k] = [0]*len(matrix[0])
            
    
        for k in zero_col:
            for i in range(len(matrix)):
                matrix[i][k] = 0


            






                        


        
   