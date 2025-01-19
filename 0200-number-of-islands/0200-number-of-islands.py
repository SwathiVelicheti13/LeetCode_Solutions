class Solution:

    def dfs(self,grid,r,c,visited):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=='0':
            return 

        direc = [(0,1),(1,0),(0,-1),(-1,0)]

        for dr, dc in direc:
            nr = r+dr
            nc = c+dc

            if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and (nr,nc) not in visited and grid[nr][nc] == '1':
                visited.add((nr,nc))
                self.dfs(grid,nr,nc,visited)
    
                
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()

        cnt = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    cnt+=1
                    visited.add((i,j))
                    self.dfs(grid,i,j,visited)
        return cnt
       