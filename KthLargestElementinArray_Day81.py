

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Build a min-heap of the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # O(k)

        # Step 2: Iterate through remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # If num is larger than smallest in heap
                heapq.heappop(min_heap)   # Remove smallest
                heapq.heappush(min_heap, num)  # Add current number

        # Step 3: The root of the heap is the Kth largest
        return min_heap[0]

