class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):

            arr.append(i)
        print(arr) 
        temp=k-1
        return self.helper(arr,k,temp) 
    def helper(self,arr,k,s) :
        if len(arr)==1:
            return arr[0]
        arr.pop(s) 
        s=(s+k-1)%len(arr)   
        return self.helper(arr,k,s) 
