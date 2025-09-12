from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means uncolored, 0 and 1 will be the two colors

        for start in range(n):
            if color[start] == -1:  # not colored yet
                queue = deque([start])
                color[start] = 0  # start coloring with 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]  # alternate color
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False  # adjacent nodes have same color
        return True


