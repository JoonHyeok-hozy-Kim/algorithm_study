# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        # Recursive Sol.
        if p is None:
            if q is None:
                return True
            else:
                return False
        elif q is None:
            return False

        if p.val != q.val:
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False

        return True
    
        '''
        # Queue Sol.
        Q = deque()

        if p is None and q is None:
            return True
        else:
            Q.append((p, q))
        
        while Q:
            pp, pq = Q.popleft()
            if pp is None or pq is None:
                return False
            
            if pp.val != pq.val:
                return False
            
            if pp.left:
                if pq.left:
                    Q.append((pp.left, pq.left))
                else:
                    return False
            elif pq.left:
                return False

            if pp.right:
                if pq.right:
                    Q.append((pp.right, pq.right))
                else:
                    return False
            elif pq.right:
                return False
        
        return True
        