import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-n for n in nums]
        heapq.heapify(nums)
        print(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -(nums[0])

        