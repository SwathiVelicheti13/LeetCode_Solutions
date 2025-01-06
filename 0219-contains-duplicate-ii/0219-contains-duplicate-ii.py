class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashDict = {}

        for i in range(len(nums)):
            if nums[i] in hashDict:
                if abs(i - hashDict[nums[i]]) <=k:
                    return True
            hashDict[nums[i]] = i
        return False
        