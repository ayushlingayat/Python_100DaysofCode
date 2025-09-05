#Brute Approach
# Brute Force Approach
# Time: O(N)
# Space: O(N) (extra list)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        nodes = []

        # Preorder traversal
        def preorder(node):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        # Rearrange pointers
        for i in range(1, len(nodes)):
            prev, curr = nodes[i - 1], nodes[i]
            prev.left = None
            prev.right = curr


# Better Approach
# Time: O(N^2) (because finding tail each time takes O(N))
# Space: O(N) recursion stack

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        # Flatten left and right
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            # Find tail of left
            tail = root.left
            while tail.right:
                tail = tail.right

            # Attach right subtree
            tail.right = root.right
            root.right = root.left
            root.left = None


# Optimal Approach
# Time: O(N)
# Space: O(N) recursion stack (no extra data structures)

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        # Postorder (right -> left -> root)
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

