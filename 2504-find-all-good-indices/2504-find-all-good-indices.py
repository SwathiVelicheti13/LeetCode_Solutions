class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)

        result = []

        for i in range(1,len(left)):
            if nums[i]<=nums[i-1]:
                left[i]=left[i-1]+1
        
        for j in range(len(right)-2,-1,-1):
            if nums[j]<=nums[j+1]:
                right[j]=right[j+1]+1
        
        for x in range(k,len(nums)-k):
            if left[x-1] >=k and right[x+1]>=k:
                result.append(x)
        return result

        
        