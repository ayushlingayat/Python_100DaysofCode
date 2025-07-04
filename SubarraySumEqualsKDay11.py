#Brute Force Approach
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) ->int:
#         count = 0
#         n = len(nums)
#         for start in range(n):
#             for end in range(start, n):
#                 current_sum = 0
#                 for i in range(start, end + 1):
#                     current_sum += nums[i]
#                 if current_sum == k:
#                     count += 1
#         return count

# Time Complexity: O(n cube)
# Space Complexity: O(1)


#Better Approach
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) ->int:
#         count = 0
#         n = len(nums)
#         prefix_sum = [0] * (n + 1)
#
#         for i in range(n):
#             prefix_sum[i + 1] = prefix_sum[i] + nums[i]
#
#         for start in range(n):
#             for end in range(start, n):
#                 if prefix_sum[end + 1] - prefix_sum[start] == k:
#                     count += 1
#         return count

# Time Complexity: O(n square) -> two nested loops
# Space Complexity: O(n) -> prefix sum array

#Optimal Approach

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: prefix sum 0 appears once

        for num in nums:
            curr_sum += num
            if (curr_sum - k) in prefix_sums:
                count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(n)
