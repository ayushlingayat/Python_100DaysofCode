#Brute Force Approach


# class Solution:
#     def merge(self, intervals: List[List[int]]) ->List[List[int]]:merged = []
#         for interval in intervals:
#             if not merged:
#                 merged.append(interval)
#             else:
#                 has_merged = False
#                 for i in range(len(merged)):
#                     # Check if there is overlap
#                     if interval[0] <= merged[i][1] and interval[1] >= merged[i][0]:
#                         # Merge intervals
#                         merged[i][0] = min(merged[i][0], interval[0])
#                         merged[i][1] = max(merged[i][1], interval[1])
#                         has_merged = True
#                         break
#                 if not has_merged:
#                     merged.append(interval)
#         return merged


# TC - O(n square)
# SC - O(n)


# Better and Optimal Approach

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, so merge with the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# TC - O(n log n)
# SC -  O(n) 