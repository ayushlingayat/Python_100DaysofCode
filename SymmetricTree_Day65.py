#Brute Approach
# Brute Force
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(node):
            if not node:
                arr.append(None)
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        return arr == arr[::-1]

#Better Approach
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and \
                isMirror(t1.left, t2.right) and \
                isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)

#Optimal Approach
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root.left, root.right)])

        while q:
            t1, t2 = q.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            q.append((t1.left, t2.right))
            q.append((t1.right, t2.left))

        return True


# Time Complexity : O(N) (each node checked once).
# Space Complexity  : O(W) (queue holds nodes, W = max width of tree, worst O(N)).
