# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     a_visited = set()
    #     a_curr = headA
    #     while a_curr:
    #         a_visited.add(a_curr)
    #         a_curr = a_curr.next
    #     b_curr = headB
    #     while b_curr:
    #         if b_curr in a_visited:
    #             return b_curr
    #         b_curr = b_curr.next
    #     return None
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        a_len = b_len = a_b_len = 0
        a_curr, b_curr = headA, headB
        a_next, b_next = a_curr.next, b_curr.next
        while a_next:
            a_len += 1
            a_curr = a_next
            a_next = a_next.next
        while b_next:
            b_len += 1
            b_curr = b_next
            b_next = b_next.next
        
        if a_curr != b_curr:
            return None
        
        rev_a = self.reverse_list(headA)
        b_curr = headB
        b_next = b_curr.next
        while b_next:
            a_b_len += 1
            b_curr = b_next
            b_next = b_next.next
        
        self.reverse_list(rev_a)
        answer = headA
        for i in range(a_len - (a_len+b_len-a_b_len)//2):
            answer = answer.next
        
        return answer
        
        
    def reverse_list(self, head):
        prev = head
        curr = head.next
        prev.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev