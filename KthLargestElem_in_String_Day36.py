#Brute Approach

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse=True)
        return self.stream[self.k - 1]

# Time Complexity:
# add() → O(n log n) (due to sorting)

# Space Complexity:
# O(n) (storing all elements)



#Better Appraoch
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums, reverse=True)[self.k - 1]

# Time Complexity:
# add() → O(n log n) (due to sorting)

# Space Complexity:
# O(n) (storing all elements)

#Optimal Approach
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        # Reduce heap size to k if it's larger
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]

# Time Complexity:
# add() → O(log k)

# Space Complexity:
# O(k)

