class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hash_di = defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in hash_di and hash_di[i-j] != matrix[i][j]:
                    return False
                hash_di[i-j] = matrix[i][j]    
        return True            

        