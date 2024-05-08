class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        mini = float('inf')

        for i in range(len(prices)):
            mini = min(mini,prices[i])
            cost = prices[i]-mini
            profit= max(profit,cost)   
        return profit


        