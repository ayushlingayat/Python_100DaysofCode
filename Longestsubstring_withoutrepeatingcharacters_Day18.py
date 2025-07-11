#Brute Force Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def all_unique(sub: str) -> bool:
            return len(set(sub)) == len(sub)

        max_len = 0
        n = len(s)

        for i in range(n):
            for j in range(i+1, n+1):
                if all_unique(s[i:j]):
                    max_len = max(max_len, j - i)
        return max_len


# TC - O(N³)
# SC - O(N)

#Better Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# TC - O(2N)
# SC - O(N)

#Optimal Approach

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len

# TC - O(N)
# SC - O(N)

