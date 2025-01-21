class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()

        q = deque([])

        if grid[0][0]!=0 or grid[n-1][n-1] != 0:
            return -1
        q.append((0,0,1))

        visited.add((0,0))

        short_path = float('inf')

        direc = [(1,0),(-1,0),(0,-1),(0,1),(-1,1),(1,-1),(-1,-1),(1,1)]

        while q:
            r,c,steps = q.popleft()

            if r == n-1 and c == n-1:
                return steps
            for dr,dc in direc:
                nr = dr+r
                nc = dc+c

                if nr >=0 and nr<n and nc>=0 and nc<n and (nr,nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr,nc))
                    q.append((nr,nc,steps+1))
        return -1







        