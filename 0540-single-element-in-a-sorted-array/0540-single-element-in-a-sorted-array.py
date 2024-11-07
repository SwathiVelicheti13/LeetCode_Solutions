class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low = 1
        high = len(nums)-2 

        while low<=high:
            mid = (low+high)//2
            if nums[mid-1]!=nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif mid%2 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid+1
                elif nums[mid] == nums[mid-1]:
                    high = mid-1
            elif mid%2 == 1:
                if nums[mid] == nums[mid-1]:
                    low = mid+1
                elif nums[mid] == nums[mid+1]:
                    high = mid-1
        return -1

        