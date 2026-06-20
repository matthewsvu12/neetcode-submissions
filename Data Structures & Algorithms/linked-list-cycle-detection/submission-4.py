# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        """
        slow = slow.next
        fast = fast.next.next

        slow = 1
        fast = 1

        slow = 2
        fast = 3

        slow = 3
        fast = 2

        slow = 4
        fast = 4

        while slow and fast:
        """
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

        