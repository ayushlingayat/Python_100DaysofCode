#Brute Approach

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Get length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        k = k % length
        if k == 0:
            return head

        # Rotate k times
        for _ in range(k):
            prev = None
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = head
            head = curr
        return head


# TC - O(k * n)
# SC - O(1)

#Optimal Approach

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Make it a circular list
        tail.next = head

        # Find new tail at (length - k) steps
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head

# TC - O(n)
# SC - O(1)

