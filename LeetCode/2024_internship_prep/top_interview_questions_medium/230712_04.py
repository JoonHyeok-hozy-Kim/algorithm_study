# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n = 0
        m = 0
        x = 0
        result = None
        
        walkB = headB
        while walkB:
            m += 1
            walkB = walkB.next
        
        walkA = headA
        prevA = None
        while walkA:
            n += 1
            walkA_next = walkA.next
            walkA.next = prevA
            prevA = walkA
            walkA = walkA_next    
        endA = prevA    
        
        walkB = headB
        while walkB:
            x += 1
            if walkB == headA:
                common = (m+n-x+1)//2
                walkB = headB
                for i in range(m-common):
                    walkB = walkB.next
                result = walkB
                break
            walkB = walkB.next
        
        walkA = endA
        prevA = None
        while walkA:
            walkA_next = walkA.next
            walkA.next = prevA
            prevA = walkA
            walkA = walkA_next
            
        
        return result
            