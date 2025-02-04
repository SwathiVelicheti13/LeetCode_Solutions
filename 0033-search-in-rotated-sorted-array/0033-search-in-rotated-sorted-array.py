class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low = 0
        high = length-1

        # iterate to find the mid

        while low<=high:
            mid = (low+high)//2

            # if nums[low] == nums[mid]== nums[high]:
            #     low = low+1
            #     high = high-1
            #     continue

            if nums[mid] == target:
                return mid

            if nums[low]<=nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
            


        