#Brute Approah
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head

        # Step 1: Count total nodes
        while temp:
            count += 1
            temp = temp.next

        # Step 2: Reach middle node
        mid = count // 2
        temp = head
        for _ in range(mid):
            temp = temp.next

        return temp

# TC - O(N)
# SC - O(1)

#Optimal Approach
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# TC - O(N)
# SC - O(1)