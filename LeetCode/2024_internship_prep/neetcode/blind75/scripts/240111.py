# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def _inorder(node, target, curr):
            if node.left:
                curr, result = _inorder(node.left, target, curr)
                if curr == target:
                    return curr, result
            
            curr += 1            
            if target == curr:
                return curr, node
            
            if node.right:
                curr, result = _inorder(node.right, target, curr)
                if curr == target:
                    return curr, result
            
            return curr, node
        
        cnt, result = _inorder(root, k, 0)
        return result.val