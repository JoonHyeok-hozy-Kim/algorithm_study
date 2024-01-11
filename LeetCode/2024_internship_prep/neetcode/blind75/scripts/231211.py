# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        fast = slow = head
        while slow and slow.next:
            fast = fast.next
            slow = slow.next.next
        if slow and slow.next:
            slow = slow.next
        
        mid_curr = fast.next
        fast.next = None        
        mid_prev = None
        while mid_curr:
            mid_next = mid_curr.next
            mid_curr.next = mid_prev
            mid_prev, mid_curr = mid_curr, mid_next
        
        front_curr = head
        back_curr = mid_prev

        while back_curr:
            front_next = front_curr.next
            back_next = back_curr.next

            front_curr.next = back_curr
            back_curr.next = front_next

            front_curr = front_next
            back_curr = back_next
        
        return head