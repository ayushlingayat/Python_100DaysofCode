#Brute Approach
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Store all original nodes in a list
        original_nodes = []
        curr = head
        while curr:
            original_nodes.append(curr)
            curr = curr.next

        # Step 2: Create corresponding new nodes
        new_nodes = [Node(node.val) for node in original_nodes]

        # Step 3: Link next and random
        for i, node in enumerate(original_nodes):
            if node.next:
                new_nodes[i].next = new_nodes[original_nodes.index(node.next)]
            if node.random:
                new_nodes[i].random = new_nodes[original_nodes.index(node.random)]

        return new_nodes[0]

# Time Complexity: O(N²) (because of .index() lookups)
# Space Complexity: O(N) for storing nodes


#Better Approach
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Map original node to new node
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Assign next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]

# Time Complexity: O(N)
# Space Complexity: O(N) (hash map)


#Optimal Approach
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interweave copy nodes
        curr = head
        while curr:
            copy_node = Node(curr.val, curr.next, None)
            curr.next = copy_node
            curr = copy_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and copied list
        curr = head
        copy_head = head.next
        while curr:
            copy_node = curr.next
            curr.next = copy_node.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            curr = curr.next

        return copy_head

# Time Complexity: O(N)
# Space Complexity: O(1) (excluding output list)
