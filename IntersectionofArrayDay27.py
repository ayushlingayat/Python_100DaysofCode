#Brute Force Approach
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)
        return list(result)

# Time Complexity:
# O(n * m) where n = len(nums1) and m = len(nums2)
#
# Space Complexity:
# O(min(n, m)) for the result set

#Better Approach

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result = set()
        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)

# Time Complexity:
# O(n + m) where n = len(nums1), m = len(nums2)
#
# Space Complexity:
# O(n + k) where k is size of result

#Optimal Approach
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = set()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return list(result)

# Time Complexity:
# O(n log n + m log m) for sorting, and O(n + m) for two-pointer traversal

# Space Complexity:
# O(k) where k is size of the intersection result

