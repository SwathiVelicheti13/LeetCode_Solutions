class Solution:


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        n = len(heights)
        m = len(heights[0])
        direc = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c,reachable):
            reachable.add((r,c))
        
            for dr,dc in direc:
                nr = r+dr
                nc = c+dc

                if nr>=0 and nr<n and nc>=0 and nc<m and (nr,nc) not in reachable and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,reachable)

        pacific_reachable = set()
        atlantic_reachable = set()

        for i in range(n):
            dfs(i,0,pacific_reachable)
            dfs(i,m-1,atlantic_reachable)   

        for j in range(m):
            dfs(0,j,pacific_reachable)
            dfs(n-1,j,atlantic_reachable)   

        result = list(pacific_reachable & atlantic_reachable)

        return result