#Brute Approach
# Brute Force Approach
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def findMax(node):
            while node.right:
                node = node.right
            return node.val

        def findMin(node):
            while node.left:
                node = node.left
            return node.val

        leftValid = (not root.left or findMax(root.left) < root.val) and self.isValidBST(root.left)
        rightValid = (not root.right or findMin(root.right) > root.val) and self.isValidBST(root.right)

        return leftValid and rightValid


#Better Approach
# Better Approach (Inorder Traversal with List)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def inorderTraversal(node):
            if not node:
                return
            inorderTraversal(node.left)
            inorder.append(node.val)
            inorderTraversal(node.right)

        inorderTraversal(root)

        # Check if strictly increasing
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
        return True

#Optimal Apporach
# Optimal Approach (Range Checking)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float("-inf"), float("inf"))

# Optimal: O(N) time, O(H) space.