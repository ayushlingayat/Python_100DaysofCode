#Brute Force Approach

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        # Sort based on frequency in descending order
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result

#Better Approach

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        # Use heapq.nlargest to get k elements with highest frequency
        return [item for item, freq in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]


#Optimal Approach

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        # Create buckets: index = frequency
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        res = []
        # Traverse bucket in reverse (high freq first)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Time Complexity:
# Counting: O(n)
# Bucket fill: O(n)
# Result collection: O(n)
# Total: O(n)
#
# Space Complexity:
# O(n) for map + bucket