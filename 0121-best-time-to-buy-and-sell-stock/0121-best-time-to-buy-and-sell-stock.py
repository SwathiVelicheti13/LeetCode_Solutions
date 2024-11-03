class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = float('-inf')
        for price in prices:
            cost = price - minPrice
            maxProfit = max(maxProfit,cost)
            minPrice = min(price,minPrice)
        return maxProfit




        