class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        for c in s:
            if c in ('(', '{', '['):
                S.append(c)
            elif len(S) > 0:                
                if c == ')' and S[-1] == '(':
                    S.pop()
                elif c == '}' and S[-1] == '{':
                    S.pop()
                elif c == ']' and S[-1] == '[':
                    S.pop()
                else:
                    return False
            else:
                return False
        
        if len(S) == 0:
            return True
        else:
            return False