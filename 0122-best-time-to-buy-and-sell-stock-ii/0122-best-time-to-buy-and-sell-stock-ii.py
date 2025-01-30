class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i]>minVal:
                cost = prices[i]-minVal
                maxProfit+=cost
                minVal = float('inf')
            minVal = min(minVal,prices[i])
        return maxProfit