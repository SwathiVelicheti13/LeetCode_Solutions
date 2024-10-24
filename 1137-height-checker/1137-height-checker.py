class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for hi, hj in zip(heights,expected):
            if hi!=hj:
                count+=1
        return count

        