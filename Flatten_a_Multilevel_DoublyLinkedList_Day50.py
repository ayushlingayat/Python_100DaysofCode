#Brute Approach
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodes = []

        def dfs(node):
            while node:
                nodes.append(node)
                if node.child:
                    dfs(node.child)
                node = node.next

        dfs(head)

        # Rebuild the list
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]
            nodes[i].child = None
        nodes[-1].next = None
        return nodes[0]

# TC - O(n)
# SC - O(n)

#Better Approach

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def dfs(node):
            curr = node
            last = node

            while curr:
                nxt = curr.next
                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail

                    last = child_tail
                else:
                    last = curr
                curr = nxt
            return last

        dfs(head)
        return head

# TC - O(n)
# SC - O(h)

#Optimal Approach

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        stack = [head]
        prev = None

        while stack:
            curr = stack.pop()

            if prev:
                prev.next = curr
                curr.prev = prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        return head

# TC - O(n)
# SC - O(h)

