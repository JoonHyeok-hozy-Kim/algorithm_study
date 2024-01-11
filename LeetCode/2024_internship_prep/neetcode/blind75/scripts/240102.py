# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def _is_subtree(r, s):
            if r is None and s is None:
                return True
            elif r is None:
                return False
            elif s is None:
                return False
            elif r.val != s.val:
                return False
            
            if not _is_subtree(r.left, s.left):
                return False
            if not _is_subtree(r.right, s.right):
                return False
            return True
        
        if _is_subtree(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        
        return False