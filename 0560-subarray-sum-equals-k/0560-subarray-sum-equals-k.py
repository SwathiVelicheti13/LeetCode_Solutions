class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pfDict = {0:1}
        totalSubArrays = 0
        pfSum = 0

        for i in range(len(nums)):
            pfSum+=nums[i]
            Needed = pfSum-k

            if Needed in pfDict:
                totalSubArrays+=pfDict[Needed]
            
            if pfSum not in pfDict:
                pfDict[pfSum] = 1
            else:
                 pfDict[pfSum]+= 1
        return totalSubArrays
