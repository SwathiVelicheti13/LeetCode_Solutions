class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])

        end = points[0][1]
        arrows = 1
        for x in range(1,len(points)):
            if end < points[x][0]:
                arrows+=1
                end= points[x][1]
            else:
                end = min(end, points[x][1])
        return arrows

        