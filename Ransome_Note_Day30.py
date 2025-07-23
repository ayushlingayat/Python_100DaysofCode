#Brute Approach
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for ch in ransomNote:
            if ch in magazine:
                magazine.remove(ch)
            else:
                return False
        return True

# TC - O(n* m)
# SC - O(m)

#Better Approach
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for ch in ransom_count:
            if ransom_count[ch] > magazine_count.get(ch, 0):
                return False
        return True


# TC - O(n + m)
# SC - O(1)

#Optimal Approach
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for ch in ransomNote:
            if count[ch] == 0:
                return False
            count[ch] -= 1
        return True


# TC - O(m+n)
# SC - O(1)