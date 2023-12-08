class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        letters = {}
        start, end = 0, 0
        result = 0

        for i, l in enumerate(s):
            if l in letters and letters[l] >= start:
                result = max(result, end-start+1)
                start = letters[l]+1
                
            letters[l] = i
            end = i
        
        return max(result, end-start+1)
