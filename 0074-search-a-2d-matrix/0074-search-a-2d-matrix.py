class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        inrow = -1

        for i in range(len(matrix)-1):
            if matrix[i][0] <= target < matrix[i+1][0]:
                inrow = i
                break
        if inrow  == -1:
            inrow = len(matrix)-1

        self.target = target    

        return self.binary(matrix, inrow)

    def binary(self,arr,row):

        i, j = 0, len(arr[row])-1

        while i <= j:
            mid = i + (j-i)//2
            if arr[row][mid] == self.target:
                return True
            elif arr[row][mid] > self.target:
                j = mid-1
            else:
                i = mid + 1

        return False                

        