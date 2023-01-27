class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        n=len(matrix)
        m=len(matrix[0])

        arr=[]
        for i in range(n):
            right=i
            if len(arr)==n*m:return arr
            while right<m-i-1:
                arr.append(matrix[i][right])
                right+=1
            down=i
            if len(arr)==n*m:return arr
            while down<n-i:
                arr.append(matrix[down][right]) 
                down+=1
            left=m-i-2
            if len(arr)==n*m:return arr
            while  left>i:
                arr.append(matrix[down-1][left])
                left-=1
            up=n-i-1 
            if len(arr)==n*m:return arr   
            while up>i:
                arr.append(matrix[up][left])
                up-=1
            if len(arr)==n*m:return arr    
        return arr        






