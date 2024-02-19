class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        M = {}
        visited = [0 for _ in range(n)]
        result = 0

        for a, b in edges:
            if a not in M:
                M[a] = set()
            M[a].add(b)

            if b not in M:
                M[b] = set()
            M[b].add(a)


        def _dfs(i, path):
            if i in path:
                return False
            
            if visited[i] != 0:
                return False
            
            path.add(i)
            visited[i] = 1
            if i in M:
                for j in M[i]:
                    _dfs(j, path)
            
            path.remove(i)
            return True
        
        for i in range(n):
            P = set()
            if _dfs(i, P):
                result += 1
        
        return result
