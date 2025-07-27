#Better Approach

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # Collect values
        seen = []
        current = head
        while current:
            if current.val not in seen:
                seen.append(current.val)
            current = current.next

        # Reconstruct new list
        dummy = ListNode(-1)
        tail = dummy
        for val in seen:
            tail.next = ListNode(val)
            tail = tail.next

        return dummy.next

# TC - O(N)
# SC - O(N)

#Optimal Approach

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate okk
            else:
                current = current.next
        return head

# TC - O(N)
# SC - O(1)

