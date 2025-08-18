#Brute Approach
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s):
            balance = 0
            for ch in s:
                if ch == "(":
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def generate(curr):
            if len(curr) == 2 * n:
                if isValid(curr):
                    res.append(curr)
                return
            generate(curr + "(")
            generate(curr + ")")

        generate("")
        return res


#Better Approach
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res

#Optimal Approach
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for p in range(i):
                for left in dp[p]:
                    for right in dp[i - 1 - p]:
                        dp[i].append("(" + left + ")" + right)

        return dp[n]

# TC - O(Cn * n) where Cn = Catalan number ≈ (4^n / n^1.5)
# SC - O(Cn * n) (store all results)