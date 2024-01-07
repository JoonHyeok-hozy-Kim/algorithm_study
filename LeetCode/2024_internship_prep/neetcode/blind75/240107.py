# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def _get_path(curr_node, target_node, path=None):
            if path is None:
                path = []
            
            path.append(curr_node)
            if curr_node == target_node:
                return 1, path
            
            if curr_node.left:
                found, path = _get_path(curr_node.left, target_node, path)
                if found:
                    return 1, path
            
            if curr_node.right:
                found, path = _get_path(curr_node.right, target_node, path)
                if found:
                    return 1, path
            
            path.pop()
            return 0, path
        
        p_found, p_path = _get_path(root, p)
        q_found, q_path = _get_path(root, q)
        # print(p_path)
        # print(q_path)
        result = None

        if p_found * q_found == 0:
            return result
        
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]:
                break
            result = p_path[i]
        
        return result