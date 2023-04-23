"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        dummy_head = Node(head.val)
        link = {}
        link[None] = None
        
        walk = head
        copy_walk = dummy_head
        while walk is not None:
            copy_walk.next = Node(walk.val)
            copy_walk = copy_walk.next
            link[walk] = copy_walk
            walk = walk.next
        
        walk = head
        copy_walk = dummy_head.next
        while walk is not None:
            copy_walk.random = link[walk.random]
            walk = walk.next
            copy_walk = copy_walk.next
        
        return dummy_head.next
        