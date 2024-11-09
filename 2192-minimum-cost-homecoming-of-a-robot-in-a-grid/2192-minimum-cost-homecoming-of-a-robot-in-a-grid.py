class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        total = 0

        if startPos[0]!=homePos[0]:
            if startPos[0]<homePos[0]:
                for i in range(startPos[0]+1,homePos[0]+1):
                    total+=rowCosts[i]
            else:
                for i in range(startPos[0]-1,homePos[0]-1,-1):
                    total+=rowCosts[i]
        else:
            pass
        if startPos[1]!=homePos[1]:
            if startPos[1]<homePos[1]:
                for j in range(startPos[1]+1,homePos[1]+1):
                    print(j)
                    total+=colCosts[j]
            else:
                for j in range(startPos[1]-1,homePos[1]-1,-1):
                    total+=colCosts[j]
        else:
            pass
        return total
            

        