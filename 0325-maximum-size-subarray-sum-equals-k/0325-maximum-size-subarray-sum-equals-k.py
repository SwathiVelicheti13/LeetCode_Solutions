class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pfSum = 0
        pfDict = {0:-1}
        # if k == 0 and len(nums) == 1:
        #     return 0
        maxLength = float('-inf')
        for x in range(len(nums)):
            pfSum+=nums[x]
            Needed = pfSum-k
            if Needed in pfDict:
                length = (x-pfDict[Needed])
                maxLength = max(length,maxLength)
            if pfSum not in pfDict:
                pfDict[pfSum] = x
        if maxLength == float('-inf'):
            return 0
        return maxLength


        