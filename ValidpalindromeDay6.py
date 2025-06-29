#Brute Force Approach

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ''
#         for char in s:
#             if char.isalnum():
#                 cleaned += char.lower()
#         return cleaned == cleaned[::-1]


# Time Complexity: O(n)
# Space Complexity: O(n) (due to cleaned string and reverse)

#Brute Approach

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         chars = [char.lower() for char in s if char.isalnum()]
#         return chars == chars[::-1]


# Time Complexity: O(n)
# Space Complexity: O(n) (still creating a list)

#Optimal Approach

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# Time Complexity: O(n)
# Space Complexity: O(1) (in-place comparison, no extra space)

