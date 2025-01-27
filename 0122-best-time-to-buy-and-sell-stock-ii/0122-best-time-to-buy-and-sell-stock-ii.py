class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        total = 0
        for i in range(len(prices)):
            if prices[i]>minVal:
                cost = prices[i] - minVal
                total+=cost
                minVal = float('inf')
            minVal = min(minVal,prices[i])
        return total