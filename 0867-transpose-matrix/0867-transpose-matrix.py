class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        print(arr)
        for i in range(len(matrix[0])):
            newarr = []
            for j in range(len(matrix)):
                newarr.append(matrix[j][i])
            arr.append(newarr)
        return arr        


       