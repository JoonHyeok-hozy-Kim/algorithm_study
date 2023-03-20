class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        M = {}
        for i, v in enumerate(nums):
            if v not in M:
                M[v] = 1
            else:
                M[v] += 1
            
        F = [(M[v], v) for v in M]
        F.sort()
        result = []
        for i in range(k):
            result.append(F[-1-i][1])
        
        return result
            
            
            
        