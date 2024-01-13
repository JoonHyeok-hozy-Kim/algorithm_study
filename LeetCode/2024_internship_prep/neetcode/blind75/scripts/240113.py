# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def _post_order(node):
            if node is None:
                return 0
            
            left_sum = _post_order(node.left)
            right_sum = _post_order(node.right)

            result[0] = max(result[0], node.val + left_sum + right_sum)
            temp = node.val + left_sum if left_sum > right_sum else node.val + right_sum
            return temp if temp > 0 else 0
        
        _post_order(root)
        return result[0]