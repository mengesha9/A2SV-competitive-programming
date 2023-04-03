class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        total = 0
        j = len(piles)-2
        k = len(piles)//3
        while k > 0 and j>0:
            total += piles[j]
            j -= 2
            k -= 1


        print(piles)
        return total