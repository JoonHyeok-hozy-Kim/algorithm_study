# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        Q = deque()
        result = 0
        
        if root:
            Q.append((1, root))
        
        while Q:
            n, curr = Q.popleft()
            result = max(result, n)

            if curr.left:
                Q.append((n+1, curr.left))
            if curr.right:
                Q.append((n+1, curr.right))
            
        return result