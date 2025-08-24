# Brute Approach

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(list_node, tree_node):
            if not list_node:  # reached end of list
                return True
            if not tree_node:  # tree ended first
                return False
            if list_node.val != tree_node.val:
                return False
            return dfs(list_node.next, tree_node.left) or dfs(list_node.next, tree_node.right)

        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


#Better Approach

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            return dfs(list_node.next, tree_node.left) or dfs(list_node.next, tree_node.right)

        # Only check when values match
        if head.val == root.val and dfs(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

#Optimal Approach

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Convert linked list to array (pattern)
        pattern = []
        while head:
            pattern.append(head.val)
            head = head.next

        # Build prefix table (KMP failure function)
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        # DFS on tree with pattern matching
        def dfs(node, j):
            if not node:
                return False
            while j > 0 and node.val != pattern[j]:
                j = lps[j - 1]
            if node.val == pattern[j]:
                j += 1
            if j == len(pattern):
                return True
            return dfs(node.left, j) or dfs(node.right, j)

        return dfs(root, 0)


# Time Complexity:
# Convert list → O(M)
# Build prefix table → O(M)
# DFS tree traversal → O(N) (each node visited once, with KMP rollback).
# Total → O(N + M)

# Space Complexity:
# Prefix table = O(M)
# Recursion stack = O(H)
# Total = O(M + H)
