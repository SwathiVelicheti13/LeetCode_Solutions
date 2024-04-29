import sys
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        max1 =0
        for val in nums:
            if val == 1:
                ct+=1
                max1 = max(max1,ct)
                
            else:
                ct = 0
        return max1
        