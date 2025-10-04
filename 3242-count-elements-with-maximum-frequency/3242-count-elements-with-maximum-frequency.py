from collections import Counter 

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        print(c)

        c = list(c.values())
        print(c)

        max_number = max(c)
        result = 0

        for i in c:
            if i==max_number:
                result = i+result
        return result



        