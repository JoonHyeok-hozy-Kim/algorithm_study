class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        for c in s:
            if c in ('(', '{', '['):
                S.append(c)
            elif c == ')':
                if len(S) == 0 or S[-1] != '(':
                    return False
                else:
                    S.pop()
            elif c == '}':
                if len(S) == 0 or S[-1] != '{':
                    return False
                else:
                    S.pop()
            elif c == ']':
                if len(S) == 0 or S[-1] != '[':
                    return False
                else:
                    S.pop()
        
        if len(S) == 0:
            return True
        return False