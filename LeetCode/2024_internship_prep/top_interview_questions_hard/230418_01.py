# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode()
        heap = []
        
        if len(lists) == 0:
            return None
        
        for i, l in enumerate(lists):
            if l is not None:
                heappush(heap, (l.val, i, l))
                lists[i] = l.next
        
        walk = result
        while len(heap) > 0:
            pv, pi, pn = heappop(heap)
            walk.next = pn
            walk = walk.next
            
            if lists[pi] is not None:
                heappush(heap, (lists[pi].val, pi, lists[pi]))
                lists[pi] = lists[pi].next
        
        return result.next