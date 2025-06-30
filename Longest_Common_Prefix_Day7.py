#Brute Force Solution

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         prefix = ""
#         for i in range(len(strs[0])):  # Iterate over each character index of first string
#             char = strs[0][i]          # Pick the character at position i
#
#             for s in strs[1:]:         # Check this character against the same position in the rest of the strings
#                 if i == len(s) or s[i] != char:
#                     # If we reach the end of any string OR find a char mismatch
#                     return prefix      # Return prefix found so far
#
#             prefix += char             # If no mismatch, add the char to prefix
#
#         return prefix


# TC - O(S)
# SC - O(1)

#Better Solution

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#         return ""
#
#         prefix = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix

# TC - O(S)
# SC - O(1)

#Optimal Solution -> Divide And Conquer

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def common_prefix(str1, str2):
            min_len = min(len(str1), len(str2))
            for i in range(min_len):
                if str1[i] != str2[i]:
                    return str1[:i]
            return str1[:min_len]

        def lcp_rec(start, end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            left = lcp_rec(start, mid)
            right = lcp_rec(mid + 1, end)
            return common_prefix(left, right)

        return lcp_rec(0, len(strs) - 1)

# TC - O(s)
# SC - O(m log n)


