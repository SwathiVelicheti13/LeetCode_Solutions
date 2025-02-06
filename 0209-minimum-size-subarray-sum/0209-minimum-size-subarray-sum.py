import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l =r= 0
        n = len(nums)
        currSum = 0
        minLength = float('inf')
        while r<n:
            while currSum<target and r<n:
                currSum+= nums[r]
                r+=1

            while currSum>=target and l<n:
                minLength = min(minLength ,(r-l))
    
                currSum = currSum - nums[l]
                l = l+1

        if minLength == float('inf'):
            return 0
        return minLength



        
        

        