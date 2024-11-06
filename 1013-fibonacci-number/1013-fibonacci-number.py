class Solution:
    def fib(self, n: int) -> int:
        FibList = [0,1]

        for i in range(2,n+1):
            FibList.append(FibList[i-1]+FibList[i-2])
        
        return FibList[n]
        