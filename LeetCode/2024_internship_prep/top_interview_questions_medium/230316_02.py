# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode()
        M = {v: i for i, v in enumerate(inorder)}
        self._divide(root, preorder, M, 0, len(inorder)-1)
        return root
        
    def _divide(self, node, preorder, M, start, end):
        node.val = preorder.pop(0)
        idx = M[node.val]
        if idx > start:
            node.left = TreeNode()
            self._divide(node.left, preorder, M, start, idx-1)
        if idx < end:
            node.right = TreeNode()
            self._divide(node.right, preorder, M, idx+1, end)