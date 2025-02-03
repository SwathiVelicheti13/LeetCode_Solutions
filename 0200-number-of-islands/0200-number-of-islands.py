class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r,c,visited):

            direc = [(0,-1),(1,0),(-1,0),(0,1)]

            for dr,dc in direc:
                nr = r+dr
                nc = c+dc

                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr,nc,visited)

        visited = set()
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    visited.add((i,j))
                    count+=1
                    dfs(i,j,visited)
        
        return count
            
        