# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''def _recursive(P, I):
            if len(P) == 0:
                return

            root = TreeNode(P[0])
            ii = 0
            while I[ii] != P[0]:
                ii += 1
            
            root.left = _recursive(P[1:ii+1], I[:ii])
            root.right = _recursive(P[ii+1:], I[ii+1:])

            return root
        
        return _recursive(preorder, inorder)'''

        def _recursive(pi, pj, ii, ij):
            if pi == pj:
                return
            
            node = TreeNode(preorder[pi])
            k = 0
            while preorder[pi] != inorder[ii+k]:
                k += 1
            
            node.left = _recursive(pi+1, pi+k+1, ii, ii+k)
            node.right = _recursive(pi+k+1, pj, ii+k+1, ij)

            return node
        
        return _recursive(0, len(preorder), 0, len(inorder))