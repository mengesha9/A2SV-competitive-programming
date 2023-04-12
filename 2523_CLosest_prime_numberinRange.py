class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right <= 2:
            return [-1, -1]
        
        # Generate a list of prime numbers using Sieve of Eratosthenes
        is_prime = [True] * (right+1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(right**0.5)+1):
            if is_prime[i]:
                for j in range(i**2, right+1, i):
                    is_prime[j] = False
        
        # Find the closest pair of prime numbers
        arr = []
        for i in range(left,right+1):
            if is_prime[i]:
                arr.append(i)

        
        print(arr)
        if len(arr)<2:
            return [-1,-1]
        ans = [-1, -1]
        min_gap = float('inf')
        for i in range(1, len(arr)):
                gap = arr[i]-arr[i-1]
                if gap < min_gap:
                    min_gap = gap
                    ans[0]= arr[i-1]
                    ans[1]= arr[i]
        
        return ans
