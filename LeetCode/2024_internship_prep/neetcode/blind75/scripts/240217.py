class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        M = [[] for _ in range(numCourses)]
        done = [0 for _ in range(numCourses)]

        for curr, prev in prerequisites:
            M[curr].append(prev)
        
        def _dfs(i, visited):
            temp_result = True
            if i in visited or done[i] == -1:
                temp_result = False
            else:
                if done[i] == 0:
                    visited.add(i)
                    for j in M[i]:
                        if not _dfs(j, visited):
                            temp_result = False
                            break
                    visited.remove(i)
            
            done[i] = 1 if temp_result else -1
            return temp_result
        
        V = set()
        for i in range(numCourses):
            if not _dfs(i, V):
                return False
        return True