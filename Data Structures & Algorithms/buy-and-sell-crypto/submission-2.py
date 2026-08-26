class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)-1):
            if prices[i]<minPrice:
                minPrice = min(prices[i], minPrice)

            profit = prices[i]-minPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit