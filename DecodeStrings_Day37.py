#Brute Force Approach
class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i):
            res = ""
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    decoded_str, i = decode(i + 1)
                    res += num * decoded_str
                    num = 0
                elif s[i] == ']':
                    return res, i
                else:
                    res += s[i]
                i += 1
            return res, i

        result, _ = decode(0)
        return result

# Time Complexity: O(k * n)
# Space Complexity: O(n)

#Better Approach
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                curr_str = last_str + num * curr_str
            else:
                curr_str += char

        return curr_str

# Time Complexity: O(n)
# Space Complexity: O(n)


#Optimal Approach
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = []
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((''.join(curr_str), curr_num))
                curr_str = []
                curr_num = 0
            elif char == ']':
                last_str, num = stack.pop()
                curr_str = list(last_str) + curr_str * num
            else:
                curr_str.append(char)

        return ''.join(curr_str)

# Time Complexity: O(n)
# Space Complexity: O(n)