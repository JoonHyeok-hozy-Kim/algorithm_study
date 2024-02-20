class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n-1:
            return False

        V = [0 for _ in range(n)]
        E = defaultdict(list)
        s1 = 0

        for a, b in edges:
            E[a].append(b)
            E[b].append(a)
            s1 = a
        
        def _preorder(_curr, _prev):
            if V[_curr] != 0:
                return False
            
            V[_curr] = 1
            go_on = True
            if _curr in E:
                for _next in E[_curr]:
                    if _next != _prev:
                        go_on = _preorder(_next, _curr)
                        if not go_on:
                            break
            return go_on
        
        if not _preorder(s1, None):
            return False
        
        return sum(V) == n