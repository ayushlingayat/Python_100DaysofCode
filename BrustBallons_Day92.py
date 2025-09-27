from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        balloons = [1] + nums + [1]
        m = len(balloons)  # m = n + 2

        dp = [[0] * m for _ in range(m)]

        for gap in range(1, n + 1):

            for i in range(m - gap - 1):
                j = i + gap + 1

                for k in range(i + 1, j):
                    coins = (balloons[i] * balloons[k] * balloons[j] +
                             dp[i][k] +
                             dp[k][j])

                    dp[i][j] = max(dp[i][j], coins)

        return dp[0][m - 1]

