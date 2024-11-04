class Solution:
    def minimumChairs(self, s: str) -> int:
        achairs = 0
        max1 = 0
        for eve in s:
            if eve == 'E':
                achairs= achairs+1    
            else:
                 achairs=achairs-1
            max1 = max(max1,achairs)
        return max1





        