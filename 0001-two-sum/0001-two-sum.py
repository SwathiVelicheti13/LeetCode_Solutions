class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pfSum = {}

        for val in range(len(nums)):
            Needed = target-nums[val]

            if Needed in pfSum:
                return [pfSum[Needed],val]

            pfSum[nums[val]] = val

        return [0,0]