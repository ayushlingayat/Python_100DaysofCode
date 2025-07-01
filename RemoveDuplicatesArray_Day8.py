#Brute Force Solution
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         i = 0
#         while i < len(nums) - 1:
#             j = i + 1
#             while j < len(nums) and nums[j] == nums[i]:
#                 # Remove duplicate at j by shifting left
#                 nums.pop(j)
#             i += 1
#         return len(nums)
from socketserver import TCPServer


#TC- O(n square)
#SC - O(1)

#Better Solution

# class Solution:
#     def removeDuplicates(self, nums: List[int]) ->int:
#         if not nums:
#             return 0
#         unique = []
#         for num in nums:
#             if not unique or unique[-1] != num:
#                 unique.append(num)
#         for i in range(len(unique)):
#             nums[i] = unique[i]
#         return len(unique)


#TC- O(n)
#SC - O(n)

#Optimal Solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

# TC - O(n)
# SC - O(1)



