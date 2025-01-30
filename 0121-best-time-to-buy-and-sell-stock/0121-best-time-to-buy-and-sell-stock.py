class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            cost = prices[i] - minVal

            maxProfit = max(maxProfit,cost)

            minVal = min(minVal,prices[i])
        return maxProfit