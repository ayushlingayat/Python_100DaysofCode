#Brute Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].next = nodes[i - 1]

        nodes[0].next = None
        return nodes[-1]

# Time Complexity: O(N)
# Space Complexity: O(N) (for storing nodes)

#Better Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

# Time Complexity: O(N)
# Space Complexity: O(N) (due to recurssion call stack)

#Optimal Approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

# Time Complexity: O(N)
# Space Complexity: O(1) (in-place)
