#Brute Force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        for num in nums:
            curr = num
            length = 1
            while curr + 1 in nums:
                curr += 1
                length += 1
            max_len = max(max_len, length)
        return max_len

# TC -  O(N²)
# SC -  O(1)

#Better Approach
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1

        return max_len


# TC - O(N log N) (due to sorting)
# SC - O(1)


#Optimal Code
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:  # Start of a sequence
                curr = num
                curr_len = 1

                while curr + 1 in num_set:
                    curr += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len

# TC - O(N)
# SC - O(N)