class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele =-1
        for i in range(len(nums)):
            if count == 0:
                ele = nums[i]
            
            if ele == nums[i]:
                count+=1
            else:
                count = count-1
        ct = 0
        for val in nums:
            if ele == val:
                ct+=1
            if ct >(len(nums)/2):
                return ele
        return -1




        