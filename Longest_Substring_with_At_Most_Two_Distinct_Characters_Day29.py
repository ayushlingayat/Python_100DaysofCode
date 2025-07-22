#Brute Force Approach
class Solution:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        max_len = 0
        n = len(s)

        for i in range(n):
            unique_chars = set()
            for j in range(i, n):
                unique_chars.add(s[j])
                if len(unique_chars) > 2:
                    break
                max_len = max(max_len, j - i + 1)

        return max_len

# TC - O(N^2)
# SC - O(1)

#Optimal Approach
from collections import defaultdict

class Solution:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:
        left = 0
        max_len = 0
        char_freq = defaultdict(int)

        for right in range(len(s)):
            char_freq[s[right]] += 1

            # Shrink window until we have at most 2 distinct chars
            while len(char_freq) > 2:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

# TC - O(N)
# SC - O(1)