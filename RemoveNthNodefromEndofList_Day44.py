# Brute Approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        index_to_remove = len(nodes) - n
        if index_to_remove == 0:
            return head.next

        prev = nodes[index_to_remove - 1]
        prev.next = prev.next.next
        return head

# TC - O(2N)
# SC - O(N)

# Better Approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        if n == length:
            return head.next

        temp = head
        for _ in range(length - n - 1):
            temp = temp.next

        temp.next = temp.next.next
        return head

# TC - O(2N)
# SC - O(1)

# Optimal Approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next

# TC - O(N)
# SC - O(1)