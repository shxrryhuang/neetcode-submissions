class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = float("-inf")

        for i in range(1, len(prices)):
            if prices[i]<minPrice:
                minPrice = min(prices[i], minPrice)

            profit = prices[i]-minPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit