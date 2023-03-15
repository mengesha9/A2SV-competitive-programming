class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        return self.rec(n, k)

    def rec(self, n, k):

            if n == 1:
                return '0'
            length = 2**n
            if k == (length)//2:
                return "1"
            elif k < (length)//2:
                return self.rec(n-1, k) 
            else:
                return str(1-int(self.rec(n-1, length-k)) ) 




       
