# Brute Approach

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Recursive copy with swapped children
        def build(node):
            if not node:
                return None
            new_node = TreeNode(node.val)
            new_node.left = build(node.right)   # swap
            new_node.right = build(node.left)  # swap
            return new_node

        return build(root)

# Better: Recursive DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap children
        root.left, root.right = root.right, root.left

        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Optimal: Iterative BFS
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            # swap children
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

