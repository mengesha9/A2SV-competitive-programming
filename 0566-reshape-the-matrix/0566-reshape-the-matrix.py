class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        if r*c != len(mat)*len(mat[0]):
            return mat


        arr = [] 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr.append(mat[i][j])

        answer = []
        k = 0

        for i in range(r):
            newarr = []
            for j in range(c):
                newarr.append( arr[k])
                k += 1
            answer.append(newarr)

        return answer        




        