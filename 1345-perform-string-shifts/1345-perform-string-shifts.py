class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        direc = 0
        n = len(s)
        for face,num in shift:
            if face==0:
                direc+=num
            else:
                direc=direc -num

        start = direc%n

        return s[start:]+s[:start]
        