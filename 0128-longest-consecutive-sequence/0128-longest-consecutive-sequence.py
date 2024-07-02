class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_count = 1
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                x = num
                count=1
                while x+1 in nums:
                    count+=1
                    x+=1
                max_count = max(count,max_count)
        return max_count
