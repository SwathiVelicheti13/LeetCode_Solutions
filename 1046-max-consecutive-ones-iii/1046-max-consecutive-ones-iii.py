class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l= r =0
        zeroes = 0
        maxlen = 0

        while r<len(nums):
            if nums[r] == 0:
                zeroes+=1
            while zeroes>k:
                if nums[l] == 0:
                    zeroes = zeroes-1
                l+=1
            if zeroes<=k:
                len1 = (r-l)+1
                maxlen = max(maxlen,len1)
            r+=1
        return maxlen
        