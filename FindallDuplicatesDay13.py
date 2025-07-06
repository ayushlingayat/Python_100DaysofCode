#Brute Approach
# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j] and nums[i] not in result:
#                     result.append(nums[i])
#         return result

# Time Complexity: O(n^2)
# Space Complexity: O(1) (Ignoring output list)

#Better Approach

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         freq = {}
#         result = []
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#         for num in freq:
#             if freq[num] == 2:
#                 result.append(num)
#         return result

# Time Complexity: O(n)
# Space Complexity: O(n) (for frequency dictionary)

#Optimal Approach


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]
        return result

# Time Complexity: O(n)
# Space Complexity: O(1) (in-place, excluding result)

