#Brute Force Solution

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         n = len(prices)
#
#         for i in range(n):
#             for j in range(i + 1, n):
#                 profit = prices[j] - prices[i]
#                 max_profit = max(max_profit, profit)
#
#         return max_profit

        # TC - O(N
        # square)
        # SC - O(1)

# Better/Optimal Approach

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # start with very high value so any price will be smaller
        max_profit = 0  # track the best profit so far we set to zero initial okk

        for price in prices:
            if price < min_price:
                min_price = price  # found a lower price to buy finding it by doing this
            else:
                profit = price - min_price  # check profit if sold today
                max_profit = max(max_profit, profit)  # update max profit if higher okk

        return max_profit #then at last returning max_profit as said in question