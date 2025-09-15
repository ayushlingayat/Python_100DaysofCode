from collections import defaultdict
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Build adjacency list (graph)
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        n = len(values)
        visited_count = [0] * n  # track visits per node
        self.max_score = 0

        def dfs(node, time, score):
            # If visiting node for the first time add its value
            if visited_count[node] == 0:
                score += values[node]
            visited_count[node] += 1

            # If back at 0 update max score
            if node == 0:
                self.max_score = max(self.max_score, score)

            # Explore neighbors
            for nei, t in graph[node]:
                if time + t <= maxTime:
                    dfs(nei, time + t, score)

            # Backtrack
            visited_count[node] -= 1

        dfs(0, 0, 0)
        return self.max_score
