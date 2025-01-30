class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        kMoves = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        
        moves = k
        dp = [[[0 for _ in range(moves+1)]for _ in range(n)]for _ in range(n)]
        visited = [[[False for _ in range(moves+1)]for _ in range(n)]for _ in range(n)]

        def p(x,y,k):
            if k == 0:
                if x == row and y == column:
                    return 1.0
                else:
                    return 0.0
            
            if visited[x][y][k] == True:
                return dp[x][y][k]
            totalProb = 0.0

            for dx,dy in kMoves:
                nx = dx+x
                ny = dy+y

                if 0<=nx<n and 0<=ny<n:
                    totalProb+=p(nx,ny,k-1)
                
            visited[x][y][k] = True
            dp[x][y][k] = totalProb/8
            return dp[x][y][k]

        totalProb=0.0
        for x in range(n):
            for y in range(n):
                totalProb+=p(x,y,moves)
        return totalProb

        