class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0

        for i in range(2,n+1):
            winner =(k+winner)%i
        return winner+1
       