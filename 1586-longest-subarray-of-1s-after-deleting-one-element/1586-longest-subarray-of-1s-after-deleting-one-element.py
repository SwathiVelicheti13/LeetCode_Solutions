class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        k = 1
        zeroes = 0
        maxlen = 0

        while r<len(nums):
            if nums[r]==0:
                zeroes+=1
            if zeroes>1:
                if nums[l]==0:
                    zeroes = zeroes-1
                l+=1
            if zeroes<=1:
                len1 = r-l
                maxlen = max(maxlen,len1)
            r+=1
        return maxlen

        