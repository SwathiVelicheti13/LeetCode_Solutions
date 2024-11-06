class Solution:
    def climbStairs(self, n: int) -> int:
        cStairs = [0,1,2]

        for i in range(3,n+1):
            cStairs.append(cStairs[i-1]+cStairs[i-2])
        
        return cStairs[n]