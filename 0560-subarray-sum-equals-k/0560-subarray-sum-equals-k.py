class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preDict={0:1}
        n = len(nums)
        count = 0
        pfSum = 0
        for val in nums:
            pfSum+=val
            if pfSum-k in preDict:
                count+=preDict[pfSum-k]

            if pfSum not in preDict:
                preDict[pfSum] = 1
            else:
                preDict[pfSum] =  preDict[pfSum]+1
        return count
        