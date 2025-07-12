#Brute Force Approach
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        min_len = float('inf')
        res = ""

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                window = s[i:j]
                window_count = Counter(window)

                if all(window_count[char] >= t_count[char] for char in t_count):
                    if (j - i) < min_len:
                        min_len = j - i
                        res = window

        return res
# Time Complexity:O(n^3)
# (Because generating substrings is O(n^2) and checking counts is O(n))
#
# Space Complexity:O(n) (for storing counters)



#Optimal Approach
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window_count = {}

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Pop from left of window
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""

# Time Complexity: O(n) where n is the length of s (each character is visited at most twice)
# Space Complexity:O(m) where m is the number of unique characters in t

