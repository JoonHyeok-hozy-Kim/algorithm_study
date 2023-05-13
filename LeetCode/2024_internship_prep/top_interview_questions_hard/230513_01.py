# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
        
        def _recursive(curr):
            left_sum = _recursive(curr.left) if curr.left else 0
            right_sum = _recursive(curr.right) if curr.right else 0
            
            partial = max(curr.val, curr.val+left_sum, curr.val+right_sum)
            result[0] = max(result[0], partial, curr.val+right_sum+left_sum)
            
            return partial
        
        temp = _recursive(root)
        return max(result[0], temp)