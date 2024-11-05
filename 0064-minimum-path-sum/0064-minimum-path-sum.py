class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        p = float("inf")
        DP = [[p for _ in range(len(grid[0])) ]for _ in range(len(grid))]
        if len(grid) == 1 and len(grid[0]) == 1:
            return grid[0][0]
        def pathSum(i,j,DP):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]

            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return float('inf')
            
            if DP[i][j]!=float('inf'):
                return DP[i][j]

            DP[i][j] = grid[i][j]+min(pathSum(i+1,j,DP),pathSum(i,j+1,DP))
            return DP[i][j]
            
        pathSum(0,0,DP)
        return DP[0][0]

        
        
