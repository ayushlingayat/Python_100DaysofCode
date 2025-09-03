#Brute Approach
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        preorder = []
        inorder = []

        def dfs(node):
            if not node: return
            preorder.append(str(node.val))
            dfs(node.left)
            inorder.append(str(node.val))
            dfs(node.right)

        dfs(root)
        return ','.join(preorder) + "|" + ','.join(inorder)

    def deserialize(self, data):
        if not data: return None
        preorder_str, inorder_str = data.split('|')
        preorder = preorder_str.split(',')
        inorder = inorder_str.split(',')

        inorder_index = {val: i for i, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(int(root_val))
            root_index = inorder_index[root_val]
            left_size = root_index - in_start

            root.left = build(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
            root.right = build(pre_start + left_size + 1, pre_end, root_index + 1, in_end)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

#Better Approach

from collections import deque

class Codec:
    def serialize(self, root):
        if not root: return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)

    def deserialize(self, data):
        if not data: return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root


#Optimal Approach

class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "null,"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

