class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = []
        if right <= 2:
            return [-1,-1] 
            
        for i in range(max(2,left),right+1):
            if self.isprime(i):
                arr.append(i)
        anser = []
        l = 0
        r = 1
        while r < len(arr): 
            if len(anser) == 0:
                anser.append(arr[l])
                anser.append(arr[r])
            elif anser and arr[r]-arr[l] < anser[1] - anser[0]:
                anser[0] = arr[l]
                anser[1] = arr[r]
            r += 1
            l += 1

        return anser if len(anser) == 2 else [-1,-1]

    def isprime(self, n):
        d = 2
        while d*d <= n:
            if n % d == 0:
                return False
            d += 1    
        return True