#Brute Force

# class Solution:
    # def rotate(self, nums, k):
    #     n = len(nums)
    #     k = k % n  # In case k > n
    #
    #     for _ in range(k):
    #         last = nums[-1]
    #         for i in range(n - 1, 0, -1):
    #             nums[i] = nums[i - 1]
    #         nums[0] = last

#
# Time Complexity: O(n * k)
# Space Complexity: O(1) (in-place)


#Better Solution

# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n  # In case k > n
#         temp = [0] * n
#
#         for i in range(n):
#             temp[(i + k) % n] = nums[i]
#
#         for i in range(n):
#             nums[i] = temp[i]

# Time Complexity: O(n)
# Space Complexity: O(n) (using temp array)

#Optimal Approach

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


# Time Complexity: O(n)
# Space Complexity: O(1) (in-place)

