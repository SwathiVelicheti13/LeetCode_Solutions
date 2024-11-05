class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets =[]
        l = r = k = 0
        for l in range(len(nums)):
            if l!=0 and nums[l] == nums[l-1]:
                continue
            r = l+1
            k = len(nums)-1
            while r<k:
                tripSum = nums[l]+nums[r]+nums[k]
                if tripSum == 0:
                    triplets.append([nums[l],nums[r],nums[k]])
                    r+=1
                    k = k-1
                    while r<k and nums[r] == nums[r-1]:
                        r+=1
            
                    while k<len(nums)-1 and r<k and nums[k] == nums[k+1] :
                        k = k-1
                elif tripSum<0:
                    r+=1
                else:
                    k= k-1
                
        return triplets


                    

        