class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh_oranges = 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges+=1
                elif grid[i][j] == 2 and visited[i][j]!=1:
                    q.append([i,j])
                    visited[i][j] = 1
        
        if fresh_oranges==0:
            return 0
        timewait = 0

        while q:
            timewait+=1

            for _ in range(len(q)):
                r,c = q.popleft()

                for dire in direc:
                    nr = r+dire[0]
                    nc = c+dire[1]

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and visited[nr][nc]!=1:
                        grid[nr][nc] = 2
                        visited[nr][nc] = 1
                        q.append([nr,nc])
                        fresh_oranges = fresh_oranges-1
        

        if fresh_oranges >= 1:
            return -1
        return timewait-1



        
        