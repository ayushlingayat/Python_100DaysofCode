#Brute Approach

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         rows, cols = len(matrix), len(matrix[0])
#         temp = [[1] * cols for _ in range(rows)]
#
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     for k in range(cols):
#                         temp[i][k] = 0
#                     for k in range(rows):
#                         temp[k][j] = 0
#
#         for i in range(rows):
#             for j in range(cols):
#                 if temp[i][j] == 0:
#                     matrix[i][j] = 0


# Time Complexity: O(m * n * (m + n))
# Space Complexity: O(1) if using -1 trick, otherwise O(m + n)

#Better Approach

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         rows, cols = len(matrix), len(matrix[0])
#         row_flags = [0] * rows
#         col_flags = [0] * cols
#
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     row_flags[i] = 1
#                     col_flags[j] = 1
#
#         for i in range(rows):
#             for j in range(cols):
#                 if row_flags[i] == 1 or col_flags[j] == 1:
#                     matrix[i][j] = 0

# Time Complexity: O(m * n)
# Space Complexity: O(m + n)

#Optimal Approach

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        col0 = 1

        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[i][j] = 0
                    matrix[0][j] = 0

        for i in reversed(range(rows)):
            for j in reversed(range(1, cols)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

# Time Complexity: O(m * n)
# Space Complexity: O(1) (in-place)