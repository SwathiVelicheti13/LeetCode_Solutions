class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pfSum = 0
        minSum = float('inf')

        for x in nums:
            pfSum+=x
            minSum = min(minSum,pfSum)

        if minSum<0:
            return -(minSum)+1
        return 1
        
       