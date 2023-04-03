class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0 :
           return True
        
        self.tmp = math.sqrt(c)

        for i in range(math.ceil(self.tmp)):
            num = math.sqrt(c - (i*i))

            if self.search(num):
                return True
        return False 

    def search(self,n):

        left = 0
        right = self.tmp

        while left <= right:
            mid = left + (right - left)//2

            if mid > n:
                right = mid - 1
            elif mid < n:
                left = mid + 1
            else:
                return True

        return False             








