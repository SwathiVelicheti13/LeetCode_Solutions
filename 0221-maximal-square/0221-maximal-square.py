class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(cols)]for _ in range(rows)]
        maxside = 0

        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
            maxside = max(maxside,dp[i][0])

        for j in range(cols):
            dp[0][j] = int(matrix[0][j])
            maxside = max(maxside,dp[0][j])
        

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == '0':
                    dp[i][j]= 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxside = max(maxside,dp[i][j])
    
        return maxside*maxside



            
            
        
        