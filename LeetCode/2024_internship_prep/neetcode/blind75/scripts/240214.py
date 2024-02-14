"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        M = {}

        def _dfs(curr):
            if curr is None:
                return None

            if curr not in M:
                new_node = Node(curr.val, None)
                M[curr] = new_node
            
                if curr.neighbors:
                    new_node.neighbors = []
                    for nn in curr.neighbors:
                        if nn not in M:
                            _dfs(nn)
                        new_node.neighbors.append(M[nn])
            
            return M[curr]
        
        return _dfs(node)