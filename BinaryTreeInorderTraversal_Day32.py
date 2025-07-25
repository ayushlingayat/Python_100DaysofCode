#Brute Force Approach
#Using a class-level/global list (not recommended)

class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result

# TC - O(N)
# SC - O(N)

#Better Approach
#Recursive and pure

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        return inorder(root)

# TC - O(N)
# SC - O(N)

#Optimal Approach
#Iterative using Stack

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res

# TC - O(N)
# SC - O(N)