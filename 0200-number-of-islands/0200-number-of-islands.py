class Solution:

    def dfs(self,row, col, visited, grid):
        visited[row][col] = 1
        n = len(grid)
        m = len(grid[0])

        directions = [(0,-1),(0,1),(1,0),(-1,0)]

        for dire in directions:
            nrow,ncol = row+dire[0],col+dire[1]
        # for i in range(-1,2):
        #     for j in range(-1,2):
        #         if i == 0 and j == 0:
        #         nrow = row+i
        #         ncol = col+j
            if 0 <= nrow < n and 0 <= ncol < m and visited[nrow][ncol] == 0 and grid[nrow][ncol] == "1":
                self.dfs(nrow,ncol,visited, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        visited = [[0 for _ in range(m)]for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if visited[row][col]!=1 and grid[row][col]=="1":
                    cnt+=1
                    self.dfs(row,col,visited, grid)
        return cnt