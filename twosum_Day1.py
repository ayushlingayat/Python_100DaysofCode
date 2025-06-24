
#Optimal Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i


# Brute Force Solution

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         #first pointer on i
#         for i in range(len(nums)):
#             #second pointer on i + 1
#             for j in range(i+1, len(nums))
#                 if nums[i] + nums[j] == target
#                     return [i,j]


# TC - O(n square)
# SC - O(1)

#Better Solution

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_map ={}
#
#         # this is first iteration  key value pair creation in dictionary
#         for i in range(len(nums)):
#             nums_map[nums[i]] = i
#
#         #now second iteration to check present value in dictory if there use it
#         for i in range(len(nums)):
#             complement =  target -nums[i]
#             if complement in num_map and num_map[complement] != i:
#                 return [i, num_map[complement]]

# TC - O(n)
# SC - O(n)





