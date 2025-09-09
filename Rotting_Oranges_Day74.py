from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Add all initially rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # store (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1

        # Step 2: BFS
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, t = q.popleft()
            time = max(time, t)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # rot it
                    fresh -= 1
                    q.append((nr, nc, t + 1))

        # Step 3: Check if all fresh are rotten
        return time if fresh == 0 else -1


# Time Complexity: O(n × m)
# Space Complexity: O(1) extra (besides queue).