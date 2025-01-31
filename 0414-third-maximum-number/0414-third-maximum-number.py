class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1 = set(nums)
        nums = [-x for x in nums1]
        if len(nums) == 1:
            return -nums[0]
        if len(nums)==2:
            return max(-nums[0],-nums[1])
        heapq.heapify(nums)

        for i in range(3):
            val = heapq.heappop(nums)

        return -(val)
        



        
        