class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0

        for val in nums:
            if val > currSum+val or currSum == 0:
                currSum = val
            else:
                currSum+=val
            maxSum = max(currSum,maxSum)
        return maxSum
        