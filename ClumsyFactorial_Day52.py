#Brute Approach

class Solution:
    def clumsy(self, n: int) -> int:
        ops = ['*', '/', '+', '-']
        res = str(n)
        idx = 0
        for i in range(n - 1, 0, -1):
            res += ops[idx] + str(i)
            idx = (idx + 1) % 4
        return eval(res)   # brute-force evaluation

# TC - O(n)
# SC - O(n)


#Better Approach
class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        n -= 1
        idx = 0  # operation index

        while n > 0:
            if idx % 4 == 0:        # multiplication
                stack[-1] *= n
            elif idx % 4 == 1:      # division
                stack[-1] = int(stack[-1] / n)  # truncate toward zero
            elif idx % 4 == 2:      # addition
                stack.append(n)
            else:                   # subtraction
                stack.append(-n)
            idx += 1
            n -= 1

        return sum(stack)

# TC - O(n)
# SC - O(n)


#Optimal Approach
class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 6
        if n == 4: return 7

        if n % 4 == 0: return n + 1
        if n % 4 == 1: return n + 2
        if n % 4 == 2: return n + 2
        return n - 1

# TC - O(1)
# SC - O(1)
