# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappop, heappush

        result = ListNode()
        curr = result
        H = []
        
        for i, l in enumerate(lists):
            if l:
                heappush(H, (l.val, i, l))
        
        while H:
            v, i, l = heappop(H)
            curr.next = l
            curr = curr.next

            if l.next:
                heappush(H, (l.next.val, i, l.next))
        
        return result.next