#Brute Force Approach

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            found = False
            next_greater = -1
            for i in range(len(nums2)):
                if nums2[i] == num:
                    found = True
                if found and nums2[i] > num:
                    next_greater = nums2[i]
                    break
            res.append(next_greater)
        return res

# Time Complexity: O(n * m)
# Space Complexity: O(1) (excluding result list)

#Better Approach

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            index = nums2.index(num)
            next_greater = -1
            for j in range(index + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break
            res.append(next_greater)
        return res

# Time Complexity: O(n * m)
# Space Complexity: O(1)



#Optimal Approach

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_map = {}

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater_map[num] = stack[-1] if stack else -1
            stack.append(num)

        return [next_greater_map[num] for num in nums1]

# Time Complexity: O(n + m)
# Space Complexity: O(m)