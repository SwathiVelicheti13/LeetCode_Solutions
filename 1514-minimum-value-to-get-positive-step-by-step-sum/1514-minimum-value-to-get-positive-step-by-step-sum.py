class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0  # Track the minimum cumulative sum
        curr_sum = 0  # Initialize current cumulative sum

        # Calculate cumulative sum and track minimum
        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)

        # Calculate the required start value to ensure min_sum >= 1
        startValue = 1 - min_sum

        return startValue