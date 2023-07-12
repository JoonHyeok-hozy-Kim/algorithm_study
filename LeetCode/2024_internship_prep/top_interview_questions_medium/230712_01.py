class Solution:   
    def lengthOfLongestSubstring(self, s: str) -> int:
        M = {}
        result = 0
        start = 0
        
        for i, c in enumerate(s):
            if c not in M:
                result = max(result, i-start+1)
                M[c] = i
                
            else:
                start = max(start, M[c]+1)
                result = max(result, i-start+1)
                M[c] = i                
        
        return result