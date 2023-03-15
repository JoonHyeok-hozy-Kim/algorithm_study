# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result_list = []
        if root:
            self._inorder_traversal(root, result_list)
            
        return result_list
        
    def _inorder_traversal(self, node, result_list):
        if node.left:
            self._inorder_traversal(node.left, result_list)
            
        result_list.append(node.val)
        
        if node.right:
            self._inorder_traversal(node.right, result_list)