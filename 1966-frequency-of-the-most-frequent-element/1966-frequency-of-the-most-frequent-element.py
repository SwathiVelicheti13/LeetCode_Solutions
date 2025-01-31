class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 0
        ans = 0
        sum1 = 0
        while r<len(nums):
            sum1+=nums[r]
            while (r - l + 1) * nums[r] > sum1+k:
                sum1 -= nums[l]
                l += 1
              
            ans = max(ans, r - l + 1)
            r+=1        
        return ans