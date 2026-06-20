# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = [0,1,2,3]
        # prev     curr   temp
        # (dum) -> (0) -> (1) -> (2) temp = curr.next
        # (dum) <- (0)    (1) -> (2) curr.next = prev
        #       curr/prev
        # (dum) <- (0)    (1) -> (2) prev = curr
        #.         prev  curr
        # (dum) <- (0)   (1) -> (2) curr = temp       

        #  (dum) -> (0) -> (1)

        # dummy = ListNode(-1)
        # dummy.next = head

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
