class Solution:
    def myPow(self, x: float, n: int) -> float:
        def find(k):
            if k == 0:
                return 1
            elif k % 2 == 0:
                half_pow = find(k//2)
                return half_pow *half_pow
            else:
                half_pow = find((k-1)//2) 
                return half_pow*half_pow* x
        if n == 0:
            return 1
        elif n > 0:
            return find(n)
        else:
            return 1/find(-n)               

        
