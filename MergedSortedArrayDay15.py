#Brute Approach

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

# Time Complexity: O((m+n) * log(m+n))
# Space Complexity: O(1) — in-place sorting.

#Better Approach

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        i = j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        for k in range(len(result)):
            nums1[k] = result[k]

# Time Complexity: O(m + n)
# Space Complexity: O(m + n) — uses extra list.

#Optimal Approach

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # pointer for nums1
        j = n - 1  # pointer for nums2
        k = m + n - 1  # fill position from end

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # if any elements left in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Time Complexity: O(m + n)
# Space Complexity: O(1) — fully in-place.



