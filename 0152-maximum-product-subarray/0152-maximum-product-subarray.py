class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0
        currMax = currMin = maxProd = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]

            if num < 0:
                currMax, currMin = currMin, currMax

            currMax = max(num,currMax * num)
            currMin = min(num,currMin * num)

            maxProd = max(maxProd,currMax)
        return maxProd





       