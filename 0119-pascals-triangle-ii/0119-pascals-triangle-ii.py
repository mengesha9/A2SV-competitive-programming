class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        return  self.pascal(rowIndex)

    def pascal(self, n):
        if n == 0:
            return [1] 
        elif n == 1:
            return [1,1]

        pas = self.pascal(n-1)

        newarr = []  

        for i in range(1,len(pas)):
            newarr.append(pas[i]+pas[i-1]) 
        
        return [1] + newarr + [1]

