# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val < list2.val:
            curr = list1 
            l1 = list1.next
            l2 = list2
        else:
            curr = list2
            l1 = list1
            l2 = list2.next
        result = curr

        while l1 or l2:
            if l2 is None or (l1 is not None and l1.val < l2.val):
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        return result