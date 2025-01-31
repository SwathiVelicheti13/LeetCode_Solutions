class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 1
        r = len(nums)-2
        n = len(nums)
        if nums[0]>nums[1]:
            return 0

        if nums[n-1]>nums[n-2]:
            return n-1

        
        while l<=r:
            mid = (l+r)//2

            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid

            elif nums[mid] > nums[mid-1]:
                l = mid+1 
            elif nums[mid]>nums[mid+1]:
                h = mid-1
            else:
                l = mid-1
        
        return -1


       
      