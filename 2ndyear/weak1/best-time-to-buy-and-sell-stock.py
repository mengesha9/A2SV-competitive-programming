class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        intialprofit = float("-inf")
        intialbuy = float("inf")

        for i in range(len(prices)):
            intialprofit = max(intialprofit, prices[i]-intialbuy)
            intialbuy = min(intialbuy , prices[i])

        return intialprofit if intialprofit > 0 else 0 


        