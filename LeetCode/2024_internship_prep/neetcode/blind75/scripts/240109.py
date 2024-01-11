# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def _in_order_tranversal(node, record, cnt=0):
            if len(record) == cnt:
                record.append([])
            
            record[cnt].append(node.val)
            if node.left:
                _in_order_tranversal(node.left, record, cnt+1)
            if node.right:
                _in_order_tranversal(node.right, record, cnt+1)
        
        result = []
        if root:
            _in_order_tranversal(root, result)
        return result