# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, we cannot rob children
            rob = node.val + left[1] + right[1]
            # If we don't rob this node, we can take max from children
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))
