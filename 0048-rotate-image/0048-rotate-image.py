class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
     
        r=len(matrix)
        for i in range(r):
            right=i
            d=r-i-1
            left=r-i-1
            up=i
            while right<r-i-1:
                temp1=matrix[i][right]
                matrix[i][right]=matrix[r-right-1][up]
                matrix[r-right-1][up]=matrix[left][r-right-1]
                matrix[left][r-right-1]=matrix[right][d]
                matrix[right][d]=temp1
                right+=1



                
                




 