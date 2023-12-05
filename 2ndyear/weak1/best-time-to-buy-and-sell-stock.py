class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        bought = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            bought = min(bought , prices[i])
            profit = max(profit,prices[i]-bought)

        return profit    

        