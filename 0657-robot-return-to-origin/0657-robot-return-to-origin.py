class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coord = [0,0]

        for i in range(len(moves)):
            if moves[i] == 'U':
                coord[1] = coord[1]+1
            elif moves[i] == 'D':
                coord[1] = coord[1]-1
            elif moves[i] == 'L':
                coord[0] = coord[0]+1
            elif moves[i] == 'R':
                coord[0] = coord[0]-1
        return coord == [0,0]
        