import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        prev_freq, prev_char = 0, ''
        result = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            # If previous char still has count left, push it back
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            # Decrease frequency (since freq is negative)
            prev_freq, prev_char = freq + 1, char

        res = ''.join(result)
        return res if len(res) == len(s) else ""

