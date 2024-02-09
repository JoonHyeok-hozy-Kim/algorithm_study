class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def _dfs(i, summed, curr):
            summed += candidates[i]
            curr.append(candidates[i])

            if summed == target:
                cp = deepcopy(curr)                
                result.append(cp)
                
            elif summed < target:
                for j in range(i, len(candidates)):
                    _dfs(j, summed, curr)
            
            curr.pop()
            summed -= candidates[i]
        
        for i, n in enumerate(candidates):
            _dfs(i, 0, [])
            
        return result