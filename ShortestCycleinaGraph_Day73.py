from collections import defaultdict, deque
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        min_cycle = float("inf")

        for start in range(n):
            dist = [-1] * n
            parent = [-1] * n
            q = deque([start])
            dist[start] = 0

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if dist[nei] == -1:  # not visited
                        dist[nei] = dist[node] + 1
                        parent[nei] = node
                        q.append(nei)
                    elif parent[node] != nei:  # found a cycle
                        min_cycle = min(min_cycle, dist[node] + dist[nei] + 1)

        return -1 if min_cycle == float("inf") else min_cycle
