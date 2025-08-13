#Brute Approach
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head

        # Step 1: Store all values in array
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Step 2: Reverse in chunks of k
        for i in range(0, len(arr), k):
            if i + k <= len(arr):
                arr[i:i + k] = reversed(arr[i:i + k])

        # Step 3: Rebuild linked list
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

# TC - O(n)
# SC - O(n)
#Better Approach
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while True:
            stack = []
            temp = curr
            # Push k nodes into stack
            for _ in range(k):
                if not temp:
                    return dummy.next
                stack.append(temp)
                temp = temp.next

            # Pop from stack to reverse
            while stack:
                prev.next = stack.pop()
                prev = prev.next

            # Connect last node of reversed group to next group
            prev.next = temp
            curr = temp

# TC - O(n)
# SC - O(k)

#Optimal Approach

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            kth = self.getKth(prev_group_end, k)
            if not kth:
                break
            group_end = kth.next

            # Reverse the group
            prev, curr = kth.next, prev_group_end.next
            while curr != group_end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prev_group_end.next
            prev_group_end.next = kth
            prev_group_end = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# TC - O(n)
# SC - O(1)

