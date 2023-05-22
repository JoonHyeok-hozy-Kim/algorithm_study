class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        route = set()
        link = defaultdict(list)
        for [_to, _from] in prerequisites:
            link[_to].append(_from)
        
        def _dfs(i):
            if i in route:
                return False
            elif visited[i]:
                return True
            
            visited[i] = True
            route.add(i)
            for j in link[i]:
                go_on = _dfs(j)
                if not go_on:
                    return False
            route.remove(i)
            return True
        
        for i, v in enumerate(visited):
            if not v:
                temp = _dfs(i)
                if not temp:
                    return False
        return True