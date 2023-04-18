# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            if fast is None or fast.next is None:
                temp = slow
                slow = slow.next
                temp.next = None
            else:
                slow = slow.next
                
        head = self.sortList(head)
        slow = self.sortList(slow)
        return self._merge(head, slow)
    
    def _merge(self, n1, n2):
        walk = ListNode()
        result = walk
        while n1 is not None or n2 is not None:
            if n2 is None or (n1 is not None and n1.val < n2.val):
                walk.next = n1
                n1 = n1.next
            else:
                walk.next = n2
                n2 = n2.next
            walk = walk.next
        
        return result.next