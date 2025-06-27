#Brute Force Solution

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#
#         for i in range(n):
#             count = 0
#             for j in range(n):
#                 if nums[j] == nums[i]:
#                     count = count +1
#             if count > n//2:
#                 return nums[i]


#Better Solution
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count_map = {}
#         n = len(nums)
#
#         for num in nums:
#             count_map[num] = count_map.get(num, 0) + 1
#             if count_map[num] > n // 2:
#                 return num

#Optimal Solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate