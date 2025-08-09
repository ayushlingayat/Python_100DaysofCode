# Brute Approach
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Convert l1 to integer
        num1, place = 0, 1
        while l1:
            num1 += l1.val * place
            place *= 10
            l1 = l1.next

        # Convert l2 to integer
        num2, place = 0, 1
        while l2:
            num2 += l2.val * place
            place *= 10
            l2 = l2.next

        # Add numbers
        total = num1 + num2

        # Convert sum to linked list
        dummy = ListNode()
        curr = dummy
        if total == 0:
            return ListNode(0)
        while total > 0:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next

        return dummy.next

# Time: O(m + n) for conversion + O(k) for building output → O(m + n)
# Space: O(1) extra space (excluding output list)

#Better Approach

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1, arr2 = [], []

        # Store digits from l1
        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        # Store digits from l2
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        carry = 0
        dummy = ListNode()
        curr = dummy

        # Add using array indices
        i = 0
        while i < len(arr1) or i < len(arr2) or carry:
            x = arr1[i] if i < len(arr1) else 0
            y = arr2[i] if i < len(arr2) else 0
            total = x + y + carry

            curr.next = ListNode(total % 10)
            carry = total // 10

            curr = curr.next
            i += 1

        return dummy.next

# Time: O(m + n) (one pass to collect digits, one pass to sum)
# Space: O(m + n) for storing arrays

# Optimal Approach (Single-Pass Digit Addition)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            curr.next = ListNode(total % 10)
            carry = total // 10

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Time: O(max(m, n))
# Space: O(1) extra space , only output list is stored