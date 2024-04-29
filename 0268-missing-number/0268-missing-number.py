class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max1 = max(nums)

        for i in range(max1+2):
            if i not in nums:
                return i
        