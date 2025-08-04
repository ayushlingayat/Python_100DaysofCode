#Brute Approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        dummy = ListNode()
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

# Time Complexity:
# Collecting values: O(n + m)
# Sorting: O((n + m) * log(n + m))
# Creating new list: O(n + m)
# Total: O((n + m) * log(n + m))
# Space Complexity: O(n + m) (for the array)

#Better Approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next

        while list1:
            tail.next = ListNode(list1.val)
            list1 = list1.next
            tail = tail.next

        while list2:
            tail.next = ListNode(list2.val)
            list2 = list2.next
            tail = tail.next

        return dummy.next

# Time Complexity: O(n + m)
# Space Complexity: O(n + m) (new list created)

#Optimal Approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

# Time Complexity: O(n + m)
# Space Complexity: O(1) (in-place)
