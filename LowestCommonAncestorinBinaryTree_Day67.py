#Brute Approach

# Brute Force: Root-to-Node Path Method
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Helper to get path from root to a node
        def getPath(root, target, path):
            if not root:
                return False
            path.append(root)
            if root == target:
                return True
            if getPath(root.left, target, path) or getPath(root.right, target, path):
                return True
            path.pop()
            return False

        path1, path2 = [], []
        getPath(root, p, path1)
        getPath(root, q, path2)

        # Compare paths
        lca = None
        for u, v in zip(path1, path2):
            if u == v:
                lca = u
            else:
                break
        return lca

#Better Approach

# Better: Parent Mapping + Ancestor Set
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {root: None}

        # DFS to store parent of each node
        def dfs(node):
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        dfs(root)

        # Store ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # First common ancestor for q
        while q not in ancestors:
            q = parent[q]
        return q


#Optimal Approach

# Optimal: Single DFS recursion
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right

# Time Complexity = O(N)
# Space Complexity = O(H)

