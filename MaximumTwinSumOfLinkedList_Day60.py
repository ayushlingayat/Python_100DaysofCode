# Brute Approach

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)
        max_sum = 0
        for i in range(n // 2):
            max_sum = max(max_sum, arr[i] + arr[n - 1 - i])
        return max_sum

# Better Approach

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle using slow-fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Push second half to stack
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next

        max_sum = 0
        curr = head
        while stack:
            max_sum = max(max_sum, curr.val + stack.pop())
            curr = curr.next
        return max_sum

#Optimal Approach

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle (slow will be at mid)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare and calculate max twin sum
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        return max_sum


# Time: O(n)
# Space: O(1) 
