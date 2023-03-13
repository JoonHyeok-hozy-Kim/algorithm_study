# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        
        walk = result
        carry = 0
        while l1 is not None or l2 is not None:
            temp = carry
            if l1 is not None:
                temp += l1.val
                l1 = l1.next
            if l2 is not None:
                temp += l2.val
                l2 = l2.next
            
            carry = temp // 10
            temp %= 10
            
            walk.val = temp
            if l1 is None and l2 is None:
                if carry > 0:
                    walk.next = ListNode(1)
                break
                
            walk.next = ListNode()
            walk = walk.next
        
        return result
        
        
        