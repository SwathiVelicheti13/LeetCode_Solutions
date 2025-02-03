class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x:x[1])
        
        arrows = 1
        end = points[0][1]
        for point in points:
            if end < point[0]:
                arrows+=1
                end = point[1]

        return arrows