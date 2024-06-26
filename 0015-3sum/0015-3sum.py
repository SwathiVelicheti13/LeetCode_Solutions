class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1
            while j<k:
                sum1 = nums[i]+nums[j]+nums[k]
                if sum1<0:
                    j+=1
                elif sum1>0:
                    k= k-1
                else:
                    temp = [nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j = j+1
                    k = k-1
                    while j<k and nums[j] == nums[j-1]:
                        j = j+1
                    while j<k and nums[k] == nums[k+1]:
                        k = k-1
                
        return res