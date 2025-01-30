class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0 
        y = 0
        dir_ind = 0

        direc = [(0,1),(1,0),(0,-1),(-1,0)]


        for ins in instructions:
            if ins == 'G':
                x+=direc[dir_ind][0]
                y+=direc[dir_ind][1]
            elif ins == 'L':
                dir_ind = (dir_ind-1)%4
            elif ins == 'R':
                dir_ind = (dir_ind+1)%4

        return (x==0 and y==0) or (dir_ind!=0)