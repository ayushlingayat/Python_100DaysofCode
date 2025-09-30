import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        seen = {1}
        heap = [1]

        for _ in range(n):
            curr = heapq.heappop(heap)
            for p in primes:
                nxt = curr * p
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return curr


