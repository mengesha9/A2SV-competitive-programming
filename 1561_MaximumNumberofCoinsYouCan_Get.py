class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=piles[len(piles)//3:len(piles)]
        sum=0
        if len(n)%2==0:
            for i in range(len(n)):
                if i%2==0:
                    sum+=n[i]
                else:
                    continue
        else:
            for i in range(len(n)):
                if i%2==0:
                    continue
                else:
                    sum+=n[i]
        return sum   
    
