class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        
        route = []
        added = [False] * numCourses
        from_to = defaultdict(list)
        to_from = defaultdict(list)
        
        for [_to, _from] in prerequisites:
            from_to[_from].append(_to)
            to_from[_to].append(_from)
        
        candidates = []
        for i in range(numCourses):
            if i not in to_from:
                candidates.append(i)
        
        while candidates:
            popped = candidates.pop()
            route.append(popped)
            added[popped] = True
            
            for j in from_to[popped]:
                if j not in to_from:
                    candidates.append(j)
                else:
                    go_on = True
                    for pre in to_from[j]:
                        go_on = added[pre]
                        if not go_on:
                            break
                    if go_on:
                        candidates.append(j)
        
        if len(route) == numCourses:
            return route
        else:
            return []