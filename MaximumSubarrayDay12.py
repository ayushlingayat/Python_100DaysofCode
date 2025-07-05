#Brute Force Approach

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_sum = float('-inf')
#
#         for i in range(n):
#             for j in range(i, n):
#                 curr_sum = 0
#                 for k in range(i, j + 1):
#                     curr_sum += nums[k]
#                 max_sum = max(max_sum, curr_sum)
#
#         return max_sum


# Time Complexity: O(n³)
# Space Complexity: O(1)


#Better Approach

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_sum = float('-inf')
#
#         for i in range(n):
#             curr_sum = 0
#             for j in range(i, n):
#                 curr_sum += nums[j]
#                 max_sum = max(max_sum, curr_sum)

        # return max_sum

# Time Complexity: O(n²)
# Space Complexity: O(1)

#Optimal Approach:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum

# Time Complexity: O(n)
# Space Complexity:O(1)

