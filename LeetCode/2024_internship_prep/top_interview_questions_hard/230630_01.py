class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        S = []
        result = 0
        
        for i, h in enumerate(heights):
            idx = i
            
            while len(S) > 0 and S[-1][1] > h:
                j, l = S.pop()
                result = max(result, (i-j)*l)
                idx = j
        
            S.append([idx, h])
        
        last_idx = len(heights)
        while S:
            prev_idx, prev_height = S.pop()
            result = max(result, (last_idx - prev_idx) * prev_height)
        
        return result