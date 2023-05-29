class Solution:
    def isMatch(self, s:str, p:str) -> bool:
        dp = {}

        def _dfs(si, pi):
            if (si, pi) in dp:
                return dp[(si, pi)]
            
            result = False
            if pi == len(p):
                if si == len(s):
                    result = True
            
            elif p < len(p)-1 and p[pi] == '*':
                if si == len(s):
                    if _dfs(si, pi+2):
                        result = True
                else:
                    if _dfs(si, pi+2):
                        result = True
                    elif (p[pi] == '.' or p[pi] == s[si]) and _dfs(si+1, pi):
                        result = True

            elif si == len(s):
                result = False

            elif p[pi] == '.' or s[si] == p[pi]:
                result = _dfs(si+1, pi+1)

            dp[(si, pi)] = result
            return result
        
        return _dfs(0, 0)

                
            
