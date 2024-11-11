class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        uglyHeap = [1]
        heapq.heapify(uglyHeap)
        visited = set()
        visited.add(1)

        for _ in range(n):
            uglyNum = heapq.heappop(uglyHeap)
            for prime in primes:
                newUgly = uglyNum*prime
                if newUgly not in visited:
                    heapq.heappush(uglyHeap,newUgly)
                    visited.add(newUgly)
        return uglyNum
        