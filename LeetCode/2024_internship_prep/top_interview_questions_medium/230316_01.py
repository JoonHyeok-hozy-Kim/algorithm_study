# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            Q = deque()
            curr_level = -1
            Q.append((root, 0))
            while Q:
                node, level = Q.popleft()
                if level == curr_level:
                    result[-1].append(node.val)
                else:
                    if len(result) > 0 and curr_level % 2 != 0:
                        result[-1].reverse()
                    curr_level += 1
                    result.append([node.val])
                    
                if node.left:
                    Q.append((node.left, curr_level+1))
                if node.right:
                    Q.append((node.right, curr_level+1))
                    
            if len(result) > 0 and curr_level % 2 != 0:
                result[-1].reverse()
                    
        return result
                
        