class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            if pow(2,i) == n:
                return  True
            elif pow(2,i) > n:
                return False
        return False

        