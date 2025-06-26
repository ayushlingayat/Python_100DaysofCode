#Brute Force Approach

# def moveZeroes(nums):
#     temp = []
#
#     # Step 1: Collect non-zero elements
#     for num in nums:
#         if num != 0:
#             temp.append(num)
#
#     # Step 2: Count and append zeros
#     zero_count = len(nums) - len(temp)
#     temp.extend([0] * zero_count)
#
#     # Step 3: Copy back to original list
#     for i in range(len(nums)):
#         nums[i] = temp[i]

#Better Approach

# def moveZeroes(nums):
#     index = 0  # Position to place the next non-zero
#
#     # First pass: move all non-zero elements to the front
#     for num in nums:
#         if num != 0:
#             nums[index] = num
#             index += 1
#
#     # Second pass: fill the rest with zeros
#     while index < len(nums):
#         nums[index] = 0
#         index += 1


#Optimal Approach

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroPos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastNonZeroPos] = nums[lastNonZeroPos], nums[i]
                lastNonZeroPos += 1


