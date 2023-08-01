class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bought = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < bought:
                bought = prices[i]
            elif prices[i] > bought + fee:
                profit += prices[i] - bought - fee
                bought = prices[i] - fee
        
        return profit