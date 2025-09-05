#Optimal Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = l
# Optimal Approach
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left, in_right):
            nonlocal pre_idx
            if in_left > in_right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)

