class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}

        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        
        for val in dict1.values():
            if val >1:
                return True
        return False

        