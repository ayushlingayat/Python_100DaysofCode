#Brute Force Approach

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Complexity:
# Sorting takes O(n log n), where n = len(s) or len(t)
#
# Space Complexity:
# O(n) for storing sorted lists


# we can do like this also

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Better Approach

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t

# TC - O(n)
# SC - O(n)

#Optimal Approach

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)

        for char in t:
            if char not in count_s:
                return False
            count_s[char] -= 1
            if count_s[char] == 0:
                del count_s[char]

        return len(count_s) == 0

# TC - O(n)
# SC - O(1)