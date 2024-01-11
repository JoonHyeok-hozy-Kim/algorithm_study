# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        cnt = 0

        while curr:
            if cnt == n:
                prev = head
            elif cnt > n:
                prev = prev.next
            
            curr = curr.next
            cnt += 1
        
        if prev is None:
            return head.next
        else:
            if prev.next:
                prev.next = prev.next.next
            else:
                prev.next = None
        
        return head