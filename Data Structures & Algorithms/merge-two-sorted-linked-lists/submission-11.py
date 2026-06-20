# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        ptr1 = list1
        ptr2 = list2
        prev = ListNode()
        head = prev
       
        # while ptr2 and ptr2.val < ptr1.val:
        #     ptr2 = ptr2.next        

        # We're going to traverse both lists at the same time.
        # If the value at ptr1 and ptr2 are the same we connect ptr1.next to ptr2, then advance both ptr1 and ptr2 forward
        # if val at ptr1 is less than val at ptr2, we connect ptr1.next to ptr2, then advance ptr1
        # if val at ptr2 is less than val at ptr1, we connect ptr2.next to ptr1, then advance ptr2
        # we end when ptr1 or ptr2 is not None
        # [1, 2, 4], [1, 3, 5]
        # 1 -> 1
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                prev.next = ptr1
                ptr1 = ptr1.next
            else:
                prev.next = ptr2
                ptr2 = ptr2.next
            prev = prev.next
        
        prev.next = ptr1 or ptr2
        
        return head.next