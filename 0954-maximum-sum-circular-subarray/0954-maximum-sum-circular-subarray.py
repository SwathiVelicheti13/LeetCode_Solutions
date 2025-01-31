class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMaxsum = nums[0]
        currMinsum = nums[0]

        maxSum = nums[0]
        minSum = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            if currMaxsum+nums[i]<nums[i]:
                currMaxsum = nums[i]
            else:
                currMaxsum+=nums[i]
            maxSum = max(maxSum,currMaxsum)

            if currMinsum+nums[i]>nums[i]:
                currMinsum = nums[i]
            else:
                currMinsum+=nums[i]
            
            minSum = min(minSum,currMinsum)
            total+=nums[i]
        if minSum == total:
            return maxSum
        return max(maxSum, total-minSum)
