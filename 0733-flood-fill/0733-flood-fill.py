class Solution:
    def dfs(self,image,sr,sc,color,oldcolor):
        if image[sr][sc] == oldcolor:
            image[sr][sc] = color
        else:
            return
        print(image,sr,sc)
        directions=[(0,-1),(0,1),(1,0),(-1,0)]

        for dire in directions:
            nr = sr+dire[0]
            nc = sc+dire[1]
            
            if nr >= 0 and nc>=0 and nr<len(image) and nc<len(image[0]):
                self.dfs(image,nr,nc,color,oldcolor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        oldcolor = image[sr][sc]
        # image[sr][sc] = color

        self.dfs(image,sr,sc,color,oldcolor)

        return image

    
