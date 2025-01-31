class Solution:
    def nthUglyNumber(self, n: int) -> int:

        primes = [2,3,5]
        uglyHeap = [1]
        heapq.heapify(uglyHeap)
        visited = set()
        visited.add(1)

        for _ in range(n):
            uglyNum = heapq.heappop(uglyHeap)
            for x in primes:
                new_ugly = uglyNum*x
                if new_ugly not in visited:
                    heapq.heappush(uglyHeap,new_ugly)
                    visited.add(new_ugly)
        return uglyNum

        # O(N) approach

        # ugly = [1] * n
        # p2 = p3 = p5 = 0

        # for i in range(1,n):
        #     next_ugly = min(ugly[p2] * 2,ugly[p3] * 3,ugly[p5] * 5)
        #     ugly[i] = next_ugly

        #     if next_ugly == ugly[p2] * 2:
        #         p2+=1
        #     if next_ugly == ugly[p3] * 3:
        #         p3+=1
        #     if next_ugly == ugly[p5] * 5:
        #         p5+=1
            
        # return ugly[-1]

        # primes = [2,3,5]
        # uglyHeap = [1]
        # heapq.heapify(uglyHeap)
        # visited = set()
        # visited.add(1)

        # for _ in range(n):
        #     uglyNum = heapq.heappop(uglyHeap)
        #     for prime in primes:
        #         newUgly = uglyNum*prime
        #         if newUgly not in visited:
        #             heapq.heappush(uglyHeap,newUgly)
        #             visited.add(newUgly)
        # return uglyNum
        