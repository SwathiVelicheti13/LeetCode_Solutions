class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxprofit = 0
        for price in prices:
            if mini < price:
                cost = price - mini
                maxprofit+=cost
                mini = float('inf')
            mini = min(mini, price)
        return maxprofit

        