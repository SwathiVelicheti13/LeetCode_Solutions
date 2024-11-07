class Solution:
    def findMin(self, nums: List[int]) -> int:
        min1 = float("inf")
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                min1 = min(min1,nums[low])
                low = mid+1
            else:
                print(nums[mid])
                min1 = min(min1,nums[mid])
                high = mid -1
        return min1


        