class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pfSum = 0
        dict1 = {0:1}
        count = 0
        for i in range(len(nums)):
            pfSum+=nums[i]
            rem = pfSum-k
            if rem in dict1:
                count+=dict1[rem]
            if pfSum not in dict1:
                dict1[pfSum] = 1
            else:
                dict1[pfSum]+=1
        return count

    