"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
#         if root is None:
#             return None
        
#         if root.left:
#             root.left.next = root.right
            
#             lr = root.left.right
#             rl = root.right.left
#             while rl is not None and lr is not None:
#                 lr.next = rl
#                 lr = lr.right
#                 rl = rl.left
            
#             self.connect(root.left)
#             self.connect(root.right)

        Q = deque()
        curr_node = root
        curr_level = 0
        if root and root.left:
            Q.append((root.left, 1))
            Q.append((root.right, 1))
            
        while Q:
            next_node, next_level = Q.popleft()
            if curr_level == next_level:
                curr_node.next = next_node
            
            if next_node.left:
                Q.append((next_node.left, next_level+1))
                Q.append((next_node.right, next_level+1))
            
            curr_node, curr_level = next_node, next_level                
        
        return root