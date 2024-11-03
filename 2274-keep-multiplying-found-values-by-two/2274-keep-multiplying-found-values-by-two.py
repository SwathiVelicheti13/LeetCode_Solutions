class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in nums:
            if original in nums:
                original = original*2
            else:
                return original

        return original

    

        