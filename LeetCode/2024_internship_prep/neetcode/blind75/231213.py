# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ''' Memory usint set sol.
        record = set()
        curr = head

        while curr:
            if curr in record:
                return True
            record.add(curr)
            curr = curr.next
        
        return False
        '''

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast is None:
                return False
            elif slow == fast or slow == fast.next:
                return True
        
        return False