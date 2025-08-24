#Brute Approach
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Put nodes in array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: Reorder using two pointers
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        # Step 3: End the list
        nodes[left].next = None


#Better Approach
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Store values
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        # Step 2: Reassign values in required order
        left, right = 0, len(vals) - 1
        curr = head
        while curr:
            if left <= right:
                curr.val = vals[left]
                left += 1
            if curr.next and left <= right:
                curr.next.val = vals[right]
                right -= 1
                curr = curr.next
            curr = curr.next


#Optimal Approach
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle (slow-fast pointer)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # Cut the list into two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

