class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0 
        y = 0

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        d = 0

        for ins in instructions:
            if ins == 'G':
                x= x + directions[d][0]
                y= y + directions[d][1]
            elif ins == 'L':
                d = (d-1)%4
            elif ins == 'R':
                d = (d+1)%4
        
        return(x == 0 and y == 0) or d != 0


        
        