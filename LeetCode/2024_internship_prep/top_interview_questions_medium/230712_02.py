class Solution:
    def longestPalindrome(self, s: str) -> str:
        rs, re = 0, 0
        
        def _odd_case(i):
            start = end = i
            while start-1 >= 0 and end+1 < len(s) and s[start-1] == s[end+1]:
                start -= 1
                end += 1
            return start, end
        
        def _even_case(i):
            start = end = i
            if end+1 < len(s) and s[end+1] == s[start]:
                end += 1
                while start-1 >= 0 and end+1 < len(s) and s[start-1] == s[end+1]:
                    start -= 1
                    end += 1
            return start, end
        
        for i, c in enumerate(s):
            start, end = _odd_case(i)
            if end-start+1 > re-rs+1:
                rs, re = start, end
            
            start, end = _even_case(i)
            if end-start+1 > re-rs+1:
                rs, re = start, end
        
        return s[rs:re+1]