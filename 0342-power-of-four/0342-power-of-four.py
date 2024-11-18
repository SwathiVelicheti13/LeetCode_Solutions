class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n):
            if pow(4,i) == n:
                return  True
            elif pow(4,i) > n:
                return False
        return False
        