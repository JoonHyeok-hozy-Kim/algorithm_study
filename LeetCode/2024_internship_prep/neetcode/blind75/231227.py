# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        # Recursive Sol.
        if root:        
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            
            root.left, root.right = root.right, root.left
        
        return root
        '''

        # Queue Sol.
        Q = deque()
        if root:
            Q.append(root)

        while Q:
            p = Q.popleft()
            p.left, p.right = p.right, p.left
            if p.left:
                Q.append(p.left)
            if p.right:
                Q.append(p.right)
        
        return root