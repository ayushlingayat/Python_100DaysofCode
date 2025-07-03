#Brute Force Approach

# class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     max_area = 0
    #     n = len(height)
    #
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             area = min(height[i], height[j]) * (j - i)
    #             max_area = max(max_area, area)
    #
    #     return max_area

# TC - O(n square)
# SC - O(1)

#Optimal Approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # Update maximum area if current is larger
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# TC - O(n)
# SC - O(1)