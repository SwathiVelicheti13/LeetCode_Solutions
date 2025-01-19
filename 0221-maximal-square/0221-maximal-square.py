class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        maxarea = 0
        for i in range(m):
            dp[0][i]= int(matrix[0][i])
        
        for j in range(n):
            dp[j][0] = int(matrix[j][0])

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == "0":
                    print(matrix[i][j],i,j)
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j-1],min(dp[i][j-1],dp[i-1][j]))+1

        maxarea = 0

        for i in range(n):
            for j in range(m):
                maxarea = max(maxarea,dp[i][j])
        maxarea = int(math.pow(maxarea,2))
        return maxarea

        