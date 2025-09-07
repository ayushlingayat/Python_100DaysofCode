#Optimal Code

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        queue = deque([node])

        # Clone first node
        visited[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)
                visited[curr].neighbors.append(visited[nei])

        return visited[node]
