class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the numbers to work with the smallest ones first
        l = 0
        r = 0
        sum1 = 0
        ans = 0
        
        while r<len(nums):
            sum1 += nums[r]
            
            # Check if we can make all elements between nums[l] and nums[r] the same with k operations
            while (r - l + 1) * nums[r] > sum1+k:
                sum1 -= nums[l]
                l += 1
            
            # Update the result with the largest window size
            ans = max(ans, r - l + 1)
            r+=1
        
        return ans

        