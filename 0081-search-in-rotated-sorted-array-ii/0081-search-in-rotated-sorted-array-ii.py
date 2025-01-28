class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        h = len(nums)-1

        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] == nums[h]:
                l = l+1
                h = h-1
                continue
            elif nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<=target<=nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        return False
        