class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_temp = []
        for c in p:
            if c == '*' and len(p_temp) > 0 and p_temp[-1] == '*':
                continue
            else:
                p_temp.append(c)
        
        newP = ''.join(p_temp)
        dp = {}
        
        def _dfs(si, pi):
            if (si, pi) in dp:
                return dp[(si, pi)]
            
            if pi == len(newP):
                if si == len(s):
                    result = True
                else:
                    result = False
            
            elif newP[pi] == '*':
                if _dfs(si, pi+1):
                    result = True
                elif si < len(s) and _dfs(si+1, pi):
                    result = True
                else:
                    result = False
            
            elif si == len(s):
                result = False
                
            elif newP[pi] == '?' or newP[pi] == s[si]:
                result = _dfs(si+1, pi+1)
                
            else:
                result = False
            
            dp[(si, pi)] = result
            return result
        
        return _dfs(0, 0)