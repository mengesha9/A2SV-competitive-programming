class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        arr = []
        for i in range(1, n+1):
            arr.append(i)

        idx = k -1

        return self.rec(arr,idx,k)
    def rec (self, arr, ind, k):
        if len(arr) == 1:
            return arr[0]
        arr.pop(ind)
        ind = (ind + k -1)  % len(arr)   

        return self.rec(arr, ind, k)

        