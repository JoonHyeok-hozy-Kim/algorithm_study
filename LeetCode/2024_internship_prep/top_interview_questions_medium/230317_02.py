# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self._result_list = [k, None]
        self._inorder_traversal(root)
        return self._result_list[1]
    
    
    def _inorder_traversal(self, node):
        if self._result_list[1] is None:
            if node.left:
                self._inorder_traversal(node.left)
                if self._result_list[1]:
                    return
            
            self._result_list[0] -= 1
            if self._result_list[0] == 0:
                self._result_list[1] = node.val
                return
                
            if node.right:
                self._inorder_traversal(node.right)