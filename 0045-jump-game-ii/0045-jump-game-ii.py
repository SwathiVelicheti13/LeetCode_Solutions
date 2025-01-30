class Solution:
    def jump(self, nums: List[int]) -> int:

        currentEnd = 0
        maxReach = 0
        jumps = 0
        for i in range(len(nums)-1):
            maxReach = max(maxReach,i+nums[i])

            if i == currentEnd:
                jumps+=1
                currentEnd = maxReach

            if currentEnd>=len(nums)-1:
                return jumps
        return jumps
            
        