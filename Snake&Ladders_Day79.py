from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # Converting 2D board to 1D array for easier traversal
        arr = [-1]  # Index 0 unused for convenience (board squares start from 1)
        reverse = False
        for row in range(n - 1, -1, -1):  # Start from bottom row
            row_values = board[row][:]
            if reverse:
                row_values.reverse()
            arr.extend(row_values)
            reverse = not reverse

        # BFS
        queue = deque([(1, 0)])  # (current square, number of moves)
        visited = set([1])

        while queue:
            square, moves = queue.popleft()

            # If we reach the last square, return moves
            if square == n * n:
                return moves

            # Try all dice rolls (1 to 6)
            for roll in range(1, 7):
                next_square = square + roll
                if next_square > n * n:
                    continue

                # If there's a snake or ladder, move to its destination
                if arr[next_square] != -1:
                    next_square = arr[next_square]

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1  # If it's impossible to reach the end
