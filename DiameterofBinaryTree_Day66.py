#Brute Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # diameter passing through root
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        diameter_through_root = left_height + right_height

        # diameter in left or right subtree
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(diameter_through_root, left_diameter, right_diameter)


#Optimal Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            # update diameter
            self.diameter = max(self.diameter, left + right)

            # return height
            return 1 + max(left, right)

        dfs(root)
        return self.diameter

# Time: O(N) → each node visited once.
# Space: O(H) recursion stack (O(N) worst case, O(logN) best case).