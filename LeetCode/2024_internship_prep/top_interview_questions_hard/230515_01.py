class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set([i for i in range(len(isConnected))])
        result = 0
        
        def _dfs(i, V):
            for j, connected in enumerate(isConnected[i]):
                if connected and j in V:
                    V.remove(j)
                    _dfs(j, V)
        
        while visited:
            result += 1
            _dfs(visited.pop(), visited)
        
        return result