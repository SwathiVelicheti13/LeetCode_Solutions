class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1,-1]
        first = -1
        last = -1

        l = 0
        h = len(nums)-1

        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                first = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        
        while l<=h:
            mid1 = (l+h)//2

            if nums[mid1] == target:
                last = mid1
                l=mid1+1
            elif nums[mid1] > target:
                h = mid1-1
            else:
                l = mid1+1
        
        if first!= float('inf') and last!=-1:
            return [first,last]
        return [-1,-1]

        