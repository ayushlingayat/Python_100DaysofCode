#Brute Approach

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            max_val = max(nums[i:i + k])
            result.append(max_val)
        return result

# Time Complexity:
# O(n * k)
# For each of the n - k + 1 windows, we do a k size scan.

# Space Complexity:
# O(n) for the output list (but O(1) extra space)

#Better Approach

import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_heap = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))  # push negated value for max heap

            # Remove elements outside the current window
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            if i >= k - 1:
                result.append(-max_heap[0][0])

        return result

# Time Complexity:
# O(n * log k)
# Inserting and popping from heap costs log k.

# Space Complexity:
# O(k) for the heap

#Optimal Approach

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        result = []

        for i in range(n):
            # Remove elements out of window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from rear
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Append max of window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

# Time Complexity:
# O(n)
# Each element is added and removed from the deque at most once.

# Space Complexity:
# O(k) for the deque