class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pfSum = 0
        minSum = 0

        for x in nums:
            pfSum+=x
            minSum = min(minSum,pfSum)

        startValue =  1-minSum

        return startValue
        
       