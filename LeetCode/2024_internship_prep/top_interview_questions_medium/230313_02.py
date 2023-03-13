# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head        
        if head.next is None:
            return head
        
        odd_start = head
        odd_walk = odd_start
        even_start = head.next
        even_walk = even_start
        
        while True:
            if even_walk is not None and even_walk.next is not None:
                odd_walk.next = even_walk.next
                odd_walk = odd_walk.next
            else:
                odd_walk.next = None
                break

            if odd_walk is not None and odd_walk.next is not None:
                even_walk.next = odd_walk.next
                even_walk = even_walk.next            
            else:
                even_walk.next = None
                break
        
        odd_walk = odd_start
        while odd_walk.next is not None:
            odd_walk = odd_walk.next
        
        odd_walk.next = even_start
        
        return odd_start
        