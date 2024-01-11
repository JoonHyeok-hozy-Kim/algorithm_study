
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _inorder(node, lower_bound=None, upper_bound=None):
            print('{} start. L : {},  U : {}'.format(node.val, lower_bound, upper_bound))
            if node.left:
                if node.left.val >= node.val:
                    return False
                if lower_bound is not None and node.left.val <= lower_bound:
                    return False
                new_upper_bound = node.val if upper_bound is None else min(upper_bound, node.val) 
                go_on = _inorder(node.left, lower_bound, new_upper_bound)
                if not go_on:
                    return False
            
            if node.right:
                if node.val >= node.right.val:
                    return False
                if upper_bound is not None and node.right.val >= upper_bound:
                    return False
                new_lower_bound = node.val if lower_bound is None else max(lower_bound, node.val) 
                go_on = _inorder(node.right, new_lower_bound, upper_bound)
                if not go_on:
                    return False
            
            print(node.val, " end.")
            return True
        
        return _inorder(root)