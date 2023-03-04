
class Solution:
    def translate(self, c: chr) -> int:
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
        else:
            return None
    
    def romanToInt(self, s: str) -> int:
        idx = len(s) - 1
        prev = self.translate(s[idx])
        result = prev
        idx -= 1
        
        while idx >= 0:
            curr = self.translate(s[idx])
            if curr >= prev:
                result += curr
            else:
                result -= curr
            prev = curr
            idx -= 1
        return result