class Solution:
    def bfs(self,i,j,grid,n,m,visited):
        visited[i][j] = 1
        q = [[i,j]]
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r, c = q.pop(0)
            for dire in direction:
                nr = r+dire[0]
                nc = c+dire[1]

                if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]=='1' and visited[nr][nc]!=1:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
            
                
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        visited = [[0 for _ in range(m)]for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j]!=1:
                    cnt+=1
                    self.bfs(i,j,grid,n,m,visited)
        return cnt


      