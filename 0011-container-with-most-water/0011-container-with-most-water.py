class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxWater = 0
        while l<r:
            currWater = (r-l) * min(height[l],height[r])
            maxWater = max(maxWater,currWater)

            if height[l]<=height[r]:
                l+=1
            else:
                r = r-1
        return maxWater


        