#Better Approach

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        s = s.replace(' ', '')

        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # truncate toward 0
                sign = ch
                num = 0
        return sum(stack)


#TC - O(n)
#SC - O(n)

#Optimal Approach

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        res = 0
        curr = 0
        last = 0
        sign = '+'

        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            if not ch.isdigit() or i == len(s) - 1:
                if sign == '+':
                    res += last
                    last = curr
                elif sign == '-':
                    res += last
                    last = -curr
                elif sign == '*':
                    last = last * curr
                elif sign == '/':
                    last = int(last / curr)
                sign = ch
                curr = 0
        res += last
        return res

#TC - O(n)
#SC - O(1)