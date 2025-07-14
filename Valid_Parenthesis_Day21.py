#Brute Force code
from socketserver import TCPServer


class Solution:
    def isValid(self, s: str) -> bool:
        prev_length = -1
        while prev_length != len(s):
            prev_length = len(s)
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""

# TC - O(n²)
# SC - O(1)


#Better Approach
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (ch == ')' and top != '(') or \
                   (ch == '}' and top != '{') or \
                   (ch == ']' and top != '['):
                    return False
        return not stack

# TC - O(n)
# SC - O(n)


#Optimal Approach
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# TC - O(n)
# SC - O(n)
