from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task
        freq = Counter(tasks)

        # Step 2: Build a max heap (negative counts for max behavior)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            cycle = n + 1  # One cycle of cooldown

            while cycle > 0 and max_heap:
                count = heapq.heappop(max_heap)
                if count + 1 < 0:  # still tasks remaining
                    temp.append(count + 1)
                time += 1
                cycle -= 1

            # Push remaining tasks back into heap
            for item in temp:
                heapq.heappush(max_heap, item)

            # If heap still has tasks, we must account for idle time
            if max_heap:
                time += cycle

        return time
