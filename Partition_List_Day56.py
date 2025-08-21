#Brute Approach
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        new_vals = [v for v in values if v < x] + [v for v in values if v >= x]

        dummy = ListNode(0)
        curr = dummy
        for v in new_vals:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next

# Time: O(n) (one traversal to collect + one to rebuild)
# Space: O(n) (array + new list)

#Better Approach
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        small = smaller_dummy
        great = greater_dummy

        while head:
            if head.val < x:
                small.next = ListNode(head.val)
                small = small.next
            else:
                great.next = ListNode(head.val)
                great = great.next
            head = head.next

        small.next = greater_dummy.next
        return smaller_dummy.next

# Time: O(n)
# Space: O(n) (since creating new nodes)

#Optimal Approach

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        small = smaller_dummy
        great = greater_dummy

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                great.next = head
                great = great.next
            head = head.next

        great.next = None  # Important: avoid cycle
        small.next = greater_dummy.next
        return smaller_dummy.next

# TC - O(n)
# SC - O(1)