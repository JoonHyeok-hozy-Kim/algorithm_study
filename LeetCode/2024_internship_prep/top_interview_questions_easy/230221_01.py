from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        Q = deque()
        Q.append([root, 0])
        while (Q):
            popped_node = Q[0][0]
            popped_level = Q[0][1]
            Q.popleft();
            
            if popped_node is None:
                continue
            
            if len(result) <= popped_level:
                initial_result = len(result)
                for i in range(popped_level - initial_result + 1):
                    result.append([])
            result[popped_level].append(popped_node.val)
            
            if popped_node.left:
                Q.append([popped_node.left, popped_level+1])
            if popped_node.right:
                Q.append([popped_node.right, popped_level+1])
                
        return result
        